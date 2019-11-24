# 10 EJEMPLOS DE CREACION
#1
D=[]
print(D)
#2
d=["profesor","aplicado"]
print(d)
#3
LIS=list(range(1,10,2))
print(LIS)
#4
D=[152]
print(D)
#5
DC=["A","B","C","D"]
print(DC)
#6
DS=list("HOLA")
print(DS)
#7
Q=["GINO","BANCES"]
print(Q)
#8
A=["LIMA","FRUTA","CIUDAD","HERRAMIENTA"]
print(A)
#9
L=["BIENVENIDO"]
print(L)
#10
dicc=["HOLA","SALUDO","CORDIALES"]
print(dicc)

# 10 EJEMPLOS DE PERTENENCIA
#1
D=[1,2,3,4,5,6,7,8,9,10]
print( 2 in D)
#2
S=["EJEMPLOS","DE","PERTENENCIA"]
print("PERTENENCIA" in S)
#3
S=list(range(1,10))
print(1 in S)
#4
DC=["EL","ES","REY"]
print("REY" in DC)
#5
DA=[1,5,10,15,20]
print(3 not in DA)
#6
G=["MANZANA","FRUTA","ARROZ","RICO","ACE","DETERGENTE"]
print("FRUTASA" in G)
#7
SA=list(range(1,20,3))
print(6 in SA)
#8
B=[]
print(1 not in B)
#9
A=["TU","COSTILLA","TE","LA","REGALO","DIOS"]
print(2 in A)
#10
A=[4,8,12,16]
print(12 in A)

#10 EJEMPLOS DE CONCATENACION
#1
A=[1,2,3]
B=[4,5,6]
S=A+B
print(S)
#2
a=list(range(10,20))
b=list(range(20,41))
s=a+b
print(s)
#3
n=list(range(1,20,2))
m=list(range(21,40,2))
p=n+m
print(p)
#4
NOM=["PROFESOR"]
DES=["GUAPO"]
RES=NOM+DES
print(RES)
#5
X=["DIME","TU","NOMBRE"]
Y=["YO","ME","LLAMO","GINO"]
Z=X+Y
print(Z)
#6
V1=list(range(1,5))
V2=list(range(5,10))
V=V1+V2
print(V)
#7
numero=[1]
nombre=["uno"]
resultado=numero+nombre
print(resultado)
#8
TU=["QUIERES","CASARTE"]
YO=["CONMIGO"]
SOY=TU+YO
print(SOY)
#9
A=["SOMOS"]
B=["UNIDOS"]
C=A+B
print(C)
#10
EN=["TUS","MALOS","MOMENTOS"]
SOLO=["DIOS","TE","PUEDE","AYUDAR"]
PRIN=EN+SOLO
print(PRIN)

# 10 EJEMPLOS DE COMPARACION
#1
D=[1,2,3,4]
D1=[1,2,3,4]
print(D==D1)
#2
d=["hola","si","tu"]
d1=["hola","si","tu"]
print(d==d1)
#3
A=[]
B=list()
print(A>B)
#4
S=[1,2,3,4,5,6]
Z=[1,2,3,4]
print(S>Z)
#5
Q=["A","B","C"]
P=["A","B","C"]
print(P==Q)
#6
Z=[10,11,12,13,14]
A=list(range(1,3))
print(Z>A)
#7
X=["A","E","I"]
Y=["uno","dos","tres","cuatro","cisnco"]
print(X<Y)
#8
A=[]
B=[]
print(A==B)
#9
P=[]
Q=[]
print(P>Q)
#10
A=list(range(1,10,2))
Z=[1,2,3,4]
print(A>Z)

# 10 EJEMPLOS DE INDEXACION
#1
A=[1,2,3,4,5]
print(A[2])
#2
D=[1,2,3,4,5,6,7,8,9]
print(D[1])
#3
S=["A","B","C","D","E"]
print(S[3])
#4
Z=list(range(1,20))
print(Z[10])
#5
D=["NUMERO","SIMBOLO","A","VOCAL"]
print(D[2])
#6
SD=[1,3,5,7,9]
print(SD[0])
#7
D=[1,2]
print(D[1])
#8
Z=list(range(0,5))
print(Z[1])
#9
SA=list(range(0,6))
print(SA[0])
#10
A=["tu","y","yo"]
print(A[1])

#10 EJEMPLOS DE CORTADO
#1
a=[1,2,3,4,5,6]
print(a[0:4])
#2
dias_de_clase=["lun","mar","mier","jue","vie","sab","dom"]
print(dias_de_clase[0:5])
#3
x=list(range(10,15))
print(x[10:1:-1])
#4
n=["a","b","c","d","e"]
print(n[4:1:-1])
#5
m=["uno","dos","tres","cuatro"]
print(m[3:1:-2])
#6
p=["hola","corazon"]
print(p[0:2])
#7
a=list(range(1,11))
print(a[0:6])
#8
v1=[0,1,2,3]
print(v1[0:4])
#9
cinco=list(range(1,10,2))
print(cinco[2:3])
#10
numeros_pares=[1,2,3,4,5,6,7,8,9,10]
print(numeros_pares[1:10:2])

# 10 EJEMPLOS DE LONGITUD
#1
A=["a","b","c"]
print(len(A))
#2
Z=list(range(0,20,2))
print(len(Z))
#3
A=[]
print(len(A))
#4
Q=["somos","tu","y","yo"]
print(len(Q))
#5
P=[12,13,14,19,19]
Q=["LENYS","LUIS","ANGELA","SANSON","JUAN"]
DCS=P+Q
print(len(DCS))
#6
X=[1,2,3,4,5]
S=len(X)
print(S)
#7
Q=["A","E","I","O","U"]
print(len(Q))
#8
Z=["T","E","A","M","O"]
print(len(Z))
#9
Z1=list(range(1,13))
print(len(Z1))
#10
S=list(range(0,21,3))
print(len(S))

# 10 EJEMPLOS DE ITERACION
#1
Z=[1,2,3,4,5]
for k in Z:
    print(k)
#2
Q=["JORGE","LUIS","ANGELA","SANSON","JUAN"]
for k in Q:
    print(k)
#3
A=[1,3,5,7,9,11,13,15]
for k in A:
    print(k)
#4
Z=list(range(1,10,2))
for k in Z:
    print(k)
#5
D=["HOLA","MUNDO","BB","HHH","JJJ","LLLL"]
for k in D:
    print(k)
#6
A=["como","estas"]
for v in A:
    print(v)
#7
v=["FERIHA","APELLIDO","VILMAZ"]
for a in v:
    print(a)
#8
A=["planeta","tierra"]
for x in A:
    print(x)
#9
q =list(range(0,10))
for y in q:
    print(y)
#10
R=["HOLA","QUE","ESTAS","HACIENDO"]
for i in R:
    print(i)

# 10 EJEMPLOS DE BUSQUEDA
#1
A=[1,11,111,1111]
print(s.index(11))
#2
D=["MANZANA","FRUTA"]
print(D.index("MANZANA"))
#3
N=list(range(10,20))
print(N.index(12))
#4
S=["w","x","y"]
print(S.index("x"))
#5
X=["!","#","$>","F"]
print(X.index("!"))
#6
Z=list(range(1,9,3))
print(Z.index(1))
#7
CANDIDATOS=["LUIS ESPERANZA","JOSE BARATA","MARCO OCRAM"]
print(CANDIDATOS.index("JOSE BARATA"))
#8
CANDIDATOS=[1,2,3,4]
print(CANDIDATOS.index(2))
#9
C=[1,2,3,4,5]
print(C.index(2))
#10
S=["HOLA","COMO","ESTAS"]
print(S.index("HOLA"))

#10 EJEMLOS DE CONTEO
#1
d=["a","e","i","o","u","a","a"]
print(d.count("a"))
#2
a=["mayo","por","siempre","mayo"]
print(a.count("mayo"))
#3
b=list(range(1,11))
print(b.count(2))
#4
x=["juana","jose","jeremias","jose"]
print(x.count("jose"))
#5
n=[1,2,3,1,1,2,3,4,5,5,5]
print(n.count(5))
#6
m=["t","e","l","e"]
print(m.count("e"))
#7
lista=["somosunidos"]
print(lista.count("o"))
#8
y=list(range(2,10))
print(y.count(6))
#9
nombre=["a","r","c","h","i","p","i","e","l","a","g","o"]
print(nombre.count("i"))
#10
numeros=[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
print(numeros.count(12))

#10 EJEMPLOS DE MAXMIN
#1
s=[1,2,3,4,14,18]
print(max(s))
#2
n=[10,100,10000]
print(max(n))
#3
nro=list(range(10,100,10))
print(max(nro))
#4
D=[12,19,2,1,-8]
print(min(D))
#5
lista=["jose","ana"]
print(min(lista))
#6
biblia=["DIOS","TODOPODEROSO"]
print(max(biblia))
#7
t=list(range(1,10,5))
print(min(t))
#8
n=[1,2,3,4,5,-1,-3,-6]
print(min(n))
#9
o=[-2019,2019,-2020]
print(min(o))
#10
q=[100,101,102,103,130]
print(max(q))

#10 EJEMPLOS DE MULTIPLICACION
#1
a=[1,2,3,4,5]
n=2
a*=n
print(a)
#2
p=["TE","AMO"]
M=3
p*=M
print(p)
#3
q=["ooooo","eeeeeee"]
r=2
q*=r
print(q)
#4
m=[1,2,3]
s=5
m*=s
print(m)
#5
o=list(range(0,4,2))
l=4
o*=l
print(o)
#6
palabra=["HOLA"]
RPTE=6
palabra*=RPTE
print(palabra)
#7
I=10
E=["UNO"]
I*=E
print(I)
#8
D=list(range(20,30))
s=2
D*=s
print(D)
#9
N=list(range(0,10))
M=1
N*=M
print(N)
#10
S=["SIGA","EL","CAMINO"]
P=4
S*=P
print(S)

# 10 EJEMPLOS DE ELIMINACION
#1
P=[1,2,3,4,5]
del P[1:2]
print(P)
#2
Q=["A","a","E","e","I","i","O","o","U","u"]
del Q[6:10]
print(Q)
#3
b=[1,2,3,4,5,6,7,8,9]
del b[1:2]
print(b)
#4
P=["dime","tu","nombre"]
del P[0:1]
print(P)
#5
S=["HOLA",1,"MUNDO",2]
del S[1:2]
print(S)
#6
P=["ERES","Y","POR","SIEMPRE","LO","SERAS"]
del P[0:4]
print(P)
#7
p1=[1,"!"]
del p1[0:2]
print(p1)
#8
X=list(range(0,31))
del X[6:25]
print(X)
#9
X=list(range(0,10))
del X[0:2]
print(X)
#10
Y=[13,14,15,16,17,18,19,20]
del Y[0:3]
print(Y)

# 10 EJEMPLOS DE REEMPLAZO
#1
Y=[1,2,12,13,16,75]
Y[1]=20
print(Y)
#2
Z=["hola","que","bonita"]
Z[1]="estas"
print(Z)
#3
I=["A",1,"E",2,"I",3]
I[1]=10
print(I)
#4
W=list(range(1,10))
W[1]=5
print(W)
#5
SA=["a","b","c","d",1,2,3,4]
SA[7]=13
print(SA)
#6
X=[1,2,3,"hola"]
X[0]="A"
print(X)
#7
OP=[1,2,3,4]
OP[0]=9
print(OP)
#8
A=["W","Q","O","P"]
A[1]="K"
print(A)
#9
W=list(range(20,30))
W[1]=25
print(W)
#10
F=[1,"O",2,"U"]
F[1]="I"
print(F)

# 10 EJEMPLOS DE AGREGADO
#1
D=[]
A="EDUARDO"
D.append(A)
print(D)
#2
A=list()
Y="HOLA"
A.append(Y)
print(A)
#3
A=[1,2]
B="UNO Y DOS"
A.append(B)
print(A)
#4
S=list(range(0,5))
S.append(10)
print(S)
#5
W=list()
A=["HOLA","MUNDO"]
W.append(A)
print(W)
#6
SA=[]
SA.append(1)
SA.append(2)
SA.append(5)
SA.append(3)
print(SA)
#7
D=list()
D.append("a")
D.append("c")
D.append("e")
D.append("g")
D.append("i")
print(D)
#8
X=[1,2,3,4,5,6]
X.append(7)
X.append(100)
print(X)
#9
SA=list(range(1,10))
SA.append(3)
SA.append("W")
SA.append("#")
SA.append(11)
print(SA)
#10
O=[]
O.append("GINO")
print(O)

# 10 EJEMPLOS DE ANULACION
#1
A=[]
A.clear()
print(A)
#2
D=[12,13,14]
del D[1:2]
print(D)
#3
D1=[1,2,3,4,5]
del D1[1:3]
print(D1)
#4
A1=[1,2,3,4,5]
del A1[2:3]
print(A1)
#5
SA=["tu","y","yo"]
del SA[1:2]
print(SA)
#6
Z=["lun","mar","mie","jue","vie"]
del Z[1:4]
print(Z)
#7
XZ=["ESTARE","SIEMPRE","CONTIGO"]
del XZ[1:2]
print(XZ)
#8
A=[1,10,100,2,20,200]
del A[1:3]
print(A)
#9
C=["AA","HOLA","BB","AYUDA","CC","ESTOY ACA"]
del C[1:4]
print(C)
#10
Z=list(range(20,30))
Z.clear()
print(Z)

# 10 EJEMPLOS DE CLONADO
#1
XZ=[1,9,"W","K","G","J"]
x=XZ.copy()
print(x)
#2
X=[]
Z=X.copy()
print(Z)
#3
A=["lista"]
F=A.copy()
print(F)
#4
CX=[1,2,3,4,5]
B=CX.copy()
print(B)
#5
Z=["HOLA","A","TODOS"]
C=Z.copy()
print(C)
#6
SA=list("BIENVENIDO")
D=SA.copy()
print(D)
#7
XZ=[1,9,10,0,2,6,"G","g"]
x=XZ.copy()
print(x)
#8
I=["NUMER0",12,"DNI",1234567,"NOMBRE","ALEX"]
S=I.copy()
print(S)
#9
XZO=list("preguntastepormi")
R=XZO.copy()
print(R)
#10
X=["FE","EN","DIOS"]
x=X.copy()
print(x)

#10 EJEMPLOS EXTENSION
#1
A=["QUIEN"]
B=["ERES"]
A.extend(B)
print(A)
#2
D=["EL","AlUMNO"]
N=list("GINO")
D.extend(N)
print(D)
#3
E=["CUENTAME","LOS","NUMEROS"]
I=list(range(1,10))
E.extend(I)
print(E)
#4
t=list(range(1,5))
p=list(range(5,10))
t.extend(p)
print(t)
#5
X=["la","clase","de","hoy","sera"]
Y=list("listas")
X.extend(Y)
print(X)
#6
W=[10,"DIEZ",11,"ONCE"]
T=["EL","QUE","SIGUE","ES"]
W.extend(T)
print(W)
#7
valor=["tu","mirada"]
val=["dice","todo"]
valor.extend(val)
print(valor)
#8
t=["frutas","manzana","naranja"]
p=["platano","fresa"]
t.extend(p)
print(t)
#9
f=["NOMBRE","Y","APELLIDO1"]
g=["GINO","BANCES"]
f.extend(g)
print(f)
#10
h=["dos","mas","tres"]
u=["igual","cinco"]
h.extend(u)
print(h)

# 10 EJEMPLOS DE INSERCION
#1
X=[1,9,"W","K","G","J"]
X.insert(2,1)
print(X)
#2
A=["HOLA","MUNDO"]
A.insert(2,"GENIO")
print(A)
#3
B=list("AEIOU")
B.insert(0,"VOCALES")
print(B)
#4
S=["QUIERO"]
S.insert(0,"TE")
print(S)
#5
SA=list(range(1,10,2))
SA.insert(6,"numeros inpares")
print(SA)
#6
XZ=[]
XZ.insert(0,20)
print(XZ)
#7
AD=["SIEMPRE","ESPERANZA"]
AD.insert(2,"HAY")
print(AD)
#8
X1=["I","N","O"]
X1.insert(0,"G")
print(X1)
#9
S=["te","lo","confieso"]
S.insert(3,"te amo")
print(S)
#10
ZX=["A",1,"E",2,"I",3,"O",4]
ZX.insert(8,"U")
ZX.insert(9,5)
print(ZX)

# 10 EJEMPLOS DE EXTRACCION
#1
A=[1,2,3,4,5]
Z=A.pop(1)
print(Z)
#2
S=["YO","SOY","EL","QUE","SOY"]
ZZ=S.pop(1)
print(ZZ)
#3
SA=list(range(1,10))
S=SA.pop(3)
print(S)
#4
CX=["A","E","I","O","U","W"]
C=CX.pop(1)
print(C)
#5
WA=["dime","que","si"]
V=WA.pop(2)
print(V)
#6
D=["A",1,"B",2,"C",8]
SA=D.pop(5)
print(SA)
#7
D1=["A","J"]
S=D1.pop(1)
print(S)
#8
S=list("HOLA")
DS=S.pop(0)
print(DS)
#9
CX=["A","E","I","O","U","W"]
X=CX.pop(4)
print(X)
#10
X=["TE","DIGO","AMOR"]
A=X.pop(2)
print(A)

#10 EJEMPLOS DE SEPARACION
#1
D1=["A","J"]
D1.remove("A")
print(D1)
#2
A=["SOLO","VIVE","LA","VIDA"]
A.remove("SOLO")
print(A)
#3
B=["hermosura","pasajera"]
B.remove("pasajera")
print(B)
#4
C=[1,2,3,4,5,6,7,8]
C.remove(8)
print(C)
#5
D=["ELEMINA","PECADO"]
D.remove("PECADO")
print(D)
#6
E=list(range(1,10))
E.remove(5)
print(E)
#7
F=["a","avion","u","unia","i"]
F.remove("i")
print(F)
#8
G=["UNO",1,"DOS",2,"TRES",3]
G.remove("TRES")
G.remove(3)
print(G)
#9
q=["lista","nombres","varones"]
q.remove("varones")
print(q)
#10
d=["nombre","GINO","BANCES","VALDERA"]
d.remove("nombre")
print(d)

#10 EJEMPLOS DE REVERSA
#1
A=[1,2,3,4,5,6,7,8,9]
x=A.reverse()
print(A)
#2
B=["JUANITA","LAVA","ROPA"]
Y=B.reverse()
print(B)
#3
C=list("anitalavalatina")
e=C.reverse()
print(C)
#4
n=list(range(10,20,2))
s=n.reverse()
print(n)
#5
v1=list(range(100,200,10))
v=v1.reverse()
print(v1)
#6
q=[9,8,7,6,5,4,3,2,1]
r=q.reverse()
print(q)
#7
notas=["DO","RE","MI","FA","SOL","LA","SI"]
s1=notas.reverse()
print(notas)
#8
pje=[10,11,12,1,3]
si=pje.reverse()
print(pje)
#9
p1=["YO","SOY"]
P=p1.reverse()
print(p1)
#10
nbre=["ANA","ROSA","JUAN","LEO"]
A=nbre.reverse()
print(nbre)
# 10 EJEMPLOS DE ORDENADO
#1
A=[1,3,5,2,7,9,8,4]
A.sort()
print(A)
#2
B=[10,2,40,21,14]
B.sort()
print(B)
#3
C=["B","D","A","C"]
C.sort()
print(C)
#4
D=list(range(1,5))
D.sort()
print(D)
#5
E=[12,1234,1,2020]
E.sort()
print(E)
#6
F=["E","O","A","U","I"]
F.sort()
print(F)
#7
G=["g1","g12","g123"]
G.sort()
print(G)
#8
H=[-1,-4,-8,22,12]
H.sort()
print(H)
#9
I=[]
I.sort()
print(I)
#10
J=list("unidos")
J.sort()
print(J)

#FIN_LISTAS