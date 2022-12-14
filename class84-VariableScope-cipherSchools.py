#scope
x=5 #global variable
def func():
    global x #denotes the global variable i.e. x=5
    x=7 #local varibles
    return x
print(x) #value of x will be changed if function will be called before printing x
print(func())
print(x)