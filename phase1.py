from random import random
from typing import List
from matplotlib import image
from matplotlib import pyplot
from numpy import asarray
import numpy as np


# print(myImage.dtype)
# print(myImage.shape)

# data = asarray(myImage)

# print(data[79])

# data2 = np.ndarray.flatten(data)
# print(data2)
k=0

st=""
imageArr = list()
for i in range(1,411):
    if (i%10 == 1):
        k +=1
    si = str(i)
    sk = str(k)
    st = si+"_"+sk
    # print(st)
    myImage = image.imread("E:/taha/code/HW1/src/ORL/"+st+".jpg")
    print(myImage.shape)
    data = asarray(myImage)
    dataFlat = np.ndarray.flatten(data)
    imageArr.append(dataFlat)

from sklearn.cluster import KMeans
kmean = KMeans(init=random,n_clusters=41).fit(imageArr)
    
