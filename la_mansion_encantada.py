import sys
import time

while True:
    print("""
                       " L A   M A N S I Ó N    E N C A N T A D A "


                   *         .              *            _.---._
                                 ___   .            ___.'       '.   *
            .              _____[LLL]______________[LLL]_____     \\
                          /     [LLL]              [LLL]     \     |
                         /____________________________________\    |    .
                          )==================================(    /
         .      *         '|I .-. I .-. I .--. I .-. I .-. I|'  .'
                      *    |I |+| I |+| I |. | I |+| I |+| I|-'`       *
                           |I_|+|_I_|+|_I_|__|_I_|+|_I_|+|_I|      .
                  .       /_I_____I_____I______I_____I_____I_\\
                           )================================(   *
           *         _     |I .-. I .-. I .--. I .-. I .-. I|          *
                    |u|  __|I |+| I |+| I |<>| I |+| I |+| I|    _         .
               __   |u|_|uu|I |+| I |+| I |~ | I |+| I |+| I| _ |U|     _
           .  |uu|__|u|u|u,|I_|+|_I_|+|_I_|__|_I_|+|_I_|+|_I||n|| |____|u|
              |uu|uu|_,.-' /I_____I_____I______I_____I_____I\`'-. |uu u|u|__
              |uu.-'`      #############(______)#############    `'-. u|u|uu|
             _.'`              ~"^"~   (________)   ~"^"^~           `'-.|uu|
          ,''          .'    _                             _ `'-.        `'-.
      ~"^"~    _,'~"^"~    _( )_                         _( )_   `'-.        ~"^"~
          _  .'            |___|                         |___|      ~"^"~     _
        _( )_              |_|_|          () ()          |_|_|              _( )_
        |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
        |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|
        |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
        |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/[===]\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|
        |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
        |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|
        |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
    ~""~|_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_lc|~""~
       [_____]            [_____]                       [_____]            [_____]
    \n\n""")

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
                break

        if choice1.lower() == 'salir':
            print('\n"Venga, vamos a ver qué hay por ahí..."\n')
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
        print('''            .                                                      .
                .n                   .                 .                  n.
          .   .dP                  dP                   9b                 9b.    .
         4    qXb         .       dX                     Xb       .        dXp     t
        dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
        9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
         9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
          `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
            `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
                ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                                )b.  .dbo.dP'`v'`9b.odb.  .dX(
                              ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                             dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                            dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                            9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                             `'      9XXXXXX(   )XXXXXXP      `'
                                      XXXX X.`v'.X XXXX
                                      XP^X'`b   d'`X^XX
                                      X. 9  `   '  P )X
                                      `b  `       '  d'
                                       `             ' \n''')
        time.sleep(4)
        print('"Hasta luego Lucas..."\n')
        time.sleep(1.75)
        print('Un demonio horrible proveniente del inframundo se ha hecho palillos de dientes con tus huesos.')
        time.sleep(3)
        print('\n"¡MÁS SUERTE LA PRÓXIMA VEZ!"\n')
        time.sleep(5)
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
        print('''
     ____________________
    /                    \\
    |     En caso de     |
    |     frustración    |
    \____________________/
             !  !
             !  !
             L_ !
            / _)!
           / /__L
     _____/ (____)
            (____)
     _____  (____)
          \_(____)
             !  !
             !  !
             \__/

        ''')
    time.sleep(3)

    choice3 = input('Más o menos a la mitad del pasillo hay otra puerta a la derecha. Entrar, '
                    '¿Sí o No?\n')

    if choice3.lower() == ('si' or 'sí'):
        print('''
                                                             |
                                                __________   |
                               _    __    _    |          |  |
                              /_\  /  \  /_\   |          |  |
                              =|= | // | =|=   |          |  |
                               !   \__/   !    |          |  |
                                     _         |          |  |
     ___               ___          //'        |          |  |
    [___]       _   :=|   |=:   __T_||_T__     |p=        |  |
    |  ~|     =)_)=   |   |    [__________]    |          |  |
    |   |      (_(    |xXx|     \_      _/     |          |  |
    |   |      )_)    """""       \    /       |          |  |
    \___|                          |  |        |          |  |
     |  `========,                 |  |        |          |  |
    __`.        .'_________________|  |________|__________lc_|
        `.    .'                  (____)                      \\
        _|    |_...             .;;;;;;;;.                     \\
       (________);;;;          :;;;;;;;;;;:
            :::::::'            '::::::::'
        ''')
        time.sleep(3)
        print('"Madre mía, qué puto asco."\n')
        time.sleep(2)
        print('"Está todo lleno de sangre y huele a cadáver 4 meses descomponiéndose"')
        time.sleep(2)
        print('"Mejor no correr la cortina de la bañera..."')
        time.sleep(2)
        print('"Voy a volver al pasillo y a seguir investigando."\n')
        time.sleep(10)

    elif choice3.lower() == 'no':
        pass

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
    print('''
                                         _,-----------._        
                                     _,-'_,-----------._`-._   
                                  ,'_,-'  ___________  `-._`.
                                ,','  _,-'___________`-._  `.`.
                               ,','  ,'_,-'     .     `-._`.  `.`.
                              /,'  ,','        >|<        `.`.  `.\\\\
                             //  ,','      ><  ,^.  ><      `.`.  \\\\
                            //  /,'      ><   / | \   ><      `.\  \\\\
                           //  //      ><    \/\^/\/    ><      \  \\\\
                          ;;  ;;              `---'              ::  ::
                          ||  ||              (____              ||  ||
                         _||__||_            ,'----.            _||__||_
                        (o.____.o)____        `---'        ____(o.____.o)
                          |    | /,--.)                   (,--.\ |    |
                          |    |((  -`___               ___`   ))|    |
                          |    | \\,'',  `.           .'  .``.// |    |
                          |    |  // (___,'.         .'.___) \\  |    |
                         /|    | ;;))  ____) .     . (____  ((\\ |    |\\
                         \|.__ | ||/ .'.--.\/       `/,--.`. \;: | __,|;
                          |`-,`;.| :/ /,'  `)-'   `-('  `.\ \: |.;',-'|
                          |   `..  ' / \__.'         `.__/ \ `  ,.'   |
                          |    |,\  /,                     ,\  /,|    |
                          |    ||: : )          .          ( : :||    |
                         /|    |:; |/  .      ./|\,      ,  \| :;|    |\\
                         \|.__ |/  :  ,/-    <--:-->    ,\.  ;  \| __,|;
                          |`-.``:   `'/-.     '\|/`     ,-\`;   ;'',-'|
                          |   `..   ,' `'       '       `  `.   ,.'   |
                          |    ||  :                         :  ||    |
                          |    ||  |                         |  ||    |
                          |    ||  |                         |  ||    |
                          |    |'  |            _            |  `|    |
                          |    |   |          '|))           |   |    |
                          ;____:   `._        `'           _,'   ;____:
                         {______}     \___________________/     {______}
                         |______|_______________________________|______|
        ''')
    time.sleep(5)
    print('¿¡Es esa la puerta principal!?\n')
    choice4 = input('¿Quieres salir? ¿Sí o No?\n')

    while True:
        if choice4.lower() == 'no':
            print('\n¿¡En serio te vas a quedar aquí!?', end=" ")
            time.sleep(2)
            choice4 = input('A ver, sales, ¿¡no!? ¿Sí o No?\n')
            while True:
                if choice4.lower() == 'no':
                    print('\n¿¡En serio te vas a quedar aquí!?', end=" ")
                    time.sleep(3)
                    choice4 = input('Va, vamos a centrarnos. Quieres salir, ¿verdad?,'
                                    ' ¿Sí o No?\n')
                    if choice4 == ('si' or 'sí'):
                        break
                    if choice4 == 'no':
                        continue
                elif choice4.lower() == ('si' or 'sí'):
                    break
            if choice4.lower() == ('si' or 'sí'):
                print('\nGracias a Dios. Ya estás fuera. Enhorabuena.\n')
                break

        if choice4.lower() == ('si' or 'sí'):
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
    break
sys.exit('FIN')
