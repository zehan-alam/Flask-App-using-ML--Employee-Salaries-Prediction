## Predicting MNC's Base Salary: An End-to-End Machine Learning Project

This project leverages a general machine learning approach to predict the base salary of employees in multinational corporations (MNCs). The dataset, sourced from [Data.gov](https://catalog.data.gov/dataset/employee-salaries-2023), initially comprised 10,291 entries and 7 columns.

### Project Highlights:
- **Data Manipulation:** Performed data manipulation to handle null values and prepare the dataset for analysis.
- **Exploratory Data Analysis (EDA):** Conducted EDA to explore the distribution of base salaries and other relevant factors such as department, division, grade, and gender.
- **Statistical Analysis:** Utilized Chi-square tests to assess the dependence between categorical variables, yielding significant results.
- **Model Selection:** Employed one-hot encoding for categorical variables and standardization for numerical columns. Evaluated various regression models including RandomForestRegressor, GradientBoostingRegressor, and XGBRegressor, with XGBRegressor emerging as the optimal choice based on performance metrics (RMSE and execution time).
- **Model Tuning:** Fine-tuned the XGBRegressor model using RandomizedSearchCV to optimize performance.
- **Web Application Development:** Implemented the final model into a web application using Flask, HTML, CSS, and Bootstrap. Users can input employee details through a form and receive predicted salary estimates.

This project demonstrates a comprehensive end-to-end workflow encompassing data preprocessing, feature selection, model training, tuning, and deployment as a user-friendly web application.
