import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(r'C:\Users\jose_\OneDrive\Documentos\Estudos\Python\Exercicios\ex021.mp3')
pygame.mixer.music.play()
m=input('Digite "Stop" para parar: ')