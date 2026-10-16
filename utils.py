import sys 
import time
import os

def animacao_incialializador():

    for i in range(10):

        pontos = "." * (i % 4)

        sys.stdout.write(f"\rLigando{pontos}   ")

        sys.stdout.flush()

        time.sleep(0.5)

    print("\nSistema Ligado.")

    time.sleep(2)

    os.system('cls')


def animacao_desligamento():

    for i in range(10):

        pontos = "." * (i % 4)

        sys.stdout.write(f"\rDesligando{pontos}   ")

        sys.stdout.flush()

        time.sleep(0.5)

    print("\nSistema desligado.")