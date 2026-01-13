## 🎓 Student Performance Indicator

### 📌 Project Overview
This project predicts student's Math scores based on demographic and academic factors using Machine Learning.
It also identifies academically at-risk students, enabling early interventions by educators.

### The system includes:

* Exploratory Data Analysis (EDA)                                                                                                                 
* End-to-end ML pipeline                                                                                                                          
* Web application using Flask                                                                                                                     

### 🎯 Problem Statement

Student academic performance is influenced by multiple factors such as gender, parental education, lunch type, and preparation courses.
Early prediction of poor performance helps schools provide timely academic support.

### 🚀 Solution Approach

- Analyze student data using EDA                                                                                                                  
- Train regression models to predict Math scores                                                                                                  
- Deploy a Flask web app for real-time predictions
                                                                                               
### 🧠 Use Cases

* Identify Struggling Students – Early prediction of students who may perform poorly in Math                                                      
* Tailored Interventions – Helps teachers provide focused support to at-risk students                                                             
* Data-Driven Decisions – Enables schools to improve curriculum planning                                                                          
* Performance Insights – Helps educators understand key factors affecting performance                                                              
### 📊 Exploratory Data Analysis (EDA)

* EDA was performed to:
* Understand data distribution
* Detect missing values and outliers
* Analyze relationships between features and Math scores
* Identify important predictors influencing performance

### Key EDA Insights:

* Student's Performance is related with lunch, race, parental level education.
* Females lead in pass percentage and also are top-scorers.
* Student's Performance is not much related with test preparation course.
* Finishing preparation course is benefitial.

### 🧩 Features Used

Gender                                                                                                                                            
Race/Ethnicity                                                                                                                                    
Parental Level of Education                                                                                                                       
Lunch Type                                                                                                                                        
Test Preparation Course                                                                                                                           
Reading Score                                                                                                                                     
Writing Score                                                                                                                                     

### ⚙️ Machine Learning Pipeline

* Data Ingestion
* Data Transformation (Encoding & Scaling)
* Model Training
* Model Evaluation
* Model Serialization
* Prediction Pipeline

### 🤖 Models Used

Multiple regression models were trained and evaluated:                                                                                            
Linear Regression                                                                                                                                 
Lasso Regression                                                                                                                                  
Ridge Regression                                                                                                                                  
Decision Tree Regressor                                                                                                                           
Random Forest Regressor                                                                                                                           
XGBoost Regressor                                                                                                                                 
CatBoost Regressor                                                                                                                                
AdaBoost Regressor                                                                                                                                

The best-performing model was selected based on R² score.

### 🌐 Web Application

Built using Flask
Takes student inputs through a web form
Predicts Math score in real time

### 🛠️ Tech Stack

Python 3.8                                                                                                                                        
Flask                                                                                                                                             
scikit-learn                                                                                                                                      
pandas                                                                                                                                            
NumPy                                                                                                                                             
Matplotlib & Seaborn

### ▶️ How to Run Locally
#### 1️⃣ Clone Repository :
git clone https://github.com/your-username/student-exam-performance.git                                                                                                                           
cd student-exam-performance

#### 2️⃣ Create Virtual Environment :                                                                                                             
conda create -p venv python==3.8 -y                                                                                                               
conda active venv/                                                                                                                                

#### 3️⃣ Install Dependencies
pip install -r requirements.txt

#### 4️⃣ Run Application
python app.py


### Open browser at:
http://127.0.0.1:5000

### 📈 Results

+ Accurate Math score predictions
+ Identified key performance-driving factors
+ End-to-end ML lifecycle implemented successfully

