#Anton Durham
#8/10/2019
#Desc: Function to subtract from a list 4 given integers
def cutting_grass(a, b, c, d,e):
    l1 = []
    l2 = []
    l1.append(b)
    l1.append(c)
    l1.append(d)
    l1.append(e)
    
    for i in range(len(a)):
        print(l2)
        for j in range(len(l1)):
            l1.append(a[j] - l1[j])
            if(l1[j] == 0):
                print(l2)
                return(l2,"Done")
        
        




cutting_grass([3, 4, 4, 4], 1, 1, 1, 1)
