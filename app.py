import streamlit as st

# Aplicar CSS para cambiar el color de los botones
st.markdown(
    """
    <style>
    div.stButton > button, div.stFormSubmitButton > button {
        color: white !important;
        background-color: red !important;
        border-color: red !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
    background-image: url("https://images.pexels.com/photos/2908175/pexels-photo-2908175.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
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
            st.session_state.page = "crear_habito"  # Cambiar a la pantalla de crear hábito
        else:
            st.error("Usuario o contraseña incorrectos")

# Función para la pantalla de crear hábito
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

    # Botones para guardar el hábito y ver mis hábitos
    col1, col2 = st.columns([3, 1])
    if col1.button("Aceptar"):
        st.session_state.habit_name = habit_name
        st.session_state.days_of_week = days_of_week
        st.session_state.sanction = sanction
        st.success(f"Hábito {habit_name} creado exitosamente!")
    
    if col2.button("Ver mis hábitos"):
        st.session_state.page = "dashboard"  # Cambiar a la pantalla de dashboard

# Función para mostrar la pantalla de dashboard
# Función para mostrar la pantalla de dashboard
def dashboard():
    st.title("Dashboard")
    
    # Mostrar los hábitos creados
    st.write("Hábitos creados:")
    st.write(st.session_state.habit_name)
    st.write(st.session_state.days_of_week)
    st.write(st.session_state.sanction)
    
    # Tabla de seguimiento de los días
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    # Crear una lista para almacenar los días que se han cumplido
    if "dias_cumplidos" not in st.session_state:
        st.session_state.dias_cumplidos = [False] * len(dias_semana)
    
    # Mostrar la tabla de seguimiento
    tabla_seguimiento = []
    for i, dia in enumerate(dias_semana):
        tabla_seguimiento.append([dia, st.checkbox(f"Cumplido el {dia}", key=f"dia_{i}", value=st.session_state.dias_cumplidos[i])])
    
    # Calcular el progreso
    progreso = sum(1 for dia in tabla_seguimiento if dia[1]) / len(dias_semana) * 100
    
    # Mostrar el gráfico de progreso
    st.write("Progreso:")
    import streamlit.components.v1 as components
    components.html(
        """
        <style>
        .progress-circle {
            position: relative;
            display: inline-block;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background-color: #f2f2f2;
        }
        
        .progress-circle::after {
            content: '%s%%' %s;
            position: absolute;
            top: 50%%;
            left: 50%%;
            transform: translate(-50%%, -50%%);
            font-size: 20px;
            font-weight: bold;
        }
        
        .progress-circle .progress {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%%;
            height: 100%%;
            border-radius: 50%%;
            background-color: #4CAF50;
            clip-path: polygon(50%% 50%%, 50%% 0, 100%% 0, 100%% 50%%, 50%% 50%%);
            transform: rotate(-90deg);
            transform-origin: center;
        }
        
        .progress-circle .progress::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%%;
            height: 100%%;
            border-radius: 50%%;
            background-color: #4CAF50;
            clip-path: polygon(50%% 50%%, 50%% 0, 100%% 0, 100%% 50%%, 50%% 50%%);
            transform: rotate(%sdeg);
            transform-origin: center;
        }
        </style>
        
        <div class="progress-circle">
            <div class="progress" style="--progress:%s;"></div>
        </div>
        """ % (int(progreso), 'center', int(progreso * 3.6), int(progreso)),
        height=150,
    )
    
    # Botón para guardar los cambios
    if st.button("Guardar cambios"):
        st.session_state.dias_cumplidos = [tabla_seguimiento[i][1] for i in range(len(dias_semana))]
        st.success("Cambios guardados exitosamente!")
    
    # Mostrar la tabla de seguimiento
    st.table(tabla_seguimiento)
