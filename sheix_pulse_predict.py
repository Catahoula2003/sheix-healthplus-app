<details>
<summary>Tap to expand</summary>
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("SheiX Pulse Vital Predictor")

st.markdown("""
This tool uses the **Sheispot sequence** to predict the sum of 10 pulse measurements based on early values.

🟡 **Rule**: First value (A1) must be **smaller** than second value (A2).  
🔵 The 7th value is used for prediction: `A7 × 11 = Total Sum (A1–A10)`
""")

def generate_sheispot_sequence(a1, a2):
    if a1 >= a2:
        return None, "A1 must be less than A2"
    sequence = [a1, a2]
    while len(sequence) < 10:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence, None

def run_prediction(sequence):
    actual_sum = sum(sequence)
    predicted_sum = sequence[6] * 11
    return predicted_sum, actual_sum

st.subheader("Input the first two pulse measurements")

a1 = st.number_input("A1 (must be smaller)", min_value=0, step=1, value=1)
a2 = st.number_input("A2 (must be greater)", min_value=0, step=1, value=2)

if st.button("Generate Sequence and Predict"):
    sequence, error = generate_sheispot_sequence(a1, a2)

    if error:
        st.error(error)
    else:
        st.success("Valid Sheispot sequence generated:")
        st.write(f"Sequence (A1–A10): {sequence}")
        
        predicted_sum, actual_sum = run_prediction(sequence)
        
        st.write(f"✅ Predicted Total (A7 × 11): `{predicted_sum}`")
        st.write(f"📊 Actual Total (sum of A1–A10): `{actual_sum}`")

        st.subheader("Pulse Sequence Visualization")
        fig, ax = plt.subplots()
        ax.plot(range(1, 11), sequence, marker='o', color='blue', label="Pulse Data")
        ax.axhline(y=predicted_sum/10, linestyle='--', color='red', label="Predicted Avg")
        ax.set_xlabel("Measurement Index (A1–A10)")
        ax.set_ylabel("Pulse Value")
        ax.legend()
        st.pyplot(fig)
      </details>

      
