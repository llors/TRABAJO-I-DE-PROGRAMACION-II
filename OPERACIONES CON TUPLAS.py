# 10 EJEMPLOS DE CREACION
#1
D=()
print(D)
#2
d=("PROFE",)
print(d)
#3
DIC=(1,2,3,4)
print(DIC)
#4
D=("hola","GINO")
print(D)
#5
DC="A","B","C","D"
print(DC)
#6
DS=1,2,3,4
print(DS)
#7
Q=("GINO","BANCES")
print(Q)
#8
A=("LIMA","FRUTA","CIUDAD","HERRAMIENTA")
print(A)
#9
TUPLAS=("BIENVENIDO",)
print(TUPLAS)
#10
TUPL=1,2,3,4,5,"sinpatia"
print(TUPL)

# 10 EJEMPLOS DE PERTENENCIA
#1
D=1,2,3,4,5,6,7,8,9,10
print( 2 not in D)
#2
S=("EJEMPLOS","DE","TUPLAS")
print("TUPLAS" in S)
#3
S=("camino")
print("camino" in S)
#4
DC=("EL","ES","REY")
print("REY" in DC)
#5
DA=(1,5,10,15,20)
print(3 not in DA)
#6
G="MANZANA","FRUTA","ARROZ","RICO","ACE","DETERGENTE"
print("FRUTASA" in G)
#7
SA=(6,7,8,9,)
print(6 in SA)
#8
B=()
print(1 not in B)
#9
A=("TU","COSTILLA","TE","LA","REGALO","DIOS",1)
print(2 in A)
#10
A=4,8,12,16,"doce"
print(12 in A)

# 10 EJEMPLOS DE CONCATENACION
#1
T=()
P=(18,)
S=T+P
print(S)
#2
R=(1,"GINO")
r=(2,"BANCES")
s=R+r
print(s)
#3
a=(1,2,3,4)
b=(5,6,7,8,9)
c=a+b
print(c)
#4
q=1,2,3
a=4,5,6
s=q+a
print(s)
#5
a="cuantos","anios","tienes"
b="tengo",20
p=a+b
print(p)
#6
d=(1,2,"uno","dos")
b=3,4,"tres","cuatro"
g=d+b
print(g)
#7
e="ingeniero","bances"
q="como","estas"
w=e+q
print(w)
#8
A=(1,2,3)
B=(4,5,6)
S=A+B
print(S)
#9
N=("PROFESOR",1)
S=("GUAPO",2)
R=N+S
print(R)
#10
numero=1,2
nombre="uno","dos"
resultado=numero+nombre
print(resultado)

# 10 EJEMPLOS DE COMPARACION
#1
D=1,2,3,4
D1=1,2,3,4
print(D==D1)
#2
d="hola","si","tu"
d1="hola","si","tu"
print(d==d1)
#3
A=("a","b","c")
B=("a","b")
print(A==B)
#4
S=(1,2,3,4,5,6)
Z=(1,2,3,4)
print(S>Z)
#5
Q=("A","B","C")
P=("A","B","C")
print(P>Q)
#6
Z=(10,11,12,13,14)
A=(1,3,"a","b")
print(Z>A)
#7
X="A","E","I"
Y=("uno","dos","tres","cuatro","cisnco")
print(X<Y)
#8
A=()
B=()
print(A==B)
#9
P=1
Q=1
print(P>Q)
#10
A=(1,10,2)
Z=1,2,3,4
print(A>Z)

# 10 EJEMPLOS DE INDEXACION
#1
A=1,2,3,4,5
print(A[2])
#2
D=(1,2,3,4,5,6,7,8,9)
print(D[1])
#3
S="A","B","C","D","E"
print(S[3])
#4
Z=(1,2,3,4,5,6,7,8,9,20)
print(Z[7])
#5
D=("NUMERO","SIMBOLO","A","VOCAL")
print(D[2])
#6
SD=(1,3,5,7,9)
print(SD[0])
#7
D=(1,2)
print(D[1])
#8
Z=(0,5,"CERO","CINCO")
print(Z[1])
#9
SA="NUMERO",0,6
print(SA[0])
#10
A="tu","y","yo"
print(A[1])

#10 EJEMPLOS DE CORTADO
#1
a=(1,2,3,4,5,6)
print(a[0:4])
#2
dias_de_clase=("lun","mar","mier","jue","vie","sab","dom")
print(dias_de_clase[0:5])
#3
x=(10,11,15)
print(x[1:2])
#4
n="a","b","c","d","e"
print(n[4:1:-1])
#5
m=1,2,3,4,"uno","dos","tres","cuatro"
print(m[3:1:-1])
#6
p="hola","corazon","MIO"
print(p[0:2])
#7
a="A","E","I","O","U",10,20,30
print(a[0:6])
#8
v1=(0,1,2,3)
print(v1[0:3])
#9
cinco=(1,10,2,"CORTADO",100)
print(cinco[0:3])
#10
numeros_pares=(1,2,3,4,5,6,7,8,9,10)
print(numeros_pares[1:10:2])

# 10 EJEMPLOS DE LONGITUD
#1
A=("a","b","c")
print(len(A))
#2
Z=(0,20,2)
print(len(Z))
#3
A=()
print(len(A))
#4
Q=("somos","tu","y","yo")
print(len(Q))
#5
P=(12,13,14,19,19)
Q=("LENYS","LUIS","ANGELA","SANSON","JUAN")
DCS=P+Q
print(len(DCS))
#6
X=(1,2,3,4,5)
S=len(X)
print(S)
#7
Q=("A","E","I","O","U")
print(len(Q))
#8
Z="T","E","A","M","O"
print(len(Z))
#9
Z1=1,13
Z2="H","W"
A=Z1+Z2
print(len(A))
#10
S=("contar",1,2,3)
print(len(S))

# 10 EJEMPLOS DE ITERACION
#1
Z=(1,2,3,4,5)
for k in Z:
    print(k)
#2
Q=("JORGE","LUIS","ANGELA","SANSON","JUAN")
for k in Q:
    print(k)
#3
A=1,3,5,7,9,11,13,15
for k in A:
    print(k)
#4
Z=("deveulve","los","numeros")
for k in Z:
    print(k)
#5
D="HOLA","MUNDO","BB","HHH","JJJ","LLLL"
for k in D:
    print(k)
#6
A=("como","estas")
for v in A:
    print(v)
#7
v=(1,"FERIHA",2,"APELLIDO",3,"VILMAZ")
for a in v:
    print(a)
#8
A=("planeta","tierra")
for x in A:
    print(x)
#9
q ="t","e","a","m","o"
for y in q:
    print(y)
#10
R=("QUE","ESTAS","HACIENDO")
for i in R:
    print(i)

# 10 EJEMPLOS DE BUSQUEDA
#1
A=(1,1,1,1,11,111,1111)
print(s.index(2))
#2
D=("MANZANA","FRUTA")
print(D.index("FRUTA"))
#3
N=(10,20)
print(N.index(10))
#4
S="w","x","y"
print(S.index("x"))
#5
X=("!","#","$>","F")
print(X.index("!"))
#6
Z=(1,9,3)
print(Z.index(1))
#7
CANDIDATOS=("LUIS ESPERANZA","JOSE BARATA","MARCO OCRAM")
print(CANDIDATOS.index("JOSE BARATA"))
#8
C=("H","O","L","A",1,2)
print(C.index("L"))
#9
C=("uno",1,2,3,4,5,"dos")
print(C.index("dos"))
#10
S=("HOLA","COMO","ESTAS","v","v2")
print(S.index("v2"))

#10 EJEMLOS DE CONTEO
#1
d="a","e","i","o","u","a","a"
print(d.count("a"))
#2
a=("mayo","por","siempre","mayo")
print(a.count("mayo"))
#3
b=(1,1,1,1,1,1,1,111)
print(b.count(1))
#4
x=("juana","jose","jeremias","jose")
print(x.count("jose"))
#5
n=(1,2,3,1,1,2,3,4,5,5,5)
print(n.count(5))
#6
m="t","e","l","e"
print(m.count("e"))
#7
lista="somosunidos"
print(lista.count("o"))
#8
y="a","b","a","a","c"
print(y.count("a"))
#9
nombre=("a","r","c","h","i","p","i","e","l","a","g","o")
print(nombre.count("i"))
#10
numeros=(12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12)
print(numeros.count(12))

# 10 EJEMPLOS DE MAXMIN
#1
s=1,2,3,4,14,18
print(max(s))
#2
n=10,100,10000
print(max(n))
#3
nro=(10,100,10)
print(max(nro))
#4
D=12,19,2,1,-8
print(min(D))
#5
lista=("jose","ana")
print(min(lista))
#6
biblia="DIOS","TODOPODEROSO"
print(max(biblia))
#7
t=(1,10,5)
print(min(t))
#8
n=(1,2,3,4,5,-1,-3,-6)
print(min(n))
#9
o=(-2019,2019,-2020)
print(min(o))
#10
q=(1,6,123,100,101,102,103,130)
print(max(q))

#10 EJEMPLOS DE MULTIPLICACION
#1
a=(1,2,3,4,5)
n=2
a*=n
print(a)
#2
p="TE","AMO"
M=3
p*=M
print(p)
#3
q="ooooo","eeeeeee"
r=2
q*=r
print(q)
#4
m=(1,2,3)
s=5
m*=s
print(m)
#5
o=("NUEMRO","NEUTRO",0)
l=4
o*=l
print(o)
#6
palabra=("HOLA","BEBE")
RPTE=6
palabra*=RPTE
print(palabra)
#7
I=(10)
E=("UNO",1)
I*=E
print(I)
#8
D=(20,"PROMEDIO")
s=2
D*=s
print(D)
#9
N="REPITE","FE","EN","DIOS"
M=2
N*=M
print(N)
#10
S=("SIGA","EL","CAMINO")
P=4
S*=P
print(S)

# 10 EJEMPLOS DE CLONADO
#1
XZ=(1,9,"W","K","G","J")
x=XZ[:]
print(x)
#2
X=()
Z=X[:]
print(Z)
#3
A="lista",1,"uno"
F=A[:]
print(F)
#4
CX=1,2,3,4,5
B=CX[:]
print(B)
#5
Z=("HOLA","A","TODOS")
C=Z[:]
print(C)
#6
SA="BIENVENIDO","MUCHACHOS"
D=SA[:]
print(D)
#7
XZ=(1,9,10,0,2,6,"G","g")
x=XZ[:]
print(x)
#8
I="NUMER0",12,"DNI",1234567,"NOMBRE","ALEX"
S=I[:]
print(S)
#9
XZO=("A","B","C","D")
R=XZO[:]
print(R)
#10
X=("FE","EN","DIOS")
x=X[:]
print(x)

#fin_tuplas