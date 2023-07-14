import streamlit as st
from textcortex import TextCortex

# Create the TextCortex object and enter your API Key
text_cortex = TextCortex(api_key='gAAAAABksMGMKiiYt3eFB_7EMau13166KzO48vThLHLSR8f_GzcQL0Qmcs268G63DhfeMEoUAcrCldvaXwYv1otTdAdXDhM2eU75RMNWOSrZrvzSZM6o8k5tFPzotOEsZnz-egz2jZ17')

# Function to generate content while maintaining style and tone
def generate_content(prompt, token_count, source_language, temperature, n_gen):
    # Extend the prompt using Hemingwai
    extended_text = text_cortex.extend(
        prompt=prompt,
        token_count=token_count,
        source_language=source_language,
        temperature=temperature,
        n_gen=n_gen
    )

    # Paraphrase the extended text
    paraphrased_text = text_cortex.paraphrase(
        prompt=extended_text,
        source_language=source_language,
        temperature=temperature,
        n_gen=n_gen
    )

    return paraphrased_text

# Streamlit app
def run_app():
    st.title("Generative Content Generation Tool")

    # Input fields
    prompt = st.text_area("Enter the existing content:")
    token_count = st.number_input("Enter the desired token count:", min_value=1, step=1)
    source_language = st.selectbox("Enter the source language:",
    ('en, 'auto', 'ko','es','el','ru))
    temperature = st.slider("Select the temperature:", min_value=0.1, max_value=1.0, step=0.1, value=0.7)
    n_gen = st.number_input("Enter the number of generated content:", min_value=1, step=1)

    # Generate content button
    if st.button("Generate Content"):
        if prompt:
            # Generate content
            generated_content = generate_content(prompt, token_count, source_language, temperature, n_gen)

            # Display generated content
            st.subheader("Generated Content:")
            st.write(generated_content)

# Run the Streamlit app
run_app()
