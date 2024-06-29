import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from dataset_handler import DatasetHandler

def main():
    # Load and preprocess the dataset
    handler = DatasetHandler('data/ukraine_result.csv')
    handler.load_data()
    data = handler.get_data()

    # Prepare features and labels
    features = data[['Home/Away', 'Home_Score', 'Away_Score']]
    labels = (data['Home_Score'] > data['Away_Score']).astype(int)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, predictions)
    print(f'Model accuracy: {accuracy * 100:.2f}%')

if __name__ == '__main__':
    main()
