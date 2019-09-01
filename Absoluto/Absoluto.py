#!/usr/bin/env python
# coding: utf-8

def abs(numero):
    return numero * -1 if numero < 0 else numero
def main():
    print(abs(-4)) # 4
    print(abs(0)) # 0
    print(abs(-9)) # 9


if __name__ == '__main__':
    main()

