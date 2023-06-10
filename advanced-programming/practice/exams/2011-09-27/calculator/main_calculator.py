from calculator import *

if __name__ == "__main__":
    print("### test +2*-53/63")
    calc = calculator('+2*-53/63') # ((6/3)*(5-3))+2
    print(calc.eval())
    print(calc.code(),end='')
