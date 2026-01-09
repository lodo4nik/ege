# https://education.yandex.ru/ege/inf/task/6f8036d3-2c53-45ae-bb66-9bfcc4879e93

def f(x, end):
    if x > end: return 0
    if x == end: return 1
    return f(x+3, end)+f(x*2, end)
    
print(f(3, 30)*f(30, 105))