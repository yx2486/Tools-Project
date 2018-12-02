'''       
two linkage methods: single, complete.
'''
def single(cluster1,cluster2):
    min_c1 = min(cluster1)# find min, max within cluster
    max_c1 = max(cluster1)
    min_c2 = min(cluster2)
    max_c2 = max(cluster2)
    distance1 = abs(min_c2-max_c1) 
    distance2 = abs(min_c1-max_c2)
    distance = min(distance1,distance2)
    return distance

#complete linkage, this will return the disrance of two farthest points
def complete(cluster1,cluster2):
    min_c1 = min(cluster1)
    max_c1 = max(cluster1)
    min_c2 = min(cluster2)
    max_c2 = max(cluster2)
    distance1 = abs(max_c2-min_c1)
    distance2 = abs(max_c1-min_c2)
    distance = max(distance1,distance2)
    return distance



'''
Matrix class
'''
class Matrix(object): # object representation of the matrix
    def __init__(self, data, function):
        self.data = data           # list of data
        self.function = function   # function used to calculate values
    
    def getmatrix(self): # generate the matrix
        self.matrix = []
        for rowindex, item1 in enumerate(self.data):
            row = {}
            if not hasattr(item1, '__iter__') or isinstance(item1, tuple):
                item1 = [item1]
            for colindex, item2 in enumerate(self.data):
                if not hasattr(item2, '__iter__') or isinstance(item2, tuple):
                    item2 = [item2]
                if colindex < rowindex:
                    pass
                else:
                    row[colindex] = self.function(item1,item2)
                
            for colindex, item2 in enumerate(self.data):
                if colindex >= rowindex:
                    break
                row[colindex] = self.matrix[colindex][rowindex]
            row_indexed = [row[index] for index in range(len(self.data))]
            self.matrix.append(row_indexed)
            
            
            
'''
Cluster class
'''
def flatten(list_):
    flattened_items = []
    for item in list_:
        if hasattr(item, 'items'):
            flattened_items = flattened_items + flatten(item.items)
        else:
            flattened_items.append(item)
    return flattened_items  

class Cluster():
    def __init__(self,clust_distance,*args):
        self.clust_distance = clust_distance
        if len(args)==0:
            self.items = []
        else:
            self.items = args
            
    def __iter__(self):
        for item in self.items:
            if isinstance(item, Cluster):
                for recursed_item in item:
                    yield recursed_item
            else:
                yield item
                
    def distance(self, max_distance): # max_distance is where the user would like to separate the clusters
        clust1 = self.items[0]
        clust2 = self.items[1]
        
        # check the cluster's level and flattern them if necessary

        # if both clusters are below the max_distance, just flatten them
        if self.clust_distance <= max_distance:
            return [flatten(self.items)]
        
        # this part checks if one of the clusters is above the max_distance
        # if yes, recursively apply the function
        if isinstance(clust1, Cluster) and clust1.clust_distance <= max_distance:
            if isinstance(clust2, Cluster):
                return [flatten(clust1.items)] + clust2.distance(max_distance)
            else:
                return [flatten(clust1.items)] + [[clust2]]
        elif isinstance(clust2, Cluster) and clust2.clust_distance <= max_distance:
            if isinstance(clust1, Cluster):
                return clust1.distance(max_distance) + [flatten(clust2.items)]
            else:
                return [[clust1]] + [flatten(clust2.items)]

        # this part checks if both clusters are above the max_distance
        # if yes, recursively apply the function
        if isinstance(clust1, Cluster) and isinstance(clust2, Cluster):
            return clust1.distance(max_distance) + clust2.distance(max_distance)
        elif isinstance(clust1, Cluster):
            return clust1.distance(max_distance) + [[clust2]]
        elif isinstance(clust2, Cluster):
            return [[clust1]] + clust2.distance(max_distance)
        else:
            return [[clust1], [clust2]]

        

'''
HierarchicalClustering class
'''
class HierarchicalClustering():
    def __init__(self,data,linkage):
        self._data = data
        self.linkage = linkage
    
    # this function performs clustering   
    def cluster(self):
        clust_distance = 0
        matrix = []
        while matrix == [] or len(matrix) > 2:
            dist_matrix = Matrix(self._data,self.linkage)
            dist_matrix.getmatrix()
            matrix = dist_matrix.matrix
            
            # find the closest distance
            closest = None
            min_dist = None
            rowindex = 0
            for row in matrix:
                colindex = 0
                for cell in row:
                    if rowindex != colindex:
                        if (min_dist is None) or cell < min_dist:
                            closest = (rowindex, colindex)
                            min_dist = cell
                    colindex +=1
                rowindex += 1
            clust_distance = matrix[closest[0]][closest[1]]
            cluster = Cluster(clust_distance, self._data[closest[0]],self._data[closest[1]])
            
            # remove items after clustering                                   
            if closest[0] > closest[1]:
                self._data.remove(self._data[closest[0]])
                self._data.remove(self._data[closest[1]])
            else:
                self._data.remove(self._data[closest[1]])
                self._data.remove(self._data[closest[0]])
            self._data.append(cluster)
    
    # this function returns all clusters with max_distance                                       
    def distance(self,max_distance):
        self.cluster() 
        return self._data[0].distance(max_distance)                                     
                     

