import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


class AILogic:
    df = None
    target = None
    model = LinearRegression()

    @classmethod
    def load_data(cls, filepath):
        cls.df = pd.read_csv(filepath, sep=';')

    @classmethod
    def select_target(cls, target):
        for col in cls.df.columns:
            print(col)
        if target not in cls.df.columns:
            raise ValueError('Target not found in dataset')
        cls.target = target

    @classmethod
    def predict(cls):
        X = cls.df.drop(cls.target, axis=1)
        y = cls.df[cls.target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        cls.model.fit(X_train, y_train)
        predictions = cls.model.predict(X_test)
        return predictions.tolist()
