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
                print('clusters:', clusters)
            