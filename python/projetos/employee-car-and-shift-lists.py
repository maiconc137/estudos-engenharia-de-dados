"""

Criar um programa que gera 3 listas de acordo com a necesssidade logo abaixo:

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trablham durante o dia
Lista3 = Funcionários que não tem carro

"""

# Lista de funcionários com informações sobre carro e horário de trabalho
funcionarios = [
    {"nome": "Ana", "tem_carro": True, "trabalha_noite": True},
    {"nome": "João", "tem_carro": True, "trabalha_noite": False},
    {"nome": "Pedro", "tem_carro": False, "trabalha_noite": False},
    {"nome": "Maria", "tem_carro": True, "trabalha_noite": True},
    {"nome": "Lucas", "tem_carro": False, "trabalha_noite": True},
    {"nome": "Paula", "tem_carro": True, "trabalha_noite": False},
]

# Inicializando conjuntos
todos_funcionarios = {funcionario["nome"] for funcionario in funcionarios}
funcionarios_com_carro = {funcionario["nome"] for funcionario in funcionarios if funcionario["tem_carro"]}
funcionarios_trabalham_noite = {funcionario["nome"] for funcionario in funcionarios if funcionario["trabalha_noite"]}

# Lista 1: Funcionários que têm carro e trabalham à noite (intersection)
lista1 = funcionarios_com_carro.intersection(funcionarios_trabalham_noite)

# Lista 2: Funcionários que têm carro e trabalham durante o dia (difference)
lista2 = funcionarios_com_carro.difference(funcionarios_trabalham_noite)

# Lista 3: Funcionários que não têm carro (difference)
lista3 = todos_funcionarios.difference(funcionarios_com_carro)

# Imprimindo as listas geradas
print("Lista 1 - Funcionários que têm carro e trabalham à noite:", lista1)
print("Lista 2 - Funcionários que têm carro e trabalham durante o dia:", lista2)
print("Lista 3 - Funcionários que não têm carro:", lista3)
