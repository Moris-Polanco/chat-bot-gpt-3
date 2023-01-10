
# Define the function that will generate responses from GPT-3
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

# create a chatbot
st.set_page_config(page_title="Chatbot GPT-3", page_icon=":guardsman:", layout="wide")
st.title("Chatbot GPT-3")

# Create a function that will be called when the user sends a message
def chatbot(message):
    st.write("Tu: " + message)
    response = generate_response(message)
    st.write("Bot: " + response)
