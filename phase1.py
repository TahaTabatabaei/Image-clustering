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
# (400 * 5600) array for images
imageArr = list()
# array for actuall labels
myLabels = list()
# loop to transform images to array based by their pixels
for i in range(1,401):
    if (i%10 == 1):
        k +=1
    # set label
    myLabels.append(k-1)

    # read image from file
    si = str(i)
    sk = str(k)
    st = si+"_"+sk
    myImage = image.imread("E:/taha/code/HW1/src/ORL/"+st+".jpg")
    # turn (80*70) image into 5600 1dim array
    dataFlat = np.ndarray.flatten(myImage)
    # add image to list
    imageArr.append(dataFlat)

# KMeans algorithem
from sklearn.cluster import KMeans

kmeans = KMeans(init="random",n_clusters=40).fit(imageArr)
# pprint(kmeans.labels_)

# DBSCAN algorithem
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=2550,min_samples=5).fit(imageArr)
# pprint(dbscan.labels_)

# Agglomerative algorithems
from sklearn.cluster import AgglomerativeClustering

aglo_avg = AgglomerativeClustering(linkage='average',n_clusters=40).fit(imageArr)
aglo_single = AgglomerativeClustering(linkage='single',n_clusters=40).fit(imageArr)
aglo_comp = AgglomerativeClustering(linkage='complete',n_clusters=40).fit(imageArr)
# pprint(aglo_avg.labels_)
# pprint(aglo_single.labels_)
# pprint(aglo_comp.labels_)

# rand Index algorithem
from Rand_Index import rand_Index

print("\n*************\nkKMeans(n_clusters=40):")
print("RI:",rand_Index(myLabels,kmeans.labels_))

print("\n*************\nDBSCAN(eps=2550,min_samples=5):")
print("RI:",rand_Index(myLabels,dbscan.labels_))

print("\n*************\nAgglomerativeClustering(linkage='average',n_clusters=40):")
print("RI:",rand_Index(myLabels,aglo_avg.labels_))

print("\n*************\nAgglomerativeClustering(linkage='single',n_clusters=40):")
print("RI:",rand_Index(myLabels,aglo_single.labels_))

print("\n*************\nAgglomerativeClustering(linkage='complete',n_clusters=40):")
print("RI:",rand_Index(myLabels,aglo_comp.labels_))

