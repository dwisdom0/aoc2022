from unittest import TestCase

from p2 import search_stream

class TestPart2(TestCase):
  def test_1(self):
    stream = 'abcdefghijklmnopqrstuvwxyz'
    res = search_stream(stream)
    self.assertEqual(res, 14)

  def test_2(self):
    stream = 'abcdefghijklmnn'
    res = search_stream(stream)
    self.assertEqual(res, 14)

