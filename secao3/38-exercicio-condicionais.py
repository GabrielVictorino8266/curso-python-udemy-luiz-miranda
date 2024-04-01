primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite o segundo valor: ")


if ord(primeiro_valor) >= ord(segundo_valor):
    print(f'{primeiro_valor=} e maior/igual {segundo_valor=}')
else:
    print(f'{segundo_valor=} e maior {primeiro_valor=}')
#ord retorna qual o ascii do char correspondente.
print("\n\n")

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} e maior/igual {segundo_valor=}')
else:
    print(f'{segundo_valor=} e maior {primeiro_valor=}')
