menu = '''

[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == 'd':
    print('Informe o valor que deseja depositar: ')
    valor = float(input())

    if valor > 0:
      saldo += valor
      extrato = extrato + f"Depósito: R$ {valor:.2f}\n"

    else:
      print('A operação falhou! O valor informado é inválido.')
    
  elif opcao == 's':
    valor = float(input('Informe o valor do saque: '))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques > LIMITE_SAQUES

    if excedeu_saldo:
      print('A operação falhou! Saldo insuficiente. ')

    elif excedeu_limite:
      print('A operação falhou! O valor excede o limite de saque disponível para este banco.')
    
    elif excedeu_saques:
      print('A operação falhou! O número máximo de saques foi excedido. ')
    
    elif valor > 0:
      saldo -= valor
      extrato += f'Saque: R$ {valor:.2f}\n'
      numero_saques += 1
    else:
      print('Operação falhou! O valor informado é inválido. ')

  elif opcao == 'e':
    print('\n --------------- EXTRATO --------------- ')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('------------------------------------------')

  elif opcao == 'q':
    break
  else:
    print('Operação inválida! Por favor, selecione novamente a operação desejada. ')