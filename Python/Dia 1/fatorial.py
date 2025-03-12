valor = int(input('Digite um valor entre 2 e 15 '))
fat = 1
cont = 0
while(valor>=1):
    fat = fat * valor
    valor = valor - 1
    
print('O fatorial de ',valor,'é', fat)