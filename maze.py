from cell import Cell
from directions import Directions
import unittest

class Maze():
    def __init__(self, width, height, cell_dict):
        def neighbour_cell(x, y):
            if not x == 0:
                yield (x - 1, y, Directions.N)
            if not y == 0:
                yield (x, y - 1, Directions.W)
            if not x == width - 1:
                yield (x + 1, y, Directions.S)
            if not y == height - 1:
                yield (x, y + 1, Directions.E)

        self.width = width
        self.height = height
        self.cell_dict = {}

        # Check if there is enough cells in the dictionary.
        if len(cell_dict) < width * height:
            raise ValueError('There is not enough cells in the dictionary (got ' 
                             + str(len(cell_dict))+ ' expected ' + 
                             str(width * height) + ')')

        # Check if there is not too many cells in the dictionary.
        if len(cell_dict) > width * height:
            raise ValueError('There too many cells in the dictionary (got ' + 
                             str(len(cell_dict))+ ' expected ' + 
                             str(width * height) + ')')

        # Check if the set of cells defined by cell_dict is consistent.
        for x, y in cell_dict:
            if 0 <= x < width and 0 <= y < height:
                for x_n, y_n, direction in neighbour_cell(x, y):
                    if not cell_dict[(x, y)].is_compatible(cell_dict[(x_n, y_n)], direction):
                        raise ValueError('Inconsistency in the set of cells: (' + str((x, y)) +
                                         ') is incompatible with (' + str((x_n, y_n)) + ')')
            else:
                raise ValueError('The coordinates (' + str(x) + ',' + str(y) + 
                                 ') is not compatible with the size: ' + 
                                 str(width) + 'x' + str(height) + '.')
        self.cell_dict = cell_dict.copy()

    def __str__(self):
        return "Maze: " + \
               ', '.join([str(coord) + \
               ' -> '+ \
               str(cell) for coord, cell in self.cell_dict.items()])

    def _pretty_print_repr(self):
        result = []
        for i in range(self.width):
            lines = [[] for _ in range(3 if i == 0 else 2)]
            for j in range(self.height):
                cell_pp = self.cell_dict[(i, j)].pretty_print_repr(i == 0, j == 0)

                for line_repr, cell_repr in zip(lines, cell_pp):
                    line_repr.append(cell_repr)

            for line in lines:
                result.append(''.join(line))
        return('\n'.join(result))
         
    def pretty_print(self):
        print(self._pretty_print_repr())
       
    def get_format(self):
        return (self.width, self.height)

class TestMazeMethods(unittest.TestCase):
    def test_init(self):
        # test of not enough entries.
        with self.assertRaises(ValueError):
            Maze(1, 2, dict([]))
        # test of too many entries.
        with self.assertRaises(ValueError):
            Maze(1, 2, {1:1, 2:2, 3:3})
        # test of invalid x coord.
        with self.assertRaises(ValueError):
            Maze(1, 2, {(0, 0) : 1, (3, 0) : 1})
        # test of invalid y coord.
        with self.assertRaises(ValueError):
            Maze(1, 2, {(0, 0) : 1, (0, 3) : 1})
        c1 = Cell({Directions.N})
        c2 = Cell({Directions.S})
        c3 = Cell({Directions.E})
        c4 = Cell({Directions.W})
        Maze(1, 2, {(0, 0): c1, (0, 1): c3})
        # Invalid construction.
        with self.assertRaises(ValueError):
            Maze(1, 2, {(0, 0): c1, (0, 1): c4})
        # Invalid construction.
        with self.assertRaises(ValueError):
            Maze(2, 1, {(0, 0): c2, (1, 0): c3})
        # Valid construction.
        try:
            Maze(2, 1, {(0, 0): c2, (1, 0): c1})
        except ValueError:
            self.fail("This maze should be valid but raised an exception")

    def test_get_format(self):
        m = Maze(1, 2, {(0,0) : Cell({}), (0,1) : Cell({})})
        self.assertEqual(m.get_format(), (1, 2))

    def test_pretty_print(self):
        #TODO
        pass

if __name__ == '__main__':
    c1 = Cell({Directions.N})
    c2 = Cell({Directions.S})
    c3 = Cell({Directions.N, Directions.S, Directions.W, Directions.E})
    c4 = Cell({Directions.N, Directions.W, Directions.E})
    c5 = Cell({Directions.S, Directions.W, Directions.E})
    # m1 = Maze(2, 1, {(0, 0): c2, (1, 0): c1})
    # m1.pretty_print()
    m2 = Maze(3, 3, 
              {
                  (0,0) : c3,
                  (0,1) : c3,
                  (0,2) : c3,
                  (1,0) : c3,
                  (1,1) : c4,
                  (1,2) : c3,
                  (2,0) : c3,
                  (2,1) : c5,
                  (2,2) : c3
              }
          )
    m2.pretty_print()

