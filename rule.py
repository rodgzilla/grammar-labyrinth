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
        if not sum((proba for proba, _ in rewrittings)) == 100:
            raise ValueError("The probability values do not add up to 100")

        self.rewritting_format = rewrittings[0][1].get_format()
        if not all((self.rewritting_format == maze.get_format() 
                    for _, maze in rewrittings)):
            raise ValueError("The mazes do not have an identical format")

        

    def get_rule_format(self):
        pass

    def apply_rule(self):
        pass
        
class TestRuleMethods(unittest.TestCase):
    def test_get_rule_format(self):
        pass

    def test_apply_rule(self):
        pass

    def testB(self):
        pass

    def testC(self):
        pass

    def testD(self):
        pass
