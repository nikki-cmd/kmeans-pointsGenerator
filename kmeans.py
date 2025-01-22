import numpy as np
import random


def k_means_cluster(k, points):
    centroids = [points[random.randint(0, len(points) - 1)] for _ in range(k)]
    
    clusters = [[] for _ in range(k)]
    done = False
    while not done:
        clusters = [[] for _ in range(k)]
        for point in points:
                distances_to_each_centroid = [dist(point, centroid) for centroid in centroids]
                cluster_assignment = np.argmin(distances_to_each_centroid)
                clusters[cluster_assignment].append(list(point))
                
        clusters = [x for x in clusters if x]
        new_centroids = [calculate_centroid(cluster) for cluster in clusters]
        done = (centroids == new_centroids)
        centroids = new_centroids
        if done:
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
    
    
    