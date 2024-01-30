from random import randint


def create_cases(number_of_cases):
    print(number_of_cases)
    for _ in range(number_of_cases):
        case_length = randint(5, 500)
        target = randint(0, case_length * 100)
        number_list = ""
        for i in range(case_length):
            if i == 0:
                number_list += f"{randint(0,50)}"
            else:
                number_list += f" {randint(0,50)}"
        print(number_list)
        print(target)


if __name__ == "__main__":
    create_cases(100)
