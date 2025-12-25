#USACO BRONZE EASY PROBLEM 1 - WORD PROCESSOR

N = int(input()) #Words
K = int(input()) #Max Words

sentence = str(input())
listt = sentence.split(" ")
print(listt)
#count = 0
bob = 0
for value in listt:
    bob = bob + len(value)
    if bob <= K:
        print(value, "", end="")
    else:
        bob = len(value)
        print("\n" + value, "", end="",)