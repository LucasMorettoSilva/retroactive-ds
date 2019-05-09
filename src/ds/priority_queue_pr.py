from src.ds.avl_tree       import AVLTree
from src.ds.prefix_sum_bst import PrefixSumBST


class PriorityQueuePR:

    def __init__(self):
        self.__now      = AVLTree()
        self.__dels     = AVLTree()
        self.__ins      = AVLTree()
        self.__updates  = PrefixSumBST()
        self.__cur_time = None

    def size(self):
        return self.__now.size()

    def __len__(self):
        return self.size()

    def min(self):
        if self.__now.empty():
            return None
        return self.__now.min()

    def insert(self, key, time):
        if self.__dels.empty():
            max_k = key
        else:
            del_keys = self.__dels.keys(time, self.__dels.max())
            dels     = [self.__dels.get(t) for t in del_keys]
            max_k    = max(key, max(dels))

        self.__update_time(time)
        self.__ins.put(time, key)

        if max_k == key:
            self.__now.put(key, time)
            self.__updates.put(time, key, 0)
        else:
            self.__updates.put(time, key, 1)

    def delete_min(self, time):
        if self.__updates.empty():
            self.__updates.put(time, "delete-min", -1)
            return None

        if self.__update_time(time):
            min_k = self.__now.min()
            min_time  = self.__now.get(min_k)

            self.__now.delete_min()
            self.__dels.put(min_time, min_k)
            self.__updates.put(time, "delete-min", -1)

            return min_k

        keys = self.__updates.keys(time, self.__updates.max())
        for t in keys:
            if self.__updates.prefix_sum(t) == 0:
                bridge = t
                break

        if self.__dels.empty():
            dels = []
        else:
            dels = self.__dels.keys(self.__dels.min(), bridge)

        min_k = None
        min_time  = None
        for t in self.__ins:
            if t not in dels:
                val = self.__ins.get(t)
                if min_time is None or val < min_k:
                    min_k  = val
                    min_time = t

        self.__now.delete(min_k)
        self.__dels.put(min_time, min_k)
        self.__updates.put(time, "delete-min", -1)

        return min_k

    def __update_time(self, time):
        if self.__cur_time is None or \
           time >= self.__cur_time:
            self.__cur_time = time
            return True
        return False

