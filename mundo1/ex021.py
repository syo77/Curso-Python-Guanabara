"""
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""
import pygame
from os import system
pygame.init()
pygame.mixer.music.load("mundo1/ex021.mp3")
pygame.mixer.music.play()
system('cls')
input("Pressione enter para interromper: ")
pygame.event.wait()