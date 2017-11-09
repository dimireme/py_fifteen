import tkinter
import random

class Cell(tkinter.Label):

    cell_list = []
    cell_order_list = []
    size = None

    def __init__(self, main_window, image, row, column, size):
        tkinter.Label.__init__(self, main_window, image=image)
        self.size = size
        self.row = row
        self.column = column
        self.x = row * self.size + column
        self.cell_list.append(self)
        self.cell_order_list.append(self)

    def getUpItem(self):
        if self.row > 0:
            x_near = (self.row - 1) * self.size + self.column
            return Cell.cell_list[x_near]
        return None

    def getDownItem(self):
        if self.row < self.size - 1:
            x_near = (self.row + 1) * self.size + self.column
            return Cell.cell_list[x_near]
        return None

    def getLeftItem(self):
        if self.column > 0:
            x_near = self.row * self.size + self.column - 1
            return Cell.cell_list[x_near]
        return None

    def getRightItem(self):
        if self.column < self.size - 1:
            x_near = self.row * self.size + self.column + 1
            return Cell.cell_list[x_near]
        return None

    def swapWith(self, near):
        Cell.cell_list[self.x], Cell.cell_list[near.x] = Cell.cell_list[near.x], Cell.cell_list[self.x]
        self.row, near.row = near.row, self.row
        self.column, near.column = near.column, self.column
        self.x, near.x = near.x, self.x

        self.renderCell()
        near.renderCell()


    def renderCell(self):
        self.grid(row=self.row, column=self.column)
