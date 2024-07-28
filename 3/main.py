#!/usr/bin/env python3

import pygame
import math
from pygame.locals import *
from pygame import mixer as pyg_mixer
from sys import exit

pygame.init()
pygame.mixer.init()

pygame.mixer.music.set_volume(0.1)
musicaFundo = pygame.mixer.music.load('/mnt/c/Users/jotav/Desktop/pygame/2/Musica/BoxCat Games - Tricks.mp3')
pygame.mixer.music.play(-1)
pong = pygame.mixer.Sound('/mnt/c/Users/jotav/Desktop/pygame/2/Musica/Pong.wav')
largura = 640
altura = 480
x = 0
y = altura/2 - 30
x2 = largura - 15
y2 = altura/2 - 30
xC = 300
yC = 260
direcao = 1
direcaoY = 1
modificador = 1
pontos = 0
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
clock = pygame.time.Clock()
run = True
morreu = False
font = pygame.font.SysFont('arial', 40, True, True)

def movimentaJogador(y):
    if pygame.key.get_pressed()[K_s]:
        if (verificaMovimento(2, y + 20) == 0):
            y = y + 20
    if pygame.key.get_pressed()[K_w]:
        if (verificaMovimento(2, y - 20) == 0):
            y = y - 20
    return y
def movimentaJogador2(y):
    if pygame.key.get_pressed()[K_DOWN]:
        if (verificaMovimento(2, y + 20) == 0):
            y = y + 20
    if pygame.key.get_pressed()[K_UP]:
        if (verificaMovimento(2, y - 20) == 0):
            y = y - 20
    return y
def movimentaBola(xC, yC, direcaoX, direcaoY, modificador):
    xC = xC + (-2 * direcaoX) * modificador
    yC = yC + (-1 * direcaoY) * modificador
    return xC, yC
def calculaDistancia(y, yR):
    distancia = y - yR
    return distancia

def reiniciarJogo():
    global x, y, x2, y2, xC, yC, direcao, direcaoY, modificador, pontos, morreu
    x = 0
    y = altura/2 - 30
    x2 = largura - 15
    y2 = altura/2 - 30
    xC = 300
    yC = 260
    direcao = 1
    direcaoY = 1
    modificador = 1
    pontos = 0
    morreu = False

while (run):
    clock.tick(90)
    tela.fill((0,0,0))
    mens = f'Pongs: {pontos}'
    texto = font.render(mens, False, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    tela.blit(texto, (450, 40))

    pygame.display.update()
    