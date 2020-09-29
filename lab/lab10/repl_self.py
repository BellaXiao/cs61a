try:
	import readline
except ImportError:
	pass
import sys

from reader import reader
from expr import global_env

# start of the program
if __name__ == '__main__':
	"""
	Used to run a read-eval-print loop
	two main funcs:
		1) 'python3 repl.py': start an interactive REPL
		2) 'python3 repl.py --read': to interactive read expressions
		and print their python representation.
	"""
	# decide which kind using read_only
	read_only = (len(sys.argv) == 2 and sys.argv[1] == '--read')

	# start the loop
	while True:
		try:
			# use input to print the prompt, waits and return users' input
			user_input = input('> ')
			expr = read(user_input)
			if expr is not null:
				if read_only:
					print(repr(expr))
				else:
					print(expr.eval(global_env))
		except (SyntaxError, NameError, TypeError) as err:
			print(type(err).__name__+':',err)
		except (KeyboardInterrupt, EOFError): # Ctrl+C, Ctrl+D
			print() # add a blank line
			break


































