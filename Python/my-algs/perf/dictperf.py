import timeit

def benchkeys():
    if 1 in d.keys():
        return d[1]
    else:
        return None
def benchhaskey():
    if 1 in d:
        return d[1]
    else:
        return None
def forgiveme():
    try:
        return d[1]
    except:
        return None
def default():
    return d.get(1, None)

d={}
for exponent in range(1, 4):
    d={}
    for newitem in range(1, 10**exponent):
        d[newitem]=newitem
    timekeys=timeit.timeit(benchkeys)
    timehaskey=timeit.timeit(benchhaskey)
    timeforgive=timeit.timeit(forgiveme)
    timedefault=timeit.timeit(default)
    print(f"{timekeys=}, {timehaskey=}, {timeforgive=}, {timedefault=}")
    assert str(type(d.keys())) == "<class 'dict_keys'>"

