import streamlit as st

# Simulación de usuarios registrados
USERS = {
    "admin": "1234",
    "usuario1": "contraseña123",
}

# Variables de sesión
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

if "screen" not in st.session_state:
    st.session_state.screen = "login"  # Pantalla inicial es el login

# Fondo con la imagen y el color de texto blanco
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/foto-gratis/personas-que-toman-clases-pilates-reformador_23-2151093272.jpg?t=st=1738638246~exp=1738641846~hmac=c98b8738e3217cfda46863036a62ca7f8745ab9d61d03d3e99de187a0da9ea6a&w=2000");
    background-size: cover;
    color: white;
}

[data-testid="stButton"] {
    color: black;
    background-color: #f0f0f0;
    border-radius: 50px;
    padding: 10px 20px;
    margin: 5px;
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"] {
    right: 2rem;
}

h1, h2, h3, h4, h5, h6, p {
    color: white;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Función de login
def login():
    st.title("🔐 Inicio de Sesión")

    # Campos de inicio de sesión
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    # Botón de iniciar sesión
    if st.button("Iniciar sesión"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.screen = "crear_habito"  # Cambiar a la pantalla de crear hábito
        else:
            st.error("❌ Usuario o contraseña incorrectos")

# Control de flujo de la aplicación
login()
