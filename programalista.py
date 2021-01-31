def a(num):
    for x in num:
        yield x
prenume=["Mihai","George","Ana","Dan","Ion","Geta","Vio"]
varsta=[14,23,15,14,12,41,39]
x1=a(prenume)
x2=a(varsta)
for i,j in zip(x1,x2):
    print(i,' are ',j,' ani')

prenume=prenume+["Andreea","Ioan"]
varsta=varsta+[34,23]
print("\n")
def a(num):
    for x in num:
        yield x
x1=a(prenume)
x2=a(varsta)
for i,j in zip(x1,x2):
    print(i,' are ',j,' ani')
del prenume[2]
del varsta[2]
print ("\n")
print (prenume[0:3])
y=prenume
prenume.reverse()
print("\n")
print(prenume)
print("\n")
print(y[2],varsta[2])
print("\n")
print(y[0:5],varsta[0:5])






