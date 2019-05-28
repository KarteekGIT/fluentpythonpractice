'''
Created on May 28, 2019

@author: AA
'''
from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlsize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlsize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlsize.register(numbers.Integral)
def __(n):
    return '<pre>{0} (0x{0:X})</pre>'.format(n)

@htmlsize.register(tuple)
@htmlsize.register(abc.MutableSequence)
def ___(seq):
    inner = '</li>\n<li>'.join(htmlsize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'

if __name__ == '__main__':
    print(htmlsize({1,2,3}))
    print(htmlsize(abs))
    print(htmlsize('Helmlich & co.\n- a game'))
    print(htmlsize(42))
    print(htmlsize(['alpha', 61, {3,2,1}]))
    