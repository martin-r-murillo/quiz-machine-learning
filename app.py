import streamlit as st
import time

# --- 1. DATOS (Base de datos de preguntas) ---
# He incluido una muestra representativa. Para el examen completo, 
# expande esta lista con el mismo formato.

FULL_DATA = [
    {
        "tema": "Tema 1. Introducción al Machine Learning",
        "tests": [
            {
                "id": "Microtest 1.2",
                "questions": [
                    {"q": "¿Qué tipo de aprendizajes existen dentro del machine learning?", "options": ["Aprendizaje supervisado", "Aprendizaje automático", "Aprendizaje no supervisado", "Aprendizaje por refuerzo"], "answer": ["Aprendizaje supervisado", "Aprendizaje no supervisado", "Aprendizaje por refuerzo"], "type": "multi", "explanation": "Los tres pilares son supervisado, no supervisado y refuerzo. 'Automático' es el nombre del campo."},
                    {"q": "En el aprendizaje supervisado encontramos los siguientes tipos de problema:", "options": ["Problemas de regresión", "Problemas de no linealidad", "Problemas de clasificación", "Problemas de generalización"], "answer": ["Problemas de regresión", "Problemas de clasificación"], "type": "multi", "explanation": "Se divide en clasificación (clases) y regresión (valores continuos)."},
                    {"q": "Señale las afirmaciones FALSAS sobre el aprendizaje automático:", "options": ["Existe un solo algoritmo universal", "Es una de las áreas de la IA", "Es una de las tres áreas del machine learning", "Aprendizaje automático y machine learning son lo mismo"], "answer": ["Existe un solo algoritmo universal", "Es una de las tres áreas del machine learning"], "type": "multi", "explanation": "No existe un algoritmo único (No Free Lunch) y la afirmación de las 'tres áreas' es recursiva/falsa."}
                ]
            }
        ]
    },
    {
        "tema": "Tema 2. Regresión",
        "tests": [
             {
                "id": "Microtest 2.3 (Cálculo de Errores)",
                "questions": [
                    { "q": "Dados los errores cuadráticos, hallar el MSE (Mean Squared Error):", "options": ["9.68", "21.05", "3.11", "58.07"], "answer": ["9.68"], "type": "single", "explanation": "Es el promedio de los errores al cuadrado." },
                    { "q": "Hallar el MAE (Mean Absolute Error):", "options": ["2.78", "3.45", "1.12", "0.99"], "answer": ["2.78"], "type": "single", "explanation": "Es el promedio de las diferencias absolutas." }
                ]
            }
        ]
    },
    {
        "tema": "Tema 3. Clasificación",
        "tests": [
            {
                "id": "Microtest 3.3",
                "questions": [
                    { "q": "Dada una matriz de confusión, hallar la Exactitud (Accuracy):", "options": ["0.92", "0.88", "0.95", "0.45"], "answer": ["0.92"], "type": "single", "explanation": "(TP+TN)/Total = 0.92." },
                    { "q": "Hallar la Precisión con truncamiento a 2 decimales:", "options": ["0.91", "0.92", "0.85", "0.99"], "answer": ["0.91"], "type": "single", "explanation": "El cálculo da 0.918... Truncado es 0.91." }
                ]
            }
        ]
    }
]

# --- 2. CONFIGURACIÓN Y ESTILOS. ---
st.set_page_config(page_title="Microtest Simulator", page_icon="🎓", layout="centered")

# --- 2. CONFIGURACIÓN Y ESTILOS ---
st.set_page_config(page_title="Microtest Simulator", page_icon="🎓", layout="centered")

# CSS FINAL: Corrección específica para textos de opciones
st.markdown("""
    <style>
    /* 1. Fondo general claro */
    .stApp {
        background-color: #f5f7f9;
    }
    
    /* 2. Tarjeta blanca para la pregunta */
    .question-card {
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }

    /* 3. FUERZA BRUTA: Todo el texto a negro casi puro */
    h1, h2, h3, h4, h5, h6, p, label, span, div {
        color: #1f1f1f !important;
    }
    
    /* 4. CORRECCIÓN ESPECÍFICA PARA OPCIONES (Radio y Checkbox) */
    /* Esto arregla el texto invisible al lado de los botones */
    div[data-testid="stMarkdownContainer"] p {
        color: #1f1f1f !important;
    }
    
    /* 5. Excepción: Botones (Mantener texto blanco) */
    div.stButton > button {
        color: white !important;
        background-color: #ff4b4b;
        border: none;
    }
    div.stButton > button p {
        color: white !important; /* Forzar texto blanco dentro del botón */
    }
    
    /* 6. Barra de estado */
    .status-bar {
        color: #666 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. GESTIÓN DEL ESTADO (SESSION STATE) ---
if 'current_test_id' not in st.session_state:
    st.session_state.current_test_id = None
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False
if 'last_answer_correct' not in st.session_state:
    st.session_state.last_answer_correct = None
if 'show_explanation' not in st.session_state:
    st.session_state.show_explanation = False

# --- 4. FUNCIONES DE LÓGICA ---
def reset_quiz():
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.quiz_finished = False
    st.session_state.show_explanation = False
    st.session_state.last_answer_correct = None

def submit_answer(user_selection, correct_answers, q_type):
    # Lógica de corrección
    is_correct = False
    if q_type == "single":
        if user_selection == correct_answers[0]:
            is_correct = True
    else: # Multi
        # En multi, verificamos que la selección esté dentro de las correctas
        # Simplificación para UI: Si selecciona AL MENOS UNA correcta cuenta parcial o total
        # Para este simulador estricto: Debe coincidir exactamente con el set
        if set(user_selection) == set(correct_answers):
            is_correct = True
    
    if is_correct:
        st.session_state.score += 1
        st.session_state.last_answer_correct = True
    else:
        st.session_state.last_answer_correct = False
    
    st.session_state.show_explanation = True

def next_question(total_questions):
    if st.session_state.q_index < total_questions - 1:
        st.session_state.q_index += 1
        st.session_state.show_explanation = False
        st.session_state.last_answer_correct = None
    else:
        st.session_state.quiz_finished = True

# --- 5. INTERFAZ ---

# BARRA LATERAL (Selección de Tema)
with st.sidebar:
    st.title("📚 Temario")
    temas = [t["tema"] for t in FULL_DATA]
    tema_sel = st.selectbox("Elige un Módulo:", temas)
    
    datos_tema = next(item for item in FULL_DATA if item["tema"] == tema_sel)
    tests_ids = [t["id"] for t in datos_tema["tests"]]
    test_sel = st.radio("Elige Microtest:", tests_ids)
    
    if st.session_state.current_test_id != test_sel:
        st.session_state.current_test_id = test_sel
        reset_quiz()
    
    st.divider()
    st.markdown(f"**Puntuación Actual:** {st.session_state.score}")
    if st.button("🔄 Reiniciar Test"):
        reset_quiz()
        st.rerun()

# ÁREA PRINCIPAL
datos_test = next(t for t in datos_tema["tests"] if t["id"] == test_sel)
preguntas = datos_test["questions"]
total_q = len(preguntas)

# PANTALLA DE RESULTADOS FINAL
if st.session_state.quiz_finished:
    st.balloons()
    st.markdown("<div class='question-card'>", unsafe_allow_html=True)
    st.title("🏆 ¡Test Completado!")
    
    nota = (st.session_state.score / total_q) * 10
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.metric("Nota Final", f"{nota:.2f} / 10")
        if nota >= 9:
            st.success("¡Excelente trabajo! Dominas este tema.")
        elif nota >= 6:
            st.warning("Aprobado, pero repasa los errores.")
        else:
            st.error("Necesitas reforzar conceptos.")
            
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("Intentar de nuevo"):
        reset_quiz()
        st.rerun()

# PANTALLA DE PREGUNTA (Quiz Activo)
else:
    q_actual = preguntas[st.session_state.q_index]
    
    # Barra de Progreso
    progreso = (st.session_state.q_index + 1) / total_q
    st.progress(progreso)
    st.markdown(f"<div class='status-bar'>Pregunta {st.session_state.q_index + 1} de {total_q}</div>", unsafe_allow_html=True)

    # Tarjeta de Pregunta
    st.markdown(f"""
    <div class='question-card'>
        <h3>{q_actual['q']}</h3>
    </div>
    """, unsafe_allow_html=True)

    # Área de Respuesta (Si no ha respondido aún)
    if not st.session_state.show_explanation:
        with st.form(key=f"form_{st.session_state.q_index}"):
            if q_actual["type"] == "single":
                respuesta = st.radio("Selecciona una opción:", q_actual["options"], index=None, key="radio_option")
            else:
                st.write("*Selección Múltiple (marca todas las correctas):*")
                respuesta = []
                for opt in q_actual["options"]:
                    if st.checkbox(opt, key=opt):
                        respuesta.append(opt)
            
            st.markdown("<br>", unsafe_allow_html=True)
            submit = st.form_submit_button("Comprobar Respuesta ➔")
            
            if submit:
                if not respuesta:
                    st.warning("Por favor selecciona una opción.")
                else:
                    submit_answer(respuesta, q_actual["answer"], q_actual["type"])
                    st.rerun()

    # Área de Feedback (Después de responder)
    else:
        if st.session_state.last_answer_correct:
            st.success("✅ ¡Correcto!")
        else:
            st.error("❌ Incorrecto")
            st.write(f"**La respuesta correcta era:** {', '.join(q_actual['answer'])}")
        
        st.info(f"💡 **Explicación:** {q_actual['explanation']}")
        
        if st.button("Siguiente Pregunta ➔"):
            next_question(total_q)
            st.rerun()
