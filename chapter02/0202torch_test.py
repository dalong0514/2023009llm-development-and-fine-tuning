#-*- coding: utf-8 -*- 

import time
import torch

def torch_test():
    result = torch.tensor(1.0) + torch.tensor(2.0)
    print(result)

if __name__ == '__main__':
    start_time = time.time()
    torch_test()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')