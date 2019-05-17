class PrefixSumBST:

    class __Node:

        def __init__(self, key=None, val=None, height=0, size=0, w=0, active=True):
            self.key = key
            self.val = val

            self.height = height
            self.size   = size

            # Children
            self.left  = None
            self.right = None

            # Retroactive heap
            self.max_sub = None
            self.min_sub = None
            self.active  = active

            # Prefix Sum
            self.w = w
            self.left_sum  = self.w
            self.right_sum = 0

    def __init__(self, cmp=None):
        self.__root = None
        self.__cmp  = cmp

    def __len__(self):
        return self.size()

    def __compare(self, a, b):
        if self.__cmp is not None:
            return self.__cmp(a, b)
        if a < b:
            return -1
        if a > b:
            return 1
        return 0

    def __parent(self, x, key, parent):
        if x is None:
            return None
        cmp = self.__compare(key, x.key)
        if cmp < 0:
            return self.__parent(x.left, key, x)
        if cmp > 0:
            return self.__parent(x.right, key, x)
        return parent

    def find_bridge_before(self, key):
        if key is None:
            raise ValueError("Invalid argument 'key' of None Type")
        return self.__find_bridge_before(self.predecessor(key), key, key)

    def __find_bridge_before(self, x, key, so_far):
        if x is None:
            return so_far
        if self.prefix_sum(x) == 0:
            return x
        return self.__find_bridge_before(self.predecessor(x), key, so_far)

    def prefix_sum(self, key):
        if key is None:
            raise ValueError("Invalid argument 'key' of None Type")
        if key not in self:
            raise ValueError("'key' = {}, not in BST".format(key))
        return self.__prefix_sum(self.__root, key)

    def __prefix_sum(self, x, key):
        if x is None:
            return 0
        cmp = self.__compare(key, x.key)
        if cmp < 0:
            return self.__prefix_sum(x.left, key)
        if cmp > 0:
            return x.left_sum + self.__prefix_sum(x.right, key)
        return x.left_sum

    def update(self, key, active):
        x = self.__get(self.__root, key)
        x.active = active
        parent = self.__parent(self.__root, key, None)
        while parent is not None:
            self.__update_max_min(parent)
            parent = self.__parent(self.__root, parent.key, None)

    def values(self, lo, hi):
        if lo is None or \
           hi is None:
           raise ValueError("Illegal argument of None Type")
        q = []
        self.__values(self.__root, q, lo, hi)
        return q

    def __values(self, x, q, lo, hi):
        if x is None:
            return
        cmplo = self.__compare(lo, x.key)
        cmphi = self.__compare(hi, x.key)
        if cmplo < 0:
            self.__values(x.left, q, lo, hi)
        if cmplo <= 0 <= cmphi:
            q.append(x.val)
        if cmphi > 0:
            self.__values(x.right, q, lo, hi)

    def max_sub(self, key):
        x = self.__get(self.__root, key)
        if x is None:
            return None
        return x.max_sub

    def min_sub(self, key):
        x = self.__get(self.__root, key)
        if x is None:
            return None
        return x.min_sub

    @staticmethod
    def __max_sub(x):
        if x is None:
            return None
        return x.max_sub

    @staticmethod
    def __min_sub(x):
        if x is None:
            return None
        return x.min_sub

    @staticmethod
    def __left_sum(x):
        if x is None:
            return 0
        return x.left_sum

    @staticmethod
    def __right_sum(x):
        if x is None:
            return 0
        return x.right_sum

    def rank(self, key):
        if key is None:
            raise ValueError()
        return self.__rank(self.__root, key)

    def __rank(self, x, key):
        if x is None:
            return 0
        cmp = self.__compare(key, x.key)
        if cmp < 0:
            return self.__rank(x.left, key)
        if cmp > 0:
            return 1 + self.__size(x.left) + self.__rank(x.right, key)
        return self.__size(x.left)

    def successor(self, key):
        if key is None:
            raise ValueError("Illegal argument of None type")
        if key not in self:
            return None
        x = self.__successor(self.__root, key)
        if x is None:
            return None
        return x.key

    def __successor(self, x, key):
        if x is None:
            return None
        cmp = self.__compare(key, x.key)
        if cmp < 0:
            t = self.__successor(x.left, key)
            if t is not None:
                return t
            return x
        return self.__successor(x.right, key)

    def predecessor(self, key):
        if key is None:
            raise ValueError("Illegal argument of None type")
        if key not in self:
            return None
        x = self.__predecessor(self.__root, key)
        if x is None:
            return None
        return x.key

    def __predecessor(self, x, key):
        if x is None:
            return None
        cmp = self.__compare(key, x.key)
        if cmp <= 0:
            return self.__predecessor(x.left, key)
        t = self.__predecessor(x.right, key)
        if t is not None:
            return t
        return x

    def empty(self):
        return self.__root is None

    def size(self):
        return self.__size(self.__root)

    @staticmethod
    def __size(x):
        if x is None:
            return 0
        return x.size

    def height(self):
        return self.__height(self.__root)

    @staticmethod
    def __height(x):
        if x is None:
            return -1
        return x.height

    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        if key is None:
            raise ValueError("Illegal argument of None type")
        x = self.__get(self.__root, key)
        if x is None:
            return None
        return x.val

    def __get(self, x, key):
        if x is None:
            return None
        cmp = self.__compare(key, x.key)
        if cmp < 0:
            return self.__get(x.left, key)
        if cmp > 0:
            return self.__get(x.right, key)
        return x

    def __contains__(self, key):
        return self[key] is not None

    def put(self, key, val, w=0, active=True):
        if key is None:
            raise ValueError()
        if val is None:
            self.delete(key)
            return
        self.__root = self.__put(self.__root, key, val, w, active)

    def __put(self, x, key, val, w, active):
        if x is None:
            return self.__Node(key, val, 0, 1, w, active)

        cmp = self.__compare(key, x.key)
        if cmp < 0:
            x.left = self.__put(x.left, key, val, w, active)
        elif cmp > 0:
            x.right = self.__put(x.right, key, val, w, active)
        else:
            x.val = val
            x.active = active

        x.size      = 1 + self.__size(x.left) + self.__size(x.right)
        x.height    = 1 + max(self.__height(x.left), self.__height(x.right))
        x.left_sum  = x.w + self.__left_sum(x.left) + self.__right_sum(x.left)
        x.right_sum = self.__left_sum(x.right) + self.__right_sum(x.right)

        if x.max_sub is None or x.max_sub < key:
            if not active:
                x.max_sub = key
        if x.min_sub is None or x.min_sub > key:
            if active:
                x.min_sub = key

        return self.__balance(x)

    def __update_max_min(self, x):
        max_sub = list(filter(None.__ne__, [self.__max_sub(x.left), self.__max_sub(x.right)]))
        min_sub = list(filter(None.__ne__, [self.__min_sub(x.left), self.__min_sub(x.right)]))
        if x.left is not None:
            if x.left.active:
                min_sub.append(x.left.key)
            else:
                max_sub.append(x.left.key)
        if x.right is not None:
            if x.right.active:
                min_sub.append(x.right.key)
            else:
                max_sub.append(x.right.key)
        if len(max_sub) == 0:
            x.max_sub = None
        else:
            x.max_sub = max(max_sub)
        if len(min_sub) == 0:
            x.min_sub = None
        else:
            x.min_sub = min(min_sub)

    def __balance_factor(self, x):
        return self.__height(x.left) - self.__height(x.right)

    def __balance(self, x):
        if self.__balance_factor(x) < -1:
            if self.__balance_factor(x.right) > 0:
                x.right = self.__rotate_right(x.right)
            x = self.__rotate_left(x)
        elif self.__balance_factor(x) > 1:
            if self.__balance_factor(x.left) < 0:
                x.left = self.__rotate_left(x.left)
            x = self.__rotate_right(x)
        return x

    def __rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        y.size = x.size
        x.size = 1 + self.__size(x.left) + self.__size(x.right)
        x.height = 1 + max(self.__height(x.left), self.__height(x.right))
        y.height = 1 + max(self.__height(y.left), self.__height(y.right))

        self.__update_max_min(x)
        self.__update_max_min(y)

        x.left_sum = x.w + self.__left_sum(x.left) + self.__right_sum(x.left)
        x.right_sum = self.__left_sum(x.right) + self.__right_sum(x.right)

        y.left_sum = y.w + self.__left_sum(y.left) + self.__right_sum(y.left)
        y.right_sum = self.__left_sum(y.right) + self.__right_sum(y.right)

        return y

    def __rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        y.size = x.size
        x.size = 1 + self.__size(x.left) + self.__size(x.right)
        x.height = 1 + max(self.__height(x.left), self.__height(x.right))
        y.height = 1 + max(self.__height(y.left), self.__height(y.right))

        self.__update_max_min(x)
        self.__update_max_min(y)

        x.left_sum  = x.w + self.__left_sum(x.left) + self.__right_sum(x.left)
        x.right_sum = self.__left_sum(x.right) + self.__right_sum(x.right)

        y.left_sum  = y.w + self.__left_sum(y.left) + self.__right_sum(y.left)
        y.right_sum = self.__left_sum(y.right) + self.__right_sum(y.right)

        return y

    def delete(self, key):
        if key is None:
            raise ValueError()
        if key in self:
            self.__root = self.__delete(self.__root, key)

    def __delete(self, x, key):
        cmp = self.__compare(key, x.key)
        if cmp < 0:
            x.left = self.__delete(x.left, key)
        elif cmp > 0:
            x.right = self.__delete(x.right, key)
        else:
            if x.left is None:
                return x.right
            if x.right is None:
                return x.left
            y = x
            x = self.__min(y.right)
            x.right = self.__delete_min(y.right)
            x.left = y.left
            x.max_sub = y.max_sub
            x.min_sub = y.min_sub

        x.size      = 1 + self.__size(x.left) + self.__size(x.right)
        x.height    = 1 + max(self.__height(x.left), self.__height(x.right))
        x.left_sum  = x.w + self.__left_sum(x.left) + self.__right_sum(x.left)
        x.right_sum = self.__left_sum(x.right) + self.__right_sum(x.right)
        self.__update_max_min(x)

        return self.__balance(x)

    def delete_min(self):
        if self.empty():
            raise AttributeError("AVL Tree underflow")
        self.__root = self.__delete_min(self.__root)

    def __delete_min(self, x):
        if x.left is None:
            return x.right
        x.left = self.__delete_min(x.left)
        x.size = 1 + self.__size(x.left) + self.__size(x.right)
        x.height = 1 + max(self.__height(x.left), self.__height(x.right))

        x.left_sum = x.w + self.__left_sum(x.left) + self.__right_sum(x.left)
        x.right_sum = self.__left_sum(x.right) + self.__right_sum(x.right)

        self.__update_max_min(x)
        return self.__balance(x)

    def delete_max(self):
        if self.empty():
            raise AttributeError("AVL Tree underflow")
        self.__root = self.__delete_max(self.__root)

    def __delete_max(self, x):
        if x.right is None:
            return x.left
        x.right = self.__delete_max(x.right)
        x.size = 1 + self.__size(x.left) + self.__size(x.right)
        x.height = 1 + max(self.__height(x.left), self.__height(x.right))

        x.left_sum = x.w + self.__left_sum(x.left) + self.__right_sum(x.left)
        x.right_sum = self.__left_sum(x.right) + self.__right_sum(x.right)

        self.__update_max_min(x)
        return self.__balance(x)

    def min(self):
        if self.empty():
            raise AttributeError("AVL Tree underflow")
        return self.__min(self.__root).key

    def __min(self, x):
        if x.left is None:
            return x
        return self.__min(x.left)

    def max(self):
        if self.empty():
            raise AttributeError("AVL Tree underflow")
        return self.__max(self.__root).key

    def __max(self, x):
        if x.right is None:
            return x
        return self.__max(x.right)

    def keys(self, lo, hi):
        if lo is None or \
           hi is None:
            raise ValueError("Illegal argument of None Type")
        q = []
        self.__keys(self.__root, q, lo, hi)
        return q

    def __keys(self, x, q, lo, hi):
        if x is None:
            return
        cmplo = self.__compare(lo, x.key)
        cmphi = self.__compare(hi, x.key)
        if cmplo < 0:
            self.__keys(x.left, q, lo, hi)
        if cmplo <= 0 <= cmphi:
            q.append(x.key)
        if cmphi > 0:
            self.__keys(x.right, q, lo, hi)

    def keys_in_order(self):
        keys  = []
        stack = []
        cur   = self.__root
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            keys.append(cur.key)
            cur = cur.right
        return keys

    def floor(self, key):
        if key is None:
            raise ValueError("Illegal argument of None type")
        if self.empty():
            raise AttributeError("AVLTree underflow")
        x = self.__floor(self.__root, key)
        if x is None:
            return None
        return x.key

    def __floor(self, x, key):
        if x is None:
            return None
        cmp = self.__compare(key, x.key)
        if cmp == 0:
            return x
        if cmp < 0:
            return self.__floor(x.left, key)
        t = self.__floor(x.right, key)
        if t is not None:
            return t
        return x

    def ceiling(self, key):
        if key is None:
            raise ValueError("Illegal argument of None type")
        if self.empty():
            raise AttributeError("AVLTree underflow")
        x = self.__ceiling(self.__root, key)
        if x is None:
            return None
        return x.key

    def __ceiling(self, x, key):
        if x is None:
            return None
        cmp = self.__compare(key, x.key)
        if cmp == 0:
            return x
        if cmp > 0:
            return self.__ceiling(x.right, key)
        t = self.__ceiling(x.left, key)
        if t is not None:
            return t
        return x

    def select(self, k):
        if self.empty():
            raise AttributeError("AVLTree underflow")
        if k < 0 or k >= self.size():
            raise ValueError("Argument 'k' is not in range [0, {}]".format(self.size() - 1))
        return self.__select(self.__root, k).key

    def __select(self, x, k):
        if x is None:
            return None
        t = self.__size(x.left)
        if t > k:
            return self.__select(x.left, k)
        if t < k:
            return self.__select(x.right, k - t - 1)
        return x
