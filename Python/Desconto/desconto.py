#Descontos do salário com alíquotas fixas
salario = float(input("Digite seu salário bruto:R$"))
if salario <= 1518:
    salario_liquido = salario - (salario * 7.5 / 100 )
elif 1518.01 <= salario <= 2793.88:
    salario_liquido = salario - (salario * 9 / 100)
elif 2793.89 <= salario <= 4190.83:
    salario_liquido = salario - (salario * 12 / 100)
elif 4190.84 <= salario <= 8157.41:
    salario_liquido = salario - (salario * 14 / 100)
else:
    salario_liquido = salario - (salario * 14 / 100)

print(f"Salário líquido: R${salario_liquido:.2f}")
