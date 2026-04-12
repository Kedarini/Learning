import random


class Program:
    liczby = [0] * 49
    suma = 0

    print("Liczby: ")
    for i in range(len(liczby)):
        liczby[i] = random.randint(1, 1000)
        nieparzyste = [liczba for liczba in liczby if liczba % 2 != 0]
        suma += liczby[i]
        print(f"{i + 1}: {liczby[i]}")

    print("Liczby nieparzyste:")
    for nieparzysta in nieparzyste:
        print(nieparzysta)

    print(f"Razem nieparzystych: {len(nieparzyste)}")
    print(f"Średnia: {suma // len(liczby)}")


if __name__ == "__main__":
    Program()
