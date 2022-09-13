n = int(input())
l = list(map(int,input().strip().split()))[:n]
new_list = [*set(l)]
new_list.sort()
if(len(new_list) >= 2):
    print(new_list[-2])
else:
    print(new_list[0])