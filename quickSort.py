def quickSort(S):
    import random as r
    if len(S) <= 1:
        return S
    else:
        pivot = r.choice(S) #randomly chosen element in list
        leftside = [] #all values less than pivot
        rightside = [] #all values greater than pivot
        for s in S:
            if s < pivot:
                leftside.append(s)
            elif pivot < s:
                rightside.append(s)
                
        S1 = quickSort(leftside) #sort sublist
        S2 = quickSort(rightside) #sort sublist
        return S1 + [pivot] + S2 #return concatination of lists
    
### test for quickSort ###
import random as r
alist = r.sample(range(1,500),50)
print (alist, len(alist))
a = quickSort(alist)
print (a, len (a))
