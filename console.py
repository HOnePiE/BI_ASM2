import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor

# Read the dataset from the CSV file
data = pd.read_csv("predictData.csv")

# Separate the features (inputs) and the class labels
X = data.iloc[:, :]  # Features
y = data.iloc[:,]   # Class labels

# Create a Random Forest classifier
rf = ExtraTreesRegressor()
# Train the classifier
rf.fit(X, y)

def run_prediction():
    print("Please input the following values:")
    quantity_value = float(input("Quantity: "))
    up_value = float(input("Unit Price: "))
    total_value = float(input("Total: "))
    gpm_value = float(input("Gross Profit Margin (GPM): "))
    profit_value = float(input("Profit: "))
    tax_value = float(input("Tax: "))
    cogs_value = float(input("Cost of Goods Sold (COGS): "))

    # Create a DataFrame with the input values
    input_data = pd.DataFrame([[
        quantity_value,
        up_value,
        total_value,
        gpm_value,
        profit_value,
        tax_value,
        cogs_value,
    ]],
       columns=X.columns)

    # Make a prediction
    predicted_value = rf.predict(input_data)

    # Print the prediction result
    print("Predicted Profit: ", predicted_value[0])

run_prediction()
