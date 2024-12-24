## Salary Prediction Using Random Forest and Logistic Regression

The goal of this project is to predict the salary of a person based on the job description.

### Tools and Libraries Used:
- Python
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn


Thought process:
- Import dataset
- EDA to understand the dataset and its distributions:
  - Data summary: describe, info
  - Data quality assessment: 
    - Check for missing values
    - Check for duplicates
    - Check for outliers
  - Data visualization: 
    - Distribution of target variable
    - Distribution of numerical features
    - Distribution of categorical features
    - Correlation heatmap
- Data Preprocessing, Cleaning, Feature Engineering and Feature Selection:
  - Data Preprocessing:
    - One-hot encoding for categorical features (features with high cardinality)
    - Label encoding for categorical features (features with low cardinality)
    - Train-test split
  - Data Cleaning:
    - Impute missing values if any
    - Remove duplicates if any
    - Handle outliers if any
  - Feature Engineering:
    - Feature scaling (StandardScaler)
    - Feature selection (SelectKBest)
- Model Building, Training and Evaluation:
  - Model Building:
    - Logistic Regression
    - Random Forest
  - Model Training:
    - Train the model using training data
    - Predict the target variable using test data
  - Model Evaluation:
    - Accuracy
    - Precision
    - Recall
    - F1 Score
    - Confusion Matrix
    - ROC-AUC Curve
- Hyperparameter Tuning and Model Evaluation:
  - Hyperparameter Tuning:
    - GridSearchCV
  - Model Evaluation using the same metrics as above
- Conclusion

Next Steps:
- Model Deployment using Streamlit and FastAPI
- Documentation