Nom1, Nom2= 'NON DEFINI1','NON DEFINI2'
argent1, argent2=0,0

print('Bienvenue sur tricount express pour 2 personnes')
while True:
    print('Commands:\/recap --> Informations\/set people name --> Modifier les noms des personnes\/add money --> ajouter de l"argent ')
    commande=(input("Command: "))
    if commande == '/recap':
        print(Nom1,'a payé',argent1)
        print(Nom2,'a payé',argent2)
    #elif commande == '/set people number': pour plus tard

    elif commande == '/set people name':
        Nom1 = (input('people 1 name: '))
        Nom2 = (input('people 2 name: '))
        
    elif commande == '/add money':
        moneyadd=(input('Qui: '))
        if moneyadd == Nom1:
            argent1 = argent1 + int(input('ajouter combien? : ')) 
        elif moneyadd == Nom2:
            argent2 = argent2 + int(input('ajouter combien? : ')) 
        else:
            print('ERROR : not a name')
        moneyadd=0
            
    elif commande == '/remove money':
        moneyremove=(input('Qui: '))
        if moneyremove == Nom1:
            argent1 = argent1 - int(input('ajouter combien? : ')) 
        elif moneyremove == Nom2:
            argent2 = argent2 - int(input('ajouter combien? : ')) 
        else:
            print('ERROR : not a name')
        moneyremove=0

    #elif commande == '/calculate':

    else:
        print('not a command')