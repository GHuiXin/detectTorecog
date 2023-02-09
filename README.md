# OCR：detection dataset convert to recognition dataset 
## the format of detection dataset：

`train/circle_Aug00001.png	[{"transcription": "上海维畅物流有限公司", "points": [[63, 440], [44, 259], [138, 103], [307, 37], [481, 87], [590, 232], [588, 414], [498, 382], [499, 262], [427, 166], [311, 133], [200, 177], [137, 280], [150, 399]]}, {"transcription": "991902342741", "points": [[177, 481], [221, 512], [272, 531], [326, 536], [379, 528], [429, 507], [472, 474], [514, 517], [459, 559], [395, 586], [327, 596], [258, 589], [193, 565], [137, 526]]}, {"transcription": "质检专用章", "points": [[166, 355], [218, 352], [270, 350], [322, 347], [374, 345], [425, 342], [477, 340], [482, 430], [430, 432], [378, 435], [326, 437], [274, 440], [223, 442], [171, 445]]}, {"transcription": "廊赶且", "points": [[197, 452], [240, 450], [283, 447], [327, 445], [370, 443], [413, 441], [456, 439], [459, 499], [416, 501], [373, 503], [330, 505], [286, 507], [243, 509], [200, 512]]}]`

## the format of recognition dataset：
`{"memetainfo": {"dataset_type": "", "task_name": ""}, "data_list": [{"instances": [{"text": "annotation"}], "img_path": "path"}]}`

As an example of the data preparation steps, you can use the following command to prepare the  dataset for text recognition task:

`python detectTorecog.py path/to/dataset`

Then, the dataset has been converted to MMOCR format, and the file directory structure is as follows:

`data/dataset
	├── crops
	│   ├── test
	│   └── train
	├── train_label.json
	└── test_label.json`