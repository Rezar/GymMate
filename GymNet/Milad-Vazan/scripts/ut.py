import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plt_show(i,dataset):
    print(dataset.name[i])
    k11 = eval(dataset.X_LShoulder[i])
    k12 = eval(dataset.Y_LShoulder[i])
    k13 = eval(dataset.X_RShoulder[i])
    k14 = eval(dataset.Y_RShoulder[i])
    k19 = eval(dataset.X_LWrist[i])
    k20 = eval(dataset.Y_LWrist[i])
    k21 = eval(dataset.X_RWrist[i])
    k22 = eval(dataset.Y_RWrist[i])
    k23 = eval(dataset.X_LHip[i])
    k24 = eval(dataset.Y_LHip[i])
    k25 = eval(dataset.X_RHip[i])
    k26 = eval(dataset.Y_RHip[i])
    k27 = eval(dataset.X_LKnee[i])
    k28 = eval(dataset.Y_LKnee[i])
    k29 = eval(dataset.X_Rknee[i])
    k30 = eval(dataset.Y_Rknee[i])
    k31 = eval(dataset.X_LAnkle[i])
    k32 = eval(dataset.Y_LAnkle[i])
    k33 = eval(dataset.X_RAnkle[i])
    k34 = eval(dataset.Y_RAnkle[i])

    


    plt.plot(k11,'r')
    plt.title(dataset.name[i]+"  "+"X:X_LShoulder")
    plt.show()
    plt.plot(k12,'g')
    plt.title(dataset.name[i]+"  "+"Y:X_LShoulder")
    plt.show()


    plt.plot(k13,'r')
    plt.title(dataset.name[i]+"  "+"X:RShoulder")
    plt.show()
    plt.plot(k14,'g')
    plt.title(dataset.name[i]+"  "+"Y:RShoulder")
    plt.show()


   

    plt.plot(k19,'r')
    plt.title(dataset.name[i]+"  "+"X:LWrist")
    plt.show()
    plt.plot(k20,'g')
    plt.title(dataset.name[i]+"  "+"Y:LWrist")
    plt.show()

    plt.plot(k21,'r')
    plt.title(dataset.name[i]+"  "+"X:Rwrist")
    plt.show()
    plt.plot(k22,'g')
    plt.title(dataset.name[i]+"  "+"Y:Rwrist")
    plt.show()

    plt.plot(k23,'r')
    plt.title(dataset.name[i]+"  "+"X:LHip")
    plt.show()
    plt.plot(k24,'g')
    plt.title(dataset.name[i]+"  "+"Y:LHip")
    plt.show()

    plt.plot(k25,'r')
    plt.title(dataset.name[i]+"  "+"X:RHip")
    plt.show()
    plt.plot(k26,'g')
    plt.title(dataset.name[i]+"  "+"Y:RHip")
    plt.show()

    plt.plot(k27,'r')
    plt.title(dataset.name[i]+"  "+"X:LKnee")
    plt.show()
    plt.plot(k28,'g')
    plt.title(dataset.name[i]+"  "+"Y:LKnee")
    plt.show()

    plt.plot(k29,'r')
    plt.title(dataset.name[i]+"  "+"X:Rknee")
    plt.show()
    plt.plot(k30,'g')
    plt.title(dataset.name[i]+"  "+"Y:Rknee")
    plt.show()

    plt.plot(k31,'r')
    plt.title(dataset.name[i]+"  "+"X:LAnkle")
    plt.show()
    plt.plot(k32,'g')
    plt.title(dataset.name[i]+"  "+"Y:LAnkle")
    plt.show()

    plt.plot(k33,'r')
    plt.title(dataset.name[i]+"  "+"X:RAnkle")
    plt.show()
    plt.plot(k34,'g')
    plt.title(dataset.name[i]+"  "+"Y:RAnkle")
    plt.show()


