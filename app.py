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

# Fondo con la imagen y el color de texto blanco
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/foto-gratis/personas-que-toman-clases-pilates-reformador_23-2151093272.jpg?t=st=1738638246~exp=1738641846~hmac=c98b8738e3217cfda46863036a62ca7f8745ab9d61d03d3e99de187a0da9ea6a&w=2000");
    background-size: cover;
    color: white;
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
            st.success(f"✅ Bienvenido, {username}!")
            st.experimental_rerun()  # Recargar la página para pasar a la siguiente pantalla
        else:
            st.error("❌ Usuario o contraseña incorrectos")

# Si el usuario no está logueado, mostrar la pantalla de login
if not st.session_state.logged_in:
    login()
else:
    st.experimental_rerun()  # Si está logueado, hacer rerun para cargar la siguiente pantalla
