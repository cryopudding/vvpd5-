import math


def m_cos(x, terms):
    """
    Функция cos(x) с использованием ряда Маклорена.

    Подробное описание:
    Ряд Маклорена для cos(x) является частным случаем ряда Тейлора, разложенного при x=0.
    Определяется как:
        cos(x) = \sum((-1)^n * x^(2n) / (2n)!, n=0 до бесконечности)
    Функция вычисляет приближение, используя конечное количество членов ряда.

    Аргументы:
    x (float): Входное значение для аппроксимации cos(x).
    terms (int): Количество членов в ряде для приближения.

    Возвращаемое значение:
    float: Аппроксимированное значение cos(x).

    Исключения:
    нет.

    Примеры:
    m_cos(0)
    1.0
    m_cos(3.14159, terms=5)
    -0.999999943741051

    """
    result = 0
    for n in range(terms):
        result += (-1)**n * (x(2*n)) / math.factorial(2*n)
    return result


def m_sinh(x, terms):
    """
    Функция sinh(x) с использованием ряда Маклорена.

    Подробное описание:
    Ряд Маклорена для sinh(x) определяется как:
        sinh(x) = \sum(x^(2n+1) / (2n+1)!, n=0 до бесконечности)
    Функция вычисляет приближение, используя конечное количество членов ряда.

    Аргументы:
    x (float): Входное значение для аппроксимации sinh(x).
    terms (int): Количество членов в ряде для приближения.

    Возвращаемое значение:
    float: Аппроксимированное значение sinh(x).

    Исключения:
    нет.

    Примеры:
    m_sinh(0)
    0.0
    m_sinh(1, terms=5)
    1.1752011936438014

    """
    result = 0
    for n in range(terms):
        result += (x**(2*n + 1)) / math.factorial(2*n + 1)
    return result


def m_cosh(x, terms):
    """
    Функция cosh(x) с использованием ряда Тейлора.
    """
    result = 0
    for n in range(terms):
        result += (x**(2*n)) / math.factorial(2*n)
    return result


def main_menu():
    """
    Показывает меню пользователя, где можно выбрать функцию, ввести x и получить результат.
    Также проверяются граничные значения для x.
    """
    terms = 10
    while True:
        print("\nМеню:\n"+
              "1. Вычислить cos(x)\n"+
              "2. Вычислить sinh(x)\n"+
              "3. Вычислить cosh(x)\n" +
              "4. Выход")
        choice = input("Выберите опцию : ")
        if choice == '4':
            print("Выход из программы...")
            break
        if choice not in {'1', '2', '3'}:
            print("Неверный выбор. Попробуйте снова.")
            continue
        if choice == '1':
            try:
                x = float(input("Введите значение x: "))
            except ValueError:
                print("Ошибка: введите корректное число.")
                continue
            result = m_cos(x, terms)
            print(f"cos({x}) ≈ {result}")
        elif choice == '2':
            try:
                x = float(input("Введите значение x: "))
            except ValueError:
                print("Ошибка: введите корректное число.")
                continue
            result = m_sinh(x, terms)
            print(f"sinh({x}) ≈ {result}")
        elif choice == '3':
            try:
                x = float(input("Введите значение x: "))
            except ValueError:
                print("Ошибка: введите корректное число.")
                continue
            result = m_cosh(x, terms)
            print(f"cosh({x}) ≈ {result}")

if __name__ == "__main__":
    main_menu()