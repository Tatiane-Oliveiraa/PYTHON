faturamento= 1000 #números inteiros
custo = 300
imposto = 0.2 #numero float
lucro1 = faturamento - custo - imposto * faturamento  
print(lucro1)

faturamento= 600
lucro2 = faturamento - custo - imposto * faturamento  
print(lucro2)

#tipos de variáveis
#int -> numeros inteiros
#float -> numeros com casa decimal
# string -> textos
# booleanos -> Verdadeiro ou Falso ( True / False )

print("O lucro da loja no primeiro mês foi de", lucro1)
print("O lucro da loja no primeiro mês foi de", lucro2)

margem_lucro = lucro2 / faturamento

print("Margem de lucro de", margem_lucro, "%")

meta = 0.2

bateu_meta = margem_lucro > meta   #booleana
print(bateu_meta)

# mod % (resto da divisão)
# // (parte inteira da divisão)
duracao_contrato = 140  # meses

anos = duracao_contrato // 12  # quantos anos tem duração em meses
meses_sobra = duracao_contrato % 12 # quantos meses falta de contrato

print("O contrato tem", anos, "anos e", meses_sobra, "meses.")



