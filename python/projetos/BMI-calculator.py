# Cálculo de IMC - Indice de Massa Corporal

"""
Qual a sua altura: 
Qualé o seu peso:
"""

# MENOR QUE 18,5 MAFREZA
# ENTRE 18,5 E 24,9 NORMAL
# ENTRE 25,0 E 29,9 SOBREPESO
# ENTRE 30,0 E 39,9 OBSIDADE
# MAIOR QUE 40,0 OBSIDADE GRAVE

altura = float(input('Qual a sua altura (em metros): '))
peso = float(input('Qual é o seu peso (em kg): '))

resultado_imc = peso / altura ** 2

if resultado_imc < 18.5:
    print(f'{resultado_imc} >> MAFREZA')
elif 18.5 <= resultado_imc < 25:
    print(f'{resultado_imc} >> NORMAL')
elif 25 <= resultado_imc < 30:
    print(f'{resultado_imc} >> SOBREPESO')
elif 30 <= resultado_imc < 40:
    print(f'{resultado_imc} >> OBSIDADE')
elif 40 <= resultado_imc:
    print(f'{resultado_imc} >> OBSIDADE GRAVE')
