'---Part1: define tree as ADT (using constructor and selector)---'

def tree(label, branches=[]):
	for branch in branches:
		assert is_tree(branch), 'Branches must be a tree!'
	return [label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)


# Define a fib tree
def fib_tree(n):
	if n <= 1:
		return tree(n)
	else:
		left, right = fib_tree(n-2), fib_tree(n-1)
		return tree(label(left)+label(right), [left, right])


def count_leaves(tree):
	if is_leaf(tree):
		return 1
	return sum([count_leaves(b) for b in branches(tree)])

def leaves(tree):
	"""Return a list containing the leaf labels of the tree."""
	if is_leaf(tree):
		return [label(tree)]
	return sum([leaves(b) for b in branches(tree)],[])

def print_tree(t, indent=0):
	print(' ' * indent + str(label(tree)))
	for b in branches(tree):
		print_tree(b, indent+1)




'-----------------Part2: define tree using class-----------------'
'difference between ADT & class:https://inst.eecs.berkeley.edu/~cs61a/fa18/lab/lab07/'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()




