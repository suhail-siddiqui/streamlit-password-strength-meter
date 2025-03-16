import streamlit as st
import re
import random
import string

def check_password_strength(password):
    strength = 0
    remarks = ""
    
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    
    if strength == 5:
        remarks = "Very Strong"
    elif strength == 4:
        remarks = "Strong"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 2:
        remarks = "Weak"
    else:
        remarks = "Very Weak"
    
    return strength, remarks

def generate_strong_password(length):
    if length < 8:
        return "Password length must be at least 8 characters."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

st.title("Password Strength Meter & Generator")

password = st.text_input("Enter your password", type="password")

if password:
    strength, remarks = check_password_strength(password)
    st.progress(strength / 5)
    st.write(f"Password Strength: {remarks}")

st.header("Generate Strong Password")
password_length = st.number_input("Select Password Length", min_value=8, max_value=32, value=12, step=1)
if st.button("Generate Password"):
    generated_password = generate_strong_password(password_length)
    st.text_input("Generated Password", generated_password)
