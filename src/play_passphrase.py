def play_pass(s, n):
    # alpha = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
    #          8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o',
    #          15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'w',
    #          22: 'x', 23: 'y', 24: 'z'}
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
        elif item != ' ' and int(item):
            item = 9 - int(item)
            new_s += str(item)
        else:
            new_s += ' '
    return new_s
