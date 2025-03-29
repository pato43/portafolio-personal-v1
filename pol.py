import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

# =============================
# Estilos personalizados y CSS
# =============================
st.markdown(
    """
    <style>
        /* Fondo degradado y tipografía moderna */
        body {
            background: linear-gradient(135deg, #1c1c1c, #3a3a3a);
            font-family: 'Arial', sans-serif;
        }
        .main { 
            background-color: transparent; 
            color: #FFFFFF; 
        }
        /* Botones estilizados */
        .stButton>button, .stDownloadButton>button {
            color: #FFFFFF; 
            background-color: #0055a2; 
            border-radius: 8px; 
            padding: 12px 24px;
            transition: all 0.3s ease; 
            font-weight: bold; 
            border: none;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        .stButton>button:hover, .stDownloadButton>button:hover {
            background-color: #003366; 
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0,0,0,0.5);
        }
        /* Encabezados de sección con animación */
        .section-header {
            font-size: 36px; 
            font-weight: bold; 
            color: #00aaff; 
            margin-top: 20px;
            animation: slideIn 1s ease-out;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        @keyframes slideIn {
            from { transform: translateX(-50px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        /* Imagen de la barra lateral */
        .sidebar-image {
            border-radius: 50%; 
            width: 180px; 
            height: 180px; 
            display: block; 
            margin: 0 auto 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.5);
            transition: transform 0.3s ease;
        }
        .sidebar-image:hover {
            transform: scale(1.1);
        }
        /* Estilos para "cards" en secciones */
        .card {
            background-color: #2c2c2c; 
            padding: 20px; 
            border-radius: 10px; 
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        .card h3 {
            margin-top: 0;
            color: #00aaff;
        }
        .card a {
            color: #00aaff;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True
)

# =============================
# Barra lateral: Información y CV
# =============================
st.sidebar.title("Alexander Eduardo Rojas Garay")
st.sidebar.image("files/WhatsApp Image 2024-10-23 at 7.23.55 PM(1).jpeg", width=180, caption="Data Scientist | Matemático y Físico")
st.sidebar.markdown("**📍 Ubicación:** CDMX")
st.sidebar.markdown("**📞 Teléfono:** 722-559-7963")
st.sidebar.markdown("**📧 Correo:** rojasalexander10@gmail.com")

# Rutas de archivos de CV
cv_es_path = "files/CV-AlexanderEduardoRojasGaray.pdf"
cv_en_path = "files/CV-AlexanderEduardoRojasGaray-EN.pdf"

# Función para descargar CVs
def crear_boton_descarga(file_path, label, file_name, unique_key):
    if Path(file_path).is_file():
        with open(file_path, "rb") as file_data:
            st.sidebar.download_button(
                label=label,
                data=file_data,
                file_name=file_name,
                mime="application/pdf",
                key=unique_key,
            )

crear_boton_descarga(cv_es_path, "📄 Descargar CV en Español", "CV-AlexanderEduardoRojasGaray.pdf", unique_key="boton_es_cv")
crear_boton_descarga(cv_en_path, "📄 Download CV in English", "CV-AlexanderEduardoRojasGaray-EN.pdf", unique_key="boton_en_cv")

# =============================
# Navegación: Pestañas
# =============================
tabs = st.tabs(["Inicio", "Experiencia", "Educación", "Certificaciones", "Habilidades"])

# =============================
# Página de Inicio
# =============================
with tabs[0]:
    st.title("Alexander Eduardo Rojas Garay")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("files/WhatsApp Image 2024-10-23 at 7.23.55 PM(1).jpeg", width=240)
    with col2:
        st.markdown("## Data Scientist | Analista de Datos")
        st.write(
            "¡Bienvenido a mi portafolio interactivo! Soy un apasionado Data Scientist con una sólida formación en Física y Matemáticas. "
            "He liderado proyectos innovadores en machine learning, desarrollo web y automatización de procesos, aportando soluciones creativas y efectivas en cada reto profesional."
        )
        st.write(
            "Mi misión es transformar datos en estrategias y soluciones que impulsen la innovación y el crecimiento. "
            "Explora mi portafolio para conocer más sobre mi trayectoria y logros destacados."
        )

# =============================
# Experiencia Profesional
# =============================
with tabs[1]:
    st.markdown("<div class='section-header'>Experiencia Profesional</div>", unsafe_allow_html=True)
    experiences = [
        {
            "role": "Data Scientist",
            "company": "Instituto de Matemáticas (UNAM)",
            "description": "Desarrollo de modelos predictivos y análisis de grandes volúmenes de datos. Implementé técnicas de machine learning para optimizar investigaciones y colaborar en publicaciones científicas de alto impacto."
        },
        {
            "role": "Machine Learning Engineer",
            "company": "Colmena Space (UNAM)",
            "description": "Diseñé simulaciones avanzadas para trayectorias de sondas lunares, optimizando recursos computacionales y elevando la precisión de los algoritmos en proyectos aeroespaciales."
        },
        {
            "role": "Analista de Datos",
            "company": "Asociación Aeroespacial de la Facultad de Ingeniería (UNAM)",
            "description": "Analicé datos experimentales de pruebas de cohetes y desarrollé dashboards interactivos para monitoreo en tiempo real, generando insights estratégicos para la optimización de lanzamientos."
        },
        {
            "role": "Desarrollador Web & Consultor Digital",
            "company": "Freelancer",
            "description": "He ejecutado diversos proyectos de desarrollo web, desde sitios informativos hasta plataformas e-commerce (ej. infrax.mx, tecistem.com), y he asesorado en transformación digital para PYMEs."
        },
        {
            "role": "Especialista en Automatización de Procesos",
            "company": "Holtmont México",
            "description": "Desarrollé sistemas de automatización utilizando Google Sheets y Apps Script, logrando reducir tiempos de respuesta y mejorar la eficiencia operativa en equipos multidisciplinarios."
        }
    ]
    for exp in experiences:
        st.markdown(
            f"<div class='card'><h3>{exp['role']} - {exp['company']}</h3><p>{exp['description']}</p></div>",
            unsafe_allow_html=True
        )

# =============================
# Educación
# =============================
with tabs[2]:
    st.markdown("<div class='section-header'>Educación</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='card'><h3>Licenciatura en Física y Matemáticas</h3>"
        "<p>Universidad Nacional Autónoma de México (UNAM) (2019 - 2024)</p>"
        "<p>Formación integral en fenómenos físicos y matemáticos, complementada con cursos avanzados en programación, análisis de datos e investigación científica. "
        "Participé en proyectos de simulación de sistemas cuánticos y diseño de algoritmos, recibiendo diversos reconocimientos académicos.</p></div>",
        unsafe_allow_html=True
    )

# =============================
# Certificaciones y Cursos
# =============================
with tabs[3]:
    st.markdown("<div class='section-header'>Certificaciones y Cursos</div>", unsafe_allow_html=True)
    certifications = [
        "Certificado en Ciencia de Datos - Microsoft",
        "Certificado en Análisis de Datos - Microsoft",
        "Certificado en SQL y Azure - Microsoft",
        "Certificado en Data Driven Astronomy - UNAM",
        "Certificado en Python - Microsoft",
        "Certificado en Python y Análisis de Datos - Santander"
    ]
    for cert in certifications:
        st.markdown(f"<div class='card'><p>{cert}</p></div>", unsafe_allow_html=True)

# =============================
# Habilidades Técnicas
# =============================
with tabs[4]:
    st.markdown("<div class='section-header'>Habilidades Técnicas</div>", unsafe_allow_html=True)
    skills = """
    - **Lenguajes:** Python, SQL, C++, JavaScript  
    - **Frameworks y bibliotecas:** numpy, pandas, matplotlib, seaborn, TensorFlow, PyTorch, scikit-learn, PySpark  
    - **Bases de datos:** SQL, MongoDB, Cassandra  
    - **Visualización:** Looker Studio, matplotlib, seaborn  
    - **Cloud y DevOps:** AWS, Azure, Docker, Git  
    - **Metodologías:** Scrum, Kanban
    """
    st.markdown(f"<div class='card'>{skills}</div>", unsafe_allow_html=True)

# =============================
# FIN DE LA PARTE 1
# =============================
# PARTE 2: Secciones adicionales
# =============================

tabs_extra = st.tabs(["Proyectos Destacados", "Visualizaciones Interactivas", "Descargas de CVs", "Logros y Reconocimientos"])

# -----------------------------
# Proyectos Destacados
# -----------------------------
with tabs_extra[0]:
    st.markdown("<div class='section-header'>Proyectos Destacados</div>", unsafe_allow_html=True)
    projects = [
        {
            "title": "Predicciones de las Elecciones de EE. UU. 2024 usando Machine Learning",
            "description": (
                "Desarrollé modelos predictivos combinando análisis de datos históricos y algoritmos de aprendizaje automático "
                "para estimar tendencias electorales en estados clave. Esta herramienta proporciona insights estratégicos para campañas y analistas, "
                "aportando un enfoque innovador en la interpretación de resultados electorales. 🗳️"
            ),
            "link": "https://lnkd.in/e7DrEZEE"
        },
        {
            "title": "Artículo de Divulgación: Nobel de Física 2024 y Materiales 2D",
            "description": (
                "Exploré el impacto de la inteligencia artificial en el descubrimiento de nuevos materiales bidimensionales. "
                "Este artículo fusiona ciencia de datos y física, mostrando cómo el análisis avanzado puede revolucionar el diseño de compuestos innovadores."
            ),
            "link": "https://lnkd.in/e6q5QQfg"
        },
        {
            "title": "Aplicación de Predicción de Enfermedades Dentales",
            "description": (
                "Implementé una solución de deep learning utilizando YOLO V5 y Flask para analizar radiografías panorámicas y detectar enfermedades dentales. "
                "La aplicación mejora la precisión diagnóstica en clínicas odontológicas, facilitando intervenciones tempranas y optimizando la atención al paciente."
            ),
            "link": "https://github.com/usuario/dental-disease-detection"
        },
        {
            "title": "Digitalización del Mercado Xochiquetzal",
            "description": (
                "Lideré el desarrollo de una plataforma e-commerce para comerciantes locales, facilitando la transición digital y aumentando la visibilidad y ventas "
                "en un mercado tradicional. Este proyecto impulsa la economía local a través de la tecnología. 💼"
            ),
            "link": "#"
        },
        {
            "title": "Hackathon Internacional: AI Innovator Challenge",
            "description": (
                "Participé y fui reconocido en un hackathon internacional presentando una solución innovadora de inteligencia artificial aplicada a la optimización "
                "de recursos en tiempo real, demostrando la capacidad de integrar técnicas avanzadas en contextos competitivos."
            ),
            "link": "#"
        },
        {
            "title": "Análisis Predictivo en el Sector Financiero",
            "description": (
                "Desarrollé modelos de análisis predictivo para identificar tendencias en el mercado financiero, permitiendo a empresas anticipar movimientos y "
                "tomar decisiones estratégicas basadas en datos. Este proyecto evidencia el poder del análisis de datos en escenarios económicos complejos."
            ),
            "link": "#"
        }
    ]
    for proj in projects:
        st.markdown(
            f"<div class='card'><h3>{proj['title']}</h3><p>{proj['description']}</p>"
            f"<a href='{proj['link']}' target='_blank'>Ver más</a></div>",
            unsafe_allow_html=True
        )

# -----------------------------
# Visualizaciones Interactivas
# -----------------------------
with tabs_extra[1]:
    st.markdown("<div class='section-header'>Visualizaciones Interactivas</div>", unsafe_allow_html=True)
    st.write(
        "Explora mis visualizaciones de datos que muestran mi dominio en el análisis y la interpretación de información. "
        "Estas herramientas interactivas permiten apreciar de forma dinámica los resultados de mis modelos y análisis."
    )
    # Ejemplo: gráfico de barras para habilidades
    data = pd.DataFrame({
        "Habilidad": ["Python", "SQL", "Machine Learning", "Visualización", "Cloud"],
        "Nivel": [95, 90, 85, 80, 75]
    })
    fig_bar = px.bar(data, x="Habilidad", y="Nivel", title="Dominio de Habilidades", labels={"Nivel": "Porcentaje (%)"})
    st.plotly_chart(fig_bar)
    
    # Ejemplo: gráfico de dispersión para mostrar progreso en proyectos
    data_scatter = pd.DataFrame({
        "Tiempo (meses)": [1, 2, 3, 4, 5, 6],
        "Progreso (%)": [10, 30, 50, 70, 85, 95]
    })
    fig_scatter = px.scatter(data_scatter, x="Tiempo (meses)", y="Progreso (%)", title="Progreso en Proyectos a lo largo del Tiempo")
    st.plotly_chart(fig_scatter)

# -----------------------------
# Descargas de CVs
# -----------------------------
with tabs_extra[2]:
    st.markdown("<div class='section-header'>Descargas de CVs</div>", unsafe_allow_html=True)
    st.write("Descarga mi CV en el idioma que prefieras para conocer más detalles sobre mi experiencia y formación profesional.")
    col1, col2 = st.columns(2)
    with col1:
        if Path(cv_es_path).is_file():
            with open(cv_es_path, "rb") as file_data:
                st.download_button(
                    label="📄 Descargar CV en Español",
                    data=file_data,
                    file_name="CV-AlexanderEduardoRojasGaray.pdf",
                    mime="application/pdf",
                    key="cv_es_extra"
                )
    with col2:
        if Path(cv_en_path).is_file():
            with open(cv_en_path, "rb") as file_data:
                st.download_button(
                    label="📄 Download CV in English",
                    data=file_data,
                    file_name="CV-AlexanderEduardoRojasGaray-EN.pdf",
                    mime="application/pdf",
                    key="cv_en_extra"
                )

# -----------------------------
# Logros y Reconocimientos
# -----------------------------
with tabs_extra[3]:
    st.markdown("<div class='section-header'>Logros y Reconocimientos</div>", unsafe_allow_html=True)
    achievements = [
        "🏆 **Premio a la Innovación Tecnológica** en hackathons internacionales, destacando soluciones basadas en machine learning.",
        "🎤 **Ponente en Conferencias Internacionales** sobre Data Science, compartiendo metodologías y experiencias innovadoras.",
        "🤝 **Colaborador Activo en Proyectos Open Source**, contribuyendo al desarrollo de herramientas y bibliotecas en Python.",
        "📈 **Reconocido por la Excelencia Profesional** en transformación digital y análisis predictivo en diversos sectores.",
        "🚀 **Participante Destacado en Programas de Innovación y Emprendimiento**, impulsando proyectos que integran ciencia de datos y tecnología."
    ]
    for achievement in achievements:
        st.markdown(f"<div class='card'><p>{achievement}</p></div>", unsafe_allow_html=True)
