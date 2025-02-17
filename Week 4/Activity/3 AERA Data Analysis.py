# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 18:05:29 2023

@author: nicho
"""

# Import the libraries we'll need
import pandas as pd
import numpy as np

# Import data
path = r"C:\Users\nicho\OneDrive\Desktop\MDS\QMSS-GR5072-Spring2025\Week 4\Activity"
data = pd.read_csv(path + r"\4 els_extracted_data_v4.csv")
data

# Filter data
data = data[data.F3ERN2011 > 0]
data = data[data.F3ERN2011 < 200000]
data = data[data.F3C02 >= 0]
data = data[data.F3JUNEDSTAT >= 3]
data = data[data.BYS14 >= 0]
data = data[data.BYRACE >= 0]
data = data[data.BYTXCSTD >= 0]
data = data[data.F3REGION >= 0]
data = data[data.BYP61 >= -0.25]
data = data[data.BYMOTHED >= 0]
data = data[data.BYTXCSTD >= 0]
data = data[data.F3B35 >= 0]

# Explore soe of data here if you need to
data.BYTXCSTD.hist()

# look at modified data
data

# Create dummies for BYSEX
data["female"] = (data["BYS14"] == 2).astype(int)

# Check that this method is working by crosstabing the results
pd.crosstab(index=data['BYS14'], columns=data['female'])

# Now that we have verified the code above works for greating dichotomus dummy variables, 
# we can use this same method to safely create the remaining variables.

# For variables which have more than 2 categories, we can use pd.get_dummies()

# Create dummies for BYP61
data["no_parent"] = (data["BYP61"] == 1).astype(int)

# Create dummies for BYMOTHED
moth_dummies = pd.get_dummies(data["BYMOTHED"], prefix="moth_ed")
data = pd.concat([data, moth_dummies], axis=1)

# Create dummies for F3REGION
region_dummies = pd.get_dummies(data["F3REGION"], prefix="region")
data = pd.concat([data, region_dummies], axis=1)

# Create dummies for high_school_grad
data["high_school_grad"] = (data["F3EVERDO"] == 0).astype(int)

# Create dummies for F3EVRGED
data["ged"] = (data["F3EVRGED"] == 1).astype(int)

# Create dummies for BYRACE2, which uses the same coding scheme used for race/ethnicity in the paper
data["BYRACE2"] = np.where(data["BYRACE"].isin([4, 5]), 4,  
                    np.where(data["BYRACE"].isin([1,6]), 1, data["BYRACE"]))

# Check your work!
pd.crosstab(index=data['BYRACE'], columns=data['BYRACE2'])

# Once you've check your work, now make dummies
race_dummies = pd.get_dummies(data["BYRACE2"])
race_dummies # we need to use better column names so it's not confusing

race_dummies.rename(columns={1:'Other', 
                             2:'Asian',
                             3:'Black',
                             4:'Hispanic',
                             7:'White'}, inplace=True) 
race_dummies

print(pd.crosstab(index=race_dummies["Other"], columns=data['BYRACE']))
print("\n")
print(pd.crosstab(index=race_dummies["Asian"], columns=data['BYRACE']))
print("\n")
print(pd.crosstab(index=race_dummies["Black"], columns=data['BYRACE']))
print("\n")
print(pd.crosstab(index=race_dummies["Hispanic"], columns=data['BYRACE']))
print("\n")
print(pd.crosstab(index=race_dummies["White"], columns=data['BYRACE']))

# note that this produces prettier print! But it does take up more space
pd.crosstab(index=race_dummies["Asian"], columns=data['BYRACE'])


# Since the dummies are good, we need to add them to our dataset
data = pd.concat([data, race_dummies], axis=1)
data

# Recode highest education into years of education 
def post_sec_edu(value):
    if value == 4:
        return 1
    elif value == 5:
        return 2
    elif value == 6:
        return 4
    elif value == 7:
        return 5
    elif value == 8:
        return 6
    elif value == 10:
        return 8
    else:
        return 0
data['post_sec_edu'] = data['F3ATTAINMENT'].apply(post_sec_edu)
pd.crosstab(index=data["post_sec_edu"], columns=data['F3ATTAINMENT'])

# See final dataset
data

# Model 1
import statsmodels.api as sm  # library for estimating regression models

# Define the formula for the model1
formula = 'np.log(F3ERN2011) ~ ged + high_school_grad + female + Black + Hispanic + Asian + Other + BYSES1 + no_parent + BYTXCSTD'

# Fit the multilevel model using the formula
model = sm.MixedLM.from_formula(formula, data, groups=data["SCH_ID"])
result = model.fit()

# Print the summary of the model
print(result.summary())

# model 2
# Define the formula for the model 2
formula = 'np.log(F3ERN2011) ~ ged + high_school_grad + female + Black + Hispanic + Asian + Other + BYSES1 + no_parent + BYTXCSTD  + F3B35 + post_sec_edu'

# Fit the multilevel model using the formula
model = sm.MixedLM.from_formula(formula, data, groups=data["SCH_ID"])
result = model.fit()

# Print the summary of the model
print(result.summary())

# Create dummies for F3EVRGED
data["GEDT"] = (data["F3EVRGED"]*data["BYTXCSTD"]).astype(int)

# model 3
# Define the formula for the model 3
formula = 'np.log(F3ERN2011) ~ ged + high_school_grad + female + Black + Hispanic + Asian + Other + BYSES1 + no_parent + BYTXCSTD  + GEDT'

# Fit the multilevel model using the formula
model = sm.MixedLM.from_formula(formula, data, groups=data["SCH_ID"])
result = model.fit()

# Print the summary of the model
print(result.summary())