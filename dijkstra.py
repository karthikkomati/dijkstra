import numpy
import math
import math1058_cwk
import time

def dijkstra1(successors, s):

    S = []
    S.append(s)
    n = len(successors)
    L = dict()
    L[s] = 0
    P = dict()
    P[s] = '-'
    while(len(S)<n):

        length= numpy.inf
        no = -1
        p = -1
        for i in S:
            for j,k in successors[i].items():
                if j not in S and (L[i] + k) < length:
                    length = L[i] + k
                    no = j
                    p = i
        if n is not -1:
            S.append(no)
            L[no] = length
            #print("node:",no)
            #print("p: " ,p)
            P[no] = p
            


    
    return L,P


def dijkstra2(successors, s):

    S = []
    S.append(s)
    n = len(successors)
    L = dict()
    L[s] = 0
    P = dict()
    P[s] = '-'
    Ver = [v for v in range(len(successors))]
    for i in set(Ver)-set([s]):
        if i not in successors[s]:
            L[i] = numpy.inf
            P[i] = s
        for i,k in successors[s].items():
            L[i] = L[s] + k
            P[i] = s
    while(len(S)<n):
        l = numpy.inf
        m = '-'
        for n in set(Ver) - set(S):
            if L[n] < l:
                l = L[n]
                m = n
        S.append(m)
        for i,l2 in successors[m].items():
            if i not in S:
                if L[m] + l2 < L[i]:
                    L[i] = L[m] + l2
                    P[i] = m
            

  

    return L,P


if __name__ == "__main__":
    adj1 = [{1 : 2, 2 : 5},
            {2 : 3},
            {3 : 4},
            {0 : 21, 1 : 8}]

    for o in range(0, 4):
        print(o) 
        print(dijkstra1(adj1, o))
        print(dijkstra2(adj1, o))


