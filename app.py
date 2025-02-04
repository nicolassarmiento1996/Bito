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

# Función de creación de hábito
def crear_habito():
    """Pantalla para crear un nuevo hábito"""
    st.title("📅 Crear Nuevo Hábito")

    # Nombre del hábito
    habit_name = st.text_input("¿Qué hábito deseas crear?", "")

    # Selección de días de la semana
    st.write("Selecciona los días de la semana para realizar tu hábito:")
    days_of_week = ["L", "M", "X", "J", "V", "S", "D"]
    selected_days = []

    # Crear botones para seleccionar los días
    for day in days_of_week:
        if st.button(day, key=day):
            selected_days.append(day)

    # Sanción
    sanction = st.text_area("Escribe una sanción si no realizas el hábito:")

    # Aceptar y guardar el hábito
    if st.button("Aceptar"):
        if habit_name and selected_days and sanction:
            new_habit = {
                "name": habit_name,
                "days": selected_days,
                "sanction": sanction
            }
            if "habitos" not in st.session_state:
                st.session_state.habitos = []
            st.session_state.habitos.append(new_habit)
            st.session_state.screen = "dashboard"  # Cambiar a la pantalla de dashboard

# Función de dashboard
def dashboard():
    """Pantalla de Dashboard"""
    st.title("📊 Dashboard de Hábitos")

    # Si no hay hábitos, mostrar mensaje
    if not st.session_state.habitos:
        st.write("No tienes hábitos registrados aún.")
    else:
        # Mostrar todos los hábitos
        for habit in st.session_state.habitos:
            st.write(f"**Hábito**: {habit['name']}")
            st.write(f"**Días**: {', '.join(habit['days'])}")
            st.write(f"**Sanción**: {habit['sanction']}")
            st.write("---")

    if st.button("Crear nuevo hábito"):
        st.session_state.screen = "crear_habito"  # Volver a la pantalla de creación de hábitos

# Control de flujo de la aplicación
if st.session_state.screen == "login":
    login()
elif st.session_state.screen == "crear_habito":
    crear_habito()
elif st.session_state.screen == "dashboard":
    dashboard()
