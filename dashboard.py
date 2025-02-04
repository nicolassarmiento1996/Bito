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
    st.session_state.page = "login"  # Asegurarse de que se inicie en la pantalla de login

# Fondo con la imagen y el color de texto blanco
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/foto-gratis/personas-que-toman-clases-pilates-reformador_23-2151093272.jpg?t=st=1738638246~exp=1738641846~hmac=c98b8738e3217cfda46863036a62ca7f8745ab9d61d03d3e99de187a0da9ea6a&w=2000");
    background-size: cover;
    color: white;  /* Establecer color blanco para el texto */
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"] {
    right: 2rem;
}

h1, h2, h3, h4, h5, h6, p {
    color: white; /* Asegura que todos los textos sean blancos */
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Función de inicio de sesión
def login():
    """Función para manejar el inicio de sesión"""
    st.title(" Inicio de Sesión")

    # Campos de inicio de sesión
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    # Botón de iniciar sesión
    if st.button("Iniciar sesión"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.page = "crear_habito"  # Página siguiente
            st.success(f"Bienvenido, {username}!")
        else:
            st.error("Usuario o contraseña incorrectos")

# Función para la página de creación de hábitos
def crear_habito():
    """Pantalla para crear hábitos"""
    st.title("Crear un Hábito")
    
    # Campo para el nombre del hábito
    habit_name = st.text_input("Nombre del hábito")

    # Selección de días de la semana
    days_of_week = st.multiselect(
        "Selecciona los días de la semana",
        ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
    )
    
    # Campo para la sanción
    sanction = st.text_input("Escribe una sanción en caso de no cumplir con el hábito")

    # Botón para guardar el hábito
    if st.button("Aceptar"):
        st.session_state.habit_name = habit_name
        st.session_state.days_of_week = days_of_week
        st.session_state.sanction = sanction
        st.session_state.page = "dashboard"  # Redirigir al dashboard
        st.success(f"Hábito {habit_name} creado exitosamente!")

# Función para el dashboard
def dashboard():
    """Pantalla del Dashboard"""
    st.title(f"Dashboard de {st.session_state.username}")

    st.write(f"Hábito: {st.session_state.habit_name}")
    st.write(f"Días de la semana: {', '.join(st.session_state.days_of_week)}")
    st.write(f"Sanción: {st.session_state.sanction}")
    
    # Botón de cerrar sesión
    if st.button("Cerrar sesión"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.page = "login"  # Regresar a login

# Control de flujo: Mostrar la pantalla correcta según el estado
if not st.session_state.logged_in:
    login()
else:
    # Usar st.radio para navegar entre las páginas después de iniciar sesión
    page = st.radio("Menú", ["Crear hábito", "Dashboard"])
    
    if page == "Crear hábito":
        crear_habito()
    elif page == "Dashboard":
        dashboard()
