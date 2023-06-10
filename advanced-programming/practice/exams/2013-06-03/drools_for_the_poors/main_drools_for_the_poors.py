from itertools import product, permutations

class Golfer(object):
    def __init__(self, num, name, color):
        self.name = name 
        self.color = color
        self.num = num

    def __str__(self):
        return f"Golfer {self.name} is in position {self.num} and wears some {self.color} pants"

class Drools(object):
    def __init__(self, rules, names, colors, nums):
        self.rules = rules
        self.names = names
        self.colors = colors
        self.nums = nums

    def eval(self):
        all_golfers = []
        for i in list(product(permutations(self.nums), permutations(self.names), permutations(self.colors))):
            tmp = []
            for j in range(4):
                tmp.append(Golfer(i[0][j], i[1][j], i[2][j]))
            all_golfers.append(tmp)

        for gg in all_golfers:
            tmp = []
            for rule in rules:
                x = rule(gg)
                tmp.append(x)
                if x == False:
                    break
            if all(tmp):
                [print(i) for i in gg]
                return

one_red_pants =                lambda gg: any([i.color == "red" for i in gg])
fred_right_blue_pants =        lambda gg: any([(j.num == i.num+1 and j.color == "blue") for j in gg for i in gg if i.name == "fred"])
joe_is_second =                lambda gg: any([i.name == "joe" and i.num == 2 for i in gg])
bob_plaid_pants =              lambda gg: any([i.name == "bob" and i.color == "plaid" for i in gg])
tom_not_four_one__not_orange = lambda gg: any([i.name == "tom" and not i.color == "orange" and i.num != 4 and i.num != 1 for i in gg])
rules = [one_red_pants, fred_right_blue_pants, joe_is_second, bob_plaid_pants, tom_not_four_one__not_orange]

if __name__ == "__main__":
    d = Drools(rules, \
             ['bob', 'joe', 'fred', 'tom'], \
             ['red', 'orange', 'blue', 'plaid'], \
             list(range(1,5)))
    d.eval()
