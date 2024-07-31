Nom1, Nom2= 'NON DEFINI1','NON DEFINI2'
argent1, argent2=0,0

print('Bienvenue sur Freidnscount 0.1')
print('')

while True:
    print('Commands:')
    print('/recap --> Informations')
    print('/set people name --> Modifier les noms des personnes')
    print('/add money --> ajouter de l"argent')
    print('/remove money --> retirer de l"argent')
    print('')
    
    commande=(input("Command: "))
    if commande == '/recap':
        print(Nom1,'a payé',argent1)
        print(Nom2,'a payé',argent2)
        print('')
    #elif commande == '/set people number': pour plus tard

    elif commande == '/set people name':
        Nom1 = (input('people 1 name: '))
        Nom2 = (input('people 2 name: '))
        print('')
         
    elif commande == '/add money':
        moneyadd=(input('Qui: '))
        if moneyadd == Nom1:
            argent1 = argent1 + int(input('ajouter combien? : ')) 
        elif moneyadd == Nom2:
            argent2 = argent2 + int(input('ajouter combien? : ')) 
        else:
            print('ERROR : not a name')
        moneyadd=0
        print('')
            
    elif commande == '/remove money':
        moneyremove=(input('Qui: '))
        if moneyremove == Nom1:
            argent1 = argent1 - int(input('ajouter combien? : ')) 
        elif moneyremove == Nom2:
            argent2 = argent2 - int(input('ajouter combien? : ')) 
        else:
            print('Error : not a name')
        moneyremove=0
        print('')
        
    #elif commande == '/calculate':

    else:
        print('Error: not a command')
        print('')

