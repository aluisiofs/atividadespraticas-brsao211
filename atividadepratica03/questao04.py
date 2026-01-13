'''
Um ano é bissexto se for divisível por 4, exceto anos centenários 
(divisíveis por 100) que não são divisíveis por 400.

'''

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("Bissexto")
        else:
            print("Não é bissexto")

    else:
        print("Bissexto")
else:
    print("Não é bissexto")