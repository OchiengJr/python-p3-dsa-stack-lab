import pytest
from Stack import Stack

class TestStack:
    """Test cases for Stack class in Stack.py"""

    def test_init(self):
        """Initialize Stack with list"""
        stk = Stack([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        for index in range(len(expected)):
            assert expected[index] == stk.items[index]

    def test_push(self):
        """Push element to stack"""
        stk = Stack([1, 2, 3, 4, 5])
        stk.push(0)
        expected = [1, 2, 3, 4, 5, 0]
        for index in range(len(expected)):
            assert expected[index] == stk.items[index]

    def test_pop(self):
        """Pop element from stack"""
        stk = Stack([1, 2, 3, 4, 5])
        stk.pop()
        expected = [1, 2, 3, 4]
        for index in range(len(expected)):
            assert expected[index] == stk.items[index]

    def test_size(self):
        """Test Stack size() method"""
        stk = Stack([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        assert stk.size() == len(expected)

    def test_isEmpty(self):
        """Test Stack isEmpty() method"""
        stk = Stack()
        assert stk.isEmpty()
        assert stk.size() == 0
        assert stk.pop() is None
        stk.push(1)
        assert not stk.isEmpty()
        assert stk.size() == 1
        assert stk.pop() == 1

    def test_full(self):
        """Test Stack full() method"""
        stk = Stack([1], 1)
        assert stk.full()
        assert stk.size() == 1
        assert stk.pop() == 1
        stk.push(1)
        stk.push(2)
        assert stk.full()
        assert stk.size() == 1
        assert stk.pop() == 1

    def test_search(self):
        """Test Stack search() method"""
        stk = Stack([5, 6, 7, 8, 9, 10])
        assert stk.search(5) == 5
        assert stk.search(6) == 4
        assert stk.search(7) == 3
        assert stk.search(8) == 2
        assert stk.search(9) == 1
        assert stk.search(10) == 0
        assert stk.search(15) == -1  # Target not in Stack
