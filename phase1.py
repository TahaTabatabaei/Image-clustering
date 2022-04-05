from cProfile import label
from ctypes import sizeof
from random import random
from typing import List
from matplotlib import image
from matplotlib import pyplot
import numpy as np
from pprint import pprint

k=0

st=""
imageArr = list()
for i in range(1,401):
    if (i%10 == 1):
        k +=1
    si = str(i)
    sk = str(k)
    st = si+"_"+sk
    # print(st)
    myImage = image.imread("E:/taha/code/HW1/src/ORL/"+st+".jpg")
    # print(i ,myImage.shape)
    # print(myImage)
    # data = np.asarray(myImage)
    # print(data)
    dataFlat = np.ndarray.flatten(myImage)
    imageArr.append(dataFlat)

from sklearn.cluster import KMeans

# kmeans = KMeans(init="random",n_clusters=40).fit(imageArr)
# pprint(kmeans.labels_)

from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=2550,min_samples=5).fit(imageArr)
pprint(dbscan.labels_)

from sklearn.cluster import AgglomerativeClustering

# aglo_avg = AgglomerativeClustering(linkage='average',n_clusters=40).fit(imageArr)
# aglo_single = AgglomerativeClustering(linkage='single',n_clusters=40).fit(imageArr)
# aglo_comp = AgglomerativeClustering(linkage='complete',n_clusters=40).fit(imageArr)

# pprint(aglo_comp.labels_)
