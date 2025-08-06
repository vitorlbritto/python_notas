class Conta_bancaria:
    def __init__(self, titular, saldo, limite = 1000):
        # Inicializa uma conta com titular, saldo inicial e limite de crédito (padrão: R$1000)
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        # Deposita um valor positivo na conta
        if valor <= 0:
            print('Valor do depósito inválido!')
            return
        self.saldo += valor
    
    def sacar(self, valor):
        # Realiza saque se o valor for válido e estiver dentro do saldo + limite         
        if valor <= 0:
            print('Saque inválido!')
            return False
         
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return True
        else:
            print('Saldo insuficiente!')
            return False
        
    def transferir(self, valor, destino):
        # Transfere valor para outra conta, se o saque for bem-sucedido
        if self.sacar(valor): 
            destino.depositar(valor)
            print(f'Transferência de valor R${valor:.2f} para {destino.titular}')
        
    def __str__(self):
        # Retorna uma representação resumida da conta
        return f'Titular: {self.titular}, Saldo R${self.saldo:.2f}, Limite: R${self.limite:.2f}'