#  Volum kalkulator
# made by Kristian Sundal/(Kesmon/)

pi=3.14159265359
start = '\n\nVelg mellom\n"kjegle","pyramide","tpyramide","sylinder","kule","prisme" eller "tprisme"\n"avslutt" for å avslutte'
trekant = 'Vil du ha trekant versjonen? "ja/nei"'
fase=''
print(start)
fase=input('> ')



while fase!= 'avslutt':
    if fase=='sylinder':
        print('\nLengden på radiusen')
        rad=int(input('> '))
    
        print('Høyden på sylinderen')
        hoyde=int(input('> '))

        volum = pi*rad*rad*hoyde
    
        print('\n',volum)

        print(start)
        fase=input('> ')

    elif fase=='kule':
        print('\nLengden på radiusen')
        rad= int(input('> '))

        volum=4*pi*rad*rad*rad/3

        print('\n',volum)

        print(start)
        fase=input('> ')

    elif fase=='prisme':
        print('\nLengden')
        lengden=int(input('> '))

        print('Høyden')
        hoyde=int(input('> '))

        print('Bredden')
        bredde=int(input('> '))

        volum=lengden*hoyde*bredde

        print('\n',volum)

        print(start)
        fase=input('> ')

    elif fase=='tprisme':
        print('\nGrunnlinje')
        glinja=int(input('> '))

        print('Høyden')
        hoyden=int(input('> '))

        print('Dybden')
        dybde=int(input('> '))

        volum=glinja*hoyden/2*dybde

        print('\n',volum)

        print(start)
        fase=input('> ')

    elif fase=='kjegle' :
        print('\nRadius')
        radius = int(input('> '))

        print('Høyde')
        hoyde=int(input('> '))

        volum=pi*radius*radius*hoyde/3

        print('\n', volum)

        print(start)
        fase=input('> ')

    elif fase=='tpyramide':
        print('\nGrunnlinje')
        glinja=int(input('> '))

        print('Høyden')
        hoyden=int(input('> '))

        print('Dybden')
        dybde=int(input('> '))

        volum=glinja*hoyden/2*dybde/3

        print('\n',volum)

        print(start)
        fase=input('> ')

    elif fase=='pyramide':
        print('\nLengden')
        lengden=int(input('> '))

        print('Bredden')
        bredde=int(input('> '))

        print('Høyden')
        hoyde=int(input('> '))

        volum=lengden*bredde*hoyde/3

        print('\n',volum)

        print(start)
        fase=input('> ')

    else :
        print('\n\nVelg et av alternativene')

        print(start)
        fase=input('> ')

        
