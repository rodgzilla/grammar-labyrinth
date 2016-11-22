from cell import Cell
from directions import Directions, opposite_direction
from maze import Maze
from rule import Rule
from itertools import combinations
import unittest

class Grammar():
    def __init__(self, rule_list):
        # No empty grammar.
        if len(rule_list) == 0:
            raise ValueError('The grammar can not be empty')
        # The grammar must contain a substitution for all the 16 base cell.
        if not len({rule.get_cell() for rule in rule_list}) == 16:
            raise ValueError('A rule is needed for every possible cell')
        # All the rules must have the same format.
        rule_format = rule_list[0].get_rule_format()
        if any((rule.get_rule_format() != rule_format for rule in rule_list)):
            raise ValueError('All rules should have the same shape')
        # For easier access, we store 16 rules in a dict where the
        # base cell is the key.
        self._rule_dict = {}
        for rule in rule_list:
            self._rule_dict[rule.get_cell()] = rule
        self._rule_width = rule_format[0]
        self._rule_height = rule_format[1]

    def __str__(self):
        s = 'Grammar: ' + str(self._rule_dict)
        return s
        # return '\n'.join([str(rule) for rule in self._rule_list])

    def iterate(self, maze):
        width, height = maze.get_format()
        new_width = width * self._rule_width
        new_height = height * self._rule_height

        new_maze_dict = {}
        for i in range(width):
            for j in range(height):
                cell = maze.get_cell(i, j)
                rule = self._rule_dict[cell]
                rewritting = rule.apply_rule()
                for k in range(self._rule_width):
                    for l in range(self._rule_height):
                        new_cell = rewritting.get_cell(k, l)
                        new_coord_x = i * self._rule_width + k
                        new_coord_y = j * self._rule_height + l
                        new_maze_dict[(new_coord_x, new_coord_y)] = new_cell

        return Maze(new_width, new_height, new_maze_dict)

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
    c1 = Cell({Directions.N})
    c2 = Cell({Directions.S})
    c3 = Cell({Directions.N, Directions.E})
    c4 = Cell({})
    maze3 = Maze(2, 1, {(0, 0): c2, (1, 0): c3})
    rules = []
    for wall_number in range(5):
        for combination in combinations(Directions, wall_number):
            rules.append(Rule(Cell(combination), [(100, maze3)]))
    grammar = Grammar(rules)
    print(grammar)

    maze3.pretty_print()
    maze4 = grammar.iterate(maze3)
    maze4.pretty_print()
    
    # unittest.main()
