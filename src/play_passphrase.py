def play_pass(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_s = ''
    counter = 0
    for item in s:
        if item.lower() in alpha:
            idx = alpha.find(item)
            if idx + n < 25:
                idx += n
            else:
                idx = (idx + n) - 26
            item = alpha[idx]
            if counter % 2 == 0:
                item = item.upper()
            else:
                item = item.lower()
        else:
            try:
                item = 9 - int(item)
            except ValueError:
                item = item
        new_s += str(item)
        counter += 1
    return new_s
