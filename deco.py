# decorator / logger
import logging
import time
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def uppercase_decorator(function):
    def wrapper():
        
        func = function()
        logging.info('So should this: ' + function.__name__)
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

@uppercase_decorator
def abc():
    return 'waga'

# print(say_hi())
# print(say_hi())
# print(abc())

# generator
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

genn = csv_reader('addresses.csv')
# print(next(genn))
# print(next(genn))
# print(next(genn))


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen_seq=infinite_sequence()
# print(next(gen_seq))
# print(next(gen_seq))
# print(next(gen_seq))
# print(next(gen_seq))
# print(next(gen_seq))
# print(next(gen_seq))

def infinite_counter(start=1,end=4):
    num = start
    while True:
        yield num
        num += 1
        if (num > end):num = start

gen_cnt=infinite_counter(6,9)

# print(next(gen_cnt))
# print(next(gen_cnt))
# print(next(gen_cnt))
# print(next(gen_cnt))
# print(next(gen_cnt))
# print(next(gen_cnt))
# print(next(gen_cnt))
for i in range(2,10):
    time.sleep(.5)
    print(next(gen_cnt))