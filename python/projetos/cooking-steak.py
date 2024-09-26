# Escreva um programa em Python que avalie a temperatura de um steak e informe o ponto provável da carne de acordo com uma tabela fornecida. O usuário deve inserir a temperatura da carne, e o programa retornará o ponto correspondente.

# Utilize a seguinte tabela de referência de temperatura e ponto da carne:

# | Temperatura (°C) | Ponto da Carne      |
# |------------------|---------------------|
# | 48 - 57          | Mal Passado (Rare)  |
# | 58 - 62          | Ao Ponto (Medium)   |
# | 68 ou mais       | Bem Passado (Well Done) |

# Regras:
# - Se a temperatura for inferior a 48°C, o programa deve informar que a carne está **crua**.
# - Se a temperatura for superior a 67°C, o programa deve retornar que a carne está **bem passada**.
# - Caso contrário, o programa deve exibir o ponto correto conforme a tabela.

# Exemplo de uso:
# Informe a temperatura da carne: 55
# A carne está ao ponto menos (Medium Rare).

# Escreva o código abaixo:

def meat_point(temperature):
    if temperature <= 48:
        print('Crua')
    if 48 < temperature <= 57:
        print('Mal passado')
    elif 58 < temperature <= 62:
        print('Ao Ponto')
    elif 68 < temperature:
        print('Bem Passado')

resposta = int(input('Temperatura da carne: '))

meat_point(resposta)
