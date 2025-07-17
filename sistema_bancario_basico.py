print("-=-=-=-=-=-=-=-=-=-= BANCO BENÍCIO =-=-=-=-=-=-=-=-=-=-")
# Criação das variáveis necessárias
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    # Faz com que o menu apareça
    opcao = input(menu)
    # Faz com que a pessoa possa digitar a letra maiúscula a com espaços  
    opcao = opcao.lower().strip()

    # Configuração de depósito
    if opcao == "d":
        print("\n---------- ÁREA DE DEPÓSITO ----------\n")
        valor = float(input("Qual o valor que será depositado?\nR$"))
        # Caso a pessoa digite um valor inválido a mensegem abaixo será exibida
        if valor <= 0:
            print("\n[ERRO] Por favor, digite um valor a partir de R$1.00.")
        else:
            saldo = saldo + valor
            #Faz com que todo valor gigitado entre no extrato
            extrato += f"Depósito: R${valor}\n"
            print("Depósito realizado com suscesso!")

        print("--------------------------------------")


    # Configuração de saque
    elif opcao == "s":
        print("\n---------- ÁREA DE SAQUES ----------\n")

        # Delimita a quantidade de saques 
        if LIMITE_SAQUES <= 0:
            print("\n[ERRO] Limite de saques atingido.")

        else:
            valor = float(input("Qual o valor a ser sacado?\nR$"))

            # Delimita o valor do saque
            if valor > 500:
                print("[ERRO] Por favor digite um valor até R$500.00")

            # Faz com que só possa ser sacado o que se tem no saldo
            elif valor > saldo:
                print("\n[ERRO] SALDO INSUFICIENTE.")    
            
            else:
                saldo = saldo - valor
                # Faz com que seja adcionado ao extrato  
                extrato += f"Saque: R${valor:.2f}\n"
                # Faz a contagem da quantidade de saques
                LIMITE_SAQUES = LIMITE_SAQUES - 1
                print("Saque realizado com suscesso!")

            print("\n-------------------------------------\n")


    # Configuração do extrato
    elif opcao == "e":
        print("\n============== EXTRATO ==============")
        # Caso não haja nada no extrato a mensagem abaixo será exibida
        if extrato == "":
            print("\nNão foram realizadas movimentações\n")

        else:
            print(f"\n{extrato}" )
            print(f"Saldo: R${saldo:.2f}")
        print("=====================================")


    # Caso a letra Q for digitada a operação se encerrará
    elif opcao == "q":
        break

    # Se for digitado algo diferente de D, S, E OU Q a mensagem abaixo será exibida
    else:
        print("[ERRO] Opreração inválida, por favor selecione a operação desejada novamente.")

# No final da operação o texto abaixo será exibido
print("""----------------------------------------------------
             Obrigado pela preferência! 
                     Até logo!
----------------------------------------------------""")
