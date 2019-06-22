def longestConsecutiveCharacter(string):
    # edge case
    if len(string) == 0:
        return "N/A : 0"

    max_length = 0
    longest_char = -1  # no ordinal char below 0
    curr_length = 1  # always at least 1 in length

    for i in range(len(string)-1):
        if ord(string[i+1]) == ord(string[i]):
            curr_length += 1
        else:
            if max_length < curr_length:
                max_length = curr_length
                longest_char = ord(string[i])
            curr_length = 1
    # one more time without a match since we're at the end of the string
    if max_length < curr_length:
        max_length = curr_length
        longest_char = ord(string[-1])

    return chr(longest_char) + ": " + str(max_length)


data = "ABABABAAACCCAAAA"
data2 = "Awwy363666aaaAAwBAwACAAevABaaaBBBCnnnnnCwCCCywywCCCwywyCCwy"
data3 = ""


print(longestConsecutiveCharacter(data))
print(longestConsecutiveCharacter(data2))
print(longestConsecutiveCharacter(data3))
