faturamento = input("Digite o faturamento desse mes:") # o padrão de um input é string, então é preciso tratar
faturamento = faturamento.replace("R$", "")
faturamento = float(faturamento) #trata a variavel para ser um float


print(faturamento)

custo = 300

lucro = faturamento - custo
print(f"O faturamento foi de {faturamento} e o lucro foi de {lucro}")