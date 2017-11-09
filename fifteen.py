import tkinter
import os
import random

from cell import Cell


IMG_PATH = 'image'
SIZE = 4


def shuffleCells():
    last_cell = Cell.cell_list.pop(-1)
    random.shuffle(Cell.cell_list)
    random.shuffle(Cell.cell_list)
    for x, cell in enumerate(Cell.cell_list):
        cell.x = x
        cell.row = x // SIZE
        cell.column = x % SIZE
    Cell.cell_list.append(last_cell)


def checkEndOfGame():
    global step
    step += 1
    print('Total steps: '.join(str(step)))
    if Cell.cell_list == Cell.cell_order_list:
        print('You finish game')


def keyPressUp():
    near = curr.getUpItem()
    if near:
        curr.swapWith(near)


def keyPressDown():
    near = curr.getDownItem()
    if near:
        curr.swapWith(near)
        checkEndOfGame()


def keyPressLeft():
    near = curr.getLeftItem()
    if near:
        curr.swapWith(near)
        checkEndOfGame()


def keyPressRight():
    near = curr.getRightItem()
    if near:
        curr.swapWith(near)
        checkEndOfGame()


main_window = tkinter.Tk()
main_window.title('Play 15')

file_list = sorted(os.listdir(IMG_PATH))

image_list = []

for file in file_list:
    file_path = os.path.join(IMG_PATH, file)
    image = tkinter.PhotoImage(file=file_path)
    image_list.append(image)

for x, image in enumerate(image_list):
    row = x // SIZE
    column = x % SIZE
    temp_cell = Cell(main_window, image=image, row=row, column=column, size=SIZE)

shuffleCells()
curr = Cell.cell_list[-1]

for cell in Cell.cell_list:
    cell.renderCell()

step = 0

main_window.bind('<Up>', lambda x: keyPressUp())
main_window.bind('<Down>', lambda x: keyPressDown())
main_window.bind('<Left>', lambda x: keyPressLeft())
main_window.bind('<Right>', lambda x: keyPressRight())

main_window.mainloop()
