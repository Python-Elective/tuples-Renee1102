# skip_tuples allows values inside tuple to be skipped by every other one.
x = ()
def skip_tuples (x):
    x = y[::2]
    return y[::2]
y = ('I', 'am', 'a', 'test', 'tuple')
print(skip_tuples(y))