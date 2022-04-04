inicial=int(input("Ingrese numero Inicial: "))
final=int(input("Ingrese numero final: "))
lista=[]
for i  in range (inicial,final):
     if (i%2)!=0:
         lista.append(i)

print(lista)

