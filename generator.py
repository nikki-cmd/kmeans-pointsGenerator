import pygame
import random

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

generated = False
while True:
    if not generated:
        for i in range(0, 20):
            new_point = [pos1[0] + random.randint(-30, 30), pos1[1] + random.randint(-30, 30)]
            points.append(Point(new_point[0], new_point[1]))
            pygame.draw.circle(screen, "black", new_point, radius)
            cluster1.append(new_point)

        for i in range(0, 20):
            new_point = [pos2[0] + random.randint(-30, 30), pos2[1] + random.randint(-30, 30)]
            points.append(Point(new_point[0], new_point[1]))
            pygame.draw.circle(screen, "black", new_point, radius)
            cluster2.append(new_point)
            
        for i in range(0, 20):
            new_point = [pos3[0] + random.randint(-30, 30), pos3[1] + random.randint(-30, 30)]
            points.append(Point(new_point[0], new_point[1]))
            pygame.draw.circle(screen, "black", new_point, radius)
            cluster3.append(new_point)
        generated = True
            
        pygame.display.update()
        print(cluster1, cluster2, cluster3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()