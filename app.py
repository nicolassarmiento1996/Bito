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
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "login"  # Inicia en la pantalla de login

# Aplicar CSS para cambiar el color del botón
st.markdown(
    """
    <style>
    div.stButton > button {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
            st.session_state.pantalla = "crear_habito"  # Cambia la pantalla
            st.experimental_rerun()  # Recarga para reflejar el cambio
        else:
            st.error("❌ Usuario o contraseña incorrectos")

# Control de flujo: decidir qué pantalla mostrar
if st.session_state.pantalla == "login":
    login()
elif st.session_state.pantalla == "crear_habito":
    import crear_habito  # Llamar la pantalla de creación de hábitos

