
# visualization
### X Axis and Y Axis 

```python
from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
dataset = pd.read_csv('/content/drive/MyDrive/workoutMOVIES/Data/Data Label (Y convert)/60.csv')
import numpy as np
#X Axis
import matplotlib.pyplot as plt
for i in range(len(dataset)):
  print(i)
  x1=eval(dataset.xX_left_shoulder[i])
  x2=eval(dataset.xX_right_shoulder[i])
  x3=eval(dataset.xX_left_elbow[i])
  x4=eval(dataset.xX_right_elbow[i])
  x5=eval(dataset.xX_left_wrist[i])
  x6=eval(dataset.xX_right_wrist[i])
  x7=eval(dataset.xX_left_hip[i])
  x8=eval(dataset.xX_right_hip[i])
  x9=eval(dataset.xX_left_knee[i])
  x10=eval(dataset.xX_right_knee[i])
  x11=eval(dataset.xX_left_ankle[i])
  x12=eval(dataset.xX_right_ankle[i])
  fig, (ax1, ax2,ax3, ax4,ax5, ax6,ax7, ax8,ax9, ax10,ax11, ax12) = plt.subplots(12)
  fig.suptitle(f'X Axis for {dataset.name[i]} With {len(eval(dataset.xX_right_hip[i]))} frames')
  fig.set_size_inches(8, 6)

  ax1.plot(x1,'k')
  ax1.set_yticks([])
  ax1.set_xticks([])
  ax1.set(ylabel='Lsh')
  ax2.plot(x2,'k')
  ax2.set_yticks([])
  ax2.set_xticks([])
  ax2.set(ylabel='Rsh')
  ax3.plot(x3,'k')
  ax3.set_yticks([])
  ax3.set_xticks([])
  ax3.set(ylabel='Lel')
  ax4.plot(x4,'k')
  ax4.set_yticks([])
  ax4.set_xticks([])
  ax4.set(ylabel='Rel')

  ax5.plot(x5,'k')
  ax5.set_yticks([])
  ax5.set_xticks([])
  ax5.set(ylabel='Lwr')

  ax6.plot(x6,'k')
  ax6.set_yticks([])
  ax6.set_xticks([])
  ax6.set(ylabel='Rwi')

  ax7.plot(x7,'k')
  ax7.set_yticks([])
  ax7.set_xticks([])
  ax7.set(ylabel='Lhip')

  ax8.plot(x8,'k')
  ax8.set_yticks([])
  ax8.set_xticks([])
  ax8.set(ylabel='Rhip')

  ax9.plot(x9,'k')
  ax9.set_yticks([])
  ax9.set_xticks([])
  ax9.set(ylabel='Lknee')

  ax10.plot(x10,'k')
  ax10.set_yticks([])
  ax10.set_xticks([])
  ax10.set(ylabel='RKnee')

  ax11.plot(x11,'k')
  ax11.set_yticks([])
  ax11.set_xticks([])
  ax11.set(ylabel='Lank')

  ax12.plot(x12,'k')
  ax12.set_yticks([])
  ax12.set_xticks([])
  ax12.set(ylabel='Rank')
      
  plt.savefig(f'/content/drive/MyDrive/plot/test/{dataset.name[i]}_X.png',dpi=100)
  
  
  #Y Axis
  for i in range(len(dataset)):
    print(i)
    x1=eval(dataset.yY_left_shoulder[i])
    x2=eval(dataset.yY_right_shoulder[i])
    x3=eval(dataset.yY_left_elbow[i])
    x4=eval(dataset.yY_right_elbow[i])
    x5=eval(dataset.yY_left_wrist[i])
    x6=eval(dataset.yY_right_wrist[i])
    x7=eval(dataset.yY_left_hip[i])
    x8=eval(dataset.yY_right_hip[i])
    x9=eval(dataset.yY_left_knee[i])
    x10=eval(dataset.yY_right_knee[i])
    x11=eval(dataset.yY_left_ankle[i])
    x12=eval(dataset.yY_right_ankle[i])
    fig, (ax1, ax2,ax3, ax4,ax5, ax6,ax7, ax8,ax9, ax10,ax11, ax12) = plt.subplots(12)
    fig.suptitle(f'X Axis for {dataset.name[i]} With {len(eval(dataset.xX_right_hip[i]))} frames')
    fig.set_size_inches(8, 6)

    ax1.plot(x1,'k')
    ax1.set_yticks([])
    ax1.set_xticks([])
    ax1.set(ylabel='Lsh')
    ax2.plot(x2,'k')
    ax2.set_yticks([])
    ax2.set_xticks([])
    ax2.set(ylabel='Rsh')
    ax3.plot(x3,'k')
    ax3.set_yticks([])
    ax3.set_xticks([])
    ax3.set(ylabel='Lel')
    ax4.plot(x4,'k')
    ax4.set_yticks([])
    ax4.set_xticks([])
    ax4.set(ylabel='Rel')

    ax5.plot(x5,'k')
    ax5.set_yticks([])
    ax5.set_xticks([])
    ax5.set(ylabel='Lwr')

    ax6.plot(x6,'k')
    ax6.set_yticks([])
    ax6.set_xticks([])
    ax6.set(ylabel='Rwi')

    ax7.plot(x7,'k')
    ax7.set_yticks([])
    ax7.set_xticks([])
    ax7.set(ylabel='Lhip')

    ax8.plot(x8,'k')
    ax8.set_yticks([])
    ax8.set_xticks([])
    ax8.set(ylabel='Rhip')

    ax9.plot(x9,'k')
    ax9.set_yticks([])
    ax9.set_xticks([])
    ax9.set(ylabel='Lknee')

    ax10.plot(x10,'k')
    ax10.set_yticks([])
    ax10.set_xticks([])
    ax10.set(ylabel='RKnee')

    ax11.plot(x11,'k')
    ax11.set_yticks([])
    ax11.set_xticks([])
    ax11.set(ylabel='Lank')

    ax12.plot(x12,'k')
    ax12.set_yticks([])
    ax12.set_xticks([])
    ax12.set(ylabel='Rank')

    plt.savefig(f'/content/drive/MyDrive/plot/test/{dataset.name[i]}_Y.png',dpi=100)
```
