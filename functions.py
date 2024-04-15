def hello():
    print('python')
hello()
print(hello)


def multiple_args(*args):
    print(args)
    print(type(args))
multiple_args('one','two','three')

def multiple_named_args(**kwargs):
    print(kwargs)
    print(type(kwargs))

multiple_named_args(first='one',last='two')