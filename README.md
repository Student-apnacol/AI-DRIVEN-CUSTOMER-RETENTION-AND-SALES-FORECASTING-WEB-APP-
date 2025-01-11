# Cohort Intelligence: AI-Driven Customer Retention and Sales Forecasting

## Project Overview
This project leverages advanced machine learning techniques to predict **month-on-month customer retention** and forecast **future sales trends**. By employing the **SARIMA model** for time-series forecasting and analyzing customer behavior through cohorts, this solution provides actionable insights for businesses to optimize retention strategies and revenue growth.

## Key Features
- **Customer Retention Analysis**: Tracks and predicts cohort retention patterns over time.
- **Sales Forecasting**: Accurately forecasts future sales using SARIMA for better resource planning.
- **End-to-End Deployment**: Integrated with a Flask API, enabling seamless deployment for production use.
- **Scalability**: Designed to handle large datasets and adapt to growing customer data efficiently.

## Tech Stack
- **Python Libraries**: NumPy, Pandas, Matplotlib, Seaborn, scikit-learn, statsmodels.
- **Machine Learning Model**: SARIMA (Seasonal Autoregressive Integrated Moving Average).
- **Web Framework**: Flask for API deployment.
- **Version Control**: Git and GitHub.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cohort-intelligence.git
   cd cohort-intelligence
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask API:
   ```bash
   python app.py
   ```
4. Access the API at `http://127.0.0.1:5000`.

## Data Sources
- **Customer Transactions Data**: Includes transaction dates, customer IDs, and purchase amounts.
- **Sales Data**: Time-series data of sales volumes.

## Project Workflow
1. **Data Preprocessing**:
   - Clean and transform raw data for cohort analysis and time-series modeling.
2. **Cohort Analysis**:
   - Group customers into cohorts based on their first purchase month.
   - Analyze retention trends and visualize behavior patterns.
3. **Sales Forecasting**:
   - Train SARIMA on historical sales data to predict future trends.
4. **API Deployment**:
   - Build and deploy a Flask API for model predictions and integration into business systems.

## Results and Impact
- Improved **customer retention rates** by identifying high-risk cohorts.
- Accurate **sales forecasts** with <10% error rate on test data.
- Real-time deployment ensures insights are accessible to business teams.

## Future Enhancements
- Integrate a **recommendation system** for improving customer retention.
- Experiment with **deep learning models** (e.g., LSTMs) for time-series forecasting.
- Automate **data pipeline** with tools like Apache Airflow for large-scale deployments.

## Contact
For queries, feel free to contact:
**Devansh Kaushal**  
Email: devanshkaushal2021jee@gmail.com  
LinkedIn: [https://www.linkedin.com/in/devansh-kaushal-97960728b](#)