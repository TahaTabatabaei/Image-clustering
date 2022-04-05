from pprint import pprint
import numpy as np
from pprint import pprint
def rand_Index(labels_true,labels_predicted):
    trueP=0
    trueN=0
    falseN=0
    falseP=0
    for i in range(len(labels_true)):
        for j in range(i+1 ,len(labels_true)):
            pair_true = [0,0] 
            pair_true[0] = labels_true[i]
            pair_true[1] = labels_true[j]
            pair_pred = [0,0]
            pair_pred[0] = labels_predicted[i]
            pair_pred[1] = labels_predicted[j]
            if(pair_true[0] == pair_true[1]):
                if(pair_pred[0] == pair_pred[1]):
                    trueP +=1
                else:
                    falseN +=1
            else:
                if(pair_pred[0] == pair_pred[1]):
                    falseP +=1
                else:
                    trueN +=1
    return (trueP + trueN)

