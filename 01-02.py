# -*-coding: utf-8 -*-

'''
打印1-num之间的数，递归打印，到998可以，999失败
'''

def printN(num):
    if (num):
        printN(num - 1)
        print(num)
    return

if __name__ == '__main__':
    #num = raw_input('请输入数字：');
    printN(998)
