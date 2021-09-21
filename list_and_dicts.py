def main():
    list = [1, "Hi", True, 43.5]
    dict = {"firstname": "Cristian", "lastname": "Rojas"}
    super_list = [
        {"firstname": "Cristian", "lastname": "Rojas"},
        {"firstname": "Maria", "lastname": "Arango"},
        {"firstname": "Javier", "lastname": "Rojas"},
        {"firstname": "Amparo", "lastname": "Quintero"}
    ]
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2]
    }

    for key, value in super_dict.items():
        print(key, "--->", value)


if __name__ == '__main__':
    main()