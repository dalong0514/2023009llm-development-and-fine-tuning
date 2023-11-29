#-*- coding: utf-8 -*- 

import numpy as np
import time

def softmax(inMatrix):
    m, n = np.shape(inMatrix)
    outMatrix = np.mat(np.zeros((m, n)))
    soft_sum = 0
    for idx in range(0, n):
        outMatrix[0, idx] = np.exp(inMatrix[0, idx])
        soft_sum += outMatrix[0, idx]
    for idx in range(0, n):
        outMatrix[0, idx] /= soft_sum
    return outMatrix

if __name__ == '__main__':
    start_time = time.time()
    a = np.array([[1, 2, 1, 2, 3, 4, 5]])
    print(softmax(a))
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')