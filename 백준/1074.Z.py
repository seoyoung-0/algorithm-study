def zet(n,r,c):
    if n==0:
        return 0
    half = 2**(n-1)
    
    if(r < half and c < half):
        return zet(n-1,r,c)
    if (r < half and c >= half):
        return half*half + zet(n-1,r, c-half)
    if(r >=half and c < half):
        return 2*half*half + zet(n-1,r-half,c)
    if (r >= half and c >= half):
        return 3*half*half + zet(n-1, r-half, c-half)

N, r, c = map(int,input().split())
print(zet(N,r,c))