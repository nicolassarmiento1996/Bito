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


st.markdown(
    """
    <style>
    .reportview-container {
        background: url('https://images.unsplash.com/photo-1574764199913-df05b1e03b0e') no-repeat center center fixed;
        background-size: cover;
        height: 100vh;
        color: red;  # Cambiar el color del texto a rojo para verificar que se aplica el CSS
    }
    .sidebar-content {
        background: rgba(0, 0, 0, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

def login():
    """Función para manejar el inicio de sesión"""
    st.title("🔐 Inicio de Sesión")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("¡Inicio de sesión exitoso!")
            st.experimental_rerun()
        else:
            st.error("❌ Usuario o contraseña incorrectos")

def home():
    """Pantalla principal después de iniciar sesión"""
    st.title(f"🎉 Bienvenido {st.session_state.username}")
    st.write("¡Has iniciado sesión exitosamente!")

    if st.button("Cerrar sesión"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# Control de flujo: Mostrar la pantalla de login si no está autenticado
if not st.session_state.logged_in:
    login()
else:
    home()


def login():
    """Función para manejar el inicio de sesión"""
    st.title("🔐 Inicio de Sesión")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

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
