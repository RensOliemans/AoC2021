def ollie(f):
    d = {x: sum([int(y[-2]) for y in f if y[0]==x])for x in ['u','d','f']}
    return (d['d']-d['u'])*d['f']


def rikkert(f):
    return sum([{'f':0,'u':-1,'d':1}[(a:=l)[0]]*int(a[-2]) for l in f])*sum([int(a[-2]) for l in f if (a:=l)[0]=='f'])


if __name__ == '__main__':
    from _02 import measure, puzzle
    print(ollie(puzzle))

    measure(lambda: ollie(puzzle))
    measure(lambda: rikkert(puzzle))
