from src.ds.avl_tree import AVLTree


class StackFR:

    class Node:

        def __init__(self, type, value):
            self.type  = type
            self.value = value

    def __init__(self):
        self.__top = None

        self.__op  = AVLTree()

        self.__push = AVLTree()
        self.__pop  = AVLTree()
        self.__cur_time = 0

    def top(self, time=None):
        if time is None or time >= self.__cur_time:
            return self.__top

        time = self.__op.floor(time)
        if time is None:
            return None

        operation = self.__op[time]
        if operation.type == "PUSH":
            return operation.value

        # TODO


        if self.__push.empty():
            return None

        if self.size(time) == 0:
            return None

        push_time = self.__push.floor(time)

        if self.__pop.empty():
            return self.__push.get(push_time)

        pop_time = self.__pop.floor(time)

        if pop_time is None or push_time > pop_time:
            return self.__push.get(push_time)

        push_rank = self.__push.rank(push_time)
        pop_rank  = self.__pop.rank(pop_time)
        return self.__push.get(self.__push.select(push_rank - pop_rank - 1))

    def push(self, val, time):
        if val  is None or \
           time is None:
            raise ValueError("Invalid argument of None Type")

        self.__check_time(time)

        if self.__update_time(time):
            self.__top = val

        self.__push.put(time, val)

    def delete(self, time):
        if time is None:
           raise ValueError("Invalid 'time' argument of None Type")

        if time in self.__push:
            self.__push.delete(time)
        elif time in self.__pop:
            self.__pop.delete(time)
        else:
            raise ValueError("'time' argument does "
                             "not correspond to any operation")

        self.__top  = self.top(self.__cur_time)

    def pop(self, time):
        self.__check_time(time)
        self.__update_time(time)

        self.__pop.put(time, time)
        self.__top = self.top(self.__cur_time)

        return self.__top

    def size(self, time=None):
        if time is None:
            time = self.__cur_time
        size = self.__push.rank(time) - self.__pop.rank(time)
        if time in self.__push:
            size += 1
        elif time in self.__pop:
            size -= 1
        if size < 0:
            return 0
        return size

    def print(self, time=None):
        if time is None:
            time = self.__cur_time

        if self.size(time) == 0:
            return "[]"

        res = []
        pushes = self.__push.keys_in_order()
        pops   = self.__pop.keys_in_order()

        ipu = 0
        ipo = 0

        if self.__pop.empty():
            for key in pushes:
                if key <= time:
                    res.insert(0, self.__push.get(key))
            return str(res)

        change = True
        while change:
            change = False
            if pushes[ipu] < pops[ipo]:
                res.insert(0, self.__push.get(pushes[ipu]))
                change = True
                if ipu + 1 < len(pushes):
                    ipu += 1

            else:
                res.pop(0)
                change = True
                if ipo + 1 < len(pops):
                    ipo += 1
        return str(res)

    def __check_time(self, time):
        if time is None:
            raise ValueError("Invalid argument 'time' of None Type")
        if time in self.__push or \
           time in self.__pop:
            raise ValueError("Given 'time' is already in use")

    def __update_time(self, time):
        if time >= self.__cur_time:
            self.__cur_time = time
            return True
        return False
