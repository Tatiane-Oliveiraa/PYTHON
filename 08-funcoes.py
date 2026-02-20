# sempre que for usar a mesma linha de código, utiliza funções.
# ou toda vez que quiser usar uma lógica isolada.

# forma mais basica de usar uma função

# def diga_oi():
#   print("Oi")

# diga_oi()


dic_produtos = { "iphone": 10000,
                "mac": 15000,
                "apple watch": 5000,
                "airpod": 2000}




def calcular_novo_preco(preco):  # função com parâmetro
    # definir tudo que preciso para calcular novo preço
    inflacao = 0.05
    iss = 0.07
    novo_preco = preco * ( 1 + (inflacao + iss))  # cálculo do novo preço
    return novo_preco  # para ela retornar o valor precisa colocar o return
 

for item in dic_produtos:
    preco_original = dic_produtos[item]
    novo_preco = calcular_novo_preco(preco_original)  # aqui já está colocando o novo preço na váriavel usando a função
    dic_produtos[item] = novo_preco

print(dic_produtos)