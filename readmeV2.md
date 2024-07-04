# Football Match Predictor

This program predicts football match outcomes based on historical data using machine learning.

## How to Use

1. **Install Dependencies:**
   - Ensure you have Python 3 installed.
   - Install required Python packages:
     ```
     pip install pandas scikit-learn
     ```

2. **Input Data Requirements:**
   - Prepare a CSV file `football_dataset.csv` with the following columns:
     - Date: Date of the match
     - Opponent: Opponent team name
     - Home/Away: Whether the match was played at home or away
     - Competition: Type of competition (e.g., league, cup)
     - Venue: Stadium or venue of the match
     - Score: Match result (e.g., Win, Loss, Draw)

3. **Running the Program:**
   - Execute the `football_predictor.py` script:
     ```
     python football_predictor.py
     ```
   - The program will load the dataset, train a machine learning model, and evaluate its accuracy.

4. **Output:**
   - The program outputs the accuracy of the trained model on predicting match outcomes.

## Example Input Data

To predict match results, input data should include details like:
- Date: "2023-05-15"
- Opponent: "Manchester United"
- Home/Away: "Home"
- Competition: "Premier League"
- Venue: "Old Trafford"

Ensure the input data matches the format specified in the `football_dataset.csv` file.

