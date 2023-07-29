from tkinter import *
import tkinter as tk
from sklearn.ensemble import ExtraTreesRegressor
import pandas as pd

# Read the dataset from the CSV file
data = pd.read_csv("predictData.csv")

# Separate the features (inputs) and the class labels
X = data.iloc[:, :]  # Features
y = data.iloc[:]   # Class labels

# Create a Random Forest classifier
rf = ExtraTreesRegressor()
# Train the classifier
rf.fit(X, y)

# Create interface window
root = Tk()
root.title("Data prediction program")
root.geometry("1000x350+250+100")
root.configure(bg="#D6B4FC")

# Create labels and input fields
quantity = Label(root, text="Please input quantity:", font=('Helvetica', 11), fg="#290C5E", bg="#D6B4FC").place(x=1, y=20)
quantityInput = tk.Entry(root, justify='center', width=35, font=('Helvetica', 15, 'bold'), bg="black", border=0,fg='white')
quantityInput.place(x = 230, y = 20)
quantityInput.focus()

unitPrice = Label(root, text="Please input Unit:", font=('Helvetica', 11), fg="#290C5E", bg="#D6B4FC").place(x=1, y=50)
UPInput = tk.Entry(root, justify='center', width=35, font=('Helvetica', 15, 'bold'), bg="black", border=0,fg='white')
UPInput.place(x = 230, y = 50)
UPInput.focus()

total = Label(root, text="Please input total:", font=('Helvetica', 11), fg="#290C5E", bg="#D6B4FC").place(x=1, y=80)
totalInput = tk.Entry(root, justify='center', width=35, font=('Helvetica', 15, 'bold'), bg="black", border=0,fg='white')
totalInput.place(x = 230, y = 80)
totalInput.focus()

gpm = Label(root, text="Please input gpm:", font=('Helvetica', 11), fg="#290C5E", bg="#D6B4FC").place(x=1, y=110)
gpmInput = tk.Entry(root, justify='center', width=35, font=('Helvetica', 15, 'bold'), bg="black", border=0,fg='white')
gpmInput.place(x = 230, y = 110)
gpmInput.focus()

profit = Label(root, text="Please input profit:", font=('Helvetica', 11), fg="#290C5E", bg="#D6B4FC").place(x=1, y=140)
profitIncome = tk.Entry(root, justify='center', width=35, font=('Helvetica', 15, 'bold'), bg="black", border=0,fg='white')
profitIncome.place(x = 230, y = 140)
profitIncome.focus()

tax = Label(root, text="Please input tax:", font=('Helvetica', 11), fg="#290C5E", bg="#D6B4FC").place(x=1, y=170)
taxInput = tk.Entry(root, justify='center', width=35, font=('Helvetica', 15, 'bold'), bg="black", border=0,fg='white')
taxInput.place(x = 230, y = 170)
taxInput.focus()

cogs = Label(root, text="Please input cogs:", font=('Helvetica', 11), fg="#290C5E", bg="#D6B4FC").place(x=1, y=200)
cogsInput = tk.Entry(root, justify='center', width=35, font=('Helvetica', 15, 'bold'), bg="black", border=0,fg='white')
cogsInput.place(x = 230, y = 200)
cogsInput.focus()

prediction = Label(root, text = "Prediction:", font = ('Helvetica', 11), fg = "#290C5E", bg = "#D6B4FC").place(x = 1, y = 300)
predictionResult = Label(root, font = ("Helvetica", 12),width=50, fg = "white", bg = "#303030")
predictionResult.place(x = 230, y = 300)

# Create a function to run the prediction
def run():
    # Get the values from the input fields
    quantity_value = float(quantityInput.get())
    up_value = float(UPInput.get())
    total_value = float(totalInput.get())
    gpm_value = float(gpmInput.get())
    profit_value = float(profitIncome.get())
    tax_value = float(taxInput.get())
    cogs_value = float(cogsInput.get())


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
    predicted_class = rf.predict(input_data)

    # Update the prediction result label
    predictionResult.configure(text=predicted_class[0])

# Create a button to run the prediction
run_btn = tk.Button(root, font=("Times New Roman", 10, 'bold'), compound="left", borderwidth=0, cursor="hand2",bg="#FFFFFF", command=run, text="Run prediction", width=15, height=2).place(x=450, y=220)

root.mainloop()
