from cell import Cell
from directions import Directions
import unittest

class Maze():
    def __init__(self, width, height, cell_dict):
        def neighbour_cell(x, y):
            if not x == 0:
                yield (x - 1, y, Directions.E)
            if not y == 0:
                yield (x, y - 1, Directions.N)
            if not x == width - 1:
                yield (x + 1, y, Directions.W)
            if not y == height - 1:
                yield (x, y + 1, Directions.S)

        self.width = width
        self.height = height
        self.cell_dict = {}

        if len(cell_dict) < width * height:
            raise ValueError('There is not enough cells in the dictionary (got ' 
                             + str(len(cell_dict))+ ' expected ' + 
                             str(width * height) + ')')
        if len(cell_dict) > width * height:
            raise ValueError('There too many cells in the dictionary (got ' + 
                             str(len(cell_dict))+ ' expected ' + 
                             str(width * height) + ')')

        for x, y in cell_dict:
            if 0 <= x < width and 0 <= y < height:
                for x_n, y_n, direction in neighbour_cell(x, y):
                    if not cell_dict[(x, y)].is_compatible(cell_dict[(x_n, y_n)], direction):
                        raise ValueError('Inconsistency in the set of cells: (' + str((x, y)) +
                                         ') is incompatible with (' + str((x_n, y_n)) + ')')
                self.cell_dict[(x,y)] = cell_dict[(x,y)]
            else:
                raise ValueError('The coordinates (' + str(x) + ',' + str(y) + 
                                 ') is not compatible with the size: ' + 
                                 str(width) + 'x' + str(height) + '.')

    def get_format(self):
        return (self.width, self.height)

class TestMazeMethods(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            Maze(1, 2, dict([]))
        with self.assertRaises(ValueError):
            Maze(1, 2, {1:1, 2:2, 3:3})
        with self.assertRaises(ValueError):
            Maze(1, 2, {(0, 0) : 1, (3, 0) : 1})
        with self.assertRaises(ValueError):
            Maze(1, 2, {(0, 0) : 1, (0, 3) : 1})
        c1 = Cell({Directions.N})
        c2 = Cell({Directions.S})
        c3 = Cell({Directions.E})
        c4 = Cell({Directions.W})
        Maze(1, 2, {(0, 0): c1, (0, 1): c3})
        with self.assertRaises(ValueError):
            Maze(1, 2, {(0, 0): c1, (0, 1): c3})

    def test_get_format(self):
        m = Maze(1, 2, {(0,0) : Cell({}), (0,1) : Cell({})})
        self.assertEqual(m.get_format(), (1, 2))
