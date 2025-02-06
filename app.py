import streamlit as st
from google import genai
import os

# Load API Key from environment variables (or manually set it here)
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY")  # Replace "YOUR_API_KEY" if needed

# Initialize the GenAI client
client = genai.Client(api_key=API_KEY)

# Function to generate AI responses using Gemini
def healthcare_ai_response(user_input):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_input
        )
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Healthcare chatbot logic
def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult a Doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the Doctor?"
    elif "medication" in user_input:
        return "It is important to take prescribed medicines regularly. If you have concerns, consult your Doctor."
    else:
        return healthcare_ai_response(user_input)

# Main function for Streamlit app
def main():
    st.title("🩺 AI Healthcare Assistant")
    
    # Display an image (Ensure pic.webp is in the same directory or adjust the path)
    st.image("pic.webp", caption="Healthcare Assistant", use_container_width=True)

    # User input field
    user_input = st.text_input("How can I assist you today?")

    # Button to submit user input
    if st.button("Submit"):
        if user_input:
            st.write("**User:**", user_input)
            response = healthcare_chatbot(user_input)
            st.write("**Healthcare Assistant:**", response)
        else:
            st.write("Please enter a message to get a response.")

# Run the app
if __name__ == "__main__":
    main()
