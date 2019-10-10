#Anton Durham

#4/11/2019

def subs(m):
    if m == []:
        return [[]]
        #if the set is empty, return an empty set
    x = subs(m[1:])
    #This line(9) recursively call the subs function with l[1:]
    #m[1:] means to start through the list, starting a 1.
    return x + [[m[0]] + y for y in x]
    #1. returns the individual last items in the list e.g. (4), then (5)
    #and after returns each possible pair for the last item, (4,5)
    #Sequence looks like this: 5,4, (4,5),3,(3,5),(3,4),(3,4,5), (2), (2,5)
    
def createlist(int n):
list = []
	for i in range(1, n+1):
        list.append(i)
	print(subs(list))
        #for loop simply creates the list of numbers we want to find subsets for
        #by appending each i up to n with a list.
def main():
    
    num = input("Enter your n ")  
    n = int(num)
    print("There are ", pow(2,n), " possible combinations of the set ")
    print(list)
   
  
          
main()
