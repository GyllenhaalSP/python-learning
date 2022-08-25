"""
La Mansión Encantada game by GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import os
import time
from art import header, demon, hammer, bathroom, front_door


def clear():
    """
    Clear the console window.
    """
    os.system('cls||clear') if os.name in ('nt', 'posix') else print('\n'*100)


while True:
    print(header)
    print('¡Bienvenido a la mansión encantada!')
    time.sleep(1)
    print('¡Tu misión es salir vivo de ella!\n')
    time.sleep(1)
    print('¡Grandes recompensas te esperan!\n')
    time.sleep(2)
    print('Te encuentras en una habitación oscura. Hay una puerta.\n')
    time.sleep(2)
    choice1 = input('¿Qué eliges? ¿Permanecer o Salir?\n')

    while True:
        if choice1.lower() == "permanecer":
            print('\n¿¡En serio te vas a quedar aquí!?', end=" ")
            time.sleep(2)
            choice1 = input('Salir, ¿Sí o No?\n')
            while True:
                if choice1.lower() == 'no':
                    print('\n¿¡En serio te vas a quedar aquí!?', end=" ")
                    time.sleep(3)
                    choice1 = input('Va, salir, ¿Sí o No?\n')
                    if choice1 == ('si' or 'sí'):
                        break
                    if choice1 == 'no':
                        continue
                elif choice1.lower() == ('si' or 'sí'):
                    break
            if choice1.lower() == ('si' or 'sí'):
                print('\n"Sí, es mejor investigar un poco..."\n')
                time.sleep(3)
                clear()
                break

        if choice1.lower() == 'salir':
            print('\n"Venga, vamos a ver qué hay por ahí..."\n')
            time.sleep(3)
            clear()
            break

    time.sleep(3)
    print('La habitación da a un pasillo oscuro...')
    time.sleep(1.75)
    print('Las paredes están tapizadas y hay muchos cuadros.')
    time.sleep(1.75)
    print('Parecen antiguos. El ambiente está lleno de polvo.')
    time.sleep(1.75)
    print('Hay una puerta más adelante, a la derecha.\n')
    time.sleep(2.5)

    choice2 = input('¿Entrar o Seguir por el pasillo?\n')

    if choice2.lower() == 'entrar':
        clear()
        print(demon)
        time.sleep(4)
        print('"Hasta luego Lucas..."\n')
        time.sleep(1.75)
        print('Un demonio horrible proveniente del inframundo se ha hecho palillos de dientes con tus huesos.')
        time.sleep(3)
        print('\n"¡MÁS SUERTE LA PRÓXIMA VEZ!"\n')
        time.sleep(5)
        clear()
        continue

    elif choice2.lower() == 'seguir':
        print('\nHay un pasillo bastante largo.')
        time.sleep(1.75)
        print('Todo el lado izquierdo está lleno de amplias cristaleras.\n')
        time.sleep(2.5)
        print('"Desde luego, en esta casa no se limpia desde el año 1486. Por lo menos."')
        time.sleep(4)
        print('"Si tuviera un botecito de Cristasol y un trapito... Qué pena de todo."\n')
        time.sleep(5)
        print(hammer)
    time.sleep(3)

    choice3 = input('Más o menos a la mitad del pasillo hay otra puerta a la derecha. Entrar, '
                    '¿Sí o No?\n')

    if choice3.lower() == ('si' or 'sí'):
        clear()
        print(bathroom)
        time.sleep(3)
        print('"Madre mía, qué puto asco."\n')
        time.sleep(2)
        print('"Está todo lleno de sangre y huele a cadáver 4 meses descomponiéndose"')
        time.sleep(2)
        print('"Mejor no correr la cortina de la bañera..."')
        time.sleep(2)
        print('"Voy a volver al pasillo y a seguir investigando."\n')
        time.sleep(10)
        clear()

    elif choice3.lower() == 'no':
        clear()

    print('\n"La verdad es que es muy largo el pasillo."')
    time.sleep(3)
    print('"Pero al final se ve el hueco de una escalera."\n')
    time.sleep(5)
    print('"Los escalones crujen como si se fueran a romper."')
    time.sleep(3)
    print('"Es un poco creepy todo esto..."\n')
    time.sleep(3)
    print('Llegas a un recibidor.')
    time.sleep(5)
    clear()
    print(front_door)
    time.sleep(5)
    print('¿¡Es esa la puerta principal!?\n')
    choice4 = input('¿Quieres salir? ¿Sí o No?\n')

    while True:
        if choice4.lower() == 'no':
            clear()
            print('\n¿¡En serio te vas a quedar aquí!?', end=" ")
            time.sleep(2)
            choice4 = input('A ver, sales, ¿¡no!? ¿Sí o No?\n')
            while True:
                if choice4.lower() == 'no':
                    print('\n¿¡En serio te vas a quedar aquí!?', end=" ")
                    time.sleep(3)
                    choice4 = input('Va, vamos a centrarnos. Quieres salir, ¿verdad?,'
                                    ' ¿Sí o No?\n')
                    if choice4.lower() == ('si' or 'sí'):
                        clear()
                        break
                    if choice4.lower() == 'no':
                        continue
                elif choice4.lower() == ('si' or 'sí'):
                    clear()
                    break
            if choice4.lower() == ('si' or 'sí'):
                clear()
                print('\nGracias a Dios. Ya estás fuera. Enhorabuena.\n')
                break

        if choice4.lower() == ('si' or 'sí'):
            clear()
            print('\n"Gracias a Dios. Ya estás fuera. Enhorabuena."\n')
            break

    time.sleep(5)
    print('¿Premio? ¿Qué premio? ¿¡Tú eres tonto!?\n')
    time.sleep(3)
    print('Bastante premio que no te hayas encontrado con el DEMONIO de la primera habitación...\n')
    time.sleep(3)
    print('En fin. De desagradecidos está lleno el mundo.\n')
    time.sleep(3)
    print('¡Disfruta de tu libertad!\n')
    time.sleep(7)
    clear()
    break

quit()
