# simpe calulator with exeptions
# 1.0.0


def main():
    try:
        a = int(input())
        b = int(input())
        op = input()
        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "/":
            print(a / b)
        elif op == "*":
            print(a * b)
        elif op == "mod":
            print(a % b)
        elif op == "pow":
            print(a ** b)
        elif op == "div":
            print(a // b)
    except ZeroDivisionError:
        print("Деление на 0!")
    except ValueError:
        print("Неверный ввод!")

