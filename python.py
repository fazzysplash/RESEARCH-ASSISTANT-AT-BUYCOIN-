# A simple python3 script  to check for Proth number

# first we Check if number is a power of two
def isPowerOfTwo(n):
    return (n and (not(n & (n - 1))))


# then we check if the number is Proth
def isProth(n):
    k = 1
    while(k < (n//k)):
        if(n % k == 0):
            if(isPowerOfTwo(n//k)):
                return True

        # update k to next odd number
        k = k + 2

    # at this point there wouldn't be a value of k being an odd number
    # and n / k is a power of 2 greater than k
    return False


# Get n from user input.
print("Enter a number")
n = int(input())


# finally Check n for Proth Number
if(isProth(n-1)):
    print(str(n) + " Is A Proth Number")
else:
    print(str(n) + " Is NOT A Proth Number")