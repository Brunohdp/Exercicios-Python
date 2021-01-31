import pygame                                   #Importa o pygame, biblioteca usada para criação de jogos
pygame.mixer.init()                             #Inicia o mixer do pygame
pygame.mixer.music.load('d021.mp3')             #Carrega o audio
pygame.mixer.music.play()                       #Toca o audio
while(pygame.mixer.music.get_busy()): pass      #Enquanto o music estiver ocupado passe
