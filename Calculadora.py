conta = True

while True:
    try:
        numero1 = float(input("Digite seu número: "))
        break
    except ValueError:
        print("Opção Invalida")


resultado_total = numero1
while conta:
    operacao = input("Digite qual a operação deseja fazer '+', '-', '*' '/': ")
    while operacao not in ["+", "-", "*", "/"]:
        print("Opção Inválida")
        operacao = input("Digite qual a operação deseja fazer '+', '-', '*' '/': ")
        
    while True:
        try:    
            numero2 = float(input("Digite o próximo número: "))
            break
        except ValueError:
            print("Opção Invalida")

    
    if operacao == "+":
        resultado_total = resultado_total + numero2
    elif operacao == "-":
        resultado_total = resultado_total - numero2
    elif operacao == "*":
        resultado_total = resultado_total * numero2
    elif operacao == "/":
        if numero2 == 0:
            print("Não é possivel dividir por 0")
        else:
            resultado_total = resultado_total / numero2


    print(resultado_total)


    continuar = input("Deseja continuar os cálculos?: (s/n): ").lower()

    while continuar not in ["s", "n"]:
        print("Opção Inválida")
        continuar = input("Deseja continuar os cálculos?: (s/n): ").lower()

    if continuar == "n":
        conta = False
    
print(f"Resultado da conta {resultado_total}")

        
        
    

