from random import randint
from time import sleep
comp = randint(0,10)
print("-=-" * 20)
print("Vou pensar em um numero de 0 a 10! Tente adivinhar se for capaz...")
print("-=-" * 20)
jogador = int(input("Numero: "))
print("PROCESSANDO")
sleep(2)
if (jogador == comp):
    print("Se é o mestre dos magos então ! Acertou o que sabe")
else:
    print("HAHAHA! ERROU FEIO! Pensei no numero: {}".format(comp))