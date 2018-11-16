#generate random variable
#随机数用random
import random
#random.randint(low,high)->int [low,high]
#random.random()->[0.0,1.0]
#random.uniform(val1,val2)->float

import numpy as np
#np.random.rand(10)->[0.0,1.0)之间，有参数时返回该参数长度大小的，没有参数时返回一个数
test_data = np.random.randint(5,size=10)
print(list(test_data))