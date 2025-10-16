s=input()
letter=0
digit=0
space=0
other=0
for c in s:
    if c.isalpha():
        letter+=1
    elif c.isdigit():
        digit+=1
    elif c.isspace():
        space+=1
    else:
        other+=1
print("英文字符：{}".format(letter))
print("数字：{}".format(digit))
print("空格：{}".format(space))
print("其他字符：{}".format(other))
