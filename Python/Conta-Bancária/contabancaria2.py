from contabancaria import Conta_bancaria

conta1 = Conta_bancaria ('Vitor', 0)
conta2 = Conta_bancaria ('Rogério', 0)

conta1.depositar(2000)
conta1.sacar(400)
conta1.transferir(1200, conta2)

conta2.depositar(400)
conta2.transferir(900, conta1)

print(conta1)
print(conta2)