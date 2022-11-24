import string

s = input("Give String: ").replace(" ", "").lower()

d = dict.fromkeys(string.ascii_lowercase, 0)
for c in s:
    d[c] += 1

print(d)
