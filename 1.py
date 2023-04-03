some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([v for v in some_list if some_list.count(v) > 1]))
#print(duplicates)


def my_decorator(func):
    def wrap_func():
        print('*' * 7)
        func()
        print('*' * 7)
    return wrap_func


@my_decorator
def hello():
    print('Hi, Valera')


hello()