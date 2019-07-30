#Anton Durham
#Date:6/30/19
#Desc: This program is designed to take any 4-digit number and
#arrange its' digits in descending/ascending order. Once
#this is complete my program will subtract the difference between the two numbers,
#then evaluate the result. If the result is 6174, we have found the number known
#as Kaprekar's constant. The program will return the # of iterations it took to find
#Kaprekar's constant as well. 


def converttoint(num1): 
      
    # Converting integer list to string list 
    s = [str(i) for i in num1] 
    # Join list items using join() 
    res = int("".join(s)) 

    return(res) 
def math(num, count):
    count = count+1 
    if(num!=6174):
        
        main(num, count)
    else:
        count = count + 1
        print("Count:", count)
        print(num)
    #if else chain to determine if we need to continue iterating through numbers to get the
    #constant 6174
def main(num, count):

    minv = []
    maxv = []
    b = str(num)
    c = []
    
    for digit in b:
         c.append (int(digit))
         #converts int to list
    
    minv = c
    maxv = c
    minv = sorted(c,key=int)
    #Sorts the list from descending to ascending
    maxv.sort(reverse=True)
    #sorts the list from ascending to descending
    newmin = converttoint(minv)
    #Calls the converttoint function to get the actual numbers
    newmax = converttoint(maxv)
    
    print(newmax-newmin)

    math(newmax-newmin, count)
    #Sends the math function the result of difference between max/minimum number and the iterations we've gone through to
    #find kaprekar's constant
    
main(3524,-1)

