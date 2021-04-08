import string
import random
plen=int(input("Enter the password length\n"))
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
# print(s)
# print("\n")
random.shuffle(s)  # for shuffling the list
print("Your Password is:")
print("".join(s[0:plen]))
# print("".join(random.sample(s,plen)))   # you can use this method to get the password