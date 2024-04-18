num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
operacao = input("digite a operacao a ser realizada, +, -, *, / : ")

if (operacao == '+'):
    print(num1 + num2)
elif (operacao == '-'):
    print(num1 - num2)
elif(operacao == '*'):
    print(num1 * num2)
elif(operacao == '/'):
    print(num1 / num2)
else: 
    print("operacao invalida!")