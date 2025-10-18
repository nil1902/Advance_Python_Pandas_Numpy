"""
interpolation mean fill the missing value with some estimated value based on some logic
linear interpolation is one of the most common methods used to estimate missing values in a dataset. It works by connecting two known data points with a straight line and using that line to estimate the missing values in between.
polynomial interpolation involves fitting a polynomial function to a set of known data points and using that function to estimate missing values. This method can capture more complex relationships in the data compared to linear interpolation.
time series interpolation is specifically designed for datasets where the data points are ordered in time. It takes into account the temporal relationships between data points to estimate missing values.
use : 1.preserve data integrity || 2.smooth trends || 3.avoid data loss
"""

import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, None, 22, 32],
    'City': ['New York', 'Los Angeles', "Delhi", 'Houston'],
    'salary': [70000, 80000, None, 90000],
    'performance_score': [88, None, 85, 95]
}
df = pd.DataFrame(data)
print("Original DataFrame with missing values:")
print(df)
# Interpolating missing values
df_interpolated = df.interpolate(method='linear', limit_direction='forward', axis=0)
print("\nDataFrame after interpolation:")
print(df_interpolated)
print("\n")
print(df_interpolated.info())  # print summary of dataframe
print(df_interpolated.describe())  # print statistical summary of dataframe

'''
advantages of interpolation in pandas:
1. Data Integrity: Interpolation helps maintain the integrity of the dataset by filling in missing values
2. Trend Preservation: It preserves the overall trends and patterns in the data, which is crucial for accurate analysis.
3. Avoids Data Loss: Instead of dropping rows with missing values, interpolation allows you to retain more data for analysis.
4. Flexibility: Pandas offers various interpolation methods (linear, polynomial, time-based) to suit different types of data and analysis needs.
5. Ease of Use: The interpolation functions in pandas are easy to implement, making it accessible for users with varying levels of expertise.

limitations of interpolation in pandas:
1. Assumption of Continuity: Interpolation assumes that the data is continuous and follows a certain pattern, which may not always be true.
2. Sensitivity to Outliers: Interpolation methods can be sensitive to outliers, which may lead to inaccurate estimates of missing values.
3. Not Suitable for Categorical Data: Interpolation is primarily designed for numerical data and may not be appropriate for categorical variables.
4. Overfitting Risk: Using complex interpolation methods (like high-degree polynomials) can lead to overfitting, where the estimated values do not generalize well.
5. Limited by Data Distribution: The effectiveness of interpolation depends on the distribution and density of the existing data points; sparse data can lead to unreliable estimates.

real life examples where interpolation is useful:
1. Weather Data Analysis: Filling in missing temperature or precipitation readings in meteorological datasets to ensure continuous time series for climate studies.
2. Financial Time Series: Estimating missing stock prices or economic indicators in financial datasets to maintain the integrity of time series analysis.
3. Sensor Data in IoT: Interpolating missing readings from sensors in Internet of Things (IoT) applications to ensure accurate monitoring and analysis.
4. Medical Research: Filling in missing patient data (e.g., blood pressure readings) in clinical trials to ensure comprehensive analysis.
5. Environmental Monitoring: Estimating missing pollution or air quality measurements in environmental datasets for accurate assessments.
 
 '''