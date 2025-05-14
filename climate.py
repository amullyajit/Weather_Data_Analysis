import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load and preprocess the data
def load_data(filepath):
    df = pd.read_csv(filepath)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    print("Available columns:", df.columns.tolist())

    # Rename and compute necessary fields
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['temperature'] = (df['temp max'] + df['temp min']) / 2
    df['precipitation'] = df['rain']  # Rename for consistency

    # Drop rows with missing values
    df = df.dropna(subset=['date', 'temperature', 'precipitation'])

    return df

# Step 2: Monthly temperature trend
def plot_monthly_trends(df):
    df['month'] = df['date'].dt.month
    monthly_avg = df.groupby('month')['temperature'].mean()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=monthly_avg.index, y=monthly_avg.values, marker='o')
    plt.title('Average Monthly Temperature')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.xticks(range(1, 13))
    plt.show()

# Step 3: Daily temperature variation
def plot_daily_variation(df):
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=df, x='date', y='temperature', linewidth=1)
    plt.title('Daily Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.show()

# Step 4: Correlation heatmap
def plot_correlation(df):
    features = ['temperature', 'precipitation']
    corr = df[features].corr()

    plt.figure(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Between Temperature and Precipitation')
    plt.show()

# Main function
if __name__ == "__main__":
    filepath = r'C:\Users\AGNIBHA\Desktop\Climate\Weather.csv'

    try:
        df = load_data(filepath)
        print("Data Loaded Successfully. Sample:")
        print(df[['date', 'temperature', 'precipitation']].head())

        plot_monthly_trends(df)
        plot_daily_variation(df)
        plot_correlation(df)

    except Exception as e:
        print(f"An error occurred: {e}")
