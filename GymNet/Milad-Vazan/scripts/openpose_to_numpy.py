import json, glob
import pandas as pd
import numpy as np
def openpose_json_to_npy(Address_JSON,name):
    merged_json = []
    for json_file in glob.glob(f"{Address_JSON}*json"):
        with open(json_file, "rb") as file:
          json_data = json.load(file)
          merged_json += json_data["people"]
    to_json = json.dumps(merged_json)
    CSV_openpose = pd.read_json(to_json)
    CSV_openpose.to_csv(index=False,columns= ['person_id', 'pose_keypoints_2d'])
    A=[]
    for i in range (len(CSV_openpose.pose_keypoints_2d)):
        A.append(CSV_openpose.pose_keypoints_2d[i])
    arr = np.array(A)
    np.save(f"npy/{name}", arr)