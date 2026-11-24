"""Entry point: runs a few calculator operations and prints the results."""
from src.calculator import add, subtract, multiply, divide


def main():
    a, b = 10, 5
    print("Pipeline Demo App")
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")


if __name__ == "__main__":
    main()
