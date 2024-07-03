# Football Match Result Predictor

This project uses machine learning to predict the results of football matches. The dataset contains information about the matches, such as date, opponent, home/away status, competition, venue, and score. The prediction model is built using Python and employs logistic regression.

## Dataset Format

The dataset should be a CSV file with the following columns:

- `Date`: The date of the match.
- `Opponent`: The name of the opposing team.
- `Home/Away`: Indicates whether the match was at home or away (`Home` or `Away`).
- `Competition`: The competition in which the match took place.
- `Venue`: The venue of the match.
- `Score`: The final score of the match in `HomeScore-AwayScore` format.

## Setup and Usage

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Prepare your dataset:**

    Place your dataset CSV file in the `data` directory and name it `ukraine_result.csv`.

5. **Run the main script:**

    ```bash
    python main.py
    ```

    The script will load the dataset, train a logistic regression model, and print the accuracy of the model on the test data.

6. **Run the visualization script:**

    ```bash
    python visualization.py
    ```

    This script will load the dataset and generate various visualizations, including the distribution of scores, the number of matches played at home vs away, and the win rate for home vs away matches.

## User Guide

### Input Data

1. **Dataset Preparation:**

    - Ensure your dataset is in CSV format with the required columns: `Date`, `Opponent`, `Home/Away`, `Competition`, `Venue`, and `Score`.
    - Place your dataset CSV file in the `data` directory and name it `ukraine_result.csv`.

2. **Running the Prediction Script:**

    - Open a terminal or command prompt.
    - Navigate to the project directory.
    - Ensure you have installed the required packages using the command:

        ```bash
        pip install -r requirements.txt
        ```

    - Run the main script to train the model and get predictions:

        ```bash
        python main.py
        ```

3. **Generating Visualizations:**

    - Run the visualization script to generate plots and graphs:

        ```bash
        python visualization.py
        ```

### Interpreting Results

- **Model Accuracy:**

    After running `main.py`, the accuracy of the prediction model will be displayed. This indicates how well the model predicts match outcomes based on the training data.

- **Visualizations:**

    The `visualization.py` script will generate and display several plots:
    
    - **Distribution of Scores:** Shows the frequency of different scores for home and away matches.
    - **Number of Matches Played at Home vs Away:** Displays the count of matches played at home and away.
    - **Win Rate for Home vs Away Matches:** Compares the win rate for matches played at home versus away.

## Files

- `dataset_handler.py`: Contains the `DatasetHandler` class for loading and preprocessing the dataset.
- `predictor.py`: The main script for training the model and making predictions.
- `visualization.py`: Script for generating visualizations.
- `main.py`: Entry point to run the prediction script.
- `requirements.txt`: File containing the list of required Python packages.
- `README.md`: This file.

## License

This project is licensed under the MIT License.
