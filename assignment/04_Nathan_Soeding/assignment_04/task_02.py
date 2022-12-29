def remove_long_words(s, n):
    l = s.split()
    l = [w for w in l if len(w) >= n]
    print(l)


remove_long_words("hello world! aaaa aaa aaaaa", 5)
