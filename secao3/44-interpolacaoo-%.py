"""
interpolacao de strings
s           string
i / d       int
f           float
x e X       hexadecimal
"""

nome = "Luiz"
preco = 300.00
variavel = '%s, total foi R$%.2f' % (nome, preco)
print(variavel)
print("Hexadecimal de %i e %04x" % (1500, 1500))
print("Hexadecimal de %i e %08x" % (1500, 1500))
