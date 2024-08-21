from datetime import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
    
=> """

saldo   = 0
limite  = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao   = input(menu)
    
    if opcao == 'd':
        while True:
            deposito        = float(input('Qual o valor do depósito: '))
            saldo           += deposito
            datadeposito    = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            logdeposito     = f"Data: {datadeposito}-> Valor depositado: {deposito:.2f} - Saldo: R$ {saldo:.2f}"
            extrato.append(logdeposito)
            print('Depósito realizado com sucesso!')
            
            choose          = input('Deseja fazer outro deposito?\n(S)sim ou (N)não: ')
            if choose.lower() != 's':
                break
        
    elif opcao == 's':
        while True:            
            if saldo > 0: 
                sacar       = float(input(f'Quanto deseja sacar: \nSaldo atual: R$ {saldo:.2f}: '))          
                if saldo > sacar:
                    if LIMITE_SAQUES > 0:
                        #print(f'Seu saldo em {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}: {saldo}')
                        #saque   = float(input('Quanto deseja sacar: '))
                        saldo   -= sacar
                        datasaque    = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        logsaque        = f"Data: {datasaque}-> Valor sacado: {sacar:.2f} - Saldo: R$ {saldo:.2f}"
                        extrato.append(logsaque)
                        LIMITE_SAQUES -= 1
                        print('Saque realizado com sucesso!')
                    else:
                        print('Você atingiu o limite de saques diários!')
                        break
                else:
                    print(f'R$ {saldo:.2f} - Saldo insuficiente para o valor do saque desejado')
            else:        
                print(f'Não há saldo em sua conta!!')
                
            choose      = input('Deseja fazer outro saque?\n(S)sim ou (N)não: ')
            if choose.lower() != 's':
                break
    
    elif opcao == 'e':
        print(f'||||||||||||||||||||||||||| EXTRATO - {datetime.now().strftime("%d-%m-%Y")} |||||||||||||||||||||||||||')
        if not extrato:
            print(f'Data: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Nenhum movimento realizado')
        else:
            for e in extrato:
                print(f'{e}')
        print(f'======================================================================================================')
    
    elif opcao == 'q':
        print('sair')
        break
    
    else:    
        print('Operação inválida, por favor selecione novamente a operação desejada.')