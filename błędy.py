try:
    print('*** dzielenie ***')
    a = int(input('podaj pierwszą liczbę:'))
    b = int(input('podaj drugą liczbę'))
    print(a/b)
except ValueError:
    print('błąd, nie podałe prawidłowej liczby!')
except ZeroDivisionError:
    print('błąd, nie mogę'
          ' podzielić przez 0!')