#!/usr/bin/env python
# coding: utf-8

import otomobil

def main():
    x = A()
    print x    

    c = otomobil.Otomobil()    

    i = 0
    while True:
        try:
            if i == 0:
                c.calistir()

            if i <= 5:
                c.hizlan()

            if i >= 5 and i <= 10:
                c.yavasla()
            elif i > 10:
                c.durdur()
                break

            i += 1
        except BenzinBitti:
            print '20lt benzin koyulacak.'


if __name__ == '__main__':
    main()