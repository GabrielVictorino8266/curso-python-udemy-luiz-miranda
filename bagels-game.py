import random


NUM_DIGITS = 3 # Qtde maxima de digitos.
TENTATIVAS_MAX = 10 # Maximo de tentativas


print("""
===========Bem-vindo ao jogo de Bagels.===========
Este e um jogo logico onde voce devera advinhar
um numero baseado em pistas.\n\n\n
""")

def main():
    print("""
    Bagels Game
Estou pensando em um numero de 3 digitos, sem digitos repetidos. Aqui estao algumas pistas:
          Pico      - Um digito correto, mas na posicao errada.
          Fermi     - Um digito certo e na posicao certa.
          Bagels    - Nenhum digito certo

""")

    while True:
        secretNum = getSecretNum() # vai gerar o numero secreto
        print("Pensei em um numero.")
        # print(secretNum)
        print(f"Voce tem {TENTATIVAS_MAX} tentativas para acertar.")

        numGuesses = 1
        while numGuesses <= TENTATIVAS_MAX:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}")
                guess = input('> ')            

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # acertou
            if numGuesses > TENTATIVAS_MAX:
                print(f"Voce ja usou todas as tentativas.\nNumero correto: {secretNum}")
                break

        print("Quer jogar novamente? y = yes  n = no")
        if not input('> ').lower().startswith('y'):
            break
    print("Obrigado por jogar.")

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers) # embaralha a lista
    
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += numbers[i]

    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return "Parabens, acertou!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #digito correto no lugar certo
            clues.append('Fermi')
        elif guess[i] in secretNum:
            #digito certo no lugar errado
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()