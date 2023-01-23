menu = '''

[d] depositar
[s] sacar
[e] Extrato
[q] Sair

'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == "d":
    valor = float(input("Por favor , coloque a quantidade : \n"))
    if valor > 0:
      saldo += valor
      extrato += f"depósito : R$ {valor:.2f} \n"

    else:
      print('Falhou!!! Por favor, retorne e coloque um valor de depósito positivo')

  elif opcao == "s":
    valor = float(
      input("Por favor , coloque a quantidade que deseja retirar : \n"))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_limite_de_saque = numero_saques >= LIMITE_SAQUES
    if excedeu_saldo:
      print('FAlHA! Saque requerido maior que o seu saldo atual ')
    elif excedeu_limite:
      print('Falha!!!excedeu o limite de quantidade possível para saque')
    elif excedeu_limite_de_saque:
      print('Falha!! Excedeu o limite diário de saques')

    elif valor > 0:
      saldo -= valor
      extrato += f'Saque de R${valor:.2f}'
      numero_saques += 1
    else:
      print('Falha!!! O valor colocado é inválido')

  elif opcao == "e":
    print('\n==============================EXTRATO========================')
    print('Não foi registrado movimentações nesta conta'if not extrato else extrato)
    print(f"Saldo : R$ {saldo:.2f}")
    print('============================================================')

  elif opcao == "q":
    break
  else:
    print(
      'FALHA!! operação inválida, por favor, informe novamente a opção desejada'
    )
