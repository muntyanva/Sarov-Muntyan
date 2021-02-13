import pygame
import sys

data = list(map(str.strip, sys.stdin))
w = data[0]
h = data[1]
if type(w) == int and type(h) == int:
    if __name__ == '__main__':
    # инициализация Pygame:
        pygame.init()
        #отступ
        x = 1
    # размеры окна:
        size = width, height = w, h
    # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Rect')
    # формирование кадра:
    # команды рисования на холсте
        pygame.draw.rect(screen, pygame.Color('red'), (x, x, w - 2 * x, h - 2 * x), 0)
    #draw(screen)
    #draw_square(screen)
    #screen_fill(screen)

    # ...
    # ...
    # смена (отрисовка) кадра:
        pygame.display.flip()
    # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
    # завершение работы:
        pygame.quit()
else:
    print("Неправильный формат ввода")