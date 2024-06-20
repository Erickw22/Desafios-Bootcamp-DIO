#Criando um sistema bancario
menu= """

[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair
=>"""

saldo = 0
limite = 500
extrato=""
numero_saques=0
LIMITE_SAQUES=3

while True:
  opcao = input (menu)

  if opcao == "d":
    valor = float(input("Qual valor voce deseja depositar? "))

    if valor >0:
      saldo += valor
      extrato += f"Deposito no valor de R$ {valor:.2f}\n"

    else:
      print("Valor informado é invalido")

  elif opcao == "s":
        valor = float(input("Qual o valor você deseja sacar? "))

        excedeu_saldo = valor>saldo
        excedeu_limite = valor>limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
          print("Saldo insuficiente. ")
        
        elif excedeu_limite:
          print("Limite de valor para saque diario atingido.")
        
        elif excedeu_saques:
          print("Limite de saques diarios atingidos.")
        
        elif valor > 0:
          saldo -=valor
          extrato += f"Saque no valor de R$ {valor:.2f}\n"
          numero_saques += 1

        else:
          print("Valor informado é invalido.")
      
  elif opcao == "e":
        print("\n----------------Extrato----------------")
        print("Não ouve nemhuma movimentação." if not extrato else extrato)
        print(f"Seu saldo é de R${saldo:.2f}")
        print("--------------------------------------------")
      
  elif opcao =="q":
        break
    
  else:
       print("Operação nao realizada, opção inserida invalida")