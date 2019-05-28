'''
Created on May 28, 2019

@author: AA
'''
import html

def htmlsize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

if __name__ == '__main__':
    print(htmlsize({1,2,3}))
    print(htmlsize(abs))
    print(htmlsize('Helmlich & co.\n- a game'))
    print(htmlsize(42))
    print(htmlsize(['alpha', 61, {3,2,1}]))
    