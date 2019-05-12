from src.ds.avl_tree       import AVLTree
from src.ds.prefix_sum_bst import PrefixSumBST


class MinPQPR:

    def __init__(self):
        self.__min       = None
        self.__cur_time  = None
        self.__now       = AVLTree()
        self.__insertion = AVLTree()
        self.__updates   = PrefixSumBST()

    def empty(self):
        return self.__min is None

    def size(self):
        return self.__now.size()

    def __len__(self):
        return self.size()

    def min(self):
        return self.__min

    def insert(self, key, time):
        self.__update_time(time)
        self.__insertion.put(time, key)

        if self.__updates.empty():
            self.__now.put(key, time)
            self.__updates.put(time, key, 0)
            self.__update_min()
            return

        bridge = time
        keys = self.__updates.keys(self.__updates.min(), time)
        for t in keys:
            if self.__updates.prefix_sum(t) == 0:
                bridge = t

        if self.__insertion.empty():
            keys = set()
        else:
            keys = set(self.__insertion.values(bridge, self.__insertion.max()))
            keys = keys - set(self.__now.keys_in_order())

        if len(keys) == 0:
            max_k = key
        else:
            max_k = max(keys)

        self.__now.put(max_k, 0)
        self.__updates.put(time, key, int(max_k != key))

        self.__update_min()

    def delete_min(self, time):
        self.__updates.put(time, "delete-min", -1)

        if self.__insertion.empty():
            self.__update_time(time)
            return None

        if self.__update_time(time):
            min_k = self.__min

            self.__now.delete_min()
            self.__update_min()

            return min_k

        bridge = time
        keys = self.__updates.keys(time, self.__updates.max())
        for t in keys:
            if self.__updates.prefix_sum(t) == 0:
                bridge = t
                break

        if self.__insertion.empty():
            keys = set()
        else:
            keys = set(self.__insertion.values(self.__insertion.min(), bridge))
            keys = keys.intersection(set(self.__now.keys_in_order()))

        min_k = min(keys)

        self.__now.delete(min_k)
        self.__update_min()

        return min_k

    def delete(self, time):
        if time is None:
            raise ValueError("Invalid 'time' argument of None Type")
        if time not in self.__updates:
            raise ValueError("'time' argument does "
                             "not correspond to any operation")

        if self.__updates.get(time) == "delete-min":
            bridge = time
            keys = self.__updates.keys(self.__updates.min(), time)
            for t in keys:
                if t != time and self.__updates.prefix_sum(t) == 0:
                    bridge = t

            if self.__insertion.empty():
                keys = set()
            else:
                keys = set(self.__insertion.values(bridge, self.__insertion.max()))
                keys = keys - set(self.__now.keys_in_order())

            self.__now.put(max(keys), 0)
        else:
            bridge = time
            keys = self.__updates.keys(time, self.__updates.max())
            for t in keys:
                if t != time and self.__updates.prefix_sum(t) == 0:
                    bridge = t
                    break

            if self.__insertion.empty():
                keys = set()
            else:
                keys = set(self.__insertion.values(self.__insertion.min(), bridge))
                keys = keys.intersection(set(self.__now.keys_in_order()))

            min_k = min(keys)
            self.__now.delete(min_k)
        self.__updates.delete(time)
        self.__update_min()

    def __update_time(self, time):
        if self.__cur_time is None or \
           time >= self.__cur_time:
            self.__cur_time = time
            return True
        return False

    def __update_min(self):
        if self.__now.empty():
            self.__min = None
        else:
            self.__min = self.__now.min()

