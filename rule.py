import unittest
import random
from cell import Cell
from directions import Directions
from maze import Maze

class Rule():
    def __init__(self, cell, rewrittings):
        """
        Initialize the rule. A rule associate to a cell a list of couples
        (probability, Maze). The probability is an integer between 1
        and 100 and correspond to the probability of the cell being
        rewritten in the maze of this couple. The sum of probabilities
        of the list have to be 100 and every maze of the list have to
        have the same format. The mazes also have to be compatible
        with the cell in the sense that if the cell do not have a
        north wall and have an east wall, every cell of the northmost
        row of each maze should not have a north wall and every cell
        of the eastmost row of each maze should have an east wall.
        """
        if any([proba <= 0 for proba, _ in rewrittings]):
            raise ValueError("The probability values have to be positives")

        if not sum([proba for proba, _ in rewrittings]) == 100:
            raise ValueError("The probability values do not add up to 100")

        self.rewritting_format = rewrittings[0][1].get_format()
        if not all((self.rewritting_format == maze.get_format() 
                    for _, maze in rewrittings)):
            raise ValueError("The mazes do not have an identical format")

        sum_of_probas = 1
        self._rewritting_rules = []
        for proba, maze in rewrittings:
            self._rewritting_rules.append(((sum_of_probas, sum_of_probas + proba - 1), maze))
            sum_of_probas += proba
        
        self._cell = cell

    def __str__(self):
        return 'Cell: ' + str(self._cell) + ' ' + str(self._rewritting_rules)

    def get_rule_format(self):
        return self._rewritting_rules[0][1].get_format()

    def get_cell(self):
        return self._cell

    def apply_rule(self):
        random_int = random.randint(1, 100)

        for ((min_proba, max_proba), maze) in self._rewritting_rules:
            if min_proba <= random_int <= max_proba:
                return maze
        
class TestRuleMethods(unittest.TestCase):
    def test_init(self):
        c1 = Cell({Directions.N})
        c2 = Cell({Directions.S})
        c3 = Cell({Directions.N, Directions.E})
        maze1 = Maze(2, 1, {(0, 0): c2, (1, 0): c1})
        maze2 = Maze(2, 1, {(0, 0): c1, (1, 0): c2})
        maze3 = Maze(1, 1, {(0, 0): c1})
        with self.assertRaises(ValueError):
            rule = Rule(c3, [(100, maze1), (100, maze2)])
        with self.assertRaises(ValueError):
            rule = Rule(c3, [(-1, maze1), (100, maze2)])
        with self.assertRaises(ValueError):
            rule = Rule(c3, [(30, maze1), (70, maze3)])

    def test_get_rule_format(self):
        c1 = Cell({Directions.N})
        c2 = Cell({Directions.S})
        c3 = Cell({Directions.N, Directions.E})
        maze = Maze(2, 1, {(0, 0): c2, (1, 0): c1})
        rule = Rule(c3, [(100, maze)])

        self.assertTrue(rule.get_rule_format() == (2, 1))
        
    def test_get_cell(self):
        c1 = Cell({Directions.N})
        c2 = Cell({Directions.S})
        c3 = Cell({Directions.N, Directions.E})
        maze = Maze(2, 1, {(0, 0): c2, (1, 0): c1})
        rule = Rule(c3, [(100, maze)])

        self.assertTrue(rule.get_cell() == c3)

    def test_apply_rule(self):
        c1 = Cell({Directions.N})
        c2 = Cell({Directions.S})
        c3 = Cell({Directions.N, Directions.E})
        maze = Maze(2, 1, {(0, 0): c2, (1, 0): c1})
        rule = Rule(c3, [(100, maze)])

        self.assertTrue(rule.apply_rule() == maze)
        
if __name__ == '__main__':
    c1 = Cell({Directions.N})
    c2 = Cell({Directions.S})
    c3 = Cell({Directions.N, Directions.E})
    maze1 = Maze(2, 1, {(0, 0): c2, (1, 0): c1})
    maze2 = Maze(2, 1, {(0, 0): c1, (1, 0): c2})
    rule = Rule(c3, [(50, maze1), (50, maze2)])
    print(rule)
    unittest.main()
