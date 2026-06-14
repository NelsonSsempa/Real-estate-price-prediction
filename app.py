# paste the full Streamlit code here
import matplotlib.pyplot as plt

# Scatter plot of actual vs predicted
st.subheader("📈 Actual vs Predicted Prices")

fig, ax = plt.subplots()
ax.scatter(y_test, y_pred, alpha=0.7, color="blue")
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=2)
ax.set_xlabel("Actual Price")
ax.set_ylabel("Predicted Price")
ax.set_title("Actual vs Predicted Prices")

st.pyplot(fig)
