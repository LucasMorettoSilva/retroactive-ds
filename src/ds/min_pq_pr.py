from src.ds.avl_tree       import AVLTree
from src.ds.prefix_sum_bst import PrefixSumBST


class MinPQPR:

    def __init__(self):
        self.__min = None
        self.__now      = AVLTree()
        self.__ins      = AVLTree()
        self.__updates  = PrefixSumBST()
        self.__cur_time = None

    def size(self):
        return self.__now.size()

    def __len__(self):
        return self.size()

    def min(self):
        return self.__min

    def insert(self, key, time):
        self.__update_time(time)

        if self.__updates.empty():
            self.__ins.put(time, key)
            self.__now.put(key, time)
            self.__updates.put(time, key, 0)
            self.__update_min()
            return

        bridge = time
        keys = self.__updates.keys(self.__updates.min(), time)
        for t in keys:
            if self.__updates.prefix_sum(t) == 0:
                bridge = t

        if self.__ins.empty():
            times = set()
        else:
            times = set(self.__ins.keys(bridge, self.__ins.max()))

        times = times - set(self.__now.keys_in_order())
        max_k = None
        max_t = None
        for t in times:
            cur = self.__ins.get(t)
            if max_k is None or cur > max_k:
                max_k = key
                max_t = t

        self.__ins.put(time, key)

        if max_k == key:
            self.__now.put(key, time)
            self.__updates.put(time, key, 0)
        else:
            self.__now.put(max_k, max_t)
            self.__updates.put(time, key, 1)

        self.__update_min()

    def delete_min(self, time):
        self.__updates.put(time, "delete-min", -1)

        if self.__ins.empty():
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

        if self.__ins.empty():
            keys = set()
        else:
            keys = set(self.__ins.values(self.__ins.min(), bridge))
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
                if self.__updates.prefix_sum(t) == 0:
                    bridge = t

            if self.__ins.empty():
                keys = set()
            else:
                keys = set(self.__ins.values(bridge, self.__ins.max()))
                keys = keys - set(self.__now.keys_in_order())

            self.__now.put(max(keys), 0)
        else:
            bridge = time
            keys = self.__updates.keys(time, self.__updates.max())
            for t in keys:
                if self.__updates.prefix_sum(t) == 0:
                    bridge = t
                    break

            if self.__ins.empty():
                keys = set()
            else:
                keys = set(self.__ins.values(self.__ins.min(), bridge))
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

