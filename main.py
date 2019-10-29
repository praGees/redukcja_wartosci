
# Cyfrowy pierwiastek jest rekurencyjną sumą wszystkich cyfr w liczbie.
# Biorąc pod uwagę n, weź sumę cyfr n. Jeśli ta wartość ma więcej niż jedną cyfrę,
# kontynuuj zmniejszanie w ten sposób, aż zostanie wygenerowana liczba jednocyfrowa.
# Dotyczy to tylko liczb naturalnych.


def do_jednego(n):
    if n<10:
        return n
    if n>10:
        wynik = 0
        for i in str(n):
            wynik = wynik + int(i)
        n = wynik
        print(n)
        return do_jednego(n)


do_jednego(43334445123123132)