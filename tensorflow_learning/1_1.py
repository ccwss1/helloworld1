import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import models, layers

dftrain_raw = pd.read_csv("./eat_tensorflow2_in_30_days/data/titanic/train.csv")
dftest_raw = pd.read_csv("./eat_tensorflow2_in_30_days/data/titanic/test.csv")
print(dftrain_raw.head(10))
ax = dftrain_raw["Survived"].value_counts().plot(kind="bar", figsize=(12, 8), fontsize=15,rot=0)
ax.set_ylabel('Counts', fontsize=15)
ax.set_xlabel("Survived", fontsize=15)
plt.show()
bx = dftrain_raw["Age"].plot(kind="hist", bins=20,color="purple",figsize=(12,8),fontsize=15)
bx.set_ylabel("Frequency",fontsize=15)
bx.set_xlabel("Age", fontsize=15)
plt.show()
