#  Volum kalkulator
# made by Kristian Sundal /(Kesmon/)

pi=3.14159265359
fase=''
print('Velg mellom "sylinder","kule","prisme" eller "tprisme"')
print('"avslutt" for å avslutte')
fase=input('> ')



while fase!= 'avslutt':
    if fase=='sylinder':
        print('\nLengden på radiusen')
        rad=int(input('> '))
    
        print('Høyden på sylinderen')
        hoyde=int(input('> '))

        volum = pi*rad*rad*hoyde
    
        print('\n',volum)

        print('\n\nVelg mellom "sylinder","kule","prisme" eller "tprisme"')
        print('"avslutt" for å avslutte')
        fase=input('> ')

    elif fase=='kule':
        print('\nLengden på radiusen')
        rad= int(input('> '))

        volum=4*pi*rad*rad*rad/3

        print('\n',volum)

        print('\n\nVelg mellom "sylinder","kule","prisme" eller "tprisme"')
        print('"avslutt" for å avslutte')
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

        print('\n\nVelg mellom "sylinder","kule","prisme" eller "tprisme"')
        print('"avslutt" for å avslutte')
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

        print('\n\nVelg mellom "sylinder","kule","prisme" eller "tprisme"')
        print('"avslutt" for å avslutte')
        fase=input('> ')

    else :
        print('Velg et av alternativene')

        print('\n\nVelg mellom "sylinder","kule","prisme" eller "tprisme"')
        print('"avslutt" for å avslutte')
        fase=input('> ')

        
