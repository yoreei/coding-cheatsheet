import codecs
from collections import Counter


def solution_q3(Wcounter, Wlen, Tline):
    r"""
    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile1.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    4

    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile2.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    0

    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile3.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    0

    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile4.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    1

    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile5.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    1

    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile6.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    2

    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile7.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    3

    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile8.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    3

    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile9.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    3

    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile10.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    0

    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile11.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    4200

    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile12.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    100

    >>> filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile13.txt"
    >>> Wcounter, Tcounter = read_input(filename)
    >>> solution_q3(Wcounter, Tcounter)
    4

    """

    if Tline < Wlen:
        return 0

    occurances = 0
    start = 0
    end = Wlen -1
    while end < len(Tline) - 1:
        curCounter = Counter(Tline[start:end])
        if curCounter == Wcounter:
            occurances += 1
        start +=1
        end += 1

    # prodaljenie...


    return occurances


def read_input(filename=None):
    if filename is None:
        filename = input()

    # filename = r"D:\git\coding-test\my-algs\mnknowledge\unicodefile.txt"
    with codecs.open(filename, encoding='utf-8') as file_content:
        Wline = next(file_content)
        Tline = next(file_content, None)
    if Tline is None:
        Tline = ""

    Wcounter = Counter(Wline)  # len >= 1
    # Tcounter = Counter(Tline)  # len >= 0

    # remove endline characters
    del Wcounter["\r"], Wcounter["\n"]# , Tcounter["\r"], Tcounter["n"]

    # print(f"{Wline=}")
    # print(f"{Tline=}")
    # print(f"{Wcounter=}")
    # print(f"{Tcounter=}")
    return Wcounter, len(Wcounter), Tline


if __name__ == '__main__':
    # uncomment to run tests
    #import doctest
    # doctest.testmod(verbose=True)
    # test args with:
    # python q3.py "D:\git\coding-test\my-algs\mnknowledge\unicodefile14.txt"

    # test input with:
    # D:\git\coding-test\my-algs\mnknowledge\unicodefile14.txt

    # handle argc and argv arguments
    import sys

    if len(sys.argv) >= 2:
        Wcounter, Tcounter = read_input(sys.argv[1])
    else:
        Wcounter, Wlen, Tline = read_input()
    print(solution_q3(Wcounter, Wlen, Tline))
