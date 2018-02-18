#print("hello")
def check(a):
    ln = len(a)
    pindex=0
    #print(a[::-1])
    for i in range(len(a)):
        for j in range(len(a)):
            if i<j:
                #print(a[i:j+1])
                front = a[i:j+1]
                #print(a[j:i-1:-1])
                if i+1==j or i-1<=0:
                    if len(a[j::-1]) > len(a[i:j+1]):
                        op = len(a[j::-1]) - len(a[i:j+1])
                        str = (a[j::-1])
                        #print(str[:-op])
                        back = str[:-op]
                        if front == back:
                            pindex = pindex+1
                    else:
                        back = a[j::-1]
                        if front == back:
                            pindex = pindex + 1
                        #print(a[j::-1])
                else:
                    back = a[j:i-1:-1]
                    if front == back:
                        pindex = pindex + 1
                    #print(a[j:i-1:-1])
                #print("-----")

    if pindex==0:
        print("No Palindrome is present")
    else:
        print(pindex)

check("abcbacba")