import random
uc=['A','B','C','D','E']
lc=['e','g','h','j','k','b','u','r']
num=['1','2','3','4','5','6']
sc=['@','#','$','%']
len=8
pasword=(random.choice(uc)+random.choice(lc)+random.choice(num)+random.choice(sc)+random.choice(uc)+random.choice(lc)+random.choice(num)+random.choice(sc))
print(pasword)
