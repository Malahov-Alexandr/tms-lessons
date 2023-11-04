def input_int_number() -> int:
    while True:
        try:
            return int(input('Введите целое число: '))
        except ValueError as e:
            print("Ошибка", e)
            continue


def calculate(left: int, right: int, operation: str):
    while True:
        if operation == "+":
            return left + right
        elif operation == "-":
            return left - right
        elif operation == "/":
            return left / right
        elif operation == "*":
            return left * right
        elif operation == "!":
            raise CalculationExeption()
        else:
            raise ValueError(f"Неподдерживаемая операция: {operation}")


def main():
    while True:
        try:
            a = input_int_number()
            b = input_int_number()
            op = input("Введите операцию: ")
            print(calculate(a, b, op))
        except ZeroDivisionError:
            print("Деление на 0!")

        except ValueError as e:
            print("Неверный ввод!", e)

        except CalculationExeption:
            print("Завершаем программу")
            break



class CalculationExeption(Exception):
    pass

if __name__ == "__main__":
    main()
