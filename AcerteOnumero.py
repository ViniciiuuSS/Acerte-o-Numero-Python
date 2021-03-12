from random import randint
from time import sleep
ale = randint(0, 5) # RANDINT CRIA UM NUMERO ALEATORIO
print("-=-" * 20)
print("Vou pensar em um numero entre 0 e 5 ! Tente adivinhar...")
print("-=-" * 20)
adi = int(input("Escolha um numero de 0 a 5 : "))
print("PROCESSANDO...")
sleep(2)
if (adi == ale):
    sleep("Processando...")
    print("Parabens voce acertou! O numero que pensei foi {}".format(ale))
else:

    print("ERROUUUO numero que pensei foi {}".format(ale))