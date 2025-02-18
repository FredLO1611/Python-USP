def maximo (x, y, z):
  if x > y and x > z:
    return x
  elif y > x and y > z:
    return y
  elif z > x and z > y:
    return z

a = 13
b = 43
c = 33

maximo(a, b, c)
