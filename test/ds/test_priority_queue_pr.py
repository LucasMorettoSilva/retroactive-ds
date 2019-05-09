import unittest

from src.ds.priority_queue_pr import PriorityQueuePR


class TestPriorityQueuePR(unittest.TestCase):

    def test_insert_withTimeAlwaysInPresent_shouldBehaveAsEphemeralMinPQ(self):
        pq = PriorityQueuePR()
        for i in range(1, 20):
            pq.insert(-i, i)
            self.assertEqual(-i, pq.min())
            self.assertEqual(i, pq.size())
            self.assertEqual(i, len(pq))

        for i in range(1, 20):
            self.assertEqual(-20 + i, pq.delete_min(19 + i))
            self.assertEqual(19 - i, pq.size())

    def test_insert_withDifferentTimes_shouldInsertItemAndPropagateChanges(self):
        pq = PriorityQueuePR()

        for i in range(1, 20):
            pq.insert(-i, i)

        for i in range(1, 20):
            pq.insert(-19 -i, i + 0.5)
            self.assertEqual(-19 -i, pq.min())
            self.assertEqual(19 + i, pq.size())

        pq.insert(-90, -90)
        self.assertEqual(-90, pq.min())


