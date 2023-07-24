# Image-clustering
naive image clustring (university assignment)

In the first phase, attempt is to try 3 diffrent clustering methods:
K-means, DBSACN & Agglomerative

also, there is a basic implementation of "Rand Index" metric for result evaluating in `Rand_index.py`

In the second phase, we find a way to estimate epsilon parameter, in order to improve DBSACN clustering.
we observe the average distance of a data to its 5 nearest nighboors. this average lead us to find a reasonable
epsilon. We assume that this average distance is a good estimation for density distribution of dataset.
