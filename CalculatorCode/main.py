import sys

def error_checking(a, b, str):
    """Проверка на ошибки, а именно неправильный ввод"""
    if len(str) != 3:
        sys.exit()
    try:
        a = int(str[0])
    except ValueError:
        print("Веденно не число")
        sys.exit(-1)
    try:
        b = int(str[2])
    except ValueError:
        print("Веденно не число")
        sys.exit(-1)

def calculating(a, b, str):
    """Обработка всех операций"""
    c = 0
    if str[1] == "+":
        c = a + b
    elif str[1] == "-":
        c = a - b
    elif str[1] == "*":
        c = a * b
    elif str[1] == "/":
        c = a / b
    elif str[1] == "**":
        c = a ** b
    elif str[1] == "//":
        c = a // b
    return c

def main():
    print("My first calulator on python (a +/-/*///**/// b) and enter 'exit' to close app")
    while 1:
        str = input()
        a = 0
        b = 0
        if str == "exit":
            sys.exit(0)
        str = str.split(" ")
        error_checking(a, b, str)
        a = int(str[0])
        b = int(str[2])
        c = calculating(a, b, str)
        print(c)

if __name__ == '__main__':
    main()

