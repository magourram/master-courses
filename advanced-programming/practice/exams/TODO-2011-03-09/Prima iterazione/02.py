# Senza usare le eccezioni

# def tail_recursion(func):
# 	def wrapper(*args, **kwargs):
# 		if wrapper.second:
# 			wrapper.second = False
# 			wrapper.args = args
# 			wrapper.kwargs = kwargs

# 			return

# 		while True:
# 			wrapper.second = True
# 			ret = func(*args, **kwargs)

# 			if wrapper.args == args and wrapper.kwargs == kwargs:
# 				break
# 			args, kwargs = wrapper.args, wrapper.kwargs

# 		return ret

# 	wrapper.args = None
# 	wrapper.kwargs = None
# 	wrapper.second = False

# 	return wrapper

# Usando le eccezioni

import inspect
import sys

class TailRecursion(Exception):
	def __init__(self, args, kwargs):
		self.args = args
		self.kwargs = kwargs

def tail_recursion(func):
	def wrapper(*args, **kwargs):
		f = inspect.currentframe()
		if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
			raise TailRecursion(args, kwargs)
		else:
			while True:
				try:
					return func(*args, **kwargs)
				except TailRecursion as tl:
					args, kwargs = tl.args, tl.kwargs

	return wrapper

@tail_recursion
def tfact(n, acc = 1):
	if n == 0:
		return acc
	return tfact(n - 1, n * acc)

@tail_recursion
def tfib(i, current = 0, next = 1):
	if i == 0:
		return current
	return tfib(i - 1, next, current + next)

if __name__ == "__main__":
	print("10000! :-", tfact(10000))
	print("fib(10000) :-", tfib(10000))