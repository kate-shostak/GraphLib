def longest_palindrome (s):
    palindroms = set()
    for i in xrange(len(s)):
        for j in xrange(i,len(s)):
            pal = s[i:j + 1]
            if pal == pal[::-1]:
                palindroms.add(len(pal))
    print max(palindroms)


longest_palindrome("baablkj12345432133d")