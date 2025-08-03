def calculadora (v1, v2):

    print("---- Calculadora ----")
    print("1 - Somar (+)")
    print("2 - Subtrair (-)")
    print("3 - Multiplicar (*)")
    print("4 - Dividir (/)")

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        resultado = v1 + v2
    elif opcao == 2:
        resultado = v1 - v2
    elif opcao == 3:
        resultado = v1 * v2
    elif opcao == 4:
        if v2 == 0:
            print("Erro: divisão por zero não é permitida!")
            return
        else:
            resultado = v1 / v2
    else:
        print("Opção inválida!")
        return
    
    print(f"Resultado: {resultado}")

while True:
    print("\n====== NOVA OPERAÇÃO ======")
    v1 = float(input("Digite o valor 1: "))
    v2 = float(input("Digite o valor 2: "))
    calculadora(v1, v2)

    continuar = input("Quer continuar?(s/n): ").strip().lower()
    if continuar == "n":
        print("Encerrando calculadora")
        break
    elif continuar == "s":
        continue       
    else:
        print("Opção inválida! Tente novamente")