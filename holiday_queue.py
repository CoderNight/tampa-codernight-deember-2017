#!/usr/bin/env python3
from collections import namedtuple


Gift = namedtuple('Gift', 'pri gift')

class GiftHeap:
    def __init__(self):
        self.elems = []

    def insert(self, pri, gift):
        self.elems.append(pri)
        self._bubble_up()

    def _bubble_up(self):
        index = len(self.elems) - 1
        while index > 0:
            index_parent = (index - 1) // 2
            if self.elems[index_parent] > self.elems[index]:
                return

            self._swap_index(index_parent, index)
            index = index_parent

    def remove(self):
        if len(self.elems) == 0:
            return None
        if len(self.elems) == 1:
            return self.elems.pop()
        elem = self.elems[0]
        self.elems[0] = self.elems.pop()
        self._bubble_down()
        return elem

    def _bubble_down(self):
        index = 0
        def get_value(i):
            return self.elems[i] if i < len(self.elems) else None

        def greatest_index():
            return max((index, index * 2 + 1, index * 2 + 2), key=get_value)

        gi = greatest_index()
        while index != gi:
            self._swap_index(gi, index)
            index = gi
            gi =  greatest_index()

    def _swap_index(self, left, right):
        self.elems[left], self.elems[right] = self.elems[right], self.elems[left]

g = GiftHeap()
g.insert(1,'wine')
g.insert(3, 'bourbon')
g.insert(2, 'rum')
g.insert(4, 'triple sec')
# g.insert(12, 'vodka')
# g.insert(7, 'cognac')
f = g.elems
el = g.remove()
f = g.elems
el = g.remove()
f = g.elems
el = g.remove()
f = g.elems
el = g.remove()
f = g.elems
el = g.remove()
