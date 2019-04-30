import unittest

from src.ds.queue_fr import QueueFR


class TestQueueFR(unittest.TestCase):

    def test_constructor_shouldCreateEmptyQueue(self):
        q = QueueFR()
        self.assertEqual(0, q.size())

    def test_size_withUpdatesAlwaysInPresentTimeAndCheckingCurrentTime_shouldBehaveAsEphemeralQueue(self):
        q = QueueFR()
        self.assertEqual(0, q.size())

        for i in range(1, 40):
            q.enqueue(i, i)
            self.assertEqual(i, q.size())
            self.assertEqual(i, q.size(i + 0.5))

        for i in range(1, 40):
            q.dequeue(40 + i)
            self.assertEqual(39 - i, q.size())

    def test_size_withDifferentTimeUpdates_shouldReturnCorrectSizeOfQueueAfterOperations(self):
        q = QueueFR()
        self.assertEqual(0, q.size())

        for i in range(1, 40):
            q.enqueue(i, i)
            self.assertEqual(i, q.size())

        for i in range(1, 40):
            q.dequeue(i + 0.5)
            self.assertEqual(0, q.size(i + 0.5))

    def test_enqueue_withNoneTypeArgumentTime_shouldRaiseValueError(self):
        q = QueueFR()
        for v in range(-20, 20):
            with self.assertRaises(ValueError):
                q.enqueue(v, None)

    def test_enqueue_withNoneTypeArgumentValue_shouldRaiseValueError(self):
        q = QueueFR()
        for t in range(-20, 20):
            with self.assertRaises(ValueError):
                q.enqueue(None, t)

    def test_enqueue_withGivenTimeAlreadyInUse_shouldRaiseValueError(self):
        q = QueueFR()
        q.enqueue(1, 20)
        with self.assertRaises(ValueError):
            q.enqueue(2, 20)

    def test_enqueue_withDifferentTimes_shouldEnqueueValueAtGivenTime(self):
        q = QueueFR()

        # Should behave as ephemeral queue
        for t in range(20):
            q.enqueue(t, t)
            self.assertEqual(0, q.front())
            self.assertEqual(t, q.back())

        for t in range(1, 20):
            q.enqueue(t + 0.5, t + 0.5)
            self.assertEqual(0, q.front(t + 0.5))
            self.assertEqual(t + 0.5, q.back(t + 0.5))

    def test_dequeue_withNoneTypeArgumentTime_shouldRaiseValueError(self):
        q = QueueFR()
        for v in range(-20, 20):
            with self.assertRaises(ValueError):
                q.dequeue(None)

    def test_dequeue_withGivenTimeAlreadyInUse_shouldRaiseValueError(self):
        q = QueueFR()
        q.enqueue(1, 20)
        with self.assertRaises(ValueError):
            q.dequeue(20)

    def test_dequeue_withDifferentTimes_shouldRemoveAndReturnFrontOfQueueAtGivenTime(self):
        q = QueueFR()

        for t in range(20):
            q.enqueue(t, t)

        for t in range(20):
            self.assertEqual(t, q.dequeue(20 + t))
            if t == 19:
                self.assertIsNone(q.front())
            else:
                self.assertEqual(t + 1, q.front())