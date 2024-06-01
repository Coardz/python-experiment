value = int(input("Value of gift:"))

if value >= 5000 and value < 25000:
    calc = (100 + (value - 5000) * 0.08)
    print(f"Amount of tax: {calc} euros")
elif value >= 25000 and value < 55000:
    calc = (1700 + (value - 25000) * 0.10)
    print(f"Amount of tax: {calc} euros")
elif value >= 55000 and value < 200000:
    calc = (4700 + (value - 55000) * 0.12)
    print(f"Amount of tax: {calc} euros")
elif value >= 200000 and value < 1000000:
    calc = (22100 + (value - 200000) * 0.15)
    print(f"Amount of tax: {calc} euros")
elif value >= 1000000:
    calc = (142100 + (value - 1000000) * 0.17)
    print(f"Amount of tax: {calc} euros")
else:
    print("No tax!")