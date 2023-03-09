# nyc-fare-and-demand-forecasting

Welcome to my Yellow Taxi Trip Records Predictive Modeling project! In this project, I have developed a scalable and efficient data science pipeline to predict fare prices and demand patterns of yellow taxis based on the trip records.

The data is available in the Apache Parquet format and contains fields capturing pick-up and drop-off dates/times, locations, trip distances, fares, rate types, payment types, and passenger counts. The dataset is of 30GB, making it a big data challenge to analyze and model.

To tackle this challenge, I have employed scalable Big Data technologies, including GCS, Dataproc, PySpark, and SparkML. GCS is used as a cloud storage solution for the dataset, while Dataproc is used as a managed Apache Spark and Apache Hadoop service to enable distributed processing of the data. PySpark is used to write Spark applications in Python, and SparkML is used to build and train machine learning models at scale.

The data science pipeline consists of several stages, including data ingestion, data preprocessing, feature engineering, model training, model evaluation, and model deployment. During data preprocessing, I have cleaned the data, removed outliers, and imputed missing values. Feature engineering involved creating new features from the existing ones to improve the model's predictive power. I have used regression models such as linear regression, random forest regression, and gradient-boosted tree regression to train the models.

Finally, I have evaluated the models using various performance metrics such as mean absolute error (MAE), mean squared error (MSE), and root mean squared error (RMSE). The best-performing model is deployed to predict fare prices and demand patterns of yellow taxis.

In conclusion, this project showcases the application of scalable Big Data technologies and machine learning algorithms to solve real-world big data challenges. I hope this project inspires you to explore more about big data technologies and their applications in data science.