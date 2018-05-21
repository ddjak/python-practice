import numpy as np

class NearestNeighbor:
	def __init__(self):
		pass

	def train(self, X, y):
		'''X represents array of images n x d
			y is a 1-dimensional array of test images'''
		self.Xtr = X
		self.ytr = y

	def predict(self, X):
		num_test = X.shape[0]
		#make sure output type matches input type
		Ypred = np.zeros(num_test, dtype = self.ytr.dtype)
		#loop over all test rows
		for i in xrange(num_test):
			#find nearest training image in i'th test image
			#using L1 distance formula
			distances = np.sum(np.abs(self.Xtr - X[i,:]), axis = 1)
			min_index = np.argmin(distances) #get the index with smallest distance
			Ypred[i] = self.ytr[min_index] #predict the label of the nearest example

		return Ypred