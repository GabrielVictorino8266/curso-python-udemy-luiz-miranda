"""
As operacoes Matematicas possuem ordem. Nesse sentido, e necessario saber usa-las

Siga a regra

PEMDAS

1. (n+n)
2. **
3. * / // %
4. + -
"""

conta_1 = 1 + 1 ** 5 + 5
print(conta_1) # 7
"""
1+1**5+5
1**5 = 1
1+1=2
2+5=7
"""


conta_2 = (1 + 1) ** 5 + 5
print(conta_2)
"""
(1+1)**5+5
(1+1) = 2
2**5 = 32
32 + 5 = 37
"""

conta_3 = (2 + (3 + 3)) - 4
print(conta_3)
"""
(2+(3+3)) - 4
(3+3)=6
(2+6)=8
8-4=4
"""