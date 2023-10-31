import pygame

# Initialisation de pygame
pygame.init()

pygame.mixer.music.load("jeu_nsi_joan_game.wav")
pygame.mixer.music.play(-1)  # -1 pour que la musique se joue en boucle
