from cell import Cell
from directions import Directions, opposite_direction
from maze import Maze
from rule import Rule
from itertools import combinations
import unittest

class Grammar():
    def __init__(self, rule_list):
        if len(rule_list) == 0:
            raise ValueError('The grammar can not be empty')
        if not len({rule.get_cell() for rule in rule_list}) == 16:
            raise ValueError('A rule is needed for every possible cell')
        self._rule_list = rule_list[:]
        
    def __str__(self):
        return '\n'.join([str(rule) for rule in self._rule_list])

    def iterate(self, maze):
        pass

class TestGrammarMethods(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            Grammar([])

        c1 = Cell({Directions.N})
        c2 = Cell({Directions.S})
        c3 = Cell({Directions.N, Directions.E})
        c4 = Cell({})
        maze1 = Maze(2, 1, {(0, 0): c2, (1, 0): c1})
        maze2 = Maze(2, 1, {(0, 0): c1, (1, 0): c2})
        maze3 = Maze(2, 1, {(0, 0): c4, (1, 0): c4})
        rule1 = Rule(c3, [(50, maze1), (50, maze2)])
        rule2 = Rule(c3, [(50, maze1), (50, maze2)])
        with self.assertRaises(ValueError):
            Grammar([rule1, rule2])
        rules = []
        try:
            for wall_number in range(5):
                for combination in combinations(Directions, wall_number):
                    rules.append(Rule(Cell(combination), [(100, maze3)]))
            grammar = Grammar(rules)
        except ValueError:
            self.fail("This grammar should be valid but raised an exception")


if __name__ == '__main__':
    unittest.main()
