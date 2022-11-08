#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    s = input('text the sentence: ')

    # разделение предложения на слова
    words = s.split(' ')

    # подсчет букв в каждом слове
    m = 0
    for i in words:
        d = len(i)
        if d > m:
            m = len(i)
            word = i
    if m == 10:
        print('yes')
    else:
        print('no')

