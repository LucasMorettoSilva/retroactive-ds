import unittest

from src.ds.insertion_tree import InsertionTree
from src.ds.prefix_sum_bst import PrefixSumBST


class TestPrefixSumBST(unittest.TestCase):

    def test_prefixSum_withNoneTypeArgument_shouldRaiseValueError(self):
        bst = PrefixSumBST()
        with self.assertRaises(ValueError):
            bst.prefix_sum(None)

    def test_prefixSum_withValueNotInBST_shouldRaiseValueError(self):
        bst = PrefixSumBST()
        with self.assertRaises(ValueError):
            bst.prefix_sum(1)

        bst.put(0, 0, 0)
        with self.assertRaises(ValueError):
            bst.prefix_sum(1)

    def test_prefixSum_withValueInBST_shouldReturnCorrectPrefixSumForEachValue(self):
        bst = PrefixSumBST()
        for i in range(20):
            bst.put(i, i, 1)
            self.assertEqual(i + 1, bst.prefix_sum(i))
        for i in range(20):
            self.assertEqual(i + 1, bst.prefix_sum(i))

        for i in range(20):
            bst.delete(i)
            if i < 19:
                self.assertEqual(1, bst.prefix_sum(i + 1))

    def test_height(self):
        bst = InsertionTree()
        for i in range(20):
            bst.put(i, i)
        bst.put(0, 0, False)
        for i in range(20):
            print("key = {},\tmax_left = {},\t\tmax_right = {}\t\tmin_left = {},\t\tmin_right = {}".format(i,bst.max_left(i), bst.max_right(i), bst.min_left(i), bst.min_right(i)))
            # print("key = {},\tmax_sub = {},\t\tmin_sub = {}".format(i, bst.max_sub(i), bst.min_sub(i)))
