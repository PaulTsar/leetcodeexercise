from random import *


def generate_code(length):
    result = []
    result.append(int(randint(1, 9)))
    for t in range(length - 1):
        if result[t] % 2 == 0:
            result.append(result[t] // 2)
        else:
            result.append(((result[t]) * 3 + 1) % 10)
    return result


def count_matches(secret, guess):
    matching = 0
    for a, b in zip(secret, guess):
        if a == b:
            matching += 1
    return matching


def main():
    length = int(input("Введите длину кода:"))
    needed = generate_code(length)
    while True:
        guess = input("Введите ваш вариант кода:")
        if len(guess) != length:
            print("некорректная длина")
            continue
        guess_digits = [int(digit) for digit in guess]
        x = count_matches(needed, guess_digits)
        if x == length:
            print("поздравляю, ты взломал!")
            break
        else:
            print(f"вы угадали {x} цифр ")


if __name__ == "__main__":
    main()
