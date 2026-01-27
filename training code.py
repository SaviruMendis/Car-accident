import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
from sklearn.pipeline import Pipeline


df1 = pd.read_csv("synthetic_road_accidents_2k.csv")
df2 = pd.read_csv("synthetic_road_accidents_10k.csv")
df3 = pd.read_csv("synthetic_road_accidents_100k.csv")

_df = pd.concat([df1, df2, df3])

_df = _df.drop_duplicates()

_df.reset_index(drop = True, inplace = True)

X = _df.drop(["accident_risk","num_reported_accidents"], axis=1)
y = _df["accident_risk"]

X["high_speed"] = (X["speed_limit"] > 45).astype(bool)
X = X.drop("speed_limit", axis=1)

# Column types
cat_cols = X.select_dtypes(include = ["object","category"]).columns
num_cols = X.select_dtypes(exclude = ["object","category","bool"]).columns
bool_cols = X.select_dtypes(include = "bool").columns

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
        ("num", "passthrough", num_cols),
        ("bool", "passthrough", bool_cols)
    ]
)

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "accident_model.pkl")
