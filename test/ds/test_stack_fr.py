import unittest

from src.ds.stack_fr import StackFR


class TestStackFR(unittest.TestCase):

    def test_constructor_shouldCreateEmptyStack(self):
        s = StackFR()
        self.assertEqual(0, s.size())
        self.assertIsNone(s.top())

    def test_top_withEmptyStackAtGivenTimes_shouldReturnNone(self):
        s = StackFR()
        self.assertIsNone(s.top())

        for i in range(-20, 20):
            self.assertIsNone(s.top(i))

    def test_top_withUpdatesInCurrentTime_shouldReturnCurrentTopOfStack(self):
        s = StackFR()
        for i in range(1, 20):
            s.push(i, i)
            self.assertEqual(i, s.top())
        for i in range(1, 20):
            s.pop(20 + i)
            if i == 19:
                self.assertIsNone(s.top())
            else:
                self.assertEqual(19 - i, s.top())

    def test_top_withUpdatesInDifferentTimes_shouldReturnCorrectTopOfStackAtGivenTime(self):
        s = StackFR()

        for t in range(1, 20):
            s.push(t, t)

        for t in range(1, 20):
            s.pop(t + 0.5)
            self.assertIsNone(s.top(t + 0.5))

    def test_size_withUpdatesAlwaysInPresentTimeAndCheckingCurrentTime_shouldBehaveAsEphemeralStack(self):
        s = StackFR()
        self.assertEqual(0, s.size())

        for i in range(1, 40):
            s.push(i, i)
            self.assertEqual(i, s.size())
            self.assertEqual(i, s.size(i + 0.5))

        for i in range(1, 40):
            s.pop(40 + i)
            self.assertEqual(39 - i, s.size())

    def test_size_withDifferentTimeUpdates_shouldReturnCorrectSizeOfStackAfterOperations(self):
        s = StackFR()
        self.assertEqual(0, s.size())

        for i in range(1, 40):
            s.push(i, i)
            self.assertEqual(i, s.size())

        for i in range(1, 40):
            s.pop(i + 0.5)
            self.assertEqual(0, s.size(i + 0.5))

    def test_push_withNoneTypeArgumentTime_shouldRaiseValueError(self):
        s = StackFR()
        for v in range(-20, 20):
            with self.assertRaises(ValueError):
                s.push(v, None)

    def test_push_withNoneTypeArgumentValue_shouldRaiseValueError(self):
        s = StackFR()
        for t in range(-20, 20):
            with self.assertRaises(ValueError):
                s.push(None, t)

    def test_push_withGivenTimeAlreadyInUse_shouldRaiseValueError(self):
        s = StackFR()
        s.push(1, 20)
        with self.assertRaises(ValueError):
            s.push(2, 20)

    def test_push_withDifferentTimes_shouldPushValueAtGivenTime(self):
        s = StackFR()

        # Should behave as ephemeral stack
        for t in range(1, 20):
            s.push(t, t)
            self.assertEqual(t, s.top())

        for t in range(1, 20):
            s.push(t + 0.5, t + 0.5)
            self.assertEqual(t + 0.5, s.top(t + 0.5))

    def test_pop_withNoneTypeArgumentTime_shouldRaiseValueError(self):
        s = StackFR()
        for v in range(-20, 20):
            with self.assertRaises(ValueError):
                s.pop(None)

    def test_pop_withGivenTimeAlreadyInUse_shouldRaiseValueError(self):
        s = StackFR()
        s.push(1, 20)
        with self.assertRaises(ValueError):
            s.pop(20)

    def test_pop_withUpdatesInCurrentTime_shouldRemoveAndReturnTopOfCurrentStack(self):
        # Should behave as ephemeral stack
        s = StackFR()

        for t in range(1, 20):
            s.push(t, t)

        for t in range(1, 20):
            if t == 19:
                self.assertIsNone(s.pop(20 + t))
                self.assertIsNone(s.top())
            else:
                self.assertEqual(20 - t, s.top())
                s.pop(20 + t)
                self.assertEqual(20 - t - 1, s.top())

    def test_pop_withDifferentTimeUpdates_shouldRemoveAndReturnTopOfStackAtGivenTime(self):
        s = StackFR()

        for t in range(1, 20):
            s.push(t, t)

        for t in range(1, 20):
            s.pop(t + 0.5)
            self.assertIsNone(s.top(t + 0.5))

    def test_delete_withNoExistingOperationInGivenTime_shouldRaiseValueError(self):
        s = StackFR()
        for i in range(-20, 20):
            with self.assertRaises(ValueError):
                s.delete(i)

        for i in range(20):
            s.push(i, i)

        for i in range(20):
            with self.assertRaises(ValueError):
                s.delete(i + 0.5)

    def test_delete_withExistingOperationInGivenTime_shouldDeleteOperationAndPropagateItsEffects(self):
        s = StackFR()

        # s = [push(1), pop(), ..., push(t), pop()]
        # s will be an empty stack at the end of the loop
        for t in range(1, 20):
            s.push(t, t)
            s.pop(t + 0.5)

        self.assertEqual(0, s.size())
        self.assertIsNone(s.top())

        # Deleting all pop operations
        # s = [19, 18, ..., 1]
        for t in range(1, 20):
            s.delete(t + 0.5)
            self.assertEqual(t, s.size())
            self.assertEqual(t, s.top())

        # Deleting all push operations
        # s = []
        for t in range(1, 20):
            s.delete(t)
            self.assertEqual(19 - t, s.size())
            if t == 19:
                self.assertIsNone(s.top())
            else:
                self.assertEqual(19, s.top())

    # def test_print_withNotUsedStackAndDifferentTimes_shouldReturnEmptyStackRepresentationAlways(self):
    #     s = StackFR()
    #     for i in range(-20, 20):
    #         self.assertEqual("[]", s.print(i))

    def test_now(self):
        s = StackFR()
        s.push(50, 1)
        s.push(51, 5)
        s.push(52, 8)
        s.pop(3)
        s.pop(10)
        self.assertEqual(51, s.top(10))


    # def test_print_withUsedStack_shouldReturnCorrectValuesAtStackInGivenTime(self):
    #     s = StackFR()
    #     expected = ["[]"]
    #     e = []
    #     for i in range(1, 20):
    #         e.insert(0, i)
    #         s.push(i, i)
    #         self.assertEqual(str(e), s.print())
    #         self.assertEqual(str(e), s.print(i))
    #         self.assertEqual(str(e), s.print(i + 0.5))
    #         expected.append(str(e))
    #
    #     for i in range(20):
    #         self.assertEqual(expected[i], s.print(i))
    #         self.assertEqual(expected[i], s.print(i + 0.5))
        #
        # for i in range(1, 20):
        #     s.pop(19 + i)
        #     self.assertEqual(expected[19 - i], s.print())
