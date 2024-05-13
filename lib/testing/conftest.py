#!/usr/bin/env python3
import pytest

def pytest_itemcollected(item):
    parent = item.parent.obj
    node = item.obj
    parent_desc = parent.__doc__.strip() if parent.__doc__ else parent.__class__.__name__
    node_desc = node.__doc__.strip() if node.__doc__ else node.__name__
    if parent_desc or node_desc:
        item._nodeid = ' '.join((parent_desc, node_desc))

if __name__ == "__main__":
    pytest.main()
