import inspect

def resource_manager(func):
	def gather_resource_count(f):
		while "resource" not in f.f_locals:
			f = f.f_back
		return f.f_locals["resource"]

	def wrapper(*args, **kwargs):
		if wrapper.resource is not None:
			wrapper.resource -= 1

		s = inspect.stack()

		if s[1].function != wrapper.name:
			wrapper.resource = gather_resource_count(s[0].frame)

		if wrapper.resource < 0:
			print("resources run out")
			raise SystemExit

		return func(*args, **kwargs)

	wrapper.resource = None
	wrapper.name = func.__name__

	return wrapper

@resource_manager
def fact(n, acc = 1):
	if n == 0:
		return acc
	return fact(n - 1, n * acc)

@resource_manager
def fibo(i):
	if i <= 1:
		return i + 1
	return fibo(i - 1) + fibo(i - 2)

if __name__== "__main__":
	resource = 10
	print("{0}! :- {1}".format(10, fact(10)))
	
	resource = 9
	try:
		print("{0}! :- {1}".format(10, fact(10)))
	except SystemExit:
		pass
	
	resource = 160
	try:
		print("fibo({0}) :- {1}".format(10, fibo(10)))
	except SystemExit:
		pass
		
	resource = 180
	print("fibo({0}) :- {1}".format(10, fibo(10)))