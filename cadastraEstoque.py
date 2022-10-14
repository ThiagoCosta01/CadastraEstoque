cadastros = []
contador = 0

#Funções:
def cadastrarPeca(codigo):
    print(f"Peça {codigo}.")
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite a fabricante da peça: ")
    valor = int(input("Digite o preço da peça: "))
    while valor < 0 or not valor:
        print("Valor inválido. Tente novamente.")
        valor = int(input("Digite o preço da peça: "))
    dicionario = {"codigo":codigo,"nome":nome, "fabricante":fabricante, "valor":valor}
    cadastros.append(dicionario.copy())

def consultar():
    while True:
        print("1 - Consultar todas as peças")
        print("2 - Consulta Peças por Código")
        print("3 - Consulta Peças por Fabricante")
        print("4 - Retornar ")
        try:
            escolha = int(input("Digite uma opção: "))
        except:
            print("Opção inválida.")
            continue
        if escolha == 1:
            for dicionarios in cadastros:
                for key,value in dicionarios.items():
                    print('{} : {}'.format(key, value))
        elif escolha == 2:
            codPesquisa = int(input("Digite o código da peça: "))
            for dicionarios in cadastros:
                if dicionarios["codigo"]== codPesquisa:
                    for key,value in dicionarios.items():
                     print('{} : {}'.format(key, value))
        elif escolha == 3:
            codPesquisa = input("Digite o nome da fabricante: ")
            for dicionarios in cadastros:
                if dicionarios["fabricante"] == codPesquisa:
                    for key,value in dicionarios.items():
                     print('{} : {}'.format(key, value))
        elif escolha == 4:
            print("Retornando ao menu principal.\n")
            break
        else:
            print("Opção inválida. ")
            continue

def removerPeca():
    codRemov = int(input("Código da peça que deseja remover: "))
    for dicionarios in cadastros:
        if dicionarios["codigo"] == codRemov:
            cadastros.remove(dicionarios)

#Programa Principal
while True:
    try:
        print("Bicicletaria do Thiago Lucas Silveira Costa.")
        print("1 - Cadastrar peça")
        print("2 - Consultar peças")
        print("3 - Remover peça")
        print("4 - Sair")
        escolha = int(input("Escolha a opção desejada: "))
    except:
        print("Opção inválida.")
        continue
    if escolha == 1:
        contador = contador + 1
        cadastrarPeca(contador)
        continue
    elif escolha == 2:
        consultar()
    elif escolha == 3:
        removerPeca()
    elif escolha == 4:
        break
