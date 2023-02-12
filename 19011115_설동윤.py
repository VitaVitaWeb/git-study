file = open(".vscode\\python_VSC\\input.txt", "r", encoding='utf-8')
file2 = open(".vscode\\python_VSC\\output.txt", "w", encoding='utf-8')
strings = file.readlines()
ll=0
n = int(strings[ll])
ll+=1
# cr변수는 행과열을 나타내는 
cr = [[0]*2 for _ in range(n)]
str3 = [[0]*1 for _ in range(n)]
t=0
s=0
while n>0:
    j=0
    if t!=0:
        strings[ll]
        ll+=1
    str3[s],cr[t][j],cr[t][j+1] = strings[ll].split()
    ll+=1
    s+=1              
    cr[t][j] = int(cr[t][j])
    cr[t][j+1] = int(cr[t][j+1])
    if t !=0:
        if ( (cr[t-1][j] != cr[t][j]) or (cr[t-1][j+1] != cr[t][j+1])):
                file2.write("+계산불가")
                print("+계산불가")
                exit()
        
    pot = [[0]*1 for _ in range(cr[0][1])]
    if t ==0:     
        sum = [[0]*1 for _ in range(cr[0][1])]
    if t ==0:      
        for i in range(0,cr[0][1]):
            pot[i] = strings[ll].split()
            ll+=1
            pot[i] = list(map(int,pot[i]))
            sum[i] = pot[i]
    else:                 
        for i in range(0,cr[0][1]):
            pot[i] = strings[ll].split()
            ll+=1
            pot[i] = list(map(int,pot[i]))
            sum[i] = [x +y for x,y in zip(sum[i],pot[i])]
    t+=1
    n-=1


for i in range(cr[0][1]):
    str2 = ' '.join(str(m) for m in sum[i])
    file2.write(str2)
    file2.write("\n")
    
    
file.close()
file2.close()
