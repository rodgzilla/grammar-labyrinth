from cell import Cell
from directions import Directions, opposite_direction
from maze import Maze
from rule import Rule
import unittest

class Grammar():
    def __init__(self, rule_list):
        if len(rule_list) == 0:
            raise ValueError('The grammar can not be empty')
        if not len({rule.get_cell() for rule in rule_list}) == 16:
            raise ValueError('A rule is needed for every possible cell')
        self._rule_list = rule_list[:]

    def iterate(self, maze):
        pass

class TestGrammarMethods(unittest.TestCase):
    def test_init(self):
        c1 = Cell({Directions.N})
        c2 = Cell({Directions.S})
        c3 = Cell({Directions.N, Directions.E})
        maze1 = Maze(2, 1, {(0, 0): c2, (1, 0): c1})
        maze2 = Maze(2, 1, {(0, 0): c1, (1, 0): c2})
        rule1 = Rule(c3, [(50, maze1), (50, maze2)])
        rule2 = Rule(c3, [(50, maze1), (50, maze2)])
        grammar = Grammar([rule1, rule2])
        with self.assertRaises(ValueError):
            Grammar([])


if __name__ == '__main__':
    unittest.main()
