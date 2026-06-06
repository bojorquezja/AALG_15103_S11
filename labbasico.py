def imprime(mat):
    for fil in mat:
        print(fil)
    print()

def sollab(lab, res):
    pass


lab = [
    [1,0,0,0],
    [1,1,1,1],
    [0,1,0,0],
    [1,1,1,1]
]
res = [[0 for _ in range(4)] for _ in range(4)]

if sollab(lab, res):
    print("Salio del lab")
else:
    print("No hay aslida")