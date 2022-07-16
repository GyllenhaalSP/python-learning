import random
import sys
import time
from art import *

print(logo)

# Variables para llevar las puntuaciones
ganadas = 0
perdidas = 0
empates = 0

while True:  # Bucle principal
    print(f'{ganadas} Ganadas, {perdidas} Perdidas, {empates} Empates\n')
    while True:  # Bucle de datos
        jugador = input('Introduce tu siguiente movimiento: Piedra'
                        ' - Papel - Tijeras o Salir \n').lower()  # Añadido lower() para normalizar el input

        if jugador == 'salir':
            sys.exit()  # Acabar el juego
        if jugador == 'piedra' or jugador == 'papel' or jugador == 'tijeras':
            break  # Sale del bucle de datos
        print('Introduce Piedra, Papel, Tijeras o Salir\n')

    # Mostrar la jugada del jugador
    if jugador == 'piedra':
        print('\nPIEDRA contra...')
        print(piedra)
        print(versus)
    elif jugador == 'papel':
        print('\nPAPEL contra...')
        print(papel)
        print(versus)
    elif jugador == 'tijeras':
        print('\nTIJERAS contra...')
        print(tijeras)
        print(versus)

    time.sleep(2)

    # Mostrar la jugada del ordenador
    numeroAleatorio = random.randint(1, 3)
    ordenador = ""
    if numeroAleatorio == 1:
        ordenador = 'piedra'
        print(piedra)
        print('PIEDRA\n')
    if numeroAleatorio == 2:
        ordenador = 'papel'
        print(papel)
        print('PAPEL\n')
    if numeroAleatorio == 3:
        ordenador = 'tijeras'
        print(tijeras)
        print('TIJERAS\n')

    # Mostrar y guardar la racha de ganadas, perdidas y empates
    if jugador == ordenador:
        print('¡Empate!')
        empates += 1
    elif jugador == 'piedra' and ordenador == 'tijeras':
        print('¡Ganaste!')
        ganadas += 1
    elif jugador == 'papel' and ordenador == 'piedra':
        print('¡Ganaste!')
        ganadas += 1
    elif jugador == 'tijeras' and ordenador == 'papel':
        print('¡Ganaste!')
        ganadas += 1
    elif jugador == 'piedra' and ordenador == 'papel':
        print('¡Has perdido!')
        perdidas += 1
    elif jugador == 'papel' and ordenador == 'tijeras':
        print('¡Has perdido!')
        perdidas += 1
    elif jugador == 'tijeras' and ordenador == 'piedra':
        print('¡Has perdido!')
        perdidas += 1
