#Anton Durham
#7/30/2019
#Desc: This program is the classic stairs of recursion problem
#solved by the fibonacci sequence's algorithm.



def main(n):
    l1 = []
    if (n == 0):
        return 1
    elif (n == 1 or n == 2 or n == 3):
        return n
    #these if and elif statements are just base cases
    #for my recursive solution
    
    else:
        return main(n-1) + main(n-2)
    
print(main(7))
