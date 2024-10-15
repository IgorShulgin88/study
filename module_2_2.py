first=int(input('Введите число: '))
second=int(input('Введите число: '))
third=int(input('Введите число: '))
if first==second==third:
    print(3)
if first==second and second!=third or first==third and third!=second:
    print(2)
if first!=second and second!=third and first!=third:
    print(0)