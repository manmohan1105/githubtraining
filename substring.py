from mimetypes import init



def solve(s,k):
    cntzero=[0]*(len(s)+1)
    cntone=[0]*(len(s)+1)
    for i in range(1,len(s)+1):
        if s[i-1]=="0":
            cntzero[i]=cntzero[i-1]+1
            cntone[i]=cntone[i-1]
        if s[i-1]=="1":
            cntone[i]=1+cntone[i-1]
            cntzero[i]=cntzero[i-1]
    cntsubstr=0
    for i in range(1,len(s)+1):
        for j in range(i+1,len(s)+1):
            if (cntone[j]-cntone[i-1])%k==0 and  (cntzero[j]-cntzero[i-1])%k==0:
                print(j,i)
                cntsubstr+=1       
    return cntsubstr

    
    
    



if __name__=="__main__":
    strinput=input()
    k=int(input())
    
    cntofstr=solve(strinput,k)
    print(cntofstr)