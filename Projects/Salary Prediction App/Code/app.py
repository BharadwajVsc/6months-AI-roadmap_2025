import streamlit as st
import pickle
import numpy as np

# importing the saved ml model
# Note: Ensure the path to the model is correct
model = pickle.load(
    open(
        r"D:\fsds\projects\code\salary prediction app\linear_regression_model.pkl", "rb"
    )
)

st.title("Salary Prediction App")
st.write(
    "This app predicts the salary based on years of experience using a simple linear regression model"
)

years_experience = st.number_input(
    "Enter your experience in years", min_value=0.0, max_value=50.0, value=1.0, step=0.5
)

# When predict button is selected
if st.button("Predict Salary"):
    experience_input = np.array(
        [[years_experience]]
    )  # Convert the input to a 2D array for prediction
    prediction = model.predict(experience_input)
    st.success(
        f"Predicted salary for {years_experience} years of experience is ${prediction[0]:,.2f}"
    )

# Display information about the model
st.write("The model was trained using a dataset of salaries and years of experience.")
