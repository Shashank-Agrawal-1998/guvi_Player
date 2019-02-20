s1, s2 = map(str, input().strip().split())
d = {}
isomorphic = True
if (len(s1)!=len(s2)):
    print('no')
else:
    for i in range(len(s1)):
        if s1[i] in d:
            if d[s1[i]]!=s2[i]:
                isomorphic = False
                break
        else:
            d[s1[i]] = s2[i]
    if isomorphic==True:
        print('yes')
    else:
        print('no')