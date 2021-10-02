result = None
choice = input("Что сконвертировать?  (USD, EUR, RUS): ")
summ = float(input("Введите число в BYN :"))
a = 2.5
b = 2.9
c = 0.034

if choice == "USD":
    result = summ / a
    print(result)
elif choice == "EUR":
    result = summ / b
    print(result)
else:
    result = summ / c
    print(result)

