import unittest

from src.ds.insertion_tree import InsertionTree


class TestInsertionTree(unittest.TestCase):

    def test_maxRight_withNotEmptyBST_shouldReturnCorrectMaxRight(self):
        bst = InsertionTree()
        for i in range(20):
            bst.put(i, i, i % 2 == 0)

        for i in range(20):
            self.assertEqual(0,  bst.min_left(i).val)
            self.assertEqual(19, bst.max_right(i).val)

