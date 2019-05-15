import unittest

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

    def test_height(self):
        bst = PrefixSumBST()
        for i in range(20):
            bst.put(i, i, i)
        for i in range(20):
            print("key = {},\tmax_sub = {},\t\tmin_sub = {}".format(i, bst.max_sub(i), bst.min_sub(i)))


