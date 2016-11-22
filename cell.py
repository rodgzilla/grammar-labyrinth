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

    def _compute_coords_pretty_print(self, draw_north, draw_west):
        if draw_north:
            if draw_west:
                north_coord = [(0, i) for i in range(5)]
                south_coord = [(-1, i) for i in range(5)]
                west_coord = [(i, 0) for i in range(3)]
                east_coord = [(i, -1) for i in range(3)]
            else:
                north_coord = [(0, i) for i in range(4)]
                south_coord = [(-1, i) for i in range(4)]
                west_coord = []
                east_coord = [(i, -1) for i in range(3)]
        else:
            if draw_west:
                north_coord = []
                south_coord = [(-1, i) for i in range(5)]
                west_coord = [(i, 0) for i in range(2)]
                east_coord = [(i, -1) for i in range(2)]
            else:
                north_coord = []
                south_coord = [(-1, i) for i in range(4)]
                west_coord = []
                east_coord = [(i, -1) for i in range(2)]

        return north_coord, south_coord, west_coord, east_coord

    def pretty_print_repr(self, draw_north = True, draw_west = True):
        res = [[' '] * (5 if draw_west else 4) for _ in range(3 if draw_north else 2)]
        north, south, west, east = self._compute_coords_pretty_print(draw_north, draw_west)

        if Directions.N in self._walls:
            for x, y in north:
                res[x][y] = '#'

        if Directions.S in self._walls:
            for x, y in south:
                res[x][y] = '#'

        if  Directions.W in self._walls:
            for x, y in west:
                res[x][y] = '#'

        if Directions.E in self._walls:
            for x, y in east:
                res[x][y] = '#'

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
