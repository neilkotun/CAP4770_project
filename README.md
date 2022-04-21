## Introduction

For our project, ‘The Group’ has elected to combine and analyze traffic stop data to see if we could accurately predict whether a warning or citation would be given.

## Hypothesis:

‘The Group’ has hypothesized that “In traffic stops, the probability of getting a warning versus a citation is associated with officer’s gender, driver’s gender, officer’s race, driver’s race, officer’s age, driver’s age, number of passengers, time of day, date”
To test our hypothesis, we performed logistic regression based on these factors to predict whether a warning or a citation would be given at traffic stops.

## Data Sets:

To feed our model, we have combined two data sets containing traffic stop data. These data sets each represented a different US region, the first being traffic stop data for Fayetteville, NC, and the second being traffic stop data for Louisville, KY. The data sets are publicly accessible data published by the Fayetteville and Louisville Police Departments. By extracting and pre-processing common features between these data sets (mentioned in our hypothesis), we were able to train our logistic regression model and draw additional insights.

## Data Pre-Processing

Unimportant data like Officer’s ID and division number, Citation number, street address and block number,location coordinates and few other features that were irrelevant to our study were filtered out.

The datasets included Driver’s and Officer’s Age range instead of their actual age. The mean of the age range was used in the regression model.

Few entries had data of few features missing and were removed from the dataset.

Dummy values were used for label encoding features like Race and Gender.

## Model Used

We used a logistic regression model (using SKlearn) for predicting whether the person will get a citation or a warning with respect to the features present in the dataset. A test-train split of 0.25 was used to divide the dataset for testing and training of the model.
 
## Evaluation of Model:

The model obtained the following scores:
Accuracy: 0.9243102907192376
Precision: 0.9260769572695824
Recall: 0.9967861043215975

The accuracy obtained was 92% but it is important to note that the dataset was highly class imbalanced. There were almost 10 times more cases where citations were issued, which could impact the results of the model on other datasets. 

## Results

Due to the high class imbalance of the data used to train the model, we are not able to conclude that the model can predict based on the given factors whether a traffic stop would result in a warning or a citation.   Data sets with a better ratio of citation vs. warning outcomes would be better for training the model to accurately predict for both cases.  Though we were not able to confirm our hypothesis through completing this experiment, insights were discovered related to traffic stop outcome and time of day, driver gender, driver race, officer gender, and officer race.

