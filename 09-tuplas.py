# tuplas é como se fosse uma lista imutável
# não pode por e não pode tirar nada dela

coordenadas = (10.2534548, 1.2684865)

print(coordenadas)

# unpacking - desempacotar

latitude, longitude = coordenadas

print(latitude)
print(longitude)


#tupla com funções

# bonus 1: R$ 2 por venda -> incentiva a quantidade de vendas
# bonus 2: 1% do valor de vendas -> incentiva a vender produtos mais caros

vendas_funcionarios = [10, 20, 50, 600, 50, 60, 400]

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)
    return bonus1, bonus2

resultado_bonus = calcular_bonus(vendas_funcionarios)
bonus1, bonus2 = resultado_bonus  # unpacking
print(bonus1)
print(bonus2)

# exemplo de tupla com for

lista_vendas = [("Lira", 100), ("Alon", 50), ("Manu", 300)]

for vendedor, vendas in lista_vendas:  # fazendo assim o python reconhece que ele vai percorrer uma tupla
    print(f"O {vendedor} vendeu {vendas}")