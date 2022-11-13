
import pandas as pd
import numpy as np
def X_Y_TO_CSV(nn,name_n):
    add="csv/"
    add_n="npy/"
    k = np.load(f"{add_n}{nn}")
    X_LShoulder=[]
    Y_LShoulder=[]
    C_LShoulder=[]

    X_RShoulder=[]
    Y_RShoulder=[]
    C_RShoulder=[]



    X_LWrist=[]
    Y_LWrist=[]
    C_LWrist=[]

    X_RWrist=[]
    Y_RWrist=[]
    C_RWrist=[]

    X_LHip=[]
    Y_LHip=[]
    C_LHip=[]

    X_RHip=[]
    Y_RHip=[]
    C_RHip=[]

    X_LKnee=[]
    Y_LKnee=[]
    C_LKnee=[]

    X_Rknee=[]
    Y_Rknee=[]
    C_Rknee=[]

    X_LAnkle=[]
    Y_LAnkle=[]
    C_LAnkle=[]

    X_RAnkle=[]
    Y_RAnkle=[]
    C_RAnkle=[]

    for i in range(len(k)):
       

        X_LShoulder.append(k[i][15])
        Y_LShoulder.append(k[i][16])
        C_LShoulder.append(k[i][17])

        X_RShoulder.append(k[i][6])
        Y_RShoulder.append(k[i][7])
        C_RShoulder.append(k[i][8])

       

        X_LWrist.append(k[i][21])
        Y_LWrist.append(k[i][22])
        C_LWrist.append(k[i][23])


        X_RWrist.append(k[i][12])
        Y_RWrist.append(k[i][13])
        C_RWrist.append(k[i][14])

        X_LHip.append(k[i][36])
        Y_LHip.append(k[i][37])
        C_LHip.append(k[i][38])

        X_RHip.append(k[i][27])
        Y_RHip.append(k[i][28])
        C_RHip.append(k[i][29])

        X_LKnee.append(k[i][39])
        Y_LKnee.append(k[i][40])
        C_LKnee.append(k[i][41])


        X_Rknee.append(k[i][30])
        Y_Rknee.append(k[i][31])
        C_Rknee.append(k[i][32])


        X_LAnkle.append(k[i][42])
        Y_LAnkle.append(k[i][43])
        C_LAnkle.append(k[i][44])

        X_RAnkle.append(k[i][33])
        Y_RAnkle.append(k[i][34])
        C_RAnkle.append(k[i][35])
        
    
    
        
    
    df_x = pd.DataFrame({"name":name_n
                        ,"X_LShoulder":[X_LShoulder],"Y_LShoulder":[Y_LShoulder],"C_LShoulder":[C_LShoulder]
                        ,"X_RShoulder":[X_RShoulder],"Y_RShoulder":[Y_RShoulder],"C_RShoulder":[C_RShoulder]
                        ,"X_LWrist":[X_LWrist],"Y_LWrist":[Y_LWrist],"C_LWrist":[C_LWrist]
                        ,"X_RWrist":[X_RWrist],"Y_RWrist":[Y_RWrist],"C_RWrist":[C_RWrist]
                        ,"X_LHip":[X_LHip],"Y_LHip":[Y_LHip],"C_LHip":[C_LHip]
                        ,"X_RHip":[X_RHip],"Y_RHip":[Y_RHip],"C_RHip":[C_RHip]
                        ,"X_LKnee":[X_LKnee],"Y_LKnee":[Y_LKnee],"C_LKnee":[C_LKnee]
                        ,"X_Rknee":[X_Rknee],"Y_Rknee":[Y_Rknee],"C_Rknee":[C_Rknee]
                        ,"X_LAnkle":[X_LAnkle],"Y_LAnkle":[Y_LAnkle],"C_LAnkle":[C_LAnkle]
                        ,"X_RAnkle":[X_RAnkle],"Y_RAnkle":[Y_RAnkle],"C_RAnkle":[C_RAnkle]
})
    df_x.to_csv(f'{add}{name_n}.csv', index = False)
