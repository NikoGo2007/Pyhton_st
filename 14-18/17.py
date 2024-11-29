def Digits(S):
    if not S:
        return 0
    if S[0].isdigit():
        return 1 + Digits(S[1:])
    else:
        return 0 + Digits(S[1:])


S = "a1bc3d45"
result = Digits(S)


print(result)
