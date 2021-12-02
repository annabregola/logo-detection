# Logo Detection

## Scope of the project

The purpose of the project is to build a model capable of recognizing and allocating 11 different logos. 

In order to do so, we train YOLOv5 over our custom dataset consisting of more than 20.000 different images


## Data Cleaning

A substantial performance improvement was achieved through the cleaning of the data. In fact, we noticed that many images were in practice not containing the logo at all. In `insert name of the notebook`, we built an algorithm in order to go over the images of the logos we decided to use for the recognition and delete those that were not suitable for the purpose


## Data Preparation

YOLOv5 requires three separate folders for train, test and validation. Each of the folders hence has to be divided into two other folders: images, containing all of the images, and labels, containing all of the labels in a `.txt` format. In order to retrieve the label files, we used [Roboflow](https://roboflow.com/). Moreover, Roboflow was used to create augmented data to improve the performance of the model.

However, we had two categories of data: 
* Images containing our logo
* Noise

The former category was present in both train, validation and test, while the latter was only inserted in the training dataset. For this reason, we first pre-processed the images from Roboflow and hence split them in train, test and validation. This operation can be found in `insert name of the notebook`.

It is important to notice that we first started with only 5 reference logos, and hence added 6 more. For this reason, we had to perform the operation of splitting into train, test and validation twice, so that the extra logos acted as noise in the first model and as actual logos in the second.

## Model training

After the evaluation of different models, we opted for YOLOv5 because of its performance in terms of accuracy. The model was downloaded through [YOLOv5 Git repository](https://github.com/ultralytics/yolov5).

## Model evaluation

The reference metric for the evaluation of the model was the IOU, the Intersection Over Union, evaluated as 

<img src="http://www.sciweavers.org/tex2img.php?eq=IOU%20%3D%20%20%5Cfrac%7BArea%20of%20Intersection%7D%7BArea%20of%20Union%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="IOU =  \frac{Area of Intersection}{Area of Union} " width="226" height="47" />
