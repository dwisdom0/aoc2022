from p1 import score_overlap

from unittest import TestCase

class TestP1(TestCase):
  def test_1(self):
    pair = ((2, 4), (6, 8))
    self.assertEqual(score_overlap(pair), 0)

  def test_2(self):
    pair = ((2, 3), (4, 5))
    self.assertEqual(score_overlap(pair), 0)

  def test_3(self):
    pair = ((5, 7), (7, 9))
    self.assertEqual(score_overlap(pair), 0)

  def test_4(self):
    pair = ((2, 8), (3, 7))
    self.assertEqual(score_overlap(pair), 1)

  def test_5(self):
    pair = ((6, 6), (4, 6))
    self.assertEqual(score_overlap(pair), 1)

  def test_6(self):
    pair = ((2, 6), (4, 8))
    self.assertEqual(score_overlap(pair), 0)

  def test_7(self):
    pair = (('47', '84'), ('46', '48'))
    self.assertEqual(score_overlap(pair), 0)

  def test_7(self):
    pair = (('14', '83'), ('5', '14'))
    self.assertEqual(score_overlap(pair), 0)
