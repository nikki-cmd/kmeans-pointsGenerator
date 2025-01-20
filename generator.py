#программа распозновая чисел(отделять цифры друг от друга с помощью алгоритмов)
import pygame
import random
from kmeans import k_means_cluster, calculate_centroid
import matplotlib.pyplot as plt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def dist(self, point):
		return np.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

def print_clusters(screen, cluster0, cluster1, cluster2, radius):
    for pos in cluster0:
        if pos:
            coords = tuple(pos)
            pygame.draw.circle(screen, "red", coords, radius)
            
    for pos in cluster1:
        if pos:
            coords = tuple(pos)
            pygame.draw.circle(screen, "green", coords, radius)
            
    for pos in cluster2:
        if pos:
            coords = tuple(pos)
            pygame.draw.circle(screen, "blue", coords, radius)
    
    coords = calculate_centroid(cluster0)
    pygame.draw.circle(screen, "black", coords, radius)
    
    coords = calculate_centroid(cluster1)
    pygame.draw.circle(screen, "black", coords, radius)
    
    coords = calculate_centroid(cluster2)
    pygame.draw.circle(screen, "black", coords, radius)
    
    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill("#FFFFFF")
pygame.display.update()

radius = 5

points = []

new_points = []


pos1 = [80, 50]
pos2 = [500, 300]
pos3 = [60, 330]

cluster1 = []
cluster2 = []
cluster3 = []

unstaged_points = []

generated = False

for i in range(0, 20):
    new_point = [pos1[0] + random.randint(-30, 30), pos1[1] + random.randint(-30, 30)]
    points.append(Point(new_point[0], new_point[1]))
    pygame.draw.circle(screen, "red", new_point, radius)
    cluster1.append(new_point)

for i in range(0, 20):
    new_point = [pos2[0] + random.randint(-30, 30), pos2[1] + random.randint(-30, 30)]
    points.append(Point(new_point[0], new_point[1]))
    pygame.draw.circle(screen, "green", new_point, radius)
    cluster2.append(new_point)
                
for i in range(0, 20):
    new_point = [pos3[0] + random.randint(-30, 30), pos3[1] + random.randint(-30, 30)]
    points.append(Point(new_point[0], new_point[1]))
    pygame.draw.circle(screen, "blue", new_point, radius)
    cluster3.append(new_point)
    
pygame.display.update()   
            
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
                c1 = calculate_centroid(cluster1)
                c2 = calculate_centroid(cluster2)
                c3 = calculate_centroid(cluster3)
                clusters = k_means_cluster(3, c1, c2, c3, unstaged_points, cluster1, cluster2, cluster3)
                print("got clusters")
                for p in clusters[0]:
                    cluster1.append(list(p))
                    
                for p in clusters[1]:
                    cluster2.append(p)
                    
                for p in clusters[2]:
                    cluster3.append(p)
                
                print("updated clusters")
                
                screen.fill((255,255,255))
                pygame.display.update()
                print_clusters(screen, cluster1, cluster2, cluster3, radius)
                
                pygame.display.update()
                
                clusters = []
                unstaged_points = []
            