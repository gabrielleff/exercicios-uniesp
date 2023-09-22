class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f'Depósito de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}'
        else:
            return 'O valor do depósito deve ser maior que zero.'
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f'Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}'
        elif valor <= 0:
            return 'O valor do saque deve ser maior que zero.'
        else:
            return 'Saldo insuficiente para realizar o saque.'

conta = ContaBancaria("João")
print(conta.depositar(500))
print(conta.sacar(250))
print(conta.sacar(900))