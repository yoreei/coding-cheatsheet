from collections import deque, Counter

def solution(overstring):
    """
    Longest Substring with no repeating characters
    """
    # special case
    if len(overstring) == 0:
        return ""
    # starting index of current substring.
    currstart_i = 0

    # length of max substring
    maxlen = 0

    # starting index of max substring.
    maxstart_i = 0

    # hashmap to check positions of already visited characters
    pos = {}

    # bootstrap the process
    pos[overstring[0]] = 0

    for i in range(1, len(overstring)):

        if overstring[i] not in pos:
            pos[overstring[i]] = i

        else:
            # char already seen => check if within current substring
            if pos[overstring[i]] >= currstart_i:

                # end of current substring => reset counters and indexes
                currlen = i - currstart_i
                if maxlen < currlen:
                    maxlen = currlen
                    maxstart_i = currstart_i


                # Example:
                # ABCABC
                #    ^ if i is here
                #  ^ this is where we set currstart_i
                currstart_i = pos[overstring[i]] + 1

            # check this
            pos[overstring[i]] = i

    # check if longest substring is at the end of the overstring
    if maxlen < len(overstring) - currstart_i:
        maxlen = len(overstring) - currstart_i
        maxstart_i = currstart_i

    return overstring[maxstart_i: maxstart_i + maxlen]

# Time: O(n)
# Space: O(n)

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
    doctest.testfile('test3.txt')
