from random import randint
import os

nivel = 5
nome = input("Digite o nome do jogador: ")
pontos = 0
nv = 1
while True:
    numero_secreto = randint(0,nivel)
    tentativas = 3
    print(f'Nível {nv} | {pontos} pontos.')
    while tentativas > 0:
        print(f"{tentativas} tentativas")
        numero = int(input("Digite um número: "))
        if numero == numero_secreto:
            #print ("\n" * 130,end='')
            print("\x1b[2J\x1b[1;1H", end="")
            print(f"Parabéns, {nome}!! Você acertou!")
            nivel += 5
            nv += 1
            break
        if numero > numero_secreto:
            print(f"Você errou! O número secreto é menor que {numero}.")
        if numero < numero_secreto:
            print(f"Você errou! O número secreto é maior que {numero}.")
        tentativas -= 1
    pontos += tentativas
    print(f'O número secreto é: {numero_secreto}')
    if tentativas == 0:
        print(f'Fim de jogo!\n{nome}, você fez {pontos} pontos e nível {nv}.')
        break

