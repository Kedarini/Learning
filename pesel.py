class Program:
    pesel = input("Podaj numer pesel: ")
    pesel = "55030101193" if pesel == "" else pesel
    plec = "k" if int(str(pesel)[9]) % 2 == 0 else "m"

    waga = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    S = 0
    for i in range(10):
        S += int(pesel[i]) * waga[i]

    M = S % 10

    R = 0 if M == 0 else 10 - M

    print("zgodna") if R == int(str(pesel)[10]) else print("niezgodna")


if __name__ == "__main__":
    Program
