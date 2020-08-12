n=int(input("Enter number of elements "))
arr=[]
print("Enter elements :")
for i in range(0,n):
    z=int(input())
    arr.append(z)

k=int(input("Enter the value of k:"))

arr.sort()
start=0
end=n-1
print(arr)
dict={}
while(start<end):
    if((arr[start]+arr[end])==k):
        print(arr[start],arr[end])
        start=start+1
        end=end-1
    elif ((arr[start]+arr[end])<k):
        start=start+1
    elif ((arr[start]+arr[end])>k):
        end=end-1


    
    