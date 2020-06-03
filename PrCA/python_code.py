import numpy as np
from numpy.linalg import eig

class PrCA:
    '''takes data as an argument and returns the principal components and transformed data'''
    
    
    def __init__(self, data):

                    
        self.data = data 
        self.centered_data = ()

    def center(self):

        """Function to center the data set.

        Args: 
            None

        Returns: 
            float: mean of the data set

"""

        self.centered_data = self.data - np.mean(self.data, axis = 0)
        return self.centered_data
    
    def corr_mat(self):
        return(self.centered_data.dot(self.centered_data.transpose()))
    
    def components(self):
        return(eig(self.corr_mat()))

data = np.array([[1,2],[3,4]])

ex = PrCA(data)
print(ex.center())
print(ex.data)
print(ex.corr_mat())
print(ex.components())



