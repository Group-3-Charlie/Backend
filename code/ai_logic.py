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
    predictions = None
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
        separator: str = ',' if open(filepath).read().count(',') > open(filepath).read().count(';') else ';'
        cls.df = pd.read_csv(filepath, sep=separator)
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
        cls.train()

    @classmethod
    def train(cls):
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

        # Return the model efficiency
        print(cls.model.score(X_test_imputed, y_test))
        return cls.model.score(X_test_imputed, y_test)

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
        return dataToNormalise

    @classmethod
    def predict(cls, filename):
        """
        Predicts the results based on the selected target and the new data.
        :param filename:
        """
        separator = ',' if open(filename).read().count(',') > open(filename).read().count(';') else ';'
        new_data = pd.read_csv(filename, sep=separator)
        new_data.select_dtypes(include=['int', 'float'])
        new_data = new_data.select_dtypes(include=['int', 'float'])
        new_data = cls.normalisation(new_data)
        new_data.drop(cls.target, axis=1, inplace=True)
        new_data_imputed = pd.DataFrame(cls.imputer.transform(new_data), columns=new_data.columns)
        predictions = cls.model.predict(new_data_imputed)
        predictions = pd.DataFrame(predictions, columns=[cls.target])

        # Rebuid the original dataset with the predictions
        new_data = pd.read_csv(filename, sep=separator)
        new_data[cls.target] = predictions
        new_data.to_csv('predictions.csv', index=False)
        cls.predictions = new_data
        return predictions
