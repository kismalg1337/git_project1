from Samples.show_map import show_map_yandex
import argparse
import pygame
import os
import math

parser = argparse.ArgumentParser()
parser.add_argument('coord_x', type=float)
parser.add_argument('coord_y', type=float)
parser.add_argument('--zoom', type=float, default=5)
res = parser.parse_args()


def main():
    # Показываем карту с фиксированным масштабом.
    ll_spn = f"ll={res.coord_x},{res.coord_y}&z={res.zoom}"
    x, y, zoom = res.coord_x, res.coord_y, res.zoom
    show_map_yandex(ll_spn, "map")
    map_file = "map.png"
    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    looping = True
    while looping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                looping = False
            key = pygame.key.get_pressed()
            step = 0.006
            if key[pygame.K_PAGEUP]:
                zoom = zoom + 1 if zoom + 1 < 20 else zoom
                ll_spn = f"ll={x},{y}&z={zoom}"
                print(ll_spn)
                show_map_yandex(ll_spn, "map")
            if key[pygame.K_PAGEDOWN]:
                zoom = zoom - 1 if zoom - 1 > 0 else zoom
                ll_spn = f"ll={x},{y}&z={zoom}"
                print(ll_spn)
                show_map_yandex(ll_spn, "map")
            if key[pygame.K_UP]:
                y += step * math.pow(2, 15 - zoom)
                ll_spn = f"ll={x},{y}&z={zoom}"
                print(ll_spn)
                show_map_yandex(ll_spn, "map")
            if key[pygame.K_DOWN]:
                y -= step * math.pow(2, 15 - zoom)
                ll_spn = f"ll={x},{y}&z={zoom}"
                print(ll_spn)
                show_map_yandex(ll_spn, "map")
            if key[pygame.K_RIGHT]:
                x += step * math.pow(2, 15 - zoom)
                ll_spn = f"ll={x},{y}&z={zoom}"
                print(ll_spn)
                show_map_yandex(ll_spn, "map")
            if key[pygame.K_LEFT]:
                x -= step * math.pow(2, 15 - zoom)
                ll_spn = f"ll={x},{y}&z={zoom}"
                print(ll_spn)
                show_map_yandex(ll_spn, "map")
        # Инициализируем pygame
        # Рисуем картинку, загружаемую из только что созданного файла.
        screen.blit(pygame.image.load(map_file), (0, 0))
        # Переключаем экран и ждем закрытия окна.
        pygame.display.flip()
        pygame.display.update()
    pygame.quit()
    # Удаляем за собой файл с изображением.
    os.remove(map_file)


if __name__ == "__main__":
    main()
