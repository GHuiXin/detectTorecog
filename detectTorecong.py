import os
import json
import argparse
import numpy as np
import cv2

def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate training and validation set')
    parser.add_argument('root_path', help='Root dir path of datasets')
    args = parser.parse_args()
    return args

def crops(points, img):
    points = np.array(points).flatten()
    xs, ys = points[::2], points[1::2]
    x, y = min(xs), min(ys)
    w, h = max(xs) - x, max(ys) - y
    crops_img = img[y : y + h, x : x + w]
    return crops_img
    
def convert(contents, path, T):
    out_json = dict(
    memetainfo=dict(dataset_type="TextRecogDataset", task_name="textrecog"),
    data_list=list())
    for content in contents:
        if T == 'train':
            imgPath = content[:25]
            content = content[26:]
        else:
            imgPath = content[:24]
            content = content[25:]
        imgName = imgPath.split('/')[1].split('.')[0]
        oldImage = os.path.join(path, imgPath)
        lines = json.loads(content)
        img = cv2.imread(oldImage)
        for i, line in enumerate(lines):
            single_info = dict(instances=list())
            instance = {}
            instance['text'] = line['transcription']
            cropImg = crops(line['points'], img)
            newName = '{}_{}.png'.format(imgName, str(i))
            file = os.path.join(path, 'crops/{}/{}'.format(T, newName))
            single_info['img_path'] = 'crops/{}/{}'.format(T, newName)
            cv2.imwrite(file, cropImg)
            single_info['instances'].append(instance)
            out_json['data_list'].append(single_info)
    return out_json
            

def open_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        contents = f.readlines()
    return contents

def write_json(contents, file):
    with open(file, 'w') as f:
        json.dump(contents, f)


def main():
    args = parse_args()
    root_path = args.root_path
    print("Processing training set...")
    files = os.listdir(root_path)
    for file in files:
        f = file.split('.')
        name = f[0]
        if len(f) == 2 and ('train' == name or 'test' == name) and 'txt' == f[1]:
           contents = open_json(os.path.join(root_path, file))
           instance = convert(contents, root_path, name)
           write_json(instance, os.path.join(root_path, '{}_label.json'.format(name)))
        else:
            continue
    print("Finish...")
    


if __name__ == '__main__':
    main()

