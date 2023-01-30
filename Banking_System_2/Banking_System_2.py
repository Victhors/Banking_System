import textwrap

def  menu():
  menu = """ \n
 ======================== MENU =============================
  [nc]\t nova conta
  [nu]\t novo usuario
  [d]\t DEPOSITAR
  [s]\t sacar
  [lc]\t listar contas
  [e]\t Extrato
  [q]\t Sair
  --> """ 
  return input(textwrap.dedent(menu))



def depositar(saldo, valor , extrato,/):
  if valor > 0 :
    saldo += valor
    extrato += 'Deposito:\t R$ %.2f \n' % valor
    print('Depósito realizado com sucesso')
  else:
    print('Operação Falhou! O valor informado é inválido')
  
  return saldo, extrato
  
def sacar(*, saldo ,valor ,extrato , limite, numero_saques, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques > limite_saques
  
  if excedeu_saldo:
    print("A operação falhou , você não tem saldo suficiente")
  elif excedeu_limite:
    print("A operação falhou, o valor de saque excede o limite")
  elif excedeu_saques:
    print("A operação falhou, número maximo de saques atingido")
    
  elif valor > 0 :
    saldo -= valor
    extrato = 'Saque:\t\t R$ %.2f \n' % valor
    numero_saques += 1
    print("Saque realizado com sucesso")
    
  else: 
    print("A operação falhou! o número informado não é válido")
    
  return saldo, extrato 

def exibir_extrato(saldo , / , * , extrato):
  print("\n ================ EXIBIR EXTRATO =================")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print("Saldo:\t\t R$ %.2f \n" % saldo)
  print("=====================================================")

def criar_usuario(usuarios):
  cpf = input('Informe o cpf (Somente Número) :')
  usuario = filtrar_usuario(cpf, usuarios)
  
  if usuario:
    print("\n Já existe um usuario com esse cpf!")
    return
  
  nome = input("Informe o nome completo: ")
  data_de_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
  endereco = input("Informe o endereco (logradouro, nro - bairro - cidade/sigla estado): ")
  
  usuarios.append({"nome": nome, "data_de_nascimento":data_de_nascimento , "endereço":endereco ,"cpf":cpf})
  print("Usuário criado com sucesso")
  
def filtrar_usuario (cpf , usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("informe o cpf do usuário: ")
  usuario = filtrar_usuario(cpf, usuarios)
  
  if usuario:
    print("\n Conta criada com sucesso")
    return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
  
  print("\n Usuario não encontrado, fluxo de criação de conta encerrado")

def listar_contas(contas):
  for conta in contas:
    linha = f"""
          Agência: \t {conta['agencia']}
          C/C :\t\t {conta['numero_conta']}
          Titular: \t {conta['usuario']['nome']}
          """
    print("=" * 100)
    print(textwrap.dedent(linha))
  
  
  
  
  




def main():

  LIMITE_SAQUES = 3
  AGENCIA = '0001'

  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  usuarios = []
  contas = []
  
  while True:

    opcao = menu()

    if opcao == "d":
      valor = float(input("Por favor , coloque a quantidade : "))

      saldo, extrato = depositar(saldo, valor , extrato)

    elif opcao == "s":
      valor = float(input("Por favor, informe o valor do saque : "))
      
      saldo , extrato = sacar(
        saldo = saldo,
        valor = valor,
        extrato = extrato,
        limite = limite, 
        numero_saques = numero_saques,
        limite_saques = LIMITE_SAQUES,
      )

    elif opcao == "e":
      exibir_extrato(saldo, extrato = extrato)
      
    elif opcao == 'nu':
      criar_usuario(usuarios)
    
    elif opcao == 'nc':
      numero_conta = len(contas) + 1 
      conta = criar_conta(AGENCIA, numero_conta, usuarios)
      
      if conta:
        contas.append(conta)
    elif opcao == 'lc':
      listar_contas = (contas)
    elif opcao == "q":
      break
    else:
      print(
        'FALHA!! operação inválida, por favor, informe novamente a opção desejada'
      )
    
main()