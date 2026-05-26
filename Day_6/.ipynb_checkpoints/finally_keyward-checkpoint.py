try:
    x = int(input("Enter the value"))
    result = 10/x
except ZeroDivisionError:
    print("O not allow")
else:
    print(result)
finally:
    print("code end")
