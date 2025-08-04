import time
print("---- Simulador de Empréstimo para Imóvel ----")

while True:
    casa = float(input("Digite o valor da casa: R$"))
    salario = float(input("Digite o salário: R$"))
    anos = int(input("Digite em quantos anos será o empréstimo:"))

    qtd_parcelas = anos * 12  # Calcula quantidade de parcelas (meses)
    prestacao = casa / qtd_parcelas  # Valor da prestação
    limite = salario * 0.30  # Calculo de 30% do salário

    print ("Calculando empréstimo...")
    time.sleep(2) # Timer de 2 segundos
    print ("Pronto! Aqui está o resultado:")

    if prestacao > limite:
        print("Empréstimo negado! Prestação excedeu o limite do salário de 30%")
    else:
        print("Empréstimo aprovado!")
        print("------ RESUMO ------")
        print(
            f"Valor da casa: R${casa:.2f}\n"
            f"Valor da prestação: R${prestacao:.2f}\n"
            f"Total de parcelas: {qtd_parcelas}"
        )
    time.sleep(2)

    escolha = input("Quer calcular novamente?(S/N)").upper()

    while escolha not in ("S", "N"):  # Enquanto a escolha não for S ou N
        print('Resposta incorreta! DIGITE "S" OU "N"')
        escolha = input("Quer calcular novamente?(S/N)").upper()

    if escolha == "N":
        print("Encerrando...")
        break