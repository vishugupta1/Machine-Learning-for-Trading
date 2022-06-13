import numpy as np

class RTLearner:
    def __init__(self, leaf_size=1, verbose=False):
        self.leafsize = leaf_size
        self.tree = None

    def query(self, Xtest):
        soln = np.zeros(Xtest.shape[0])
        for i in range(Xtest.shape[0]):
            soln[i] = self.traverse_tree(Xtest[i,:])
        return soln

    def traverse_tree(self, Xtest):
        index = 0
        while(self.tree[index,0] != 'Leaf'):
            index = int(index)
            factor = int(self.tree[index,0])
            splitval = self.tree[index,1]
            left = int(self.tree[index,2])
            right = int(self.tree[index,3])
            if(float(Xtest[factor]) <= splitval):
                index = index + left
            else:
                index = index + right
        return self.tree[index][1]
    
    def build_tree(self, data):
        if data.shape[0] <= self.leafsize:
            y = np.mean(data[:,-1])
            return np.array([['Leaf', y, None, None]])
        yColumn = data[:,-1]
        if np.unique(yColumn.size == 1):
            return np.array([['Leaf', yColumn[0, -1], None, None]])
        else:
            index = int(self.calculate_random(data))
            #SplitVal = (data[np.random.randint(data.shape[0]-1),index] + data[np.random.randint(data.shape[0]-1),index])/2
            SplitVal = np.median(data[:, index])
            if SplitVal == max(data[:, index]):
                return np.array([['Leaf', np.mean(data[:, -1]), None, None]])
            lefttree = self.build_tree(data[data[:,index]<=SplitVal])
            righttree = self.build_tree(data[data[:,index]>SplitVal])
            root = np.array([[index, SplitVal, 1, lefttree.shape[0] + 1]])
            #return np.vstack([root,lefttree,righttree])
            halfTree = np.append(root, lefttree, axis=0)
            fullTree = np.append(halfTree, righttree, axis=0)
            return fullTree

    def add_evidence(self, Xtrain, Ytrain): #numpy.ndarray
        Xtrain1 = Xtrain
        Ytrain1 = np.array([Ytrain])
        Ytrain_transpose = Ytrain1.T
        data = np.append(Xtrain1, Ytrain_transpose, axis=1)
        self.tree = self.build_tree(data)

    def calculate_random(self, data):
        return np.random.randint(0, data.shape[1]-1)


    def author(self):
            return "vgupta359"


            