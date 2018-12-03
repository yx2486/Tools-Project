
# median funcion finds the median in a list
def median(list_):
    n = len(list_)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(list_)[n//2]
    else:
            return sum(sorted(list_)[n//2-1:n//2+1])/2.0

# centroid function finds the centroid of a list of tuples
# return the result as tuple
def centroid(data):
    result = []
    for i in range(len(data[0])):
        value = []
        for number in data:
            value.append(number[i])
            med = median(value)
        result.append(med)
    return tuple(result)

# euclidean calculates the eucledian distance
# same as minkowski distance with power 2 (norm)
# it is then used to find the distance between each tuple and the centroid of clusters

def euclidean(tuple1, tuple2):
    import numpy as np
    array1 = np.array(tuple1)
    array2 = np.array(tuple2)
    return np.linalg.norm(array1-array2)

# build class KMeansClustering
class KMeansClustering():
    def __init__(self, data):
        self._clusters = []
        self._data = data
        self.distance = euclidean
    
    # assign item(tuple) from a given cluster to the closest cluster
    def check(self, item, original_cluster):
        result = False
        closest_cluster = None
        
        for cluster in self._clusters:
            if self.distance(item, centroid(cluster)) < self.distance(item, centroid(original_cluster)):
                closest_cluster = cluster
                result = True
                
        if result == True:
            self.change_cluster(item, original_cluster, closest_cluster)
            
        return result
    
    # Move item(tuple) from one cluster to anoter
    def change_cluster(self, item, original_cluster, new_cluster):
        item_index = original_cluster.index(item)
        new_cluster.append(original_cluster.pop(item_index))

    def set_clusters(self, data, clustercount):
        #initialize the clusters
        self._clusters = [] #empty lists
        for i in range(clustercount):
            self._clusters.append([])
        
        # distribute items into clusters
        count = 0
        for item in data:
            self._clusters[count % clustercount].append(item)
            count += 1

    # get the final clusters
    def getclusters(self, clustercount):
        self.set_clusters(self._data, clustercount)
        
        moved = True
        while moved is True:
            moved = False
            for cluster in self._clusters:
                for item in cluster:
                    result = self.check(item, cluster)
                    if moved is False:
                        moved = result
                        
        return self._clusters

