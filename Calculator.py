def add(x, y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

if __name__=="__main__":
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))

    result=add(num1,num2)
    print(result)
    result=substract(num1,num2)
    print(result)
    result=multiply(num1,num2)
    print(result)
    result=divide(num1,num2)
    print(result)
