#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    num = len(sys.argv)
    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op == "+":
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == "-":
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == "*":
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == "/":
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
