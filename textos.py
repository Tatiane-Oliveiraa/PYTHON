faturamento = 1000
custo = 300

lucro = faturamento - custo

print("O lucro foi de", lucro, "e o faturamento foi de", faturamento) # forma normal
mensagem = "O lucro foi de " + str(lucro) + " e o faturamento foi de " + str(faturamento) # menos usada
print(mensagem)


# f-string
texto = f"O lucro foi de R$ {lucro} e o faturamento foi de R$ {faturamento}" # mais usada
print(texto)

# fórmulas de texto

email = "EMAIL_FALSO@gmail.com"

email = email.lower() # coloca em letra minuscula
email = email.upper() # coloca em letra maiuscula

print(email)

# tamanho de um texto

tamanho_texto = len(email) # conta quantos caracteres tem no texto
print(tamanho_texto)

# posição de um caracter no texto
posicao = email.find("@")  #find procura a posição de um caracter
print(posicao)

# pedaços de um texto
nome_usuario = email[:posicao] # : significa posição inicial do texto
print(nome_usuario)

# trocar um pedaço do texto
email = email.lower() # coloca em letra minuscula
email = email.replace("gmail.com", "yahoo.com")
print(email)

# title, capitalize, upper
nome = "joão lira"
print(nome.capitalize()) # coloca a 1º letra maiuscula
print(nome.title()) # coloca a 1º letra de cada palavra maiuscula
print(nome.upper()) # coloca tudo maiusculo
print(nome)