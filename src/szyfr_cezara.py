class Program:
    @staticmethod
    def szyfruj(tekst, klucz):
        zaszyfrowany = ""
        for c in tekst:
            if "a" <= c.lower() <= "z":
                zaszyfrowany += chr((ord(c.lower()) - ord("a") + klucz) % 26 + ord("a"))
            else:
                zaszyfrowany += c
        print(zaszyfrowany)


if __name__ == "__main__":
    tekst = input("Podaj tekst do zaszyfrowania: ")
    klucz = int(input("Podaj klucz: "))
    Program.szyfruj(tekst, klucz)
