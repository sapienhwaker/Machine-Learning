import pandas as pd
from patsy import dmatrices
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

Address = ['i','me','mine','myself','you','yours','who','he','she','father','mother','girl','boy','they','spouse','husband','wife','dog','relative','gem','son','daughter','grand','parent','parents','school','shop','pharmasist','medical','store','hospital','office','behind','beside','above','below','near','far'] 
Opinion = ['help','suggest','tell','give','take','expect','want','gain','affect','result','fine','kicks','fuck','notice','examine','relate','heroin' ',''methadone','fentanyl','tramadol','oxycodone','hydrocodone','oxymorphone','hydromorphone','what','how','when','where','which','which','do']
Fear = ['pain', 'sleep', 'please','request','rest', 'restless', 'very', 'legal', 'law', 'suite', 'doctor', 'possible', 'impossible', 'never','death', 'tragedy', 'tragic', 'accident','accidently','die','preganancy','pregnenat']

#retrieving data frame form the collected data file
dataFrame = pd.read_csv('collection.csv', header=0, index_col=[0])

#for utilizing sequencial index
seq = dataFrame.index.to_series()

#crating mask using using random length dataframes
mask = np.random.rand(len(dataFrame)) < 0.7
dataFrame_train = dataFrame[mask]
dataFrame_test = dataFrame[~mask]
print('Length of the training dataset= '+str(len(dataFrame_train)))
print('Length of the testing dataset= '+str(len(dataFrame_test)))

#Setup the regression expression in patsy notation. We are telling patsy that Response is our dependent variable and
# it depends on the regression variables
# regression variables are the count of words related to Address, Opinion, Fear

expr = """Response ~ Address + Opinion + Fear"""

#Set up the X and y matrices
y_train, X_train = dmatrices(expr, dataFrame_train, return_type='dataframe')
y_test, X_test = dmatrices(expr, dataFrame_test, return_type='dataframe')

#Training the Poisson regression model on the training data set, using the statsmodels GLM class, 
poisson_training_results = sm.GLM(y_train, X_train, family=sm.families.Poisson()).fit()

#Print the training summary.
print(poisson_training_results.summary())

#Storing the prediction results
poisson_predictions = poisson_training_results.get_prediction(X_test)
#.summary_frame() returns a pandas DataFrame
predictions_summary_frame = poisson_predictions.summary_frame()
print(predictions_summary_frame)

predicted_counts=predictions_summary_frame['mean']
actual_counts = y_test['Response']

#Plotting graph
fig = plt.figure()
fig.suptitle('Predicted Responses vs Actual Responses')
predicted, = plt.plot(X_test.index, predicted_counts, 'go-', label='Predicted Score')
actual, = plt.plot(X_test.index, actual_counts, 'ro-', label='Actual Score')
plt.legend(handles=[predicted, actual])
plt.show()

#Show scatter plot of Actual responses versus Predicted responses
plt.clf()
fig = plt.figure()
fig.suptitle('Scatter plot of Actual Score versus Predicted Score')
plt.scatter(x=predicted_counts, y=actual_counts, marker='.')
plt.xlabel('Predicted Response Count')
plt.ylabel('Actual Response Count')
plt.show()
