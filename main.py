import pygame
import random
from kmeans import k_means_cluster, calculate_centroid, dist
import matplotlib.pyplot as plt
import time
import numpy as np
from operator import itemgetter

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def find_elbow(array):
    values = [item[1] for item in array]
    first_diff = np.diff(values)
    second_diff = np.diff(first_diff)
    elbow_point = np.argmin(second_diff) + 2  # +2 из-за того, что второе изменение имеет длину на 2 меньше
    
    return array[elbow_point][0]

def calc_wcss(clusters):
    wcss = 0
    for cluster in clusters:
        centroid = calculate_centroid(cluster)
        for point in cluster:
            distance = np.sqrt((point[0] - centroid[0])**2 + (point[1] - centroid[1])**2)
            wcss += distance ** 2
    return wcss

def print_centroid(screen, coords, radius):
    pygame.draw.circle(screen, "black", coords, radius)
    pygame.display.update()

def generate_points(core):
    cluster = []
    for i in range(0, 10):
        new_point = [core[0] + random.randint(-30, 30), core[1] + random.randint(-30, 30)]
        cluster.append(new_point)
    return cluster
        
def generate_core():
    pos = [random.randint(0, 600), random.randint(0, 400)]
    return pos


def print_clusters(screen, cluster, radius):
    colors =  ['blue', 'cyan', 'gold', 'gray', 'green', 'orange', 'purple', 'red', 'violet', 'yellow']
    color = colors[random.randint(0, len(colors)- 1)]
    for pos in cluster:
        if pos:
            coords = tuple(pos)
            pygame.draw.circle(screen, color, coords, radius)
    
    pygame.display.update()

def print_final_clusters(screen, clusters, radius):
    colors =  [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255) for _ in range(len(clusters))]
    for i in range(0, len(clusters)):
        for pos in clusters[i]:
            if pos:
                coords = tuple(pos)
                pygame.draw.circle(screen, colors[i], coords, radius)
    
    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill("#FFFFFF")
pygame.display.update()

radius = 5


cores = [generate_core() for _ in range(random.randint(4, 9))]

expected_clusters = len(cores)

list_points = []

for i in range(0, len(cores)):
    list_points += generate_points(cores[i])

print_clusters(screen, list_points, radius)

unstaged_points = list_points

generated = False
    
f_logs = []
            
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            pygame.draw.circle(screen, "black", pos, radius)
            pygame.display.update()
            unstaged_points.append(pos)
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for k in range(1, len(unstaged_points)):
                    clusters = k_means_cluster(k, unstaged_points)
                    screen.fill((255,255,255))
                    for cluster in clusters:
                        print_clusters(screen, cluster, radius)
                        print_centroid(screen, calculate_centroid(cluster), radius)
                    #time.sleep(1)            
                    f_logs += [[k, calc_wcss(clusters)]]
                print(f_logs)
                x = []
                y = []
                for i in range(0, len(f_logs)):
                    x.append(f_logs[i][0])
                    y.append(f_logs[i][1])
                x = np.array(x)
                y = np.array(y)
                plt.plot(x, y)
                plt.show()
                    
                optimal_klusters = find_elbow(f_logs)
                clusters = k_means_cluster(optimal_klusters, unstaged_points)
                screen.fill((255,255,255))
                
                print_final_clusters(screen, clusters, radius)
                print(f'clusters expected:{expected_clusters} got clusters:{optimal_klusters}')
                
            