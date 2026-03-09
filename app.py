import streamlit as st
import pandas as pd

st.set_page_config(page_title="F1 2026 Australian GP Predictions", layout="wide")

st.title("🏎️ 2026 Australian GP - Predicted Race Results")

# Load the latest CSV
# Replace this URL with your CSV location on GitHub or Google Drive
csv_url = "https://github.com/suhailahmed10/master/blob/main/predicted_race_results.csv"
df_pred = pd.read_csv(csv_url)

# Top-3 Podium
top3 = df_pred.sort_values("PredictedRacePos").head(3).reset_index(drop=True)
top3["Medal"] = ["🥇","🥈","🥉"]
st.subheader("🏆 Predicted Podium")
st.table(top3[["Medal","Driver","Constructor","PredictedRacePos"]])

# Full Race Table
st.subheader("📋 Full Race Results")
st.dataframe(df_pred.sort_values("PredictedRacePos"))
