from josephs_problem import *
import sys

if __name__ == "__main__":
	suicides = Hebrews(40)
	print(suicides.who_is_joseph(3))

	suicides = Hebrews(40000)
	print(suicides.who_is_joseph(30))

	suicides = Hebrews(5000)
	print(suicides.who_is_joseph(7))

	suicides = Hebrews(5000)
	print(suicides.who_is_joseph(153))