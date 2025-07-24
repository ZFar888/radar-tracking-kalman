import pygame
import numpy as np
from simulation import MovingObject
from radar import Radar
from kalman import KalmanFilter2D

WIDTH, HEIGHT = 800, 600
FPS = 60
SCALE = 10

DARK_BG = (30, 30, 30)
BLUE = (50, 150, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 100)

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radar Tracking with Kalman Filter")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial",18)


dt = 0.2
obj = MovingObject()
radar = Radar(noise_std=3.0)
kf = KalmanFilter2D()

true_trail = []
radar_trail = []
estimate_trail = []

def draw_circle(pos, color, radius=6):
    x, y = int(pos[0] * SCALE), int(pos[1] * SCALE)
    pygame.draw.circle(win, color, (x, HEIGHT - y), radius)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    true_pos = obj.update(dt)
    radar_pos = radar.get_noisy_position(true_pos)
    kf.predict()
    kf.update(radar_pos)
    estimate = kf.get_position()

    true_trail.append(true_pos.copy())
    radar_trail.append(radar_pos.copy())
    estimate_trail.append(estimate.copy())

    win.fill(DARK_BG)

    for pos in true_trail:
        draw_circle(pos, BLUE, radius=3)
    for pos in radar_trail:
        draw_circle(pos, RED, radius=2)
    for pos in estimate_trail:
        draw_circle(pos, GREEN, radius=2)

    draw_circle(true_pos, BLUE, radius=6)
    draw_circle(radar_pos, RED, radius=5)
    draw_circle(estimate, GREEN, radius=5)

    legend_blue = font.render("True position (Blue)",True, BLUE)
    legend_red = font.render("Radar Reading (Red)", True, RED)
    legend_green = font.render("Kalman Estimate (Green)", True, GREEN)


    win.blit(legend_blue, (10, 10))
    win.blit(legend_red, (10,30))
    win.blit(legend_green, (10,50))
    pygame.display.flip()

pygame.quit()
