import pygame

pygame.init()


def music_in_game():
    pygame.mixer.music.load("game_music.wav")
    pygame.mixer.music.play(-1)  # -1 pour que la musique se joue en boucle


def music_score():
    pygame.mixer.music.load("score_music.wav")
    pygame.mixer.music.play(-1)  # -1 pour que la musique se joue en boucle
