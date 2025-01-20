import numpy as np


def k_means_cluster(k, c1, c2, c3, points, cluster1, cluster2, cluster3):
    centroids = [calculate_centroid(cluster1), calculate_centroid(cluster2), calculate_centroid(cluster3)]
    
    clusters = [[], [], []]
    
    for point in points:
            distances_to_each_centroid = [dist(point, centroid) for centroid in centroids]
            cluster_assignment = np.argmin(distances_to_each_centroid)
            clusters[cluster_assignment].append(list(point))
    return clusters

def dist(point, centroid):
    return np.sqrt((point[0] - centroid[0])**2 + (point[1] - centroid[1])**2)

def calculate_centroid(cluster):
    sum_x = 0
    sum_y = 0
    for x in range(0, len(cluster)):
        sum_x += cluster[x][0]
    
    for y in range(0, len(cluster)):
        sum_y += cluster[y][1]
    return [sum_x/len(cluster), sum_y/len(cluster)]
    
    
    