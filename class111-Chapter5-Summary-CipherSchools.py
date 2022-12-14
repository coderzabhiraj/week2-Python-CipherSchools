def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('you cannot divide a number by zero')
    except TypeError as err:
        print("numbers must be int or floats")

print(divide(10,0))