import streamlit as st
import pandas as pd

st.title("🏎️ 2026 Australian GP - Predicted Podium")

# Load CSV from GitHub raw URL (replace with your URL)
csv_url = "https://raw.githubusercontent.com/suhailahmed10/master/main/predicted_race_results.csv"
df_pred = pd.read_csv(csv_url)

# Get top 3 predicted drivers
top3 = df_pred.sort_values("PredictedRacePos").head(3).reset_index(drop=True)
top3["Medal"] = ["🥇","🥈","🥉"]

# Columns to display (exclude index & PredictedRacePos)
st.table(top3[["Medal","Driver","Constructor"]])
st.subheader("📋 Full Race Results")

# Select columns to show
full_table = df_pred[["Driver","Constructor","QualRank","QualTime","GapToPole","Grid"]]


# Display table
st.dataframe(full_table)
