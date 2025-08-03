#Relatório de Alunos
lista = []
aprovados = 0
reprovados = 0
    
qtd_alunos = int(input("Quantos alunos são? "))
for i in range(qtd_alunos):
    while True:
        registro_aluno = int(input("Digite seu RM: "))
        notas = float(input("Digite sua nota:"))
        if 0 <= notas <= 10:
            break
        else:
            print("Nota inválida! Digite um valor de 0 a 10.")
   
    lista.append (registro_aluno)
    lista.append (notas)

    if notas >= 5:
        print("Aprovado!")
        aprovados += 1
    else:
        print("Reprovado!")
        reprovados += 1

print("--- RELATÓRIO FINAL ---")        
print ("Quantidade de alunos cadastrados:", len(lista) // 2)
print ("Quantidade de alunos aprovados:", aprovados)
print ("Quantidade de alunos reprovados:", reprovados)