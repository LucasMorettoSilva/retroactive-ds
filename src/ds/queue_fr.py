from src.ds.avl_tree import AVLTree


class QueueFR:

    def __init__(self):
        self.__back  = None
        self.__front = None
        self.__te = AVLTree()
        self.__td = AVLTree()
        self.__cur_time = 0

    def front(self, time=None):
        if time is None:
            # return self.__front
            time = self.__cur_time
        if self.size(time) == 0:
            return None
        if self.__td.empty():
            return self.__te.get(self.__te.min())
        time = self.__td.floor(time)
        d = self.__td.rank(time)
        return self.__te.get(self.__te.select(d + 1))

    def back(self, time=None):
        if time is None:
            return self.__back
        if self.__te.empty():
            return None
        time = self.__te.floor(time)
        rank = self.__te.rank(time)
        return self.__te.get(self.__te.select(rank + 1))

    def enqueue(self, val, time):
        if val  is None or \
           time is None:
            raise ValueError("Invalid argument of None Type")

        self.__check_time(time)
        if self.__update_time(time):
            self.__back = val
            if self.size() == 0:
                self.__front = self.__back

        self.__te.put(time, val)

    def dequeue(self, time):
        self.__check_time(time)
        self.__td.put(time, time)
        d = self.__td.rank(time)
        res = self.__te.get(self.__te.select(d))
        if self.__update_time(time):
            size = self.size()
            if size == 0:
                self.__back = None
                self.__front = None
            elif size == 1:
                self.__front = self.__back
            else:
                self.__front = self.__te.get(self.__te.select(self.__te.size() - size + 1))
        return res

    def size(self, time=None):
        if time is None:
            time = self.__cur_time
        size = self.__te.rank(time) - self.__td.rank(time)
        if size < 0:
            return 0
        return size

    def __check_time(self, time):
        if time is None:
            raise ValueError("Invalid argument 'time' of None Type")
        if time in self.__te or \
           time in self.__td:
            raise ValueError("Given 'time' is already in use")

    def __update_time(self, time):
        if time >= self.__cur_time:
            self.__cur_time = time
            return True
        return False
