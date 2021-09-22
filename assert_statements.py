def divisores(num):
    assert num < 0, "Debes ingresar un numero positivo"
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisores(int(num)))


if __name__ == '__main__':
    main()
