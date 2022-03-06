num1 = float(input())
num2 = float(input())
op = input()

def soma(num1, num2): return(num1+num2)

def sub(num1, num2): return(num1-num2)

def mult(num1, num2): return(num1*num2)

def div(num1, num2): return(num1/num2)

def res(num1, num2, op):
    if op == '+':
        return(soma(num1, num2))
    elif op == '-':
        return(sub(num1, num2))
    elif op == '*':
        return(mult(num1, num2))
    elif op == '/':
        return(div(num1, num2))


print(res(num1, num2, op))
