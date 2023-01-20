import streamlit as st
st.title("Random Password Generator")
st.header("Get a random password for maximum security")
st.subheader("Strong Password Generator to create secure passwords that are impossible to crack on your device without sending them across the Internet")
import string
import random

# using random.choices()
# generating random strings
# initializing size of string
#N=int(input("Enter the length of the password:"))
path=st.number_input("Enter Length")
path = int(path)
if path:
   res = ''.join(random.choices(string.ascii_uppercase +
							string.digits, k=path))
if st.button('run'):
    st.write('password: %s' % res)
