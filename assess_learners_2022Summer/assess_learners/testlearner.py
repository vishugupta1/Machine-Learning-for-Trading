""""""  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
"""  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Test a learner.  (c) 2015 Tucker Balch  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Atlanta, Georgia 30332  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
All Rights Reserved  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Template code for CS 4646/7646  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
and other users of this template code are advised not to share it with others  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
or to make it available on publicly viewable websites including repositories  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
or edited.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
We do grant permission to share solutions privately with non-students such  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
as potential employers. However, sharing with other current or future  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT honor code violation.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
-----do not edit anything above this line---  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
"""  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
import math  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
import sys  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
import matplotlib.pyplot as plt	  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
import numpy as np  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
import LinRegLearner as lrl  
import DTLearner as dt	
import RTLearner as rtl	  	
import BagLearner as bl
import InsaneLearner as il   
#from sklearn.metrics import mean_absolute_percentage_error	

def mape(actual, pred): 
    actual, pred = np.array(actual), np.array(pred)
    return np.mean(np.abs((actual - pred) / actual)) 	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
if __name__ == "__main__":  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    if len(sys.argv) != 2:  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        print("Usage: python testlearner.py <filename>")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        sys.exit(1)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    inf = open(sys.argv[1])  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    data = np.array(  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        [list(map(str, s.strip().split(","))) for s in inf.readlines()]  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    )  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # compute how much of the data is training and testing  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    train_rows = int(0.6 * data.shape[0])  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    test_rows = data.shape[0] - train_rows  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # separate out training and testing data  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    train_x = data[:train_rows, 0:-1]  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    train_y = data[:train_rows, -1]  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    test_x = data[train_rows:, 0:-1]  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    test_y = data[train_rows:, -1]  

    train_x = train_x[1:train_x.shape[0], 1:train_x.shape[1]]		  	
    train_y = train_y[1:train_y.shape[0]]		  
    test_x = test_x[1:test_x.shape[0], 1:test_x.shape[1]]		  	
    test_y = test_y[1:test_y.shape[0]]	

    train_x = train_x.astype(float)	
    train_y = train_y.astype(float)	
    test_x = test_x.astype(float)	
    test_y = test_y.astype(float)		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"{test_x.shape}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"{test_y.shape}")  	
    # print(f"{train_x.shape}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"{train_y.shape}")  	


    # -------------------------------------------------------------------------------------------------------


    # # create a learner and train it  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # learner = dt.DTLearner(verbose=True)  # create a LinRegLearner  	

    # learner.add_evidence(train_x, train_y)  # train it  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(learner.author())  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # # evaluate in sample  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # pred_y = learner.query(train_x)  # get the predictions  	
    # rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y[0])  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print("In sample results")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"RMSE: {rmse}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # c = np.corrcoef(pred_y, y=train_y)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"corr: {c[0,1]}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # # evaluate out of sample  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # pred_y = learner.query(test_x)  # get the predictions  		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print("Out of sample results")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"RMSE: {rmse}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # c = np.corrcoef(pred_y, y=test_y)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"corr: {c[0,1]}")  

    # Experiment 1
    in_rmse = []
    out_rmse = []
    for i in range(1, 50):
        learner = dt.DTLearner(leaf_size=i, verbose=False)
        learner.add_evidence(train_x, train_y)
        predY = learner.query(train_x) # get the predictions
        rmse = math.sqrt(((train_y - predY) ** 2).sum()/train_y.shape[0])
        in_rmse.append(rmse)
        predY = learner.query(test_x) # get the predictions
        rmse = math.sqrt(((test_y - predY) ** 2).sum()/test_y.shape[0])
        out_rmse.append(rmse)
    plt.plot(range(1, 50, 1), in_rmse, label = "In-Sample")
    plt.plot(range(1, 50, 1), out_rmse, label = "Out-Sample")
    plt.xlabel("# of Leaves")
    plt.ylabel("RMSE")
    plt.title("RMSE v. # of Leaves")
    plt.grid()
    plt.xlim(0, 50)
    plt.ylim(0, .01)
    plt.legend(ncol=3, loc="lower right")
    plt.savefig('Experiment1.png')
    plt.clf()
    #plt.show()
    # -------------------------------------------------------------------------------------------------------
  		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # create a learner and train it  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # learner = rtl.RTLearner(verbose=True)  # create a LinRegLearner  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # learner.add_evidence(train_x, train_y)  # train it  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(learner.author())  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # # evaluate in sample  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # pred_y = learner.query(train_x)  # get the predictions  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print("In sample results")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"RMSE: {rmse}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # c = np.corrcoef(pred_y, y=train_y)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"corr: {c[0,1]}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # # evaluate out of sample  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # pred_y = learner.query(test_x)  # get the predictions  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print("Out of sample results")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"RMSE: {rmse}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # c = np.corrcoef(pred_y, y=test_y)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"corr: {c[0,1]}")  		 

    # Experiment 2
    in_rmse = []
    out_rmse = []
    for i in range(1, 50):
        learner = bl.BagLearner(learner = dt.DTLearner, kwargs = {"leaf_size":i}, bags = 20, boost = False, verbose = False)		
        learner.add_evidence(train_x, train_y)
        predY = learner.query(train_x)
        rmse = math.sqrt(((train_y - predY) ** 2).sum()/train_y.shape[0])
        in_rmse.append(rmse)
        predY = learner.query(test_x)
        rmse = math.sqrt(((test_y - predY) ** 2).sum()/test_y.shape[0])
        out_rmse.append(rmse)
    plt.plot(range(1, 50, 1), in_rmse, label = "In-Sample")
    plt.plot(range(1, 50, 1), out_rmse, label = "Out-Sample")
    plt.xlabel("# of Leaves")
    plt.ylabel("RMSE")
    plt.title("RMSE v. # of Leaves")
    plt.grid()
    plt.xlim(0, 50)
    plt.ylim(0.002, .01)
    plt.legend(ncol=3, loc="lower right")
    plt.savefig('Experiment2.png')
    plt.clf()
    #plt.show() 	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
   
    # -------------------------------------------------------------------------------------------------------
   
    # Experiment 3
    mape_dt = []
    mape_rt = []
    max_error_dt = []
    max_error_rt = []
    for i in range(1, 50):
        learner = dt.DTLearner(leaf_size=i, verbose=False)
        learner.add_evidence(train_x, train_y)
        predY = learner.query(train_x) 
        #mape = np.mean(np.abs((train_y - predY)/train_y))*100
        mape1 = mape(train_y,predY)
        #mape = mean_absolute_percentage_error(train_y, predY)
        mape_dt.append(mape1)
        predY = learner.query(test_x)
        temp = abs(test_y - predY)
        max_error = max(temp)
        max_error_dt.append(max_error)
    for i in range(1, 50):
        learner = rtl.RTLearner(leaf_size=i, verbose=False)
        learner.add_evidence(train_x, train_y)
        predY = learner.query(train_x) 
        mape1 = mape(train_y,predY)
        #mape = mean_absolute_percentage_error(train_y, predY)
        mape_rt.append(mape1)
        predY = learner.query(test_x)
        temp = abs(test_y - predY)
        max_error = max(temp)
        max_error_rt.append(max_error)
    plt.plot(range(1, 50, 1), mape_dt, label = "mape_dt")
    plt.plot(range(1, 50, 1), mape_rt, label = "mape_rt")
    plt.xlabel("Leaves")
    plt.ylabel("Mape")
    plt.title("Mape v. Leaves")
    plt.grid()
    plt.xlim(0, 50)
    plt.ylim(0, 10)
    plt.legend(ncol=3, loc="lower right")
    plt.savefig('Experiment3Part1.png')
    plt.clf()


    plt.plot(range(1, 50, 1), max_error_dt, label = "max_error_dt")
    plt.plot(range(1, 50, 1), max_error_rt, label = "max_error_rt")
    plt.xlabel("Leaves")
    plt.ylabel("max_error")
    plt.title("max_error v. Leaves")
    plt.grid()
    plt.xlim(0, 50)
    plt.ylim(0, .1)
    plt.legend(ncol=3, loc="lower right")
    plt.savefig('Experiment3Part2.png')
    plt.clf()



    # learner = bl.BagLearner(learner = dt.DTLearner, kwargs = {"leaf_size":1}, bags = 20, boost = False, verbose = False)		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # learner.add_evidence(train_x, train_y)  # train it  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(learner.author())  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # # evaluate in sample  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # pred_y = learner.query(train_x)  # get the predictions  	  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print("In sample results")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"RMSE: {rmse}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # c = np.corrcoef(pred_y, y=train_y)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"corr: {c[0,1]}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # # evaluate out of sample  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # pred_y = learner.query(test_x)  # get the predictions  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print("Out of sample results")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"RMSE: {rmse}")  	  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # c = np.corrcoef(pred_y, y=test_y)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"corr: {c[0,1]}")  		  	   	

    # -------------------------------------------------------------------------------------------------------

    # create a learner and train it  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # learner = il.InsaneLearner(verbose=True)		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # learner.add_evidence(train_x, train_y)  # train it  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(learner.author())  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # # evaluate in sample  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # pred_y = learner.query(train_x)  # get the predictions  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print("In sample results")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"RMSE: {rmse}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # c = np.corrcoef(pred_y, y=train_y)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"corr: {c[0,1]}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # # evaluate out of sample  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # pred_y = learner.query(test_x)  # get the predictions  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print("Out of sample results")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"RMSE: {rmse}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # c = np.corrcoef(pred_y, y=test_y)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # print(f"corr: {c[0,1]}")  		  	   	