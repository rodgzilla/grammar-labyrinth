from directions import Directions
from directions import opposite_direction
import unittest

class Cell():
    def __init__(self, walls):
        """
        Initialize a set using a set of walls.
        """
        self.walls = walls.copy()

    def is_compatible(self, other_cell, direction):
        """
        Test if a cell is compatible with another cell. The direction
        argument indicates the wall of self to which we glue the other
        cell.
        """ 
        return (direction in self.walls) == (opposite_direction[direction] in other_cell.walls)

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
