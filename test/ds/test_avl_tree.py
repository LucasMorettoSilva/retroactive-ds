import unittest

from src.ds.avl_tree import AVLTree


class TestAVLTree(unittest.TestCase):

    @staticmethod
    def cmp(a, b):
        if a[1] < b[1]:
            return -1
        if a[1] > b[1]:
            return 1
        if a[0] < b[0]:
            return -1
        if a[0] > b[0]:
            return 1
        return 0

    def test_constructor_shouldCreateEmptyBST(self):
        self.assertEqual(0, len(AVLTree()))

    def test_put_withCompareFunctionAndKeyNotInBST_shouldAddNewKeyIncreaseBSTLengthAndMaintainBalanceFactor(self):
        bst = AVLTree(self.cmp)
        self.assertEqual(0, len(bst))

        bst.put([0, 0], 0)
        self.assertEqual(1, len(bst))
        self.assertEqual(0, bst.height())

        bst.put([0, 1], 0)
        self.assertEqual(2, len(bst))
        self.assertEqual(1, bst.height())

        bst.put([0, -1], 0)
        self.assertEqual(3, len(bst))
        self.assertEqual(1, bst.height())

        bst.put([-1, 1], 0)
        self.assertEqual(4, len(bst))
        self.assertEqual(2, bst.height())

    def test_put_withCompareFunctionAndKeyInBSTAndValueNotNone_shouldReplaceAssociatedValueByNewOneAndNotModifyBSTLength(self):
        bst = AVLTree(self.cmp)

        bst.put([0, 0], 0)
        self.assertEqual(1, len(bst))
        self.assertEqual(0, bst.get([0, 0]))

        bst.put([0, 0], 1)
        self.assertEqual(1, len(bst))
        self.assertEqual(1, bst.get([0, 0]))

        bst.put([0, 0], 12)
        self.assertEqual(1, len(bst))
        self.assertEqual(12, bst.get([0, 0]))

    def test_put_withCompareFunctionAnddNoneTypeArgumentValue_shouldRemoveAssociatedKeyFromBSTDecreaseLengthAndMaintainBalanceFactor(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 0], 1)
        bst.put([0, 1], 2)
        bst.put([0, 2], 3)
        bst.put([0, 3], 4)

        self.assertIn([0, 1], bst)
        self.assertEqual(4, len(bst))
        self.assertEqual(2, bst.height())

        bst.put([0, 1], None)
        self.assertNotIn([0, 1], bst)
        self.assertEqual(3, len(bst))
        self.assertEqual(1, bst.height())

    def test_get_withCompareFunctionANdKeyNotInBST_shouldReturnNone(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 1], 0)
        self.assertIsNone(bst.get([0, 0]))

    def test_get_withCompareFunctionAndKeyInBST_shouldReturnAssociatedValue(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 0], 1)
        bst.put([0, 1], 2)
        bst.put([0, 2], 3)
        bst.put([0, 3], 4)

        self.assertEqual(1, bst.get([0, 0]))
        self.assertEqual(2, bst.get([0, 1]))
        self.assertEqual(3, bst.get([0, 2]))
        self.assertEqual(4, bst.get([0, 3]))

    def test_getItem_withCompareFunctionANdKeyNotInBST_shouldReturnNone(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 1], 0)
        self.assertIsNone(bst[[0, 2]])

    def test_getItem_withCompareFunctionAndKeyInBST_shouldReturnAssociatedValue(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 0], 1)
        bst.put([0, 1], 2)
        bst.put([0, 2], 3)
        bst.put([0, 3], 4)

        self.assertEqual(1, bst[[0, 0]])
        self.assertEqual(2, bst[[0, 1]])
        self.assertEqual(3, bst[[0, 2]])
        self.assertEqual(4, bst[[0, 3]])

    def test_contains_withCompareFunctionAndKeyNotInBST_shouldReturnFalse(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 0], 1)
        bst.put([0, 1], 2)
        bst.put([0, 2], 3)
        bst.put([0, 3], 4)

        self.assertNotIn([1, 0], bst)
        self.assertNotIn([2, 0], bst)
        self.assertNotIn([3, 0], bst)

    def test_contains_withCompareFunctionAndKeyInBST_shouldReturnTrue(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 0], 1)
        bst.put([0, 1], 2)
        bst.put([0, 2], 3)
        bst.put([0, 3], 4)

        self.assertIn([0, 1], bst)
        self.assertIn([0, 2], bst)
        self.assertIn([0, 3], bst)
        self.assertIn([0, 3], bst)

    def test_delete_withCompareFunctionAndKeyNotInBST_shouldNotModifyBST(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 0], 1)
        bst.put([0, 1], 2)
        bst.put([0, 2], 3)
        bst.put([0, 3], 4)

        bst.delete([0, 69])
        self.assertEqual(4, len(bst))
        self.assertIn([0, 1], bst)
        self.assertIn([0, 2], bst)
        self.assertIn([0, 3], bst)
        self.assertIn([0, 3], bst)

    def test_delete_withCompareFunctionAndKeyInBST_shouldDeleteKeyFromBSTDecreaseLengthAndMaintainBalanceFactor(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 0], 1)
        bst.put([0, 1], 2)
        bst.put([0, 2], 3)
        bst.put([0, 3], 4)
        self.assertEqual(2, bst.height())

        bst.delete([0, 1])
        self.assertEqual(3, len(bst))
        self.assertEqual(1, bst.height())

        bst.delete([0, 2])
        self.assertEqual(2, len(bst))
        self.assertEqual(1, bst.height())

    def test_deleteMax_withCompareFunctionAndNotEmptyBST_shouldDeleteMaxKeyFromBSTAndDecreaseBSTLength(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 0], 1)
        bst.put([0, 1], 2)
        bst.put([0, 2], 3)
        bst.put([0, 3], 4)

        bst.delete_max()
        self.assertEqual(3, len(bst))
        self.assertNotIn([0, 3], bst)

        bst.delete_max()
        self.assertEqual(2, len(bst))
        self.assertNotIn([0, 2], bst)

        bst.delete_max()
        self.assertEqual(1, len(bst))
        self.assertNotIn([0, 1], bst)

        bst.delete_max()
        self.assertEqual(0, len(bst))
        self.assertNotIn([0, 0], bst)

    def test_deleteMin_withCompareFunctionAndNotEmptyBST_shouldDeleteMinKeyFromBSTAndDecreaseBSTLength(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 0], 1)
        bst.put([0, 1], 2)
        bst.put([0, 2], 3)
        bst.put([0, 3], 4)

        bst.delete_min()
        self.assertEqual(3, len(bst))
        self.assertNotIn([0, 0], bst)

        bst.delete_min()
        self.assertEqual(2, len(bst))
        self.assertNotIn([0, 1], bst)

        bst.delete_min()
        self.assertEqual(1, len(bst))
        self.assertNotIn([0, 2], bst)

        bst.delete_min()
        self.assertEqual(0, len(bst))
        self.assertNotIn([0, 3], bst)

    def test_max_withCompareFunctionAndNotEmptyBST_shouldReturnMaxKeyFromBST(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 1], 1)
        self.assertEqual([0, 1], bst.max())

        bst.put([0, 2], 2)
        self.assertEqual([0, 2], bst.max())

        bst.put([0, 3], 3)
        self.assertEqual([0, 3], bst.max())

        bst.put([0, 4], 4)
        self.assertEqual([0, 4], bst.max())

        bst.delete_max()
        self.assertEqual([0, 3], bst.max())

        bst.delete_max()
        self.assertEqual([0, 2], bst.max())

        bst.delete_max()
        self.assertEqual([0, 1], bst.max())

    def test_min_withCompareFunctionAndNotEmptyBST_shouldReturnMaxKeyFromBST(self):
        bst = AVLTree()
        bst.put([0, 4], 1)
        self.assertEqual([0, 4], bst.min())

        bst.put([0, 3], 2)
        self.assertEqual([0, 3], bst.min())

        bst.put([0, 2], 3)
        self.assertEqual([0, 2], bst.min())

        bst.put([0, 1], 4)
        self.assertEqual([0, 1], bst.min())

        bst.delete_min()
        self.assertEqual([0, 2], bst.min())

        bst.delete_min()
        self.assertEqual([0, 3], bst.min())

        bst.delete_min()
        self.assertEqual([0, 4], bst.min())

    def test_put_withNoneTypeArgumentKey_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            AVLTree().put(None, 1)

    def test_put_withKeyNotInBST_shouldAddNewKeyIncreaseBSTLengthAndMaintainBalanceFactor(self):
        bst = AVLTree()
        self.assertEqual(0, len(bst))

        bst.put(10, 0)
        self.assertEqual(1, len(bst))
        self.assertEqual(0, bst.height())

        bst.put(20, 0)
        self.assertEqual(2, len(bst))
        self.assertEqual(1, bst.height())

        bst.put(30, 0)
        self.assertEqual(3, len(bst))
        self.assertEqual(1, bst.height())

        bst.put(40, 0)
        self.assertEqual(4, len(bst))
        self.assertEqual(2, bst.height())

        bst.put(50, 0)
        self.assertEqual(5, len(bst))
        self.assertEqual(2, bst.height())

        bst.put(25, 0)
        self.assertEqual(6, len(bst))
        self.assertEqual(2, bst.height())

    def test_put_withKeyInBSTAndValueNotNone_shouldReplaceAssociatedValueByNewOneAndNotModifyBSTLength(self):
        bst = AVLTree()

        bst.put("A", 0)
        self.assertEqual(1, len(bst))
        self.assertEqual(0, bst.get("A"))

        bst.put("A", 1)
        self.assertEqual(1, len(bst))
        self.assertEqual(1, bst.get("A"))

        bst.put("A", 12)
        self.assertEqual(1, len(bst))
        self.assertEqual(12, bst.get("A"))

    def test_put_withNoneTypeArgumentValue_shouldRemoveAssociatedKeyFromBSTDecreaseLengthAndMaintainBalanceFactor(self):
        bst = AVLTree()
        bst.put("A", 1)
        bst.put("B", 2)
        bst.put("C", 3)
        bst.put("D", 4)

        self.assertIn("A", bst)
        self.assertEqual(4, len(bst))
        self.assertEqual(2, bst.height())

        bst.put("A", None)
        self.assertNotIn("A", bst)
        self.assertEqual(3, len(bst))
        self.assertEqual(1, bst.height())

    def test_get_withNoneTypeArgument_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            AVLTree().get(None)

    def test_get_withKeyNotInBST_shouldReturnNone(self):
        bst = AVLTree()
        bst.put("A", 0)
        self.assertIsNone(bst.get("B"))

    def test_get_withKeyInBST_shouldReturnAssociatedValue(self):
        bst = AVLTree()
        bst.put("A", 1)
        bst.put("B", 2)
        bst.put("C", 3)
        bst.put("D", 4)

        self.assertEqual(1, bst.get("A"))
        self.assertEqual(2, bst.get("B"))
        self.assertEqual(3, bst.get("C"))
        self.assertEqual(4, bst.get("D"))

    def test_getItem_withNoneTypeArgument_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            bst = AVLTree()
            bst[None]

    def test_getItem_withKeyNotInBST_shouldReturnNone(self):
        bst = AVLTree()
        bst.put("A", 0)
        self.assertIsNone(bst["B"])

    def test_getItem_withKeyInBST_shouldReturnAssociatedValue(self):
        bst = AVLTree()
        bst.put("A", 1)
        bst.put("B", 2)
        bst.put("C", 3)
        bst.put("D", 4)

        self.assertEqual(1, bst["A"])
        self.assertEqual(2, bst["B"])
        self.assertEqual(3, bst["C"])
        self.assertEqual(4, bst["D"])

    def test_contains_withNoneTypeArgument_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            None in AVLTree()

    def test_contains_withKeyNotInBST_shouldReturnFalse(self):
        bst = AVLTree()
        bst.put("A", 1)
        bst.put("B", 2)
        bst.put("C", 3)
        bst.put("D", 4)

        self.assertNotIn("E", bst)
        self.assertNotIn("F", bst)
        self.assertNotIn("G", bst)

    def test_contains_withKeyInBST_shouldReturnTrue(self):
        bst = AVLTree()
        bst.put("A", 1)
        bst.put("B", 2)
        bst.put("C", 3)
        bst.put("D", 4)

        self.assertIn("A", bst)
        self.assertIn("B", bst)
        self.assertIn("C", bst)
        self.assertIn("D", bst)

    def test_height_withEmptyBST_shouldReturnNegativeOne(self):
        self.assertEqual(-1, AVLTree().height())

    def test_height_withOneNodeBST_shouldReturnZero(self):
        bst = AVLTree()
        bst.put("A", 0)
        self.assertEqual(0, bst.height())

    def test_height_withNotEmptyBST_shouldReturnHeightOfBST(self):
        bst = AVLTree()

        bst.put(10, 0)
        self.assertEqual(0, bst.height())

        bst.put(20, 0)
        self.assertEqual(1, bst.height())

        bst.put(30, 0)
        self.assertEqual(1, bst.height())

        bst.put(40, 0)
        self.assertEqual(2, bst.height())

        bst.put(50, 0)
        self.assertEqual(2, bst.height())

        bst.put(25, 0)
        self.assertEqual(2, bst.height())

    def test_delete_withNoneTypeArgument_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            AVLTree().delete(None)

    def test_delete_withKeyNotInBST_shouldNotModifyBST(self):
        bst = AVLTree()
        bst.put("A", 1)
        bst.put("B", 2)
        bst.put("C", 3)
        bst.put("D", 4)

        bst.delete("G")
        self.assertEqual(4, len(bst))
        self.assertIn("A", bst)
        self.assertIn("B", bst)
        self.assertIn("C", bst)
        self.assertIn("D", bst)

    def test_delete_withKeyInBST_shouldDeleteKeyFromBSTDecreaseLengthAndMaintainBalanceFactor(self):
        bst = AVLTree()
        bst.put("A", 1)
        bst.put("B", 2)
        bst.put("C", 3)
        bst.put("D", 4)
        self.assertEqual(2, bst.height())

        bst.delete("A")
        self.assertEqual(3, len(bst))
        self.assertEqual(1, bst.height())

        bst.delete("C")
        self.assertEqual(2, len(bst))
        self.assertEqual(1, bst.height())

    def test_deleteMax_withEmptyBST_shouldReturnNone(self):
        self.assertIsNone(AVLTree().delete_max())

    def test_deleteMax_withNotEmptyBST_shouldDeleteMaxKeyFromBSTAndDecreaseBSTLength(self):
        bst = AVLTree()
        bst.put("A", 1)
        bst.put("B", 2)
        bst.put("C", 3)
        bst.put("D", 4)

        bst.delete_max()
        self.assertEqual(3, len(bst))
        self.assertNotIn("D", bst)

        bst.delete_max()
        self.assertEqual(2, len(bst))
        self.assertNotIn("C", bst)

        bst.delete_max()
        self.assertEqual(1, len(bst))
        self.assertNotIn("B", bst)

        bst.delete_max()
        self.assertEqual(0, len(bst))
        self.assertNotIn("A", bst)

    def test_deleteMin_withEmptyBST_shouldReturnNone(self):
        self.assertIsNone(AVLTree().delete_min())

    def test_deleteMin_withNotEmptyBST_shouldDeleteMinKeyFromBSTAndDecreaseBSTLength(self):
        bst = AVLTree()
        bst.put("A", 1)
        bst.put("B", 2)
        bst.put("C", 3)
        bst.put("D", 4)

        bst.delete_min()
        self.assertEqual(3, len(bst))
        self.assertNotIn("A", bst)

        bst.delete_min()
        self.assertEqual(2, len(bst))
        self.assertNotIn("B", bst)

        bst.delete_min()
        self.assertEqual(1, len(bst))
        self.assertNotIn("C", bst)

        bst.delete_min()
        self.assertEqual(0, len(bst))
        self.assertNotIn("D", bst)

    def test_max_withEmptyBST_shouldReturnNone(self):
        self.assertIsNone(AVLTree().max())

    def test_max_withNotEmptyBST_shouldReturnMaxKeyFromBST(self):
        bst = AVLTree()
        bst.put("A", 1)
        self.assertEqual("A", bst.max())

        bst.put("B", 2)
        self.assertEqual("B", bst.max())

        bst.put("C", 3)
        self.assertEqual("C", bst.max())

        bst.put("D", 4)
        self.assertEqual("D", bst.max())

        bst.delete_max()
        self.assertEqual("C", bst.max())

        bst.delete_max()
        self.assertEqual("B", bst.max())

        bst.delete_max()
        self.assertEqual("A", bst.max())

    def test_min_withEmptyBST_shouldReturnNone(self):
        self.assertIsNone(AVLTree().min())

    def test_min_withNotEmptyBST_shouldReturnMaxKeyFromBST(self):
        bst = AVLTree()
        bst.put("D", 1)
        self.assertEqual("D", bst.min())

        bst.put("C", 2)
        self.assertEqual("C", bst.min())

        bst.put("B", 3)
        self.assertEqual("B", bst.min())

        bst.put("A", 4)
        self.assertEqual("A", bst.min())

        bst.delete_min()
        self.assertEqual("B", bst.min())

        bst.delete_min()
        self.assertEqual("C", bst.min())

        bst.delete_min()
        self.assertEqual("D", bst.min())

    def test_keys_withNoneTypeArgument_shouldRaiseValueError(self):
        bst = AVLTree()

        with self.assertRaises(ValueError):
            bst.keys(None, 1)
        with self.assertRaises(ValueError):
            bst.keys(1, None)

    def test_keys_withEmptyBST_shouldReturnEmptyList(self):
        self.assertEqual([], AVLTree().keys(1, 2))

    def test_keys_withCompareFunctionAndEmptyBST_shouldReturnEmptyList(self):
        self.assertEqual([], AVLTree(self.cmp).keys([0, 1], [0, 2]))

    def test_keys_withNotEmptyBSTAndArgumentsInBST_shouldReturnListOfKeysInGivenRangeIncludingGivenArguments(self):
        bst = AVLTree()
        for i in range(20):
            bst.put(i, i)

        for i in range(20):
            for j in range(i, 20):
                if i == j:
                    expected = [i]
                else:
                    expected = [e for e in range(i, j + 1)]
                self.assertEqual(expected, bst.keys(i, j))

    def test_keys_withNotEmptyBSTAndArgumentsNotInBST_shouldReturnListOfKeysInGivenRangeExcludingGivenArguments(self):
        bst = AVLTree()
        for i in range(0, 20, 2):
            bst.put(i, i)

        for i in range(-1, 20, 2):
            for j in range(i, 20, 2):
                if i == j:
                    expected = []
                else:
                    expected = [e for e in range(i + 1, j + 1, 2)]
                self.assertEqual(expected, bst.keys(i, j))

    def test_keys_withCompareFunctionNotEmptyBSTAndArgumentsNotInBST_shouldReturnListOfKeysInGivenRangeExcludingGivenArguments(self):
        bst = AVLTree(self.cmp)
        for i in range(0, 20, 2):
            bst.put([0, i], i)

        for i in range(-1, 20, 2):
            for j in range(i, 20, 2):
                if i == j:
                    expected = []
                else:
                    expected = [[0, e] for e in range(i + 1, j + 1, 2)]
                self.assertEqual(expected, bst.keys([0, i], [0, j]))

    def test_keys_withCompareFunctionAndNotEmptyBST_shouldReturnListOfKeysInGivenRangeIncludingGivenArguments(self):
        bst = AVLTree(self.cmp)
        for i in range(20):
            bst.put([0, i], i)

        for i in range(20):
            for j in range(i, 20):
                if i == j:
                    expected = [[0, i]]
                else:
                    expected = [[0, e] for e in range(i, j + 1)]
                self.assertEqual(expected, bst.keys([0, i], [0, j]))

    def test_floor_withNoneTypeArgument_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            AVLTree().floor(None)

    def test_floor_withEmptyBST_shouldReturnNone(self):
        bst = AVLTree()
        for i in range(200):
            self.assertIsNone(bst.floor(i))

    def test_floor_withArgumentNotInBSTHavingFloorValue_shouldReturnGreaterStrictlyLowerElementFromBST(self):
        bst = AVLTree()
        for i in range(10):
            bst.put(i, i)
        for i in range(10):
            self.assertEqual(i, bst.floor(i + 0.5))

    def test_floor_withArgumentNotHavingFloorValue_shouldReturnNone(self):
        bst = AVLTree()
        bst.put(1, 1)
        self.assertIsNone(bst.floor(0))

    def test_floor_withCompareFunctionAndArgumentNotInBSTHavingFloorValue_shouldReturnGreaterStrictlyLowerElementFromBST(self):
        bst = AVLTree(self.cmp)
        for i in range(10):
            bst.put([0, i], i)
        for i in range(10):
            self.assertEqual([0, i], bst.floor([0, i + 0.5]))

    def test_floor_withCompareFunctionAndArgumentInBST_shouldReturnGivenArgument(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 1], 1)
        self.assertEqual([0, 1], bst.floor([0, 1]))

    def test_ceiling_withNoneTypeArgument_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            AVLTree().ceiling(None)

    def test_ceiling_withEmptyBST_shouldReturnNone(self):
        bst = AVLTree()
        for i in range(200):
            self.assertIsNone(bst.ceiling(i))

    def test_ceiling_withArgumentNotInBSTHavingCeilingValue_shouldReturnSmallerStrictlyGreaterElementFromBST(self):
        bst = AVLTree()
        for i in range(10):
            bst.put(i, i)
        for i in range(10):
            self.assertEqual(i, bst.ceiling(i - 0.5))

    def test_ceiling_withArgumentInBST_shouldReturnGivenArgument(self):
        bst = AVLTree()
        for i in range(10):
            bst.put(i, i)
        for i in range(10):
            self.assertEqual(i, bst.ceiling(i))

    def test_ceiling_withCompareFunctionAndArgumentNotInBSTHavingCeilingValue_shouldReturnSmallerStrictlyGreaterElementFromBST(self):
        bst = AVLTree(self.cmp)
        for i in range(10):
            bst.put([0, i], i)
        for i in range(10):
            self.assertEqual([0, i], bst.ceiling([0, i - 0.5]))

    def test_ceiling_withCompareFunctionAndArgumentNotHavingCeilingValue_shouldReturnNone(self):
        bst = AVLTree(self.cmp)
        bst.put([0, 1], 1)
        self.assertIsNone(bst.ceiling([0, 2]))

    def test_predecessor_withNoneTypeArgument_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            AVLTree().predecessor(None)

    def test_predecessor_withEmptyBST_shouldReturnNone(self):
        self.assertIsNone(AVLTree().predecessor(1))

    def test_predecessor_withKeyNotInBST_shouldReturnNone(self):
        bst = AVLTree()
        bst.put(1, 0)
        bst.put(2, 0)
        self.assertIsNone(bst.predecessor(4))

    def test_predecessor_withKeyInBST_shouldReturnInOrderPredecessorOfGivenKey(self):
        bst = AVLTree()
        for i in range(10):
            bst.put(i, 0)
        for i in range(10):
            if i == 0:
                self.assertIsNone(bst.predecessor(i))
            else:
                self.assertEqual(i - 1, bst.predecessor(i))

    def test_predecessor_withCompareFunctionAndEmptyBST_shouldReturnNone(self):
        self.assertIsNone(AVLTree(self.cmp).predecessor(1))

    def test_predecessor_withCompareFunctionAndKeyNotInBST_shouldReturnNone(self):
        bst = AVLTree(self.cmp)
        bst.put([1, 0], 0)
        bst.put([2, 0], 0)
        self.assertIsNone(bst.predecessor([4, 0]))

    def test_predecessor_withCompareFunctionAndKeyInBST_shouldReturnInOrderPredecessorOfGivenKey(self):
        bst = AVLTree(self.cmp)
        for i in range(10):
            bst.put([i, 0], 0)
        for i in range(10):
            if i == 0:
                self.assertIsNone(bst.predecessor([i, 0]))
            else:
                self.assertEqual([i - 1, 0], bst.predecessor([i, 0]))

    def test_successor_withNoneTypeArgument_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            AVLTree().successor(None)

    def test_successor_withEmptyBST_shouldReturnNone(self):
        self.assertIsNone(AVLTree().successor(1))

    def test_successor_withKeyNotInBST_shouldReturnNone(self):
        bst = AVLTree()
        bst.put(1, 0)
        bst.put(2, 0)
        self.assertIsNone(bst.successor(4))

    def test_successor_withKeyInBST_shouldReturnInOrderSuccessorOfGivenKey(self):
        bst = AVLTree()
        for i in range(10):
            bst.put(i, 0)
        for i in range(10):
            if i == 9:
                self.assertIsNone(bst.successor(i))
            else:
                self.assertEqual(i + 1, bst.successor(i))

    def test_successor_withCompareFunctionAndEmptyBST_shouldReturnNone(self):
        self.assertIsNone(AVLTree(self.cmp).successor(1))

    def test_successor_withCompareFunctionAndKeyNotInBST_shouldReturnNone(self):
        bst = AVLTree(self.cmp)
        bst.put([1, 0], 0)
        bst.put([2, 0], 0)
        self.assertIsNone(bst.successor([4, 0]))

    def test_successor_withCompareFunctionAndKeyInBST_shouldReturnInOrderSuccessorOfGivenKey(self):
        bst = AVLTree(self.cmp)
        for i in range(10):
            bst.put([i, 0], 0)
        for i in range(10):
            if i == 9:
                self.assertIsNone(bst.successor([i, 0]))
            else:
                self.assertEqual([i + 1, 0], bst.successor([i, 0]))

    def test_rank_withNoneTypeArgument_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            AVLTree().rank(None)

    def test_rank_withEmptyBST_shouldReturnZero(self):
        self.assertEqual(0, AVLTree().rank(1))

    def test_rank_withKeyNotInBSTAndSmallerThanEveryKey_shouldReturnZero(self):
        bst = AVLTree()
        for i in range(10, 20):
            bst.put(i, 0)
        for i in range(10):
            self.assertEqual(0, bst.rank(i))

    def test_rank_withKeyNotInBSTAndGreaterThanEveryKey_shouldReturnBSTSize(self):
        bst = AVLTree()
        for i in range(10):
            bst.put(i, 0)
        for i in range(10, 20):
            self.assertEqual(bst.size(), bst.rank(i))

    def test_rank_withKeyNotInBSTAndAmongKeys_shouldReturnCorrectNumberOfKeysStrictlySmallerThanGivenKey(self):
        bst = AVLTree()
        for i in range(0, 20, 2):
            bst.put(i, 0)
        for i in range(1, 20, 2):
            self.assertEqual((i + 1) / 2, bst.rank(i))

    def test_rank_withKeyInBST_shouldReturnCorrectNumberOfKeysStrictlySmallerThanGivenKey(self):
        bst = AVLTree()
        for i in range(20):
            bst.put(i, 0)
        for i in range(20):
            self.assertEqual(i, bst.rank(i))

    def test_rank_withCompareFunctionAndEmptyBST_shouldReturnZero(self):
        self.assertEqual(0, AVLTree(self.cmp).rank(1))

    def test_rank_withCompareFunctionAndKeyNotInBSTAndSmallerThanEveryKey_shouldReturnZero(self):
        bst = AVLTree(self.cmp)
        for i in range(10, 20):
            bst.put([i, 0], 0)
        for i in range(10):
            self.assertEqual(0, bst.rank([i, 0]))

    def test_rank_withCompareFunctionAndKeyNotInBSTAndGreaterThanEveryKey_shouldReturnBSTSize(self):
        bst = AVLTree(self.cmp)
        for i in range(10):
            bst.put([i, 0], 0)
        for i in range(10, 20):
            self.assertEqual(bst.size(), bst.rank([i, 0]))

    def test_rank_withCompareFunctionAndKeyNotInBSTAndAmongKeys_shouldReturnCorrectNumberOfKeysStrictlySmallerThanGivenKey(self):
        bst = AVLTree(self.cmp)
        for i in range(0, 20, 2):
            bst.put([i, 0], 0)
        for i in range(1, 20, 2):
            self.assertEqual((i + 1) / 2, bst.rank([i, 0]))

    def test_rank_withCompareFunctionAndKeyInBST_shouldReturnCorrectNumberOfKeysStrictlySmallerThanGivenKey(self):
        bst = AVLTree(self.cmp)
        for i in range(20):
            bst.put([i, 0], 0)
        for i in range(20):
            self.assertEqual(i, bst.rank([i, 0]))

    def test_select_withEmptyBST_shouldRaiseAttributeError(self):
        bst = AVLTree()
        for i in range(-20, 20):
            with self.assertRaises(AttributeError):
                bst.select(i)

    def test_select_withArgumentOutOfBSTRange_shouldRaiseValueError(self):
        bst = AVLTree()
        for i in range(20):
            bst.put(i, i)

        for i in range(-20, 0):
            with self.assertRaises(ValueError):
                bst.select(i)
        for i in range(20, 40):
            with self.assertRaises(ValueError):
                bst.select(i)

    def select_withValidK_shouldReturnTheKthSmallestElementInBST(self):
        bst = AVLTree()
        for i in range(20):
            bst.put(i, i)

        for i in range(20):
            self.assertEqual(i, bst.select(i))

    def test_select_withCompareFunctionAndEmptyBST_shouldRaiseAttributeError(self):
        bst = AVLTree(self.cmp)
        for i in range(-20, 20):
            with self.assertRaises(AttributeError):
                bst.select(i)

    def test_select_withCompareFunctionAndArgumentOutOfBSTRange_shouldRaiseValueError(self):
        bst = AVLTree(self.cmp)
        for i in range(20):
            bst.put([i, 0], i)

        for i in range(-20, 0):
            with self.assertRaises(ValueError):
                bst.select(i)
        for i in range(20, 40):
            with self.assertRaises(ValueError):
                bst.select(i)

    def select_withCompareFunctionAndValidK_shouldReturnTheKthSmallestElementInBST(self):
        bst = AVLTree(self.cmp)
        for i in range(20):
            bst.put([i, 0], i)

        for i in range(20):
            self.assertEqual(i, bst.select(i))


