def main():
    dict = {}

    for i in range(1, 101):
        if i % 3 != 0:
            dict[i] = i**3

    print(dict)

def comprehension():
    dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(dict)

if __name__ == '__main__':
    main()
    comprehension()
