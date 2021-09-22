def divisores(num):
    try:
        if num < 0:
            raise ValueError("Debes ingresar un numero positivo")
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def main():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisores(num))
    except ValueError:
        print("Debes ingresar un valor numerico")


if __name__ == '__main__':
    main()
