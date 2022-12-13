from unittest import TestCase

from p1 import score_forest

class TestPart1(TestCase):
  def test_1(self):
    forest = [['3', '0', '3', '7', '3'],
              ['2', '5', '5', '1', '2'],
              ['6', '5', '3', '3', '2'],
              ['3', '3', '5', '4', '9'],
              ['3', '5', '3', '9', '0']]
    for i, row in enumerate(forest):
      forest[i] = list(map(int, row))
    score = score_forest(forest)
    self.assertEqual(score, 21)
