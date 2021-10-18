#input：prediction picture and ground truth 
#output:dice coefficient

import numpy as np
def cal_dice(pred,target):
    #print(pred.shape[0],pred.shape[1])
    #same=0
    s=[]
    for i in range(pred.shape[0]):
        for j in range(pred.shape[1]):
            if pred[i,j]==target[i,j]:
                #same+=1
                s.append(pred[i,j])
    m1=np.linalg.norm(s,ord=1)
    m2=np.linalg.norm(pred.flatten(),ord=1)+np.linalg.norm(target.flatten(),ord=1)
    dice=2*m1/(m2+1e-8)
    return dice
