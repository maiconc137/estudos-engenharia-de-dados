# Leia a idade do usuário e classifique-o em:
# - Criança – 0 a 12 anos
# - Adolescente – 13 a 17 anos
# - Adulto – acima de 18 anos
# -Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

usuario = int(input('Digite sua idade: '))

if usuario < 0:
    print('Digite uma idade válida!')
elif 0 <= usuario <= 12:
    print('Criança!')
elif 13 <= usuario <= 17:
    print('Adolescente!')
else:
    print('Adulto!')
