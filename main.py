#Imagine que você está desenvolvendo um caixa eletrônico. O usuário possui R$ 1.500,00 disponíveis
#na conta. O sistema apresenta: 1 - Consultar saldo 2 - Sacar 3 - Depositar 0 - Sair O usuário pode
#realizar várias operações. Ao escolher sacar, o sistema deve verificar se o valor é positivo e se existe
#saldo suficiente. Se o valor solicitado for maior que o saldo, a operação deve ser recusada. Responda:
#Quais informações precisam ser armazenadas? Qual estrutura permite manter o menu funcionando?
#Quais condições devem ser verificadas antes de um saque? O que acontece com o saldo depois de um
#saque?

saldo = 1500

def saida(saldo,saque):
    return saldo - saque

def entrada(saldo,deposito):
    return saldo + deposito

def conta(saldo):
    print("Seu saldo é: R$ ",saldo)

def menu_principal(saldo):
    while True:
        print("="*30)
        print("Caixa Eletronico")
        print("="*30)
        print("1 - Consultar saldo")
        print("2 - Sacar")
        print("3 - Depositar")
        print("0 - Sair")

        opcao = int(input("Informe a opção desejada: "))
        print("="*30)
        if opcao == 1:
            conta(saldo)

        elif opcao == 2:
            if saldo > 0:
                saque = float(input("Informe o valor do saque: "))
                if saldo >= saque:
                    saldo = saida(saldo,saque)
                    print("Operação efetuada!")                    
                    conta(saldo)
                else:
                    print("Operação recusada, Saldo insuficiente!")
                    conta(saldo)
            else:
                print("Operação recusada, Saldo insuficiente!")
                conta(saldo)

        elif opcao == 3:
            deposito = float(input("Informe o valor a ser depositado: "))
            saldo = entrada(saldo,deposito)
            print("Operação efetuada!")
            conta(saldo)

        elif opcao == 0:
            print("Obrigado por usar nosso sistema!")
            return False
        else:
            print("Opção invalida, tente novamente.")
        
menu_principal(saldo)