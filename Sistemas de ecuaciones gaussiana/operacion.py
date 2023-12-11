def gaussiana(matriz,vector):
    n = len(matriz)
    M = matriz

    i = 0
    for x in M:
        x.append(vector[i])
        i += 1
    print(f'El sistema de ecuaciones es: ', '\n')
    for k in range(n):
        for i in range(k,n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i],M[k]
            else:
                pass
        
        for p in M:
            print (p)
        print('\n')
        
        for j in range(k+1,n):
            q = float(M[j][k]) / M[k][k]
            for m in range(k, n+1):
                M[j][m] -=  q * M[k][m]

    x = [0 for i in range(n)]

    x[n-1] =float(M[n-1][n])/M[n-1][n-1]
    for i in range (n-1,-1,-1):
        z = 0
        for j in range(i+1,n):
            z = z  + float(M[i][j])*x[j]
        x[i] = float(M[i][n] - z)/M[i][i]
    
    print('la respuesta es: ')
    for i in range(n):
        print(f'X{i} es: {x[i]}')