def verificaArquivo(arquivo):
  try:
    a = open(arquivo, 'rt')
    a.close()
  except:
    print("Arquivo não localizado")
    return False
  else:
    print("Arquivo existente.")
    return True

def criaArquivo(arquivo):
  try:
    a = open(arquivo, 'wt+')
  except:
    print("Não foi possível criar o arquivo.")
    return False
  else:
    print("Arquivo criado com sucesso.")
    return True
  finally:
    a.close()

def cadastrar(arquivo, nomeItem, localitem):
    try:
        a = open(arquivo, 'at')
    except:
        print("Erro ao abrir arquivo.")
    else:
       a.write(f"Marca: {nomeItem.upper()} | Andar: {localitem.upper()}\n")
    finally:
        a.close()

def listagem(arquivo):
  try:
    a = open(arquivo, 'rt')
  except:
    print("Erro na listagem.")
  else:
    print(a.read())
  finally:
    a.close()

def pesquisar(arquivo):
  try:
    a = open(arquivo,'rt')
  except:
    print("Erro na pesquisa.")
  else:
    print(a.readlines())
  finally:
    a.close()

a = "marcascadastradas.txt"

v = verificaArquivo(a)
if v == False:
  criaArquivo(a)

with open(a, 'r') as arquivo:
  mensagem = arquivo.readlines()

while True:
  print("***MENU***")
  print("(1) Pesquisar")
  print("(2) Cadastrar nova marca")
  print("(3) Listar todos cadastros")
  print("(4) Sair")

  try:
    op = int(input("Digite uma opção: "))
  except ValueError:
    print("Opção inválida. Tente novamente.")
    continue
  except:
    print("Erro. Digite novamente.")
    continue

  if op == 1:
    pes = input("Pesquisar: ")
    for linha in mensagem:
      if pes.upper() in linha:
        print(linha)
        bot = input("...")
        if bot:
         continue

  elif op == 2:
      marca = input("Marca: ")
      local = input("Andar (1/2/3 ou 4-outro): ")
      cadastrar(a, marca, local)
      print(f"Cadastro realizado.\n{marca.upper()}, {local}° andar.")

  elif op == 3:
    listagem(a)

  elif op == 4:
    print("Encerrando o programa...")
    break
