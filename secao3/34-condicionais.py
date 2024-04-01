"""
Aprendendo as condicionais no python

if - se
else - senao
if
"""

entrada = input("Voce quer entrar ou sair? ")

# if entrada == 'entrar':
#     print("Voce entrou.")
# else:
#     print("Voce saiu do sistema")

if entrada == 'entrar':
    print("Voce entrou no sistema")
elif entrada == 'sair':
    print("Voce saiu do sistema.")
else:
    print("Voce nao digitou nem entrar nem sair")

print("FORA DOS BLOCOS")