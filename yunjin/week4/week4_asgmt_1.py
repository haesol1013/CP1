def palindrome(a):
    if len(a) <= 1:
        return 1
    else:
        if a[0] == a[-1]:
            return palindrome(a[1:-1])
        else:
            return 0
    
        

print(palindrome("abccba"))
            

        
                   
                   
    
