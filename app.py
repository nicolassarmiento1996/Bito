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
    st.title("Crear hábito")
    
    # Formulario para crear hábito
    with st.form("crear_habito"):
        habit_name = st.text_input("Nombre del hábito")
        days_of_week = st.multiselect("Días de la semana", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
        sanction = st.text_input("Sanción")
        
        # Botón para crear hábito y ver mis hábitos
        if st.form_submit_button("Crear hábito y ver mis hábitos"):
            st.session_state.habit_name = habit_name
            st.session_state.days_of_week = days_of_week
            st.session_state.sanction = sanction
            st.session_state.dias_cumplidos = [False] * len(days_of_week)
            st.success("Hábito creado exitosamente!")
            st.session_state.page = "dashboard"

# Página de dashboard
# Página de dashboard
def dashboard():
    st.title("Dashboard")
    
    # Mostrar los hábitos creados
    st.write("Hábitos creados:")
    st.write(st.session_state.habit_name)
    st.write(st.session_state.sanction)
    
    # Tabla de seguimiento de los días
    dias_semana = st.session_state.days_of_week
    
    # Mostrar la tabla de seguimiento
    tabla_seguimiento = []
    for i, dia in enumerate(dias_semana):
        tabla_seguimiento.append([dia, st.checkbox(f"Cumplido el {dia}", key=f"dia_{i}")])
    
    # Calcular el progreso
    progreso = sum(1 for dia in tabla_seguimiento if dia[1]) / len(dias_semana) * 100
    
    # Mostrar el gráfico de progreso
    # Página de dashboard
def dashboard():
    st.title("Dashboard")

    dias_semana = st.session_state.days_of_week
    tabla_seguimiento = []
    progreso = sum(1 for dia in dias_semana if st.session_state.dias_cumplidos[dias_semana.index(dia)]) / len(dias_semana) * 100

    html_code = f"""
    <style>
    .habito {{
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
    }}
    
    .progress-circle {{
        position: relative;
        display: inline-block;
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background-color: #f2f2f2;
    }}
    
    .progress-circle::after {{
        content: '{int(progreso)}%';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 20px;
        font-weight: bold;
    }}
    
    .progress-circle svg {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }}
    
    .progress-circle svg circle {{
        stroke-width: 10;
        stroke-linecap: round;
        transform: rotate(-90deg);
        transform-origin: center;
    }}
    
    .progress-circle svg circle.progress {{
        stroke-dasharray: {int(progreso * 3.14)} 314;
    }}
    </style>
    
    <div class="habito">
        <h2>Hábito: {st.session_state.habit_name}</h2>
        <p>Sanción: {st.session_state.sanction}</p>
        
        <h3>Cumplimiento de los días:</h3>
        <ul>
    """
    for i, dia in enumerate(dias_semana):
        html_code += f"""
            <li>{dia}: {st.checkbox(f"Cumplido el {dia}", key=f"dia_{i}")}</li>
        """
        tabla_seguimiento.append([dia, st.session_state.dias_cumplidos[i]])
    html_code += f"""
        </ul>
        
        <h3>Progreso:</h3>
        <div class="progress-circle">
            <svg>
                <circle cx="50" cy="50" r="45" stroke="#ddd" stroke-width="10" fill="none"></circle>
                <circle cx="50" cy="50" r="45" stroke="#4CAF50" stroke-width="10" fill="none" class="progress"></circle>
            </svg>
        </div>
        
        <button onclick="document.getElementById('guardar').click()">Guardar cambios</button>
        <button id="guardar" style="display: none;" onclick="javascript: {{
            st.session_state.dias_cumplidos = [{', '.join(f'{dia[1]}' for dia in tabla_seguimiento)}];
            st.success('Cambios guardados exitosamente!');
        }}">Guardar cambios</button>
    </div>
    """
    st.components.v1.html(html_code, height=550)
    
    # Botón para guardar los cambios
    if st.button("Guardar cambios"):
        st.session_state.dias_cumplidos = [dia[1] for dia in tabla_seguimiento]
        st.success("Cambios guardados exitosamente!")
    

# Control de flujo: Mostrar la pantalla correcta según el estado
if not st.session_state.logged_in:
    login()
elif st.session_state.page == "crear_habito":
    crear_habito()
elif st.session_state.page == "dashboard":
    dashboard()
