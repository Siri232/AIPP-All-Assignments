def linear_search(a,v):
    for i,x in enumerate(a):
        if x==v:return i
    return -1

if __name__=="__main__":
    data=list(map(int,input("Enter numbers: ").split()))
    target=int(input("Value to find: "))
    idx=linear_search(data,target)
    print("Index:" if idx!=-1 else "Not found",idx if idx!=-1 else "")

