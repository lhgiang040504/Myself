# RANDOM FOREST INTUITION

## Ensemble Learning
- Taking multiple algorithms or the same algorithm multiple times
- Put them together to make something much more powerful than the original

## From scatch
- STEP1: Pick random K data points from the Training set.
- STEP2: Bulid the Decision Tree associated to these K data points.
- STEP3: Choose the number of Ntree of trees you want to bulid and repeat STEP1 and STEP2.
- STEP4: For a new data point, make each one of your Ntree trees predict the value of Y for the data point in question, and assign the new data point the average across all of the predicted Y values.

## Stable
    Because any changes in dataset could really impact on a tree but a forest of trees is much harder