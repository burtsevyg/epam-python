s = input("Введите строку: ")

print("-".join([s[x].upper() + s[x].lower()*(x) for x in range(len(s))]))


