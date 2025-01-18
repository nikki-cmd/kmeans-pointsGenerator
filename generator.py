#программа распозновая чисел(отделять цифры друг от друга с помощью алгоритмов)
import pygame
import random
from kmeans import k_means_cluster
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
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
              
        if not generated:
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
            generated = True
                
            pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            pygame.draw.circle(screen, "black", pos, radius)
            pygame.display.update()
            unstaged_points.append(pos)
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                clusters = k_means_cluster(3, pos1, pos2, pos3, unstaged_points)
                
                for p in clusters[0]:
                    cluster1.append(list(p))
                    
                for p in clusters[1]:
                    cluster2.append(p)
                    
                for p in clusters[2]:
                    cluster3.append(p)
                
                screen.fill((255,255,255))
                pygame.display.update()
                
                '''if len(clusters[0]) != 0:
                    for i in range(0, len(cluster1)):
                        pos = tuple(cluster1[i])
                        if pos:
                            print(pos)
                            pygame.draw.circle(screen, "red", pos, radius)
                
                if len(clusters[1]) != 0:
                    for i in range(0, len(cluster2)):
                        pos = tuple(cluster2[i])
                        if pos:
                            print(pos)
                            pygame.draw.circle(screen, "green", pos, radius)
                
                if len(clusters[2]) != 0:
                    for i in range(0, len(cluster3)):
                        pos = tuple(cluster3[i])
                        if pos:
                            print(pos)
                            pygame.draw.circle(screen, "blue", pos, radius)'''
                
                print_clusters(screen, cluster1, cluster2, cluster3, radius)
                
                pygame.display.update()
                
                clusters = []
                unstaged_points = []
            