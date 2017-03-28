def play_pass(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_s = ''
    for item in s:
        if item.lower() in alpha:
            idx = alpha.find(item)
            if idx + n < 25:
                idx += n
            else:
                idx = (idx + n) - 26
            item = alpha[idx]
            new_s += item
        else:
            try:
                item = 9 - int(item)
                new_s += str(item)
            except ValueError:
                new_s += item
    return new_s
