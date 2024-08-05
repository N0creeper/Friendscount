Nom1, Nom2= 'NON DEFINI1','NON DEFINI2'
argent1, argent2=0,0
np=None

print('Bienvenue sur Freidnscount 0.1')
print('')

while (np == None):
    test=(input('Combien etes vous? '))
    np = int(test) if test.isnumeric() else None

if np == 2:
    Nom1, Nom2= 'NON DEFINI1','NON DEFINI2'
    argent1, argent2=0,0
if np == 3:
    Nom1, Nom2, Nom3= 'NON DEFINI1','NON DEFINI2','NON DEFINI3'
    argent1, argent2, argent3=0,0,0
if np == 4:
    Nom1, Nom2, Nom3, Nom4= 'NON DEFINI1','NON DEFINI2','NON DEFINI3', 'NON DEFINI4'
    argent1, argent2, argent3, argent4=0,0,0,0
if np == 5:
    Nom1, Nom2, Nom3, Nom4, Nom5= 'NON DEFINI1','NON DEFINI2','NON DEFINI3', 'NON DEFINI4','NON DEFINI5'
    argent1, argent2, argent3, argent4, argent5=0,0,0,0,0
if np == 6:
    Nom1, Nom2, Nom3, Nom4, Nom5, Nom6= 'NON DEFINI1','NON DEFINI2','NON DEFINI3', 'NON DEFINI4','NON DEFINI5','NON DEFINI6'
    argent1, argent2, argent3, argent4, argent5, argent6=0,0,0,0,0,0
if np == 7:
    Nom1, Nom2, Nom3, Nom4, Nom5, Nom6, Nom7= 'NON DEFINI1','NON DEFINI2','NON DEFINI3', 'NON DEFINI4','NON DEFINI5','NON DEFINI6','NON DEFINI7'
    argent1, argent2, argent3, argent4, argent5, argent6, argent7=0,0,0,0,0,0,0
if np == 8:
    Nom1, Nom2, Nom3, Nom4, Nom5, Nom6, Nom7, Nom8= 'NON DEFINI1','NON DEFINI2','NON DEFINI3', 'NON DEFINI4','NON DEFINI5','NON DEFINI6','NON DEFINI7','NON DEFINI8'
    argent1, argent2, argent3, argent4, argent5, argent6, argent7, argent8=0,0,0,0,0,0,0,0


while True:
    print('Commands:')
    print('/recap --> Informations')
    print('/set --> Modifier les noms des personnes')
    print('/add --> ajouter de l"argent')
    print('/remove --> retirer de l"argent')
    print('')


    commande=(input("Command: "))
    if commande == '/recap':
        print(Nom1,'a payé',argent1)
        print(Nom2,'a payé',argent2)
        print('')
    #elif commande == '/set people number': pour plus tard

    elif commande == '/set':
        Nom1 = (input('people 1 name: '))
        Nom2 = (input('people 2 name: '))
        print('')
         
    elif commande == '/add':
        moneyadd=(input('Qui: '))
        if moneyadd == Nom1:
            argent1 = argent1 + int(input('ajouter combien? : ')) 
        elif moneyadd == Nom2:
            argent2 = argent2 + int(input('ajouter combien? : ')) 
        else:
            print('ERROR : not a name')
        moneyadd=0
        print('')
            
    elif commande == '/remove':
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

