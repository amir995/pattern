a=int(input("Enter a value under [1-26]: "))
s1=a
s2=1
alpha=list("abcdefghijklmnopqursuvwxyz")

try:
        if(0<a<=26):
                for i in range(0,a):

                        print(" "*s1+(alpha[i]+" ")*s2+""*s1)
                        s1-=1
                        s2+=1
        else:
                print("Please enter a digit under [1-26]")

except:
        print("Error occured! plz try agian with valid inputs...")
