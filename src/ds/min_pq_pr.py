from src.ds.avl_tree       import AVLTree
from src.ds.insertion_tree import InsertionTree
from src.ds.prefix_sum_bst import PrefixSumBST


class MinPQPR:

    def __init__(self):
        self.__min       = None
        self.__cur_time  = None
        self.__now       = AVLTree()
        self.__insertion = InsertionTree()
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

        if self.__updates.empty():
            self.__now.put(key, time)
            self.__updates.put(time, key, 0)
            self.__update_min()

            self.__insertion.put(time, key, True)

            return

        bridge = self.__updates.find_bridge_before(time)

        bridge = self.__insertion.ceiling(bridge)
        if bridge:
            max_in = self.__insertion.max_right(bridge)
        else: max_in = None

        if max_in is None:
            max_k = key
        else:
            max_k = max(max_in.val, key)


        if max_in and max_k == max_in.val:
            self.__now.put(max_in.val, max_in.key)
            self.__insertion.put(max_in.key, max_in.val, active=True)
            self.__updates.put(time, key, 1)
        else:
            self.__insertion.put(time, key, active=True)
            self.__now.put(key, time)
            self.__updates.put(time, key, 0)

        self.__update_min()



    def delete_min(self, time):
        self.__updates.put(time, "delete-min", -1)

        if self.__insertion.empty():
            self.__update_time(time)
            return None

        if self.__update_time(time):
            min_k = self.__min
            min_t = self.__now.get(min_k)


            self.__now.delete_min()
            self.__update_min()

            self.__insertion.put(min_t, min_k, False)

            return min_k

        bridge = self.__updates.find_bridge_after(time)

        min_in = self.__insertion.min_left(self.__insertion.floor(bridge))
        min_k = min_in.val

        self.__now.delete(min_k)
        self.__update_min()
        self.__insertion.put(min_in.key, min_in.val, False)

        return min_k

    def delete(self, time):
        if time is None:
            raise ValueError("Invalid 'time' argument of None Type")
        if time not in self.__updates:
            raise ValueError("'time' argument does "
                             "not correspond to any operation")

        if self.__updates.get(time) == "delete-min":
            bridge = self.__updates.find_bridge_before(time)

            max_in = self.__insertion.max_right(self.__insertion.ceiling(bridge))

            self.__now.put(max_in.val, max_in.key)
            self.__insertion.put(max_in.key, max_in.val, True)
        else:
            bridge = self.__updates.find_bridge_after(time)
            min_in = self.__insertion.min_left(self.__insertion.floor(bridge))
            min_k = min_in.val

            self.__now.delete(min_k)
            self.__insertion.delete(min_in.key)

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

