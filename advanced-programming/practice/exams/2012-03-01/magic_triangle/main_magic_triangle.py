from magic import *

if __name__ == "__main__":
	t = magic()
	print("... at step {0} you have {1} triangles".format(1, next(t)))
	next(t)
	print("... at step {0} you have {1} triangles".format(3, next(t)))
	next(t)
	next(t)
	next(t)
	print("... at step {0} you have {1} triangles".format(7, next(t)))
	next(t)
	next(t)
	next(t)
	next(t)
	next(t)
	next(t)
	print("... at step {0} (the whole picture) you have {1} triangles".format(14, next(t)))