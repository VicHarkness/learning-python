import random

norolls=0
nosides=0

norolls=int(input("How many dice rolls?"))
nosides=int(input("How many sides?"))

print("Rolling a %dd%d" %(norolls, nosides))

for x in range(1,norolls):
    print(random.randint(1,nosides))
    

