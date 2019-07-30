#Anton Durham
#Date:6/12/2019
#Program Desc: This is a program designed to modify the
#value of every string's char by changing the ASCII code by adding 2 to it.

def main():
    
    i = 0
    str1 = ['a', 'b', 'c', 'd', 'e', 'f']
    while (i <= len(str1)-1):
        
        new = ord(str1[i])
        #casts each char in the string to be ASCII character
        
        newstr = chr(ord(str1[i]) + 2)
        #adds 2 to the ASCII value and changes it back to a regular char character
        print(newstr)
        i += 1
    return 0

    
main()    
