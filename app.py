import streamlit as st

# Simulación de usuarios registrados
USERS = {
    "admin": "1234",
    "usuario1": "contraseña123",
}

# Configuración de la sesión
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://mejorconsalud.as.com/wp-content/uploads/2023/12/wellness-tendencias-2024-scaled.jpg");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"] {
right: 2rem;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("It's summer!")

def login():
    """Función para manejar el inicio de sesión"""
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
            st.experimental_rerun()  # Recargar la página para mostrar la siguiente pantalla
        else:
            st.error("❌ Usuario o contraseña incorrectos")

def home():
    """Pantalla principal después de iniciar sesión"""
    st.title(f"🎉 Bienvenido {st.session_state.username}")
    st.write("¡Has iniciado sesión exitosamente!")

    if st.button("Cerrar sesión"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.experimental_rerun()

# Control de flujo: Mostrar la pantalla de login si no está autenticado
if not st.session_state.logged_in:
    login()
else:
    home()
