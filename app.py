import streamlit as st
import pandas as pd

# Set page layout
st.set_page_config(page_title="F1 2026 Australian GP Predictions", layout="wide")

# Title
st.title("🏎️ 2026 Australian GP - Predicted Race Results")

# CSV URL
csv_url = "https://raw.githubusercontent.com/suhailahmed10/master/main/predicted_race_results.csv"

# Load CSV
df_pred = pd.read_csv(csv_url)

# -------------------------
# Top-3 Podium Table
# -------------------------
st.subheader("🏆 Predicted Podium")

# Get top 3 drivers
top3 = df_pred.sort_values("PredictedRacePos").head(3).reset_index(drop=True)
top3["Medal"] = ["🥇","🥈","🥉"]

# Columns to display
top3_display = top3[["Medal","Driver","Constructor"]]

# Display table without index
st.table(top3_display.style.hide_index())

# -------------------------
# Full Race Table
# -------------------------
st.subheader("📋 Full Race Results")

# Columns to show in full table (exclude PredictedRacePos)
full_table = df_pred[["Driver","Constructor","QualRank","QualTime","GapToPole","Grid"]]

# Display table without index and with gradient for readability
st.dataframe(
    full_table.style.hide_index().background_gradient(cmap='viridis')
)
