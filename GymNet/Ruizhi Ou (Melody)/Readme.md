*Updated: 10/13/2023*
*By Melody*

**Purpose** 

To identify fitness poses from input videos and return a text description of how many times/what poses/what devices are identified. E.g. *"Six curls with dumbbells"*.
- Input: video (ultimately it would be real-time video captured by camera)
- Output: text descriptions (number of times, poses, devices)

**Approach (step by step)**

1. Object Detection ([YOLOv8](https://docs.ultralytics.com/))
   - Train the model with related fitness devices data (dumbbell, barbell, kettlebell, cable, machines);
   - Detected fitness devices relative to the fitness poses performed.
2. Human figure segmentation ([Segment Anything](https://segment-anything.com/))
   - Segment and retain only the human figure of each frame of the video.
3. Pose Estimation ([MoveNet](https://github.com/tensorflow/tfjs-models/blob/master/pose-detection/README.md#pose-estimation))
   - Extract the coordinates of key joints of the human figure.
4. Pose Estimation Correction
   - Calculate the angle changes of each relative key joint;
   - Correct the abnormal changes in angles (usually due to inaccurate pose estimation).
5. Define and classify fitness poses
6. Output the text description
   
