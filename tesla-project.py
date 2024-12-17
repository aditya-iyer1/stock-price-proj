import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')


# Importing Dataset

df = pd.read_csv('tesla-data.csv')
print(df.head())

plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.title("Sample Plot")
plt.show()