# 📊 Customer Churn Prediction and Survival Analysis

A Machine Learning project focused on understanding customer behavior, predicting customer churn, and analyzing customer retention using survival analysis.

## 🎯 Project Objective

Customer churn occurs when customers stop using a company's products or services. It is an important business problem because retaining existing customers is often more cost-effective than acquiring new ones.

The objective of this project is to analyze customer data, identify factors associated with churn, predict customers who may leave a service, and estimate how long customers are likely to remain active.

The project combines Exploratory Data Analysis (EDA), Machine Learning, Survival Analysis, and Explainable AI to support data-driven customer retention strategies.

## 🚀 Project Highlights

- Performed exploratory data analysis to understand customer behavior and churn patterns.
- Analyzed the relationship between customer tenure, monthly charges, service subscriptions, contract types, and churn.
- Applied survival analysis to investigate customer retention over time.
- Used the Kaplan–Meier estimator to study customer survival probabilities.
- Applied the Log-Rank Test to compare survival patterns across customer groups.
- Used the Cox Proportional Hazards model to investigate factors associated with churn risk.
- Developed a Random Forest classification model for churn prediction.
- Explored model explainability techniques to understand the factors influencing predictions.
- Investigated customer lifetime value estimation using predicted customer survival.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Survival Analysis | Kaplan–Meier Estimator, Cox Proportional Hazards |
| Statistical Testing | Log-Rank Test |
| Model Explainability | SHAP, Permutation Importance, Partial Dependence Plots |
| Web Application | Flask |
| Deployment | Configure according to the actual hosting platform |

## 🔄 Project Workflow

1. **Data Collection:** Obtain customer data containing service usage, tenure, billing, and churn information.
2. **Exploratory Data Analysis:** Identify patterns, distributions, relationships, and potential churn indicators.
3. **Survival Analysis:** Analyze customer retention over time using survival curves and statistical methods.
4. **Feature Engineering:** Prepare customer attributes for model training.
5. **Model Development:** Train a Random Forest classifier to predict customer churn.
6. **Model Evaluation:** Evaluate performance using appropriate classification metrics.
7. **Explainability:** Investigate which customer characteristics influence model predictions.
8. **Application Development:** Present predictions and relevant insights through a web interface.

## 📈 Exploratory Data Analysis

EDA helps identify customer segments that may be more likely to discontinue a service.

The analysis focuses on:

- Customer tenure and churn rate.
- Monthly charges and customer retention.
- Contract types and subscription behavior.
- Internet service types and additional services.
- Payment methods and billing preferences.
- Relationships between customer characteristics and churn.

### Key Business Questions

- Which customer groups have higher churn rates?
- Does customer tenure relate to churn?
- Are month-to-month contracts associated with greater churn?
- How do monthly charges and service subscriptions relate to customer retention?
- Which factors should a business investigate when developing retention strategies?

These relationships can help businesses identify customers who may benefit from improved support, suitable service plans, or targeted retention offers.

## ⏳ Customer Survival Analysis

Survival analysis studies the time until an event occurs. In this project, the event of interest is customer churn.

Unlike a conventional classification model, survival analysis can examine not only whether churn occurs but also how the likelihood of remaining a customer changes over time.

### 1. Kaplan–Meier Survival Curve

The Kaplan–Meier estimator calculates the probability that a customer remains active beyond a given point in time.

It helps visualize how customer retention changes as tenure increases.

### 2. Log-Rank Test

The Log-Rank Test compares survival curves between customer groups to determine whether their observed survival patterns differ statistically.

For example, it can be used to compare retention across contract types or service categories.

### 3. Cox Proportional Hazards Model

The Cox Proportional Hazards model examines the association between customer characteristics and the hazard of churn.

It helps identify customer attributes associated with higher or lower churn risk while accounting for time-to-event information.

The proportional hazards assumption should be checked before interpreting the model.

### 4. Customer Lifetime Value

Customer lifetime value (CLV) estimates the value a customer may generate over the duration of their relationship with a business.

A simplified estimate can combine expected customer lifetime with monthly revenue. A more realistic CLV calculation can also incorporate profit margins, discounting, and retention costs.

## 🤖 Customer Churn Prediction

Customer churn prediction is a supervised binary classification problem.

The target is to predict whether a customer is likely to leave a service based on relevant customer attributes.

### Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines predictions from multiple decision trees.

It can model nonlinear relationships and interactions between customer attributes, making it a useful candidate for customer churn classification.

### Model Evaluation

Model performance should be evaluated using multiple metrics:

- **Accuracy:** Overall proportion of correct predictions.
- **Precision:** Proportion of predicted churners who actually churn.
- **Recall:** Proportion of actual churners correctly identified.
- **F1-score:** Harmonic mean of precision and recall.
- **ROC-AUC:** Ability to distinguish between churn and non-churn customers.

Recall is particularly important when a business wants to identify as many potential churners as possible. However, precision also matters because contacting too many customers unnecessarily can increase retention costs.

The final model should be evaluated on unseen data, with appropriate handling of class imbalance and data leakage.

## 🔍 Explainable AI

Model explainability helps businesses understand why a model predicts that a customer may churn.

### SHAP Values

SHAP values estimate how individual features contribute to a model prediction. They can help explain why a particular customer receives a higher or lower churn prediction relative to a baseline.

### Permutation Importance

Permutation importance measures how model performance changes when the values of a feature are randomly shuffled.

### Partial Dependence Plots

Partial dependence plots help illustrate how the model's predictions change as a feature varies, averaged across the other features in the dataset.

These techniques can support model interpretation, but their results should be treated as explanations of model behavior rather than proof of causation.

## 🌐 Application and Deployment

A web application can make the model easier to use by allowing users to enter customer information and view a churn prediction.

Potential application features include:

- Customer churn probability.
- Churn-risk classification.
- Important factors influencing the prediction.
- Customer survival curve and hazard estimates.
- Estimated customer lifetime and potential lifetime value.

**Live application:** Add your verified deployment URL here.

**GitHub repository:** Add your repository URL here.

## 💡 Business Applications

This project demonstrates how data analytics and machine learning can support customer retention decisions.

Potential applications include:

- Prioritizing customers for retention campaigns.
- Identifying customer groups with higher churn risk.
- Understanding customer retention patterns over time.
- Investigating factors associated with customer churn.
- Supporting customer segmentation and retention planning.
- Providing interpretable predictions for business teams.

## 🔮 Future Improvements

- Compare multiple classification algorithms and tune their hyperparameters.
- Improve evaluation using cross-validation and a separate test set.
- Calibrate predicted churn probabilities.
- Investigate the impact of class imbalance on model performance.
- Improve the reliability of customer lifetime value estimates.
- Monitor model performance as customer behavior changes.
- Add an interactive analytics dashboard.
- Build an API to integrate predictions into other business applications.

## 👨‍💻 About Me

**Sahim Kazi**

MCA student at the University of Mumbai, with a BSc IT background and an interest in Artificial Intelligence, Machine Learning, and Data Science.

I enjoy working on practical projects involving data analysis, feature engineering, predictive modeling, and AI-powered applications.

**Areas of Interest:** Data Analytics, Machine Learning, Generative AI, and Intelligent Business Applications.
- **GitHub:** [Your GitHub Profile](https://github.com/KaziSahim)
- **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/saim-qazi-780a55415/?isSelfProfile=true)



## ⚠️ Disclaimer

This project is intended for educational and analytical purposes. Churn predictions and survival estimates are probabilistic and should support, rather than replace, business judgment. Model performance and business outcomes depend on data quality, evaluation methodology, and the context in which the model is used.
