menu = """
---------------BANCO BENÍCIO--------------

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

    opcao = input(menu)
    opcao = opcao.lower().strip()

    if opcao == "d":
        print("\n-> ÁREA DE DEPÓSITO\n")
        valor = float(input("Qual o valor que será depositado?\nR$"))
        if valor <= 0:
            print("\n[ERRO] Por favor, digite um valor a partir de R$1.00")
        else:
            saldo = saldo + valor
            extrato += f"+ R${valor}"


    elif opcao == "s":
        print("\n-> ÁREA DE SAQUES\n")
        if LIMITE_SAQUES <= 0:
             print("\n[ERRO] Limite de saques atingido")
        else:
            valor = float(input("Qual o valor a ser sacado?\nR$"))
            LIMITE_SAQUES = LIMITE_SAQUES - 1
        
        if valor > 500:
             print("Por favor digite um valor até R$500.00")

        elif valor > saldo:
             print("\nSALDO INSUFICIENTE.")    

        else:
             saldo = saldo - valor
             extrato += f"- R${valor}"

    elif opcao == "e":
        print("\n-> EXTRATO")
        if extrato == "":
            print("\nNão foram realizadas movimentações\n")

        else:
            print(f"\n {extrato}" )
            print(f"\nVocê tem R${saldo} disponiveis na sua conta.")
        
    
    elif opcao == "q":
        break

    else:
        print("[ERRO] Opreração inválida, por favor selecione a operação desejada novamente.")
print("""------------------------------------------
        Obrigado pela preferência! 
                Até logo!
------------------------------------------""")
