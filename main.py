from PIL import Image

from classes import Ant, Field


def main():
    field = Field((1024, 1024))
    # координаты центра поля, для начального положения муравья
    coord_x, coord_y = (int(coord / 2 - 1) for coord in field.cells.shape)
    ant = Ant(coord_x, coord_y)
    while all(0 < cord < 1023 for cord in (coord_x, coord_y)):

        # while all(map(lambda cord: 0 < cord < 1023, (coord_x, coord_y))):
        coord_x, coord_y = ant.coord_x, ant.coord_y
        if field.cells[coord_x][coord_y] == 0:
            ant.turn(right=False)
        else:
            ant.turn()
        field.invertion(coord_x, coord_y)

        if ant.position in (0, 180):
            coord_y += ant.position // 90 - 1

        elif ant.position in (90, 270):
            coord_x += 270 // ant.position - 2
        ant.coord_x = coord_x
        ant.coord_y = coord_y
    # black_cells_amount = len(list(filter(lambda x: x == 0, field.cells.ravel())))
    i = Image.fromarray(field.cells)
    i.save('ant_track.bmp')


if __name__ == '__main__':
    main()
