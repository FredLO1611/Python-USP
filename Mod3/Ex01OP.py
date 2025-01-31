from math import sqrt
coordx1=int(input('Informe o X do primeiro ponto: '))
coordy1=int(input('Informe o y do primeiro ponto: '))
coordx2=int(input('Informe o X do segundo ponto: '))
coordy2=int(input('Informe o y do segundo ponto: '))

dist=sqrt((coordx1-coordx2)**2+(coordy1-coordy2)**2)

if dist>=10:
  print('longe')
else:
  print('perto')