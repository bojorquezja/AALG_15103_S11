lab = [
  [1, 1, 1, 0, 1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0, 1, 0, 0, 0],
  [1, 1, 0, 1, 1, 1, 1, 0, 1],
  [0, 1, 0, 1, 0, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 1, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 1, 0, 1, 1, 0, 1],
  [1, 0, 0, 1, 0, 1, 0, 0, 1],
  [1, 1, 1, 1, 0, 1, 1, 1, 1]
]



def imprime(mat):
  for fil in mat:
    print(fil)
  print()



def valido(lab, res, f, c):
  if f < 0 or f >= len(lab):
    return False
  if c < 0 or c >= len(lab[0]):
    return False
  if lab[f][c] == 0:
    return False
  if res[f][c] == 1:
    return False
  return True



def sollab(lab, res, f, c):
  if not valido(lab, res, f, c):
    return False
  
  res[f][c] = 1
  imprime(res)

  if f == len(lab) - 1 and c == len(lab[0]) - 1:
    return True

  for df, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
    if sollab(lab, res, f + df, c + dc):
      return True

  res[f][c] = 0
  return False



filas = len(lab)
cols = len(lab[0])

res = [[0] * cols for _ in range(filas)]

if sollab(lab, res, 0, 0):
  print("Salió del laberinto")
else:
  print("No hay salida")