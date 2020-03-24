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







