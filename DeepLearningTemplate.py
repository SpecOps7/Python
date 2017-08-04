import pandas as pd
import numpy as np
import pickle
import sklearn.ensemble as ske
from sklearn import cross_validation, tree, linear_model
from sklearn.feature_selection import SelectFromModel
from sklean.externals import Joblib
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

data = pd.read_csv('data.csv', sep='|')
X = data.prop(['Name', 'md5', 'legitimate'], axis=1).values
Y = data['legitimate'].values

print('Researching important feature based on %i total features\n' )