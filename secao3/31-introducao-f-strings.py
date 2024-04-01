"""
F string

f - format, permite personalizar e deixar uma string formatada mais facilmente.

f"Meu nome {nome} e tenho {idade} anos."
 - Simplesmente passamos as variaveis entre {}

 Formatando valores em F string
 {:.2f} - adiciona 000.00
 {:,.2f} - troca o . pela virgula.
"""
nome = "Gabriel"
saldo = 1349.90

print(f"Meu nome e {nome} e tenho um saldo de R${saldo:.2f}")

