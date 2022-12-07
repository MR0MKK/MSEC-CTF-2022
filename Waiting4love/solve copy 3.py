# def kt(a):
#     while(len(str(hex(a)))>10):
#         shit=str(hex(a))[2]
#         if(shit=="a"): 
#             shit=10
#         if(shit=="b"): 
#             shit=11
#         if(shit=="c"): 
#             shit=12
#         if(shit=="d"): 
#             shit=13
#         if(shit=="e"): 
#             shit=14
#         if(shit=="f"): 
#             shit=15    
#         a=a-int(shit)*4294967296 #16^8 la xoa ki tu bi tran   
#     return a


arr=[13, 19, 5, 3, 59, 242, 243, 35, 53, 210, 51, 113, 80,46, 159, 113, 51, 159, 134, 20, 84, 20, 51, 84, 113,3, 159, 232, 37, 8, 37, 127, 61]
arr2 = [0,1,2]
flag=[0]*33
def sushi(a):   
    ans=0
    arr1 = [0,1,2]
    for i in range(3,a+1):
	    ans = ((100*arr1[i-1])+(123*arr1[i-2]))+2*arr1[i-3]
	    arr1.append(ans)
    return str(chr(arr1[a]&0xff))
for i in range(0,33):
    flag[i]=sushi(arr[i])
key="".join(flag)
print(key)


# (a-1) (a-2) duoc luu vao ecx
# return luu vao eax
# v2 duoc luu trong ebx
# v3 duoc luu trong ebx
# gia tri luu vao thanh ghi se duoc them ham kt() de khi tràn thanh ghi sẽ xóa kí tự tràn

shit=0
arr1 = [0,1,2]
for i in range(3,14):
	ans = ((100*arr1[i-1])+(123*arr1[i-2]))+2*arr1[i-3]
	arr1.append(ans)
print(arr1)









# def func1(a):
#     if(a==0 or a==1 or a==2 ):
#         return a 
#     v2=(123*(func1(a-2)))
#     v3=(100*(func1(a-1))+v2 ) 
#     return v3+2*func1(a-3) 