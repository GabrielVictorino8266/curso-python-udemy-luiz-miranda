# nome = str(input("Qual o seu nome? "))
# print(f'Seu nome e {nome=}.') #mostra a variavel e seu valor

"""
nome = "Gabriel"
print(nome=) # A saida no terminal sera: nome='Gabriel'
"""

numero1 = int(input("Informe o numero 1: "))
numero2 = int(input("Informe o outro: "))

#nao e a melhor das praticas, chamada de typecasting ou coercion
# Permite que o usuario digite outras coisas, como letras, quebrando o programa.

"""
Uma situacao ideal seria:

int_numero_1 = int(numero1)
int_numero_2 = int(numero2)

Caso ocorra um erro, aconteceria aqui e permitiria tratar os erros dessa forma.
"""

print(f'Informe a soma dos numeros: {numero1 + numero2}')