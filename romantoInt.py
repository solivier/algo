def romanToInt(s: str) -> int:
    res = 0
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(s)):
        if i + 1 < len(s) and conv[s[i + 1]] > conv[s[i]]:
            res -= conv[s[i]]
            continue
        res += conv[s[i]]
    return res


print(romanToInt('IV'))
