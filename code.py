import random
import sys
from tracemalloc import start
from numpy import square
import pygame

width = 450
height = 450
size = width, height

pygame.init()

screen = pygame.display.set_mode(size=size)

squaresList = [0 for i in range(16)]

def addRandomNumber():
    tempList = [index for index, i in enumerate(squaresList) if i == 0]
    int = random.choice(tempList)
    squaresList[int] = random.choices([2, 4], weights=(80, 20))[0]

def swapSquares(*indexes):
    lastIndex = None
    for index in indexes:
        if type(lastIndex) == int:
            squaresList[lastIndex] = squaresList[index]
        lastIndex = index
    squaresList[lastIndex] = 0

def combineSquares(*indexes):
    lastIndex = None
    for index in indexes:
        if type(lastIndex) == int and squaresList[lastIndex] == squaresList[index]:
            squaresList[lastIndex] *= 2
            squaresList[index] = 0
        lastIndex = index

def arrowKeyEvent(a, b, c, d):
    everSwaped = False
    swap = True
    while swap:
        swap = False
        combineSquares(a, b, c, d)
        if squaresList[d] != 0 or squaresList[c] != 0 or squaresList[b] != 0 or squaresList[a] != 0:
            while squaresList[a] == 0:
                swapSquares(a, b, c, d)
                swap = everSwaped = True
            while squaresList[b] == 0 and (squaresList[c] != 0 or squaresList[d] != 0):
                swapSquares(b, c, d)
                swap = everSwaped = True
            if squaresList[c] == 0 and squaresList[d] != 0:
                swapSquares(c, d)
                swap = everSwaped = True
    return everSwaped

addRandomNumber()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == 768:
            if event.key == 1073741903:
                # right
                everSwaped = False
                for i in [3, 7, 11, 15]:
                    swaped = arrowKeyEvent(i, i - 1, i - 2, i - 3)
                    if swaped:
                        everSwaped = True
                if everSwaped:
                    addRandomNumber()

            elif event.key == 1073741904:
                # left
                everSwaped = False
                for i in [3, 7, 11, 15]:
                    swaped = arrowKeyEvent(i - 3, i - 2, i - 1, i)
                    if swaped:
                        everSwaped = True
                if everSwaped:
                    addRandomNumber()

            elif event.key == 1073741905:
                # down
                everSwaped = False
                for i in [0, 1, 2, 3]:
                    swaped = arrowKeyEvent(i + 12, i + 8, i + 4, i)
                    if swaped:
                        everSwaped = True
                if everSwaped:
                    addRandomNumber()

            elif event.key == 1073741906:
                # up
                everSwaped = False
                for i in [0, 1, 2, 3]:
                    swaped = arrowKeyEvent(i, i + 4, i + 8, i + 12)
                    if swaped:
                        everSwaped = True
                if everSwaped:
                    addRandomNumber()

    startDraw = [10, 120, 230, 340]
    iter = 0
    for i in startDraw:
        for j in startDraw:
            surface = pygame.Surface((100, 100))
            surface.fill((220, 220, 220))
            if squaresList[iter] != 0:
                font = pygame.font.SysFont(None, 48)
                color = None
                if squaresList[iter] == 2:
                    color = (65, 105, 225)
                elif squaresList[iter] == 4:
                    color = (0, 56, 168)
                elif squaresList[iter] == 8:
                    color = (0, 35, 102)
                elif squaresList[iter] == 16:
                    color = (120, 190, 33)
                elif squaresList[iter] == 32:
                    color = (0, 155, 119)
                elif squaresList[iter] == 64:
                    color = (255, 198, 0)
                elif squaresList[iter] == 128:
                    color = (255, 164, 0)
                elif squaresList[iter] == 256:
                    color = (93, 55, 84)
                elif squaresList[iter] == 512:
                    color = (187, 41, 187)
                else:
                    color = (0, 255, 0)
                surface.fill(color)
                text = font.render(str(squaresList[iter]), True, (255, 255, 255))
                text_rect = text.get_rect(center=(50, 50))
                pygame.draw.rect(text, (220, 220, 220), pygame.Rect(0, 0, 100, 100), 1)
                surface.blit(text, text_rect)
            screen.blit(surface, (j, i))
            iter += 1

    pygame.display.flip()
