import numpy as np
a = np.array([1,2,3,4,5])
print(a)
print(a.dtype)
a = np.array([1,2,3,4,5],dtype=np.float64)
print(a)
print(a.ndim, a.shape, a.size)
b = np.array([[1,2,3,4,5],[6,7,8,9,10]],dtype=np.float64)
print(b)
print(b.dtype)
print(b.ndim, b.shape, b.size)
print(np.zeros((3,3),'d'))
print(np.empty((4,4),'d'))
print(np.linspace(0,10,5))
print(np.arange(0,10,2))
print(np.random.standard_normal((2,4)))
a = np.random.standard_normal((2,3))
b = np.random.standard_normal((2,3))
np.vstack([a,b])
np.hstack([a,b])
a.transpose()
np.save('example.npy',a)
a1 = np.load('example.npy')
print("HI")
print(a1)
