#if condicao/comparacao:
#        tudo o que voce ur que aconteca se essa condição for verdadeira
#else:
#        caso o contrário, ele vai executar o que está aqui

vendas = 500
meta = 450

if vendas >= meta:
        print("Batemos a meta de vendas")
        if vendas >= ( 2 * meta):
                print("Foi muito fácil, batemos mais que o dobro da meta")
        else:
                print("Passamos por pouco da meta")
        print("No mes que vem, dobra a meta que a gente bate de novo!")
else:   
        vendas_faltantes = meta - vendas
        print(f"Faltaram {vendas_faltantes} vendas")

#faixa de bonus
#50 se ele bateu a meta
# 100 se ele bateu mais que o dobro da meta
# 0 se ele não bateu a meta

meta_funcionario = 500
vendas_funcionario = 1000


if vendas_funcionario >= ( 2 * meta_funcionario):
        bonus = 100
elif vendas_funcionario >= meta_funcionario:
        bonus = 50
else:
        bonus = 0

print(bonus)

# cadastro de produtos
lista_produtos = ["iphone", "mac", "apple watch", "airpod"]
produto_a_cadastrar = input("Digite o nome do produto:")
produto_a_cadastrar = produto_a_cadastrar.lower() # padronizei para que tudo digitado fique com letra minuscula

if produto_a_cadastrar in lista_produtos:
        print("Produto já cadastrado")
else:
        lista_produtos.append(produto_a_cadastrar)

print(lista_produtos)


# mais de uma condição
# and = e
# or = ou

meta_empresa = 500
meta_funcionario = 50
vendas_empresa = 590
vendas_funcionario = 45

if vendas_funcionario >= meta_funcionario and vendas_empresa >= meta_empresa:
        print("Vai ganhar bônus")
else:
        print("Sem bônus")
