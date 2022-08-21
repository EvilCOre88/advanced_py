from module import logger


@logger('log.txt')
def summator(*args, **kwargs):
    result = args[0]
    for i, element in enumerate(args):
        if i == 0:
            continue
        result += element
    for k in kwargs.values():
        result += k
    return result

@logger('log.txt')
def multiplier(*args, **kwargs):
    result = 1
    for element in args:
        result *= element
    for k in kwargs.values():
        result *= k
    return result

if __name__ == '__main__':
    summator(0, 8, 10, 44, a=-40, b=50, c=13.33)
    summator('a', 'b', 'c', d='d', e='e', f='f')
    multiplier(3.33, 5, a=1, b=33, c=7)