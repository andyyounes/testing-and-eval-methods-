
def sum(a, b):
    return a+b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b

    
def main():
    i = int(input("Enter a number a= "))
    j = int(input("Enter a number b= "))
    print(f'sum of {i}+{j} = {sum(i, j)}')
    print(f'Mul of {i}*{j} = {mul(i,j)}')
    print(f'sum of {i}-{j} = {sub(i,j)}')
if __name__ =='__main__':
    main()