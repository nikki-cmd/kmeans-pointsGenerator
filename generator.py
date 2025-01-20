import pygame
import random
from kmeans import k_means_cluster, calculate_centroid, dist
import matplotlib.pyplot as plt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
  
def generate_core():
    pos1 = [random.randint(0, 600), random.randint(0, 400)]
    pos2 = [random.randint(0, 600), random.randint(0, 400)]
    pos3 = [random.randint(0, 600), random.randint(0, 400)]
    
    generated = False
    
    while not generated:
        if dist(pos1, pos2) < 200 and dist(pos2, pos3) < 200 and dist(pos1, pos3) < 200:
            pos1 = [random.randint(0, 600), random.randint(0, 400)]
            pos2 = [random.randint(0, 600), random.randint(0, 400)]
            pos3 = [random.randint(0, 600), random.randint(0, 400)]
        else:
            return [pos1, pos2, pos3]


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
    pygame.draw.circle(screen, "brown", coords, radius)
    
    coords = calculate_centroid(cluster1)
    pygame.draw.circle(screen, "brown", coords, radius)
    
    coords = calculate_centroid(cluster2)
    pygame.draw.circle(screen, "brown", coords, radius)
    
    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill("#FFFFFF")
pygame.display.update()

radius = 5

points = []

new_points = []

pos1 = generate_core()[0]
pos2 = generate_core()[1]
pos3 = generate_core()[2]

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
                unstaged_points += cluster1
                unstaged_points += cluster2
                unstaged_points += cluster3
                c1 = calculate_centroid(cluster1)
                c2 = calculate_centroid(cluster2)
                c3 = calculate_centroid(cluster3)
                clusters = k_means_cluster(3, c1, c2, c3, unstaged_points, cluster1, cluster2, cluster3)
                for p in clusters[0]:
                    cluster1.append(list(p))
                    
                for p in clusters[1]:
                    cluster2.append(p)
                    
                for p in clusters[2]:
                    cluster3.append(p)
                
                screen.fill((255,255,255))
                pygame.display.update()
                print_clusters(screen, cluster1, cluster2, cluster3, radius)
                
                pygame.display.update()
                
                clusters = []
                unstaged_points = []
            