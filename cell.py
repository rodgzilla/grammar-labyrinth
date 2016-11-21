from directions import Directions
from directions import opposite_direction
import unittest

class Cell():
    def __init__(self, walls):
        """
        Initialize a set using a set of walls.
        """
        self._walls = frozenset(walls)

    def __str__(self):
        return "Cell:" + str(self._walls)

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return False
        return self._walls == other._walls

    def __hash__(self):
        return hash(self._walls)

    def is_compatible(self, other_cell, direction):
        """
        Test if a cell is compatible with another cell. The direction
        argument indicates the wall of self to which we glue the other
        cell.
        """ 
        return (direction in self._walls) == (opposite_direction[direction] in other_cell._walls)

    def pretty_print(self, draw_north = True, draw_west = True):
        res = [[' '] * 5 for _ in range(3)]

        if draw_north and Directions.N in self._walls:
            for i in range(5):
                res[0][i] = '#'

        if draw_west and Directions.W in self._walls:
            res[1][0] = '#'

        if Directions.E in self._walls:
            res[1][-1] = '#'

        if Directions.S in self._walls:
            for i in range(5):
                res[-1][i] = '#'

        return [''.join(line) for line in res]

class TestCellMethods(unittest.TestCase):
    def test_is_compatible(self):
        """
        This method checks if is_compatible have the correct behavior
        """
        c1 = Cell({Directions.N})
        c2 = Cell({Directions.S})
        c3 = Cell({Directions.E})
        c4 = Cell({Directions.W})
        
        self.assertTrue(c1.is_compatible(c2, Directions.N))
        self.assertTrue(c2.is_compatible(c1, Directions.S))
        self.assertTrue(c2.is_compatible(c1, Directions.N))
        self.assertFalse(c1.is_compatible(c3, Directions.N))
        self.assertTrue(c3.is_compatible(c1, Directions.N))
        self.assertTrue(c3.is_compatible(c4, Directions.E))

if __name__ == '__main__':
    unittest.main()
