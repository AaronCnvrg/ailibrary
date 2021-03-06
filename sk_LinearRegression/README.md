# Linear Regression

## General
In statistics, linear regression is a linear approach to modeling the relationship between a scalar response (or dependent variable) and one or more explanatory variables (or independent variables).
The case of one explanatory variable is called simple linear regression. For more than one explanatory variable, the process is called multiple linear regression.
This term is distinct from multivariate linear regression, where multiple correlated dependent variables are predicted, rather than a single scalar variable.

## Notes for this library
1) The library enables to use the algorithm both with cross validation and without. By default the library doesn't perform cross validation. If the user wishes to perform cross validation, 
the user need to use the parameter: ```--x_val=NUMBER_OF_FOLDS```, which is ```--x_val=None``` by default.
2) The path given by ```--data``` must be a path to csv file which is already processed and ready for training. Means that 
the csv must not contain: NaN values (= empty cells), strings and column names startswith 'Unnamed'.

## Parameters

### cnvrg.io params

* ```--data``` - Required param. String. Path to .csv file (the dataset). Assumes that the files includes only integers and floats (no strings), and 
the table built like: all the columns but the rightmost one are considered as features columns (X), and the rightmost one is the label column (y).

* ```--x_val``` - Integer. Number of folds for the cross-validation. Default is 5.

* ```--test_split``` - Float. The portion of the data of testing. Default is 0.2.

* ```--output_model``` - String. The name of the output file which is a trained random forests model. Default is RandomForestModel.sav

### algorithm params
```--fit_intercept``` - boolean, optional, default True. whether to calculate the intercept for this model. If set to False, no intercept will be used in calculations (e.g. data is expected to be already centered).

```--normalize``` - boolean, optional, default False. This parameter is ignored when fit_intercept is set to False. If True, the regressors X will be normalized before regression by subtracting the mean and dividing by the l2-norm. If you wish to standardize, please use sklearn.preprocessing.StandardScaler before calling fit on an estimator with normalize=False.

```--copy_X``` - boolean, optional, default True. If True, X will be copied; else, it may be overwritten.

```--n_jobs``` - int or None, optional (default=None). The number of jobs to use for the computation. This will only provide speedup for n_targets > 1 and sufficient large problems. None means 1 unless in a joblib.parallel_backend context. -1 means using all processors. See Glossary for more details.

## Link
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html



 

