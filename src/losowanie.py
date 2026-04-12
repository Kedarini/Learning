import random


class Program:
    ile = int(input("Ile wygenerować losowań? \n"))
    wystapienia = [0] * 49

    for i in range(ile):
        liczby = [str((random.randint(1, 49))) for _ in range(6)]
        print(f"Losowanie {i + 1}: {', '.join(liczby)}")

        for liczba in liczby:
            wystapienia[int(liczba) - 1] += 1

    for i in range(len(wystapienia)):
        print(f"Wystąpienia liczba {i + 1}: {wystapienia[i]}")


if __name__ == "__main__":
    Program()
