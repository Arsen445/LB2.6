#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    school = {"1а": 8, "1б": 12, "2б": 12, "6а": 4, "7в": 19}
    print (school, "количество учащихся в разных классах")
    school['1а'] = 22
    print (school, "1 изменение")
    school['1г'] = 26
    print (school, "новый класс")
    del school["2б"]
    print (school, "класс расформирован")
    k = sum(school.values())
    print(k, "кол-во учеников")
