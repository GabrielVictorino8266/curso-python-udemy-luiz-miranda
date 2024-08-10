"""
avalia qualquer condicao verdadeiro valida a expressao como verdadeiro
"""

# entrada = input('[E]ntrada [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Na operacao acima, o and e or podem ser trabalhados com ( ), dando prioridade na expressao.
    

"""
Curto Circuito
"""

print(False or False or False or 'a' or True) #vai para no true, no caso na letra 'a'
print(True or False or False or '' or True) # avalia o true e para. No caso, o primeiro.
print(False or False or False or '' or True) # avalia o True, no caso, o ultimo

senha = input('Senha: ') or "Sem senha" # atua como um if.
print(senha)