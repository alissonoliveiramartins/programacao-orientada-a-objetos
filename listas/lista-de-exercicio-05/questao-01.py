numero = int(input())
lista=[]
for i in range(1, numero+1):
 num = str(i)
 while i > 0:
   lista.append(num)
   i -= 1
 print(' '.join(map(str, lista)))
 lista=[]
