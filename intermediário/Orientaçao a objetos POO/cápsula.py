#método de encapsulamento

class banco:
    def __init__(self, saldo, titular):  #init está codificando os valores
        self.__saldo = saldo
        self.titular = titular

    def depositar(self, valor_guardado):
        if valor_guardado > 0:
            self.__saldo += valor_guardado
            print(f"VALOR GUARDADO|| Valor:{valor_guardado}/ Valor total atual: {self.__saldo}")
        else:
            print("[ERROR][ERROR][ERROR]")
            print("VALOR INVALIDO")
            print("[ERROR][ERROR][ERROR]")
    
    def sacar(self, valor_sacado):
        if 0 < valor_sacado <= self.__saldo:
            self.__saldo -= valor_sacado
            print(f"VALOR SACADO|| Valor:{valor_sacado}/ Valor total atual: {self.__saldo}")
        else:
            print("[ERROR][ERROR][ERROR]")
            print("VALOR INVALIDO")
            print("[ERROR][ERROR][ERROR]")

    def ver_saldo(self):
        return self.__saldo
    

    #def __str__(self):   mostra os valores de maneira mais agradável para visualizar
        #return f"TITULAR: {self.titular}\nSALDO: {self.__saldo}"
    

    

conta_bancária = banco(1200, "Guilherme")
#print(conta_bancária)    #Aparece o valor codificado
conta_bancária.depositar(7000)
print(conta_bancária.ver_saldo()) #mostra somente o valor, do saldo
#print(conta_bancária)
conta_bancária.sacar(250)
print(conta_bancária.ver_saldo()) #Deve estar escrito desta mesma forma para acessar e mostrar o valor
#print(conta_bancária)
conta_bancária.sacar(600)
print(conta_bancária.ver_saldo())
#print(conta_bancária)
conta_bancária.sacar(300)
print(conta_bancária.ver_saldo())
#print(conta_bancária)
conta_bancária.depositar(990)
print(conta_bancária.ver_saldo())
#print(conta_bancária)

print(conta_bancária.ver_saldo())
