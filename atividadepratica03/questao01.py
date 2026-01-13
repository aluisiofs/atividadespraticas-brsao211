'''
*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).

'''

idade = int(input("Digite a idade: "))
'''
if idade < 0:
    print("Idade inválida")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
   print("Idoso")
'''

#            V
#      F           V
if idade < 0 or idade > 150:
    print("Idade inválida")
elif idade > 0 and idade <= 12:
    print("Criança")
elif idade > 12 and idade <= 17:
    print("Adolescente")
elif idade > 17 and idade <= 59:
    print("Adulto")
else:
   print("Idoso")



