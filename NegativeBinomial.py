import pandas as pd
from patsy import dmatrices
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

Address = ['i','me','mine','myself','you','yours','who','he','she','father','mother','girl','boy','they','spouse','husband','wife','dog','relative','gem','son','daughter','grand','parent','parents','school','shop','pharmasist','medical','store','hospital','office','behind','beside','above','below','near','far'] 
Opinion = ['help','suggest','tell','give','take','expect','want','gain','affect','result','fine','kicks','fuck','notice','examine','relate','heroin' ',''methadone','fentanyl','tramadol','oxycodone','hydrocodone','oxymorphone','hydromorphone','what','how','when','where','which','which','do']
Fear = ['pain', 'sleep', 'please','request','rest', 'restless', 'very', 'legal', 'law', 'suite', 'doctor', 'possible', 'impossible', 'never','death', 'tragedy', 'tragic', 'accident','accidently','die','preganancy','pregnenat']

#create a pandas DataFrame for the counts data set
data_frame = pd.read_csv('collection.csv', header=0, index_col=[0])

#adding regression variable in sequence
ds = data_frame.index.to_series()

#getting datasets to train and test
mask = np.random.rand(len(data_frame)) < 0.8
data_frame_train = data_frame[mask]
data_frame_test = data_frame[~mask]
print('Length of training dataset='+str(len(data_frame_train)))
print('Length of testing dataset='+str(len(data_frame_test)))

#Setup the regression expression in patsy notation.
#We are telling patsy that Response is our dependent variable and it depends on the regression variables: Address + Opinion + Fear
expr = """Response ~ Address + Opinion + Fear"""

#Set up the X and y matrices for the training and testing data sets
y_train, X_train = dmatrices(expr, data_frame_train, return_type='dataframe')
y_test, X_test = dmatrices(expr, data_frame_test, return_type='dataframe')

#Using the statsmodels GLM class, train the Poisson regression model on the training data set
poisson_training_results = sm.GLM(y_train, X_train, family=sm.families.Poisson()).fit()

#print out the training summary
print(poisson_training_results.summary())

#print out the fitted rate vector
print(poisson_training_results.mu)

#Add the λ vector as a new column called 'Response_lambda' to the Data Frame of the training data set
data_frame_train['Response_lambda'] = poisson_training_results.mu

#add a derived column called 'GEN' to the pandas Data Frame. This new column will store the values of the dependent variable of the OLS regression
data_frame_train['GEN'] = data_frame_train.apply(lambda x: ((x['Response'] - x['Response_lambda'])**2 - x['Response']) / x['Response_lambda'], axis=1)

#use patsy to form the model specification for the OLSR
ols_expr = """GEN ~ Response_lambda - 1"""

#Configure and fit the OLSR model
aux_olsr_results = smf.ols(ols_expr, data_frame_train).fit()

#Print the regression params
print(aux_olsr_results.params)

#train the Negative Binomial Regression model on the training data set
negative_binomial = sm.GLM(y_train, X_train,family=sm.families.NegativeBinomial(alpha=aux_olsr_results.params[0])).fit()

#print the training summary
print(negative_binomial.summary())

#predicting with the trained model
prediction = negative_binomial.get_prediction(X_test)

#Prediction results
predictions_summary_frame = prediction.summary_frame()
print(predictions_summary_frame)

#2D graph of actual responses to the predicted responses
predicted_counts=predictions_summary_frame['mean']
actual_counts = y_test['Response']
fig = plt.figure()
fig.suptitle('Predicted versus Actual Response counts')
predicted, = plt.plot(X_test.index, predicted_counts, 'go-', label='Predicted Responses')
actual, = plt.plot(X_test.index, actual_counts, 'ro-', label='Actual Responses')
plt.legend(handles=[predicted, actual])
plt.show()
