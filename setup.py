from setuptools import setup, find_packages

setup(
    name="Month_on_Month_Cohort_Analysis",
    version="1.0.0",
    author="Devansh Kaushal",
    author_email="devanshkaushal2021jee@gmail.com",
    description="A Python package for month-on-month cohort retention analysis and sales forecasting using SARIMA.",
    packages=find_packages(),
    install_requires=[
        "Flask==3.0.3",
        "pandas==2.0.3",
        "numpy==1.24.3",
        "scikit-learn==1.3.2",
        "statsmodels==0.14.1", 
        "pmdarima==2.0.4",
        "matplotlib==3.7.5",
        "seaborn==0.13.2",
        "xgboost==2.1.2",
        "joblib==1.4.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
