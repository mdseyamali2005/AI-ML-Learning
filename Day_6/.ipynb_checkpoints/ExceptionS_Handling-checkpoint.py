try:
    x = int(input("Enter the value :"))
    ans = 10/x
except ZeroDivisionError:
    print("Infinity")
except ValueError:
    print("Enter Number")
else:
    print(ans)

