def findValue(str: str) -> int:
    smallValue = giveSmallValues()
    upperValue = givUpperValues()

    score = 0
    for i in str:
        if i == i.upper():
            score -= upperValue[i]
        else:
            score += smallValue[i]

    return score


def giveSmallValues() -> dict:
    smallLetters = "abcdefghijklmnopqrstuvwxyz"
    smallValues: dict = {}
    i = 1
    for char in smallLetters:
        smallValues[char] = i
        i = i + 1

    return smallValues


def givUpperValues() -> dict:
    upperCaseletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upperValues: dict = {}
    i = 1
    for char in upperCaseletters:
        upperValues[char] = i
        i = i + 1

    return upperValues


# print(smallLetters)

ans = findValue("acBDb")
print(ans)
