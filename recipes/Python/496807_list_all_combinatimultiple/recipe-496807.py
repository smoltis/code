a = [[1,2],[3,4,5],[6],[7,8,9,10]]

r=[[]]
for x in a:
    t = []
        for y in x:
            for i in r:
                t.append(i+[y])
    r = t

print r

-------------------------------
[[1, 3, 6, 7], [2, 3, 6, 7], [1, 4, 6, 7], [2, 4, 6, 7], [1, 5, 6, 7], [2, 5, 6, 7], [1, 3
, 6, 8], [2, 3, 6, 8], [1, 4, 6, 8], [2, 4, 6, 8], [1, 5, 6, 8], [2, 5, 6, 8], [1, 3, 6, 9
], [2, 3, 6, 9], [1, 4, 6, 9], [2, 4, 6, 9], [1, 5, 6, 9], [2, 5, 6, 9], [1, 3, 6, 10], [2
, 3, 6, 10], [1, 4, 6, 10], [2, 4, 6, 10], [1, 5, 6, 10], [2, 5, 6, 10]]