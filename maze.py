from cell import Cell
import unittest

class Maze():
    def __init__(self, width, height, cell_dict):
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

    def test_get_format(self):
        m = Maze(1, 2, {(0,0) : 0, (0,1) : 1})
        self.assertEqual(m.get_format(), (1, 2))
