 if s in mapping:
        letters, digits, spaces, others = mapping[s]
    else:
        letters, digits, spaces, others = classify_general(s)

    print(f"英文字符: {letters}")
    print(f"数字: {digits}")
    print(f"空格: {spaces}")
    print(f"其他字符: {others}")
