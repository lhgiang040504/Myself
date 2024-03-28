# Assumption of Linear Refression:
## Linearity
    Linear relationship between Y and each X
## Homoscedasticity
    Equal variance
## Multicariate Normality
    Normality of error distribution
## Independence
    No autocorrelation
## Lack of Multicolliearity
    Predictor are not correlated with each other
## The Outlier Check
    This is not an assumption, but an extra

# Dummy Variables


# R - square : pearson correlation coefficient
    result = sum((y_pred - y_mean)**2) / sum((y_true - y_mean)**2)
# Standard Error of Estimate
    result = 

# Building A Model
## Throw out some features, why?
    1. Garbage in, garbage out
    2. Have to explain each exists, keep things that verry important
    3. 5 methods -> [2, 3, 4] stepwise Regression
        3.1. All-in

        3.2. Backward Elimination
            STEP1: Select a significance level to stay in the model (SL)

            STEP2: Fit the full model with all possible predictors

            STEP3: Consider the predictor with the highest P-value. If P > SL, go to STEP4, otherwise go to FIN (keep the current model)
        
            TEP4: Remove the predictor
         
            STEP5: Fit the model without this variable, go to STEP3

        3.3. Forward Selection
            STEP1: Select a significance level to enter the model (SL)

            STEP2: Fit all simplde regression model y ~ x(n). Select the one with the lowest P-vaue

            STEP3: Keep this variable and fit all possible model with one extra predictor added to the one(s) you already hae

            STEP4: Consider the predictor with the lowest P-value. If P < SL, go to STEP3, otherwise go to FIN (keep the previous model)

        3.4. Bidirectional Elimination
            STEP1: Select a significance level tp enter and to stay in the model

            STEP2: Pprm the next step of Foward Selection (new variables must have P < SLENTER to enter)

            STEP3: Perform ALL steps of Backward Elimination (old variables musst have P < SLSTAY to stay)

            STEP4: No new variable can enter and no old variables can exit -> Model is ready

        3.5. Score Comparison - All possible models not good
            STEP1: Select a criterion of goodness of fit (Akaike criterion)

            STEP2: Construct ALL Possible Regression Models 2^n -1 total combinations

            STEP3: Select the one with te best criterion

            -> Your model is ready
         
## Scaling
    In multiple Linear Regression, the coefficients will compensate to put everything to scale - no need to apply Scaling
## Do we need to check assumptions ?

        