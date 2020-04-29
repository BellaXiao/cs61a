""" Optional Questions for Lab 07 """

from lab07 import *

# Q9
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    "iterative way"
    cur = prev = link
    while cur != Link.empty:
        cur = cur.rest
        if cur != Link.empty:
            if cur.first == value:
                prev.rest = cur.rest
            else:
                prev = prev.rest

    """Recursive way"""
    """
    if link.rest is Link.empty:
        return Link.empty
    elif link.rest.first == value:
        link.rest = link.rest.rest
        remove_all(link, value)
    else:
        remove_all(link.rest, value)
    """


# Q10
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    
    if link == Link.empty:
        return
    if isinstance(link.first,Link):
        deep_map_mut(fn, link.first)
    else:
        link.first = fn(link.first)
    deep_map_mut(fn, link.rest)



# Q11
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    dict_seen = set()
    p = link
    while p != Link.empty:
        if p in dict_seen:
            return True
        else:
            dict_seen.add(p)
        p = p.rest
    return False


def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    "self: is this count as constant space?"
    """
    p = link
    while p!= Link.empty:
        if isinstance(p.first,list) and p.first[0] == 'seen':
            t = link
            while t != p.rest:
                t.first = t.first[1]
                t = t.rest
            return True
        p.first = ['seen', p.first]
        p = p.rest
    return False
    """
    "fast point and slow point, if there's cycle, the fast one will eventually catch the slow one"
    "fast point go two steps at one time, thus if slow==fast or slow == fast.rest(meaning 1 step away)"
    "We can make sure there's cycle"
    if link is Link.empty:
        return False
    slow, fast = link, link.rest
    while fast != Link.empty:
        if fast.rest == Link.empty:
            return False
        elif fast == slow or fast.rest == slow:
            return True
        else:
            slow, fast = slow.rest, fast.rest.rest
    return False



# Q12
def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return
    l = []
    for b in t.branches:
        l.append(b.label)
    l = l[::-1]
    for i in range(len(t.branches)):
        t.branches[i].label = l[i]
        for b in t.branches[i].branches:
            reverse_other(b)
    return

























