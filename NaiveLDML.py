# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:04:38 2020

@author: Syed
"""

def ldm(tester):
    import pandas as pd
    # import matplotlib.pyplot as plt
    from sklearn.naive_bayes import GaussianNB
    # from sklearn.model_selection import train_test_split
    # from sklearn.metrics import accuracy_score
    
    df = pd.read_csv("ldds.csv")
    df = df.sample(frac=1).reset_index(drop=True)
    test = pd.read_csv("lddsp.csv")
    
    #X_test = test.iloc[:,2:26]
    #X_test = df.iloc[:,2:26]
    X_train = df.iloc[:,2:26]
    Y_train= df.iloc[:,26:27]
    

    
    clf_entropy = GaussianNB()
    clf_entropy.fit(X_train, Y_train) # train the tree
    
    y_predict = clf_entropy.predict(tester) #Test it
    
    y_predict = y_predict[0]    
    
    return y_predict
    #print("Accuracy is: ",accuracy_score(Y_test,y_predict)*100) #Compare it with actual results aka accuracy
    
    #svm, regression 
