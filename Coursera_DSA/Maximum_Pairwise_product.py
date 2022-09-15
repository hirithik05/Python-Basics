n = int(input())
l = list(map(int,input().strip().split()))[:n]
l.sort()
result = l[n-1]*l[n-2]
print(result)