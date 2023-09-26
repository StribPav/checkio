def non_repeat(line):
    list_line = []
    lett = ''

    for idx, val in enumerate(line):
        setline = set(line[idx:])

        if len(line[idx:]) == len(setline):
            list_line.append(line[idx:])
            return max(list_line, key=len, default="")
        else:
            idx += 1
            lett = val
            for v in line[idx:]:

                if v in lett:
                    list_line.append(lett)
                    lett = ''

                lett += v

    return ''

#def non_repeat(line):
#
#    for window in range(len(line),0,-1):
#        for i in range(len(line)-window+1):
#            chunk = line[i:i+window]
#            if len(set(chunk)) == len(chunk):
#                return chunk
#
#    return ''
