#Code to test the model on a new dataset

## the source couldn't be uploaded on the repository, change source to test the code

!python yolov5/detect.py --weights yolov5/train/exp23/weights/best.pt --img 608 --conf 0.25 --source data_yolov5/test/images  --save-txt
