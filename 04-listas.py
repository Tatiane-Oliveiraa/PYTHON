lista_nomes = ["Tatiane", "Andrew", "Taillanny", "Tuany"]

#tamanho da lista
print(len(lista_nomes))

#pegar um item da lista - sempre pela posição do elemento
primeiro = lista_nomes[0]
print(primeiro)

# encontrar um item na lista
existe_na_lista = "Tatiane" in lista_nomes
print(existe_na_lista)

posicao_tatiane = lista_nomes.index("Tatiane")
print(posicao_tatiane)

# outro exemplo
lista_vendas = [100, 50, 1000, 800, 35]

# total vendas
total_vendas = sum(lista_vendas)
print(total_vendas)

# maior valor
maior_valor = max(lista_vendas)

# menor valor
menor_valor = min(lista_vendas)

#média de vendas
media_vendas = total_vendas / len(lista_vendas)

print(f"Maior valor é R${maior_valor}")
print(f"Menor valor é R${menor_valor}")
print(f"Média é R${media_vendas}")

# outro exemplo

lista_precos = [5000, 3000, 2000]
novo_valor = lista_precos[0] * 1.1
lista_precos[0] = novo_valor
print(lista_precos)

#adicionar um elemento
lista_precos.append(600)

# remover um elemento
lista_nomes.remove("Tatiane")
print(lista_nomes)


# juntar duas listas
novas_contratacoes = ["Pamela", "Tais"]
lista_nomes.extend(novas_contratacoes)
print(lista_nomes)


# ordenar uma lista
lista_precos.sort()#coloca em ordem crescente
print(lista_precos) 
lista_precos.sort(reverse=True)  #coloca em ordem decrescente
print(lista_precos) 

