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

# Aplicar CSS para cambiar el color de los botones
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
            st.success(f"✅ Bienvenido, {username}!")
            st.switch_page("crear_habito.py")  # Redirigir a la pantalla de creación de hábitos
        else:
            st.error("❌ Usuario o contraseña incorrectos")

# Mostrar pantalla de login solo si el usuario no está autenticado
if not st.session_state.logged_in:
    login()
