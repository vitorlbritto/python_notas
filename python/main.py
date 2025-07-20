notas = []

for x in range (5):
    rm_aluno = int (input("RM: "))
    nota_aluno = float (input("Nota: "))
    resultado = [rm_aluno, nota_aluno]
    notas.append(resultado)

print("Quantidade de notas: ", len (notas))

for codigo_aluno, nota in notas:
    print(f"o RM {codigo_aluno} tirou a nota: {nota}")