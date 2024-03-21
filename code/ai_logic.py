import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


class AILogic:
    """
    AI Logic class to define the logic for the AI.
    """
    df = None
    target = None
    model = LinearRegression()
    imputer = SimpleImputer(strategy='mean')

    @classmethod
    def load_data(cls, filepath):
        """
        Loads the data from a CSV file.
        :param filepath:
        """
        cls.df = pd.read_csv(filepath, sep=',')
        # Select only numerical columns
        cls.df = cls.df.select_dtypes(include=['int', 'float'])

        # Normalization
        cls.normalisation(cls.df)
        print(cls.df.head())

    @classmethod
    def select_target(cls, target):
        """
        Selects the target column from the dataset.
        :param target:
        """
        if target not in cls.df.columns:
            raise ValueError('Target not found in dataset')
        cls.target = target

    @classmethod
    def predict(cls):
        """
        Predicts the results based on the selected target and the new data.
        :return:
        """
        cls.normalisation(cls.df)
        X = cls.df.drop(cls.target, axis=1)
        y = cls.df[cls.target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Impute missing values
        cls.imputer.fit(X_train)  # Fit imputer only on training data
        X_train_imputed = pd.DataFrame(cls.imputer.transform(X_train), columns=X_train.columns)
        X_test_imputed = pd.DataFrame(cls.imputer.transform(X_test), columns=X_test.columns)

        # Train the model
        cls.model.fit(X_train_imputed, y_train)

        # Make predictions
        traintestpredict = cls.model.predict(X_train_imputed)
        testpredict = cls.model.predict(X_test_imputed)

        # Make graph and compare the predictions with the actual values
        plt.scatter(y_train, traintestpredict, color='blue')
        plt.scatter(y_test, testpredict, color='green')
        plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linewidth=1)
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.show()

        # Convert predictions to a list
        predictions_list = testpredict.tolist()

        return predictions_list

    @classmethod
    def normalisation(cls, dataToNormalise: pd.DataFrame):
        """
        Normalises the data.
        """
        columns = dataToNormalise.columns
        for col in columns:
            try:
                x = dataToNormalise[[col]].values.astype(float)
                standard_normalisation = preprocessing.StandardScaler()
                res = standard_normalisation.fit_transform(x)
                dataToNormalise[col] = res
            except ValueError:  # Handle non-numeric data
                pass  # Skip columns that cannot be converted to float
