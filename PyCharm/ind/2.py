#!/usr/bin/env puthon3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    # введите слово
    s = input('введите слово: ')
    if len(s) >= 5:
        s2 = s
        s2 = s.replace(s[4], s[1])
        s = s.replace(s[1], s[4])
        s = s[:4]+s2[4:]
        print(s)
    else:
        print(
            "буквосочетание должно состоять больше чем из 5 букв",
            file=sys.stderr
        )
        exit(1)
