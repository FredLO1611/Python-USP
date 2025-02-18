lar = int(input('digite a largura: '))
alt = int(input('digite a altura: '))
con = 0
mec = 0
rip = 1
x = 0
if lar == 2 and alt == 2:
  print('##\n##')
while con != alt-2:
  if rip == 1:
    print(lar*'#')
    rip -=1
    mec += 1
  if rip != 1:
    v = ' '*(lar-2)
    print(f'#{v}#')
    x +=1
    if x == alt-2:
      print(lar*'#')

  con +=1