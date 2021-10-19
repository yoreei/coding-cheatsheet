def test():
    cross=[
"++++++-+++",
"++------++",
"++++++-+++",
"++++++-+++",
"+++------+",
"++++++-+-+",
"++++++-+-+",
"++++++++-+",
"++++++++-+",
"++++++++-+",
]
    words = "ICELAND;MEXICO;PANAMA;ALMATY"
    print(crosswordPuzzle(cross, words))

    cross=[
"++++++++++",
"+------+++",
"+++-++++++",
"+++-++++++",
"+++-----++",
"+++-++-+++",
"++++++-+++",
"++++++-+++",
"++++++-+++",
"++++++++++",
]
    words = "POLAND;LHASA;SPAIN;INDIA"
    answer="""\
++++++++++
+POLAND+++
+++H++++++
+++A++++++
+++SPAIN++
+++A++N+++
++++++D+++
++++++I+++
++++++A+++
++++++++++
"""
    print(crosswordPuzzle(cross, words))

class Place():
    def __init__(self,hor,ver, length):
        self.hor=hor
        self.ver=ver
        self.length=length
        self.string=''
        self.crosses=[]
        self.where=[]
    def crosses(self, other, where):
        self.crosses.append(other)
        self.where.append(where)
    def __repr__(self):
        return str(self.__dict__)

def find_places(crossword):
    places=[]
    for horidx, hor in enumerate(crossword):
        inword=False
        length=0
        for veridx, ver in enumerate(hor):
            if ver=='-':
                inword=True
                length+=1
            else:
                if inword and length > 1:
                    places.append(Place(horidx, ver, length))
                inword=False
                length=0

    

    return places

def solution(crossword, words):
    places=find_places(crossword)
    print(places)

def crosswordPuzzle(crossword, wordsstr):
    return solution(crossword, wordsstr.split(';'))


if __name__=='__main__':
    test()