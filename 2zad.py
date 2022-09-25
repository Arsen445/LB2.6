#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    slov = {1: "sid", 2: "Mani", 3: "Shiba"}
    print (slov)
    nn = {}
    for k, v in slov.items():
        nn[v] = k
    print (nn)
