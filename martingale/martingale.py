""""""
"""Assess a betting strategy.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
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
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Student Name: Vishu Gupta (replace with your name)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT User ID: vgupta359 (replace with your User ID)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT ID: 903717362 (replace with your GT ID)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
"""  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
import numpy as np
import matplotlib.pyplot as plt
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
def author():  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :return: The GT username of the student  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :rtype: str  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    return "vgupta359"  # replace tb34 with your Georgia Tech username.
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
def gtid():  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :return: The GT ID of the student  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :rtype: int  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    return 903717362  # replace with your GT ID number
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
def get_spin_result(win_prob):  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param win_prob: The probability of winning  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type win_prob: float  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :return: The result of the spin.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :rtype: bool  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    result = False  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    if np.random.random() <= win_prob:  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        result = True  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    return result

def ProfessorBalch(win_prob):
    episode_winnings = 0
    count = 0
    spins = np.empty(1000, dtype=float)
    spins.fill(80)
    while episode_winnings < 80:
        won = False
        bet_amount = 1
        while not won:
            spins[count] = episode_winnings
            won = get_spin_result(win_prob)
            count += 1
            if count == 1000:
                return spins
            if won == True:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2
    return spins

def ProfessorBalchReal(win_prob):
    episode_winnings = 0
    count = 0
    spins = np.empty(1000, dtype=float)
    spins.fill(80)
    while episode_winnings < 80:
        won = False
        bet_amount = 1
        while not won:
            spins[count] = episode_winnings
            won = get_spin_result(win_prob)
            count += 1
            if count == 1000:
                return spins
            if episode_winnings <= -256:
                spins[count:1000] = -256
                return spins
            if won == True:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2
                if(bet_amount > episode_winnings+256):
                    bet_amount = episode_winnings+256;
    return spins

def caclulateProb2(arry):
    thisdict = {}
    for i in range(1000):
        index = arry[i]
        thisdict[index] = thisdict.get(index, 0) + 1
   #print(thisdict)

def caclulateProb1(arry):
    #prob = np.empty(80, dtype=float)
    thisdict = {}
    for i in range(1000):
        index = arry[i]
        thisdict[index] = thisdict.get(index, 0) + 1
    #print(thisdict)






def test_code():  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    Method to test your code  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    win_prob = 0.474  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once
    #print(get_spin_result(win_prob))  # test the roulette spin
    # add your code here to implement the experiments
    """"" Experiment 1 : Figure 1 """""
    experiments = np.empty([10,1000], dtype=float)
    #plt.subplot(1, 2, 1)
    for i in range(10):
        experiments[i] = ProfessorBalch(win_prob)
        plt.plot(range(0, 1000, 1), experiments[i], label = "Episode " + str(i+1))
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Winnings v. Spins")
    plt.grid()
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend(ncol=3, loc="lower right")
    plt.savefig('Experiment1Figure1.png')
    plt.show()

    """"" Experiment 1 : Figure 2 """""
    experiments2 = np.empty([1000, 1000], dtype=float)
    #plt.subplot(1, 2, 2)
    for i in range(1000):
        experiments2[i] = ProfessorBalch(win_prob)
    caclulateProb1(experiments2[:, -1])
    column_means = experiments2.mean(axis=0)
    standard_deviations = experiments2.std(axis=0)
    standard_deviations_plus = np.add(column_means,standard_deviations)
    standard_deviations_minus = np.subtract(column_means, standard_deviations)
    plt.plot(range(0, 1000, 1), column_means, label="Mean")
    plt.plot(range(0, 1000, 1), standard_deviations_plus, label="STD Plus")
    plt.plot(range(0, 1000, 1), standard_deviations_minus, label="STD Minus")
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Winnings v. Spins")
    plt.grid()
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend(ncol=3, loc="lower right")
    plt.savefig('Experiment1Figure2.png')
    plt.show()

    """"" Experiment 1 : Figure 3 """""
    column_medians = np.median(experiments2, axis=0)
    standard_deviations_plus_med = np.add(column_medians,standard_deviations)
    standard_deviations_minus_med = np.subtract(column_medians, standard_deviations)
    plt.plot(range(0, 1000, 1), column_medians, label="Median")
    plt.plot(range(0, 1000, 1), standard_deviations_plus_med, label="STD Plus")
    plt.plot(range(0, 1000, 1), standard_deviations_minus_med, label="STD Minus")
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Winnings v. Spins")
    plt.grid()
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend(ncol=3, loc="lower right")
    plt.savefig('Experiment1Figure3.png')
    plt.show()

    """"" Experiment 2 """""
    experiments = np.empty([10, 1000], dtype=float)
    # plt.subplot(1, 2, 1)
    for i in range(10):
        experiments[i] = ProfessorBalchReal(win_prob)
        plt.plot(range(0, 1000, 1), experiments[i], label="Episode " + str(i + 1))
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Winnings v. Spins (Real)")
    plt.grid()
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend(ncol=3, loc="lower right")
    plt.savefig('Experiment2Figure1.png')
    plt.show()
    """"" Experiment 2 : Figure 4 """""
    experiments2 = np.empty([1000, 1000], dtype=float)
    for i in range(1000):
        experiments2[i] = ProfessorBalchReal(win_prob)
    caclulateProb2(experiments2[:, -1])
    column_means = experiments2.mean(axis=0)
    standard_deviations = experiments2.std(axis=0);
    standard_deviations_plus = np.add(column_means,standard_deviations)
    standard_deviations_minus = np.subtract(column_means, standard_deviations)
    plt.plot(range(0, 1000, 1), column_means, label="Mean")
    plt.plot(range(0, 1000, 1), standard_deviations_plus, label="STD Plus")
    plt.plot(range(0, 1000, 1), standard_deviations_minus, label="STD Minus")
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Winnings v. Spins (Real)")
    plt.grid()
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend(ncol=3, loc="lower right")
    plt.savefig('Experiment2Figure2.png')
    plt.show()

    """"" Experiment 2 : Figure 5 """""
    column_medians = np.median(experiments2, axis=0)
    standard_deviations_plus_med = np.add(column_medians, standard_deviations)
    standard_deviations_minus_med = np.subtract(column_medians, standard_deviations)
    plt.plot(range(0, 1000, 1), column_medians, label="Median")
    plt.plot(range(0, 1000, 1), standard_deviations_plus_med, label="STD Plus")
    plt.plot(range(0, 1000, 1), standard_deviations_minus_med, label="STD Minus")
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Winnings v. Spins (Real)")
    plt.grid()
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend(ncol=3, loc="lower right")
    plt.savefig('Experiment2Figure3.png')
    plt.show()

if __name__ == "__main__":  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    test_code()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
