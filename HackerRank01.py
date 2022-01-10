# python missing characters
def missingCharacters(s):

    normalstr = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in normalstr:
        if i not in s:
            res += i
    return res


b = "jyhfdAJGD13134WAF"
a = missingCharacters("jyhfdAJGD13134WAF")
print(a)
