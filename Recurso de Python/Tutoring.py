import matplotlib.pyplot as plt
import pywt

# Load image :)
original = pywt.data.camera()

#Descomposition :)
coeffs2 = pywt.dwt2(original, 'haar')

(O, (DH, DV, DD)) = coeffs2 

a=plt.subplots(num="Original")
plt.imshow(original,cmap=plt.cm.gray)

a=plt.subplots(num="Approximation")
plt.imshow(O,cmap=plt.cm.gray)

a=plt.subplots(num="Horizontal")
plt.imshow(DH,cmap=plt.cm.gray)

a=plt.subplots(num="Vertical")
plt.imshow(DV,cmap=plt.cm.gray)

a=plt.subplots(num="Diagonal")
plt.imshow(DD,cmap=plt.cm.gray)

#Reconstruction enhanced :)
esta= pywt.idwt2((O, (50*DH, DV, 50*DD)),'haar')
f=plt.subplots(num="original_2.0")
plt.imshow(esta,cmap = plt.cm.gray)
plt.show()
