import random
art = ['the', 'a']
noun = ['cat', 'dog', 'man', 'woman']
verb = ['sang', 'run', 'jumped']
adv = ['loudly', 'quietly','well', 'badly']
for i in range(5):
    seq = random.randint(1,2)
    if seq == 1:
        print(random.choice(art),random.choice(noun),random.choice(verb),random.choice(adv))
    else:
        print(random.choice(art),random.choice(noun),random.choice(verb))
