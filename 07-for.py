# for item in lista:
#   execute isso para cada item

lista_produtos = ["iphone", "mac", "apple watch", "airpod"]

for item in lista_produtos:
    print(item)



# for com intervalo fixo
for i in range(10):
    print(i)


# for para percorrer listas
lista_precos = [10000, 15000, 5000, 2000]
inflacao = 0.1  # aumento na inflação de 10%

nova_lista = []  # criei uma nova lista de preços vazia

for preco in lista_precos:
    novo_preco = preco * ( 1 + inflacao)  # ajustando valores que estão na lista em 10%
    nova_lista.append(novo_preco)  # adicionando os valores ajustados na nova lista
    
print(nova_lista)  # mostrando a nova lista


# usando if dentro do for

for preco in lista_precos:
    if preco > 10000:  # 
        novo_preco = preco * 1.1
    else:
        novo_preco = preco * 1.5
    nova_lista.append(novo_preco)

print(nova_lista)

# for para percorrer um dicionario de valores

dic_produtos = { "iphone": 10000,
                "mac": 15000,
                "apple watch": 5000,
                "airpod": 2000}

for item in dic_produtos:
    print(item)  # mostra o item da lista
    preco = dic_produtos[item]
    print(preco) # mostra o preço do item

# alterando o preço de um item

for item in dic_produtos:
    novo_preco = dic_produtos[item] * 1.1
    dic_produtos[item] = novo_preco
print(dic_produtos)


# while  - é usado quando não tem um fim definido. Senão fica em loop infinito

vendas = 100
meta = 200

while vendas < meta:
    print("Não bateu a meta")
    vendas = vendas + 10 # se enquandra em uma lógica para conseguir parar o