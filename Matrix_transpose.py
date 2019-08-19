#Anton Durham
#6/15/2019
#Desc: Function to transpose a given matrix

def transpose_matrix():
        a = [[1,2],[3,4],[5,6]]
        for row in a:
            print(row)
            res = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
            print("\n")
            for row in res:
                print(row)



transpose_matrix()
