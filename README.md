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

## Files

- `dataset_handler.py`: Contains the `DatasetHandler` class for loading and preprocessing the dataset.
- `predictor.py`: The main script for training the model and making predictions.
- `main.py`: Entry point to run the prediction script.
- `requirements.txt`: File containing the list of required Python packages.
- `README.md`: This file.

## License

This project is licensed under the MIT License.