import numpy as np

def k_means_cluster(k, c1, c2, c3, points):
    # Initialization: choose k centroids (Forgy, Random Partition, etc.)
    centroids = [c1, c2, c3]
    
    # Initialize clusters list
    clusters = [[] for _ in range(k)]
    
    # Loop until convergence
    converged = False
    while not converged:
        # Clear previous clusters
        clusters = [[] for _ in range(k)]
    
        # Assign each point to the "closest" centroid 
        for point in points:
            distances_to_each_centroid = [dist(point, centroid) for centroid in centroids]
            cluster_assignment = np.argmin(distances_to_each_centroid)
            clusters[cluster_assignment].append(point)
        
        # Calculate new centroids
        #   (the standard implementation uses the mean of all points in a
        #     cluster to determine the new centroid)
        new_centroids = [calculate_centroid(cluster) for cluster in clusters]
        print(new_centroids)
        
        converged = (new_centroids == centroids)
        centroids = new_centroids
        
        if converged:
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
    
    return [sum_x/3, sum_y/3]
    
    
    