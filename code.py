def function1(a):
    """
    Function 1 doc string.
    """
    b = dict()
    for c in a:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b
      
def function2(a):
    """
    Function 2 doc string.
    """
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))
      
function2(function1('ATCTGACGCGCGCCGC'))
