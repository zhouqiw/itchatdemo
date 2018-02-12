# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: numpy_torch.py
@time: 2017/10/25 下午9:16
"""

import torch
from torch.autograd import  Variable

tensor = torch.FloatTensor([[1,2],[3,4]])
variable = Variable(tensor,requires_grad = True)

# print tensor
#
# print variable


t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable*variable)

print t_out
print '*'*20
print v_out


v_out.backward()
# print variable.grad

print variable

print variable.data

print variable.data.numpy()