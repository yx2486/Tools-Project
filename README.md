# Tools Project: Clustering Methods
***Section 002: Yuan Xin, Hanjiao Zhang, Yuanqi Gai***

## Description:
***Clustering*** is a simple python library that could perform Hierachical Clustering. It could easily create different clusters from a list of data provided. In this package, two types of linkages can be performed, which are "single" and "complete". "sinlge" returns the distance of two closest points and "complete" returns the distance of two farthest points.

***K-Means Clustering*** is to find clusters in the data, with the number of clusters represented by the variable K. The algorithm works iteratively to assign each data point to one of K groups in which each point belongs to the cluster with the nearest mean based on the features that are provided.

## Basic Algorithm of Hierachical Clustering:
1. Compute the proximity matrix based on data provided
2. Let each data point be a cluster
3. **Repeat**: Merge the two closest clusters; Update the proximity matrix
4. **Until**: only a single cluster remains

## Basic Algorithm of K-Means Clustering:
1. Initialize k points, called clusters, randomly.
2. Calculate the centroid of each cluster.
3. Assign each item to its closest cluster based on the distance between each centroid and item.
4. **Repeat**: Repeat the process for a given number of iterations, moving items and at the end, we have our clusters.
5. **Until**: classify each item to its closest cluster

**Important Documentation:**
https://www.datascience.com/blog/k-means-clustering

## How to Use:
**Note:** 
Please place your python file in the same directory as our library

**Sample code and output:**

* Hierarchical Clustering
```python
>>> from Hierarchical_Clustering import *              # To import the library
```
EX 1. To get clusters of data with distance closer than 5 using single linkage method
  
```python
>>> data = [5,6,10,1,18]
>>> HierarchicalClustering(data,single).distance(5)
[[18], [1, 10, 5, 6]]
```
EX 2. To get clusters of data with distance closer than 5 using complete linkage method
```python
>>> data = [5,6,10,1,18]
>>> HierarchicalClustering(data,complete).distance(5)
[[18], [1], [10, 5, 6]]
```
