a = 'a'
b = 'b'
c = 1.1
formato = 'a={}, b={}, c={}'.format(a,b,c)

print(formato)

"""
a saida e:
    a=a, b=b, c=1.1
    formato = 'a={}, b={}, c={}, d={}'.format(a,b,c)
    # retorna index out of range = ja acabou e nao encontra.
"""

#passando valor com posicoes
formato = "c={2}, b={1}, a={0}".format(a,b,c)
# mantive a ordem, mas usei os indices respectivos.
print("Novo formato: ", formato)


str1 = 'texto1'
str2 = 'texto2'
print(str1 + str2)

int = 10
float = 1.5
print(int * float)

"""
    // - divisao inteira
    / - divisao para float
"""
divisao = 10//2
divisao2 = 10/2
print(divisao2, type(divisao2))