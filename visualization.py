import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataset_handler import DatasetHandler

def plot_data_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Home/Away', data=data)
    plt.title('Home vs Away Matches')
    plt.xlabel('Home (1) or Away (0)')
    plt.ylabel('Count')
    plt.show()

def plot_score_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Home_Score'], bins=10, kde=True, color='blue', label='Home Score')
    sns.histplot(data['Away_Score'], bins=10, kde=True, color='red', label='Away Score')
    plt.title('Score Distribution')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

def plot_model_performance(y_test, predictions):
    plt.figure(figsize=(10, 6))
    sns.heatmap(pd.crosstab(y_test, predictions, rownames=['Actual'], colnames=['Predicted'], normalize='index'), annot=True, fmt='.2f', cmap='Blues')
    plt.title('Model Performance')
    plt.show()

def main():
    # Load and preprocess the dataset
    handler = DatasetHandler('data/ukraine_result.csv')
    handler.load_data()
    data = handler.get_data()

    # Plot data distribution
    plot_data_distribution(data)
    plot_score_distribution(data)

    # Prepare features and labels
    features = data[['Home/Away', 'Home_Score', 'Away_Score']]
    labels = (data['Home_Score'] > data['Away_Score']).astype(int)

    # Split the data into training and testing sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Train a logistic regression model
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Plot model performance
    plot_model_performance(y_test, predictions)

if __name__ == '__main__':
    main()
