import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number1", type=int)
parser.add_argument("number2", type=int)
parser.add_argument("operation", type=str)
args = parser.parse_args()

if args.operation == "add":
    print(args.number1 + args.number2)
elif args.operation == "subtract":
    print(args.number1 - args.number2)
elif args.operation == "multiply":
    print(args.number1 * args.number2)
elif args.operation == "divide":
    if args.number2 == 0:
        print("Error: Division by zero")
    else:
        print(args.number1 / args.number2)
else:
    print("Unsupported operation. Use: add, subtract, multiply, divide.")
