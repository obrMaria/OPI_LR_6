#!/usr/bin/env python3
# -*- coding: utf -8 -*-

if __name__ == '__main__':
    s = 'ИТЕРНЕТН'
    print('данное слово:', s)
    xs = list(s)
    xs = s[0:1]+s[7]+s[1:7]
    s = ''.join(xs)
    print(f'правильное написанное слово: {s}')
