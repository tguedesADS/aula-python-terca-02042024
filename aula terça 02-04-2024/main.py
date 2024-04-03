#### Questão 1 ####

import os

def validar_ip(ip):
  partes = ip.split('.')
  if len(partes) != 4:
    return False
  for parte in partes:
    try:
      parte_int = int(parte)
    except ValueError:
      return False
    if parte_int < 0 or parte_int > 255:
      return False
  return True

def processar_ips(arquivo_entrada, arquivo_saida):
  ips_validos = []
  ips_invalidos = []

  try:
    with open(arquivo_entrada, "r") as arquivo:
      linhas = arquivo.readlines()
  except FileNotFoundError:
    print(f"Arquivo '{arquivo_entrada}' não foi encontrado no       diretório {os.getcwd()}.")
    return

  for linha in linhas:
    ip = linha.strip()
    if validar_ip(ip):
      ips_validos.append(ip)
    else:
      ips_invalidos.append(ip)

  with open(arquivo_saida, "w") as arquivo:
    arquivo.write("Endereços IP válidos:\n")
    for ip in ips_validos:
      arquivo.write(ip + "\n")

    arquivo.write("\nEndereços IP inválidos:\n")
    for ip in ips_invalidos:
      arquivo.write(ip + "\n")

print(f'Processamento concluído. Os resultados foram salvos em {os.getcwd()}.')

arquivo_entrada = os.path.join(os.getcwd(), "ips.txt")
arquivo_saida = os.path.join(os.getcwd(), "relatorio_ips.txt")

processar_ips(arquivo_entrada, arquivo_saida)



#### Questão 2 ####

import os

def bytes_para_mb(bytes):
  return bytes / 1024 / 1024
def calcular_percentual_uso(espaco_usuario, espaco_total):
  return (espaco_usuario / espaco_total) * 100

nome_arquivo_entrada = "usuarios.txt"
nome_arquivo_saida = "relatorio.txt"

if not os.path.exists(nome_arquivo_entrada):
  print(f"O arquivo '{nome_arquivo_entrada}' não foi encontrado no diretório")
else:
  usuarios = []
  with open(nome_arquivo_entrada, "r") as arquivo:
    for linha in arquivo:
      partes = linha.split()
      nome = partes[0]
      espaco_bytes = int(partes[1])
      usuarios.append((nome, espaco_bytes))

  espaco_total_mb = sum(bytes_para_mb(usuario[1]) for usuario in usuarios)

  relatorio_dado = []
  for nome, espaco_bytes in usuarios:
    espaco_mb = bytes_para_mb(espaco_bytes)
    percentual_uso = calcular_percentual_uso(espaco_bytes, espaco_total_mb)
    relatorio_dado.append((nome, espaco_mb, percentual_uso))

  with open(nome_arquivo_saida, "w") as relatorio:
    relatorio.write("ACME Inc. Uso do espaço em disco pelos usuários\n")
    relatorio.write("-----------------------------------------------------------------------------------------\n")
    relatorio.write("Nr. Usuário Espaço utilizado        % do uso\n")

    for i, dados in enumerate(relatorio_dado, 1):
      relatorio.write(f"{i:<5}{dados[0]:<15}{dados[1]:>10.2f} MB {dados[2]:>6.2f}%\n")

    espaco_medio_ocupado = espaco_total_mb / len(usuarios)
    relatorio.write(f"\nEspaço total ocupado: {espaco_total_mb: .2} MB")
    relatorio.write(f"\nEspaço médio ocupado: {espaco_medio_ocupado:.2} MB")



##### Questão 3 ####

def trocar_ultima_palavra(frase, palavra_antiga, palavra_nova):
  palavras = frase.split()

  ultima_palavra = None
  for i in range(len(palavras) - 1, -1, -1):
      if palavras[i] == palavra_antiga:
          ultima_palavra = i
          break

  if ultima_palavra is not None:
      palavras[ultima_palavra] = palavra_nova

  nova_frase = ' '.join(palavras)
  return nova_frase

frase = input("Digite a frase: ")
palavra_antiga = input("Digite a palavra antiga: ")
palavra_nova = input("Digite a palavra nova: ")

resultado = trocar_ultima_palavra(frase, palavra_antiga, palavra_nova)
print("Nova frase:", resultado)



#### Questão 4 ####

nome_usuario = input("Digite seu nome: ")
nome_invertido = nome_usuario.upper()[::-1]

print(f"Nome invertido: {nome_invertido}")



##### Questão 5 ####

notas = []
for i in range(1, 5):
  while True:
    try:
      nota = float(input(f"Digite a {i}ª nota: "))
      if nota < 0 or nota > 10:
        print("Por favor, insira uma nota entre 0 e 10.")
      else:
        notas.append(nota)
        break
    except ValueError:
      print("Por favor, insira um valor numérico válido.")

media = sum(notas) / len(notas)

maior_nota = max(notas)
menor_nota = min(notas)

print(f"Média final: {media:.2f}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")



##### Questão 6 ####

notas = []
for i in range(1, 5):
  while True:
    try:
      nota = float(input(f"Digite a {i}ª nota: "))
      if nota < 0 or nota > 10:
        print("Por favor, insira uma nota entre 0 e 10.")
      else:
        notas.append(nota)
        break
    except ValueError:
      print("Por favor, insira um valor numérico válido.")

media = sum(notas) / len(notas)

if media >= 7:
    print(f"\nMédia final: {media:.2f} - APROVADO")
else:
    while True:
        try:
            nota_final = float(input("Digite a nota da prova final: "))
            if nota_final < 0 or nota_final > 10:
                print("Por favor, insira uma nota entre 0 e 10.")
            else:
                break  
        except ValueError:
            print("Por favor, insira um número válido.")
    
    nova_media = (media + nota_final) / 2
    
    if nova_media >= 5:
        print(f"\nNova média final: {nova_media:.2f} - APROVADO NA FINAL")
    else:
        print(f"\nNova média final: {nova_media:.2f} - REPROVADO")



#### Questão 7 ####

numero = int(input("Digite um número inteiro: "))

antecessor = numero - 1
sucessor = numero + 1

print(f"O número informado foi {numero}.")
print(f"Seu antecessor é {antecessor}.")
print(f"Seu sucessor é {sucessor}.")



#### Questão 8 ####

def encontrar_indices(lista, x):

    indices = []
    for i, numero in enumerate(lista):
        if numero == x:
            indices.append(i)
    return indices

entrada_usuario = input("Digite uma lista de números inteiros separados por espaço: ")
lista_numeros = list(map(int, entrada_usuario.split()))

x = int(input("Digite o número inteiro x para encontrar na lista: "))

indices = encontrar_indices(lista_numeros, x)

print(f"Índices de todas as ocorrências de {x} na lista: {indices}")
