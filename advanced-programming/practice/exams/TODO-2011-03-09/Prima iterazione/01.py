def paths(h, tl, i = 0):
	if tl == []:
		return [[h]]
	
	n, *ns = tl
	return [[h] + p for p in paths(n[i], ns, i)] + [[h] + p for p in paths(n[i + 1], ns, i + 1)]

def maxpath(g):
	return sum(max(paths(g[0][0], g[1:]), key=sum))

if __name__ == "__main__":
	l0 = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
	l1 = [[11], [7, 32], [14, 14, 14], [0, 1, 2, 3], [5, 99, 1, 2, 7], [0, 25, 9, 45, 54, 1], [99, 88, 77, 66, 55, 44, 33]]
	l2 = [[-3],[-7, 1], [-14, -2, -10], [7, 0, 0, -7], [-1, 1, 0, 1, -1], [5, -5, 25, -25, -7, 7]]
	l3 = [[1.2], [-1.2, 3.14], [1, -1,0], [-3.14, 5.7, -1, .23], [.1, -.2, .3, -.4, .5]]

	print(l0, ":-", end=" ")
	print(maxpath(l0))
	# 30

	print(l1, ":-", end=" ")
	print(maxpath(l1))
	# 270

	print(l2, ":-", end=" ")
	print(maxpath(l2))
	# 22

	print(l3, ":-", end=" ")
	print(maxpath(l3))
	# 9.34
