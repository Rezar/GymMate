# GymNet
Weight training activity recognition algorithm 


# we used three different pose estimation models for VGFIT video. 

## **AlphaPose Model** [ [Show](/train/AlphaPoseV0_3_0.ipynb) ] :
The output in this model for each image is as follows:
- keypoints contains the body part locations and detection confidence formatted as x1,y1,c1,x2,y2,c2,.... c ([Keypoint Ordering ](https://github.com/MVIG-SJTU/AlphaPose/blob/master/docs/output.md) ) is the confidence score in the range [0,1] for MPII dataset and range [0,6] for COCO dataset.
- score is the confidence score for the whole person, computed by our parametric pose NMS.

#### The output has 17 joints, but since we do not need all of them, we use only 12 of them: 
1. LShoulder
1. RShoulder 
1. LWrist 
1. RWrist 
1. LHip 
1. RHip 
1. LKnee 
1. Rknee 
1. LAnkle 
1. RAnkle
1. Lelbow
1. Relbow

[To do this](/scripts/to_csv.py), we convert the output of the Jason file obtained for each video to an [Numpy](/scripts/alphapose_to_numpy.py ) file and then put it in an [CSV](/Data/VGFIT/OpenPose.csv) file [CODE](/scripts/to_csv.py )(__Here the code needs to be optimized to place the Jason file directly in CSV__).

[They were visualized to better understand time series](/scripts/ut.py ) (**For each joint, the values of X and Y are converted to a separate time series**). 
for example:

![angled leg presses:X_L_shoulder ](/Images/1.png)
![angled leg presses:Y_L_shoulder ](/Images/2.png)



## **OpenPose Model** [ [Show](/train/OpenPose.ipynb) ] :



## **BlazePose Model** [ [Show](/train/BlazePose.ipynb) ] :

In this model, we first [convert](/scripts/video_to_frames_blazepose.py) the videos into a number of images and give them to the model


# pose-estimation



