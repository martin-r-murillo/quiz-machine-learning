import streamlit as st
import random
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
                    {
                        "q": "¿Qué tipo de aprendizajes existen dentro del machine learning?",
                        "options": ["Aprendizaje supervisado", "Aprendizaje automático", "Aprendizaje no supervisado", "Aprendizaje por refuerzo"],
                        "answer": ["Aprendizaje supervisado", "Aprendizaje no supervisado", "Aprendizaje por refuerzo"],
                        "type": "multi",
                        "explanation": "Los tres paradigmas principales son: Supervisado (con etiquetas), No Supervisado (sin etiquetas) y Por Refuerzo (recompensas). 'Aprendizaje automático' es el nombre del campo en sí."
                    },
                    {
                        "q": "En el aprendizaje supervisado encontramos los siguientes tipos de problema:",
                        "options": ["Problemas de regresión", "Problemas de no linealidad", "Problemas de clasificación", "Problemas de generalización"],
                        "answer": ["Problemas de regresión", "Problemas de clasificación"],
                        "type": "multi",
                        "explanation": "El aprendizaje supervisado se divide en: Clasificación (predecir categorías discretras) y Regresión (predecir valores continuos)."
                    },
                    {
                        "q": "Señale las afirmaciones FALSAS sobre el aprendizaje automático:",
                        "options": ["Existe un solo algoritmo de aprendizaje automático que se puede adaptar a cualquier circunstancia", "El aprendizaje automático es una de las áreas de la inteligencia artificial", "El aprendizaje automático es una de las tres áreas del machine learning", "Aprendizaje automático y machine learning hacen referencia a lo mismo"],
                        "answer": ["Existe un solo algoritmo de aprendizaje automático que se puede adaptar a cualquier circunstancia", "El aprendizaje automático es una de las tres áreas del machine learning"],
                        "type": "multi",
                        "explanation": "No existe un algoritmo maestro (No Free Lunch Theorem). Además, decir que el 'aprendizaje automático es un área del machine learning' es redundante y falso (son lo mismo)."
                    }
                ]
            },
            {
                "id": "Microtest 1.3",
                "questions": [
                    {
                        "q": "No es una etapa dentro del proceso general de modelado del aprendizaje automático:",
                        "options": ["Definir el problema", "Dividir el conjunto de entrenamiento y test", "Entrenar el modelo", "Numerar los ejemplos de entrenamiento"],
                        "answer": ["Numerar los ejemplos de entrenamiento"],
                        "type": "single",
                        "explanation": "Numerar los ejemplos es una tarea trivial de gestión de datos, no una etapa fundamental del modelado predictivo como definir, dividir o entrenar."
                    },
                    {
                        "q": "La validación cruzada consiste en:",
                        "options": ["Generar 5 conjuntos de entrenamiento", "Dividir en k grupos el conjunto de datos de entrenamiento y utilizar uno de esos grupos como conjunto de test en cada una de las k iteraciones", "Utilizar la técnica de hold-out una sola vez", "Dividir el conjunto de datos en k grupos y entrenar un modelo diferente con cada grupo"],
                        "answer": ["Dividir en k grupos el conjunto de datos de entrenamiento y utilizar uno de esos grupos como conjunto de test en cada una de las k iteraciones"],
                        "type": "single",
                        "explanation": "Es la definición de K-Fold Cross Validation: rotar el conjunto de test k veces para validar la robustez del modelo."
                    },
                    {
                        "q": "En el ejercicio del iris realizado en Python la alta exactitud es debido a:",
                        "options": ["Es producto del azar", "Es un conjunto de datos muy sencillo que alcanza fácilmente una buena exactitud con cualquier modelo", "Tiene la cantidad de datos óptima", "Tiene el mismo número de datos por cada clase"],
                        "answer": ["Es un conjunto de datos muy sencillo que alcanza fácilmente una buena exactitud con cualquier modelo"],
                        "type": "single",
                        "explanation": "El dataset Iris es pequeño y sus clases (especialmente Setosa) son linealmente separables, lo que facilita obtener >95% de exactitud con modelos simples."
                    }
                ]
            },
            {
                "id": "Microtest 1.4",
                "questions": [
                    {
                        "q": "El aprendizaje supervisado se divide en problemas de agrupamiento y detección de anomalías:",
                        "options": ["Verdadero", "Falso"],
                        "answer": ["Falso"],
                        "type": "single",
                        "explanation": "El agrupamiento (clustering) es aprendizaje NO supervisado. La detección de anomalías puede ser ambos, pero la división clásica del supervisado es Regresión y Clasificación."
                    },
                    {
                        "q": "El problema de agrupamiento consiste en dividir los datos en grupos con características similares:",
                        "options": ["Verdadero", "Falso"],
                        "answer": ["Verdadero"],
                        "type": "single",
                        "explanation": "Es la definición correcta de Clustering."
                    },
                    {
                        "q": "El problema de detección de anomalías consiste en reducir la dimensionalidad para crear una nueva representación:",
                        "options": ["Verdadero", "Falso"],
                        "answer": ["Falso"],
                        "type": "single",
                        "explanation": "La detección de anomalías busca datos atípicos (outliers). Reducir la dimensionalidad es otra tarea distinta (ej. PCA)."
                    }
                ]
            }
        ]
    },
    {
        "tema": "Tema 2. Algoritmos de Regresión",
        "tests": [
            {
                "id": "Microtest 2.2",
                "questions": [
                    {
                        "q": "No es un nombre con el que se le conoce a la variable respuesta:",
                        "options": ["Clase", "Variable objetivo", "Target", "Regressors"],
                        "answer": ["Regressors"],
                        "type": "single",
                        "explanation": "'Regressors' hace referencia a las variables predictoras (inputs), no a la salida."
                    },
                    {
                        "q": "No es un nombre para la variable predictora:",
                        "options": ["Entrada o input", "Class o clase", "Variable independiente", "Características o features"],
                        "answer": ["Class o clase"],
                        "type": "single",
                        "explanation": "'Clase' es típicamente la variable objetivo en problemas de clasificación, no una predictora."
                    },
                    {
                        "q": "A la función f(x) ideal se la conoce con el nombre de:",
                        "options": ["Función estimadora", "Función perfecta", "Función de regresión", "Función objetivo"],
                        "answer": ["Función de regresión"],
                        "type": "single",
                        "explanation": "En el contexto teórico estadístico, la función verdadera que genera los datos se llama función de regresión."
                    }
                ]
            },
            {
                "id": "Microtest 2.3 (Cálculos)",
                "questions": [
                    {
                        "q": "Hallar el MSE (Mean Squared Error) de los datos proporcionados (redondeo a 2 decimales):",
                        "options": ["9.68", "21.05", "3.11", "58.07"],
                        "answer": ["9.68"],
                        "type": "single",
                        "explanation": "Suma de errores al cuadrado dividido por N. Cálculo: 58.07 / 6 ≈ 9.678 -> 9.68."
                    },
                    {
                        "q": "Hallar el MAE (Mean Absolute Error) con 2 decimales:",
                        "options": ["2.78", "3.45", "1.12", "0.99"],
                        "answer": ["2.78"],
                        "type": "single",
                        "explanation": "Promedio de las diferencias absolutas. Cálculo: 16.68 / 6 = 2.78."
                    },
                    {
                        "q": "Hallar el RMSE (Root Mean Squared Error) con truncamiento a 2 decimales:",
                        "options": ["3.11", "9.68", "1.55", "4.20"],
                        "answer": ["3.11"],
                        "type": "single",
                        "explanation": "Raíz cuadrada del MSE. sqrt(9.678) ≈ 3.1109. Truncado a dos decimales: 3.11."
                    }
                ]
            },
            {
                "id": "Microtest 2.4",
                "questions": [
                    { "q": "El error cuadrático medio puede llegar a ser muy grande:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Sí, al elevar al cuadrado, los errores grandes se penalizan mucho y la métrica no tiene límite superior." },
                    { "q": "Al entrenar un modelo para regresión se dividen los datos en entrenamiento y test:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Es fundamental para evaluar la capacidad de generalización del modelo." },
                    { "q": "El coeficiente de determinación puede ser un número muy grande:", "options": ["Verdadero", "Falso"], "answer": ["Falso"], "type": "single", "explanation": "El R² tiene un valor máximo de 1 (ajuste perfecto)." }
                ]
            }
        ]
    },
    {
        "tema": "Tema 3. Algoritmos de Clasificación",
        "tests": [
            {
                "id": "Microtest 3.2",
                "questions": [
                    { "q": "La clasificación puede ser:", "options": ["Binaria", "Multiclase", "Lineal", "Polinómica"], "answer": ["Binaria", "Multiclase"], "type": "multi", "explanation": "Según el número de clases objetivo, se divide en Binaria (2 clases) o Multiclase (>2)." },
                    { "q": "Si la probabilidad es 0.55 (clase 1) y 0.45 (clase 2), se afirma que:", "options": ["El límite de pertenencia es muy cercano", "Pertenece a la clase 1", "Pertenece a la clase 2", "No se clasifica"], "answer": ["El límite de pertenencia es muy cercano", "Pertenece a la clase 1"], "type": "multi", "explanation": "Pertenece a la clase 1 (p > 0.5) pero con baja confianza (margen estrecho)." },
                    { "q": "Debe tenerse preparado antes de crear la matriz de confusión:", "options": ["Un vector con la clasificación real", "Un vector con la clasificación predicha", "La tabla de positivos", "La variable a predecir"], "answer": ["Un vector con la clasificación real", "Un vector con la clasificación predicha"], "type": "multi", "explanation": "La matriz compara lo Real vs lo Predicho." }
                ]
            },
            {
                "id": "Microtest 3.3 (Matriz Confusión)",
                "questions": [
                    { "q": "Hallar la Exactitud (Accuracy) truncada a 2 decimales:", "options": ["0.92", "0.88", "0.95", "0.45"], "answer": ["0.92"], "type": "single", "explanation": "(TP + TN) / Total = (158 + 264) / 458 ≈ 0.921 -> 0.92." },
                    { "q": "Hallar la Precisión (Precision) con TRUNCAMIENTO a 2 decimales:", "options": ["0.91", "0.92", "0.85", "0.99"], "answer": ["0.91"], "type": "single", "explanation": "TP / (TP + FP) = 158 / (158 + 14) = 158/172 ≈ 0.9186. OJO: El test pide TRUNCAMIENTO, no redondeo. 0.91 es la correcta." },
                    { "q": "Hallar el Recall (Sensibilidad) truncado a 2 decimales:", "options": ["0.88", "0.90", "0.75", "0.82"], "answer": ["0.88"], "type": "single", "explanation": "TP / (TP + FN) = 158 / (158 + 22) ≈ 0.877 -> Redondeo/Truncado cercano 0.88." }
                ]
            },
            {
                "id": "Microtest 3.4 (Curva ROC)",
                "questions": [
                    { "q": "Una curva ROC representa tasa de verdaderos positivos vs tasa de falsos positivos:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "TPR (eje Y) vs FPR (eje X)." },
                    { "q": "El objetivo de una curva ROC es clasificar bien las instancias:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Ayuda a seleccionar el umbral óptimo de clasificación." },
                    { "q": "El área bajo la curva superior a 0.7 es un indicador de un buen modelo:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "0.5 es aleatorio. >0.7 se considera aceptable/bueno." }
                ]
            }
        ]
    },
    {
        "tema": "Tema 4. Naive Bayes",
        "tests": [
            {
                "id": "Microtest 4.2",
                "questions": [
                    { "q": "En la fórmula de Bayes, P(Xi | Z) hace referencia a:", "options": ["Probabilidad condicionada", "Probabilidad a priori", "Probabilidad a posteriori"], "answer": ["Probabilidad condicionada"], "type": "single", "explanation": "Es la probabilidad de ver los datos (Xi) dado que pertenecen a la clase (Z), también llamada Verosimilitud." },
                    { "q": "Si P(Spam) es 0.2, hablamos de:", "options": ["Probabilidad a priori", "Probabilidad a posteriori"], "answer": ["Probabilidad a priori"], "type": "single", "explanation": "Es la probabilidad base de la clase antes de analizar el mensaje." },
                    { "q": "Si P(Spam | Mensaje) es 0.7:", "options": ["Es muy probable que sea spam", "Es muy probable que sea ham"], "answer": ["Es muy probable que sea spam"], "type": "single", "explanation": "Supera el umbral de 0.5." }
                ]
            },
            {
                "id": "Microtest 4.3 (Cálculos Bayes)",
                "questions": [
                    { "q": "Hallar P(Si | Soleado):", "options": ["0.6", "0.4", "0.3", "0.9"], "answer": ["0.6"], "type": "single", "explanation": "P(Sol|Si)*P(Si) / P(Sol) = (3/9 * 9/14) / (5/14) = (3/14) / (5/14) = 3/5 = 0.6." },
                    { "q": "Hallar P(No | Soleado):", "options": ["0.4", "0.6", "0.5", "0.1"], "answer": ["0.4"], "type": "single", "explanation": "1 - P(Si|Soleado) = 1 - 0.6 = 0.4." },
                    { "q": "Hallar P(No | Lloviendo):", "options": ["0.6", "0.4", "0.2", "0.8"], "answer": ["0.6"], "type": "single", "explanation": "P(Lluvia|No)=3/5, P(No)=5/14. P(Lluvia)=5/14. Resultado: (3/5 * 5/14) / (5/14) = 3/5 = 0.6." }
                ]
            },
            {
                "id": "Microtest 4.4",
                "questions": [
                    { "q": "Tipos de datos en Naive Bayes:", "options": ["Numéricos", "Categóricos", "Numéricos discretizados y categóricos", "Enteros"], "answer": ["Numéricos discretizados y categóricos"], "type": "single", "explanation": "El NB estándar trabaja con conteos o categorías. Los continuos suelen discretizarse o usar Gaussian NB." },
                    { "q": "Ventaja de Naive Bayes:", "options": ["Bajo coste computacional", "Se ajusta perfectamente", "Fácil de integrar"], "answer": ["Bajo coste computacional"], "type": "single", "explanation": "Es muy rápido y simple." },
                    { "q": "Desventaja de Naive Bayes:", "options": ["Los predictores se consideran independientes", "Es lento", "Difícil de interpretar"], "answer": ["Los predictores se consideran independientes"], "type": "single", "explanation": "La asunción de 'ingenuidad' (independencia) casi nunca se cumple en la realidad." }
                ]
            }
        ]
    },
    {
        "tema": "Tema 5. Árboles de Decisión",
        "tests": [
            {
                "id": "Microtest 5.1",
                "questions": [
                    { "q": "¿Cuál es la base de los árboles de decisión?", "options": ["Teoría de juegos", "Análisis estadístico y teoría de la información", "Teorema de Bayes"], "answer": ["Análisis estadístico y teoría de la información"], "type": "single", "explanation": "Se basan en conceptos como Entropía y Ganancia de Información." },
                    { "q": "¿Qué representa un nodo interno?", "options": ["Una característica", "Una clase", "Una probabilidad"], "answer": ["Una característica"], "type": "single", "explanation": "Es donde se toma una decisión basada en un atributo." },
                    { "q": "¿Qué representa un nodo hoja?", "options": ["La solución o clase", "Una característica", "Una probabilidad"], "answer": ["La solución o clase"], "type": "single", "explanation": "Es el resultado final de la rama." }
                ]
            },
            {
                "id": "Microtest 5.2 (Entropía)",
                "questions": [
                    { "q": "Hallar la entropía para E(riesgo | Excelente):", "options": ["0.811", "-0.811", "0.92", "0"], "answer": ["0.811"], "type": "single", "explanation": "-(3/4 log2(3/4) + 1/4 log2(1/4)) ≈ 0.811." },
                    { "q": "Hallar la entropía para E(riesgo | Bueno) (Truncamiento/Redondeo):", "options": ["0.92", "0.91", "0.96", "-0.92"], "answer": ["0.92", "0.91"], "type": "single", "explanation": "-(4/6 log2(4/6) + 2/6 log2(2/6)) ≈ 0.918. El test suele aceptar 0.92 por redondeo o 0.91 por truncamiento." },
                    { "q": "Hallar la entropía para E(riesgo | Pobre):", "options": ["0", "1", "0.5", "0.8"], "answer": ["0"], "type": "single", "explanation": "Es un nodo puro (todos son 'Alto riesgo'). La entropía es 0." }
                ]
            },
            {
                "id": "Microtest 5.3",
                "questions": [
                    { "q": "Los árboles complejos pueden caer en overfitting:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Si crecen mucho, memorizan el ruido de los datos." },
                    { "q": "La estrategia de poda consiste primero en generar un árbol grande y luego crear subárboles:", "options": ["Verdadero", "Falso"], "answer": ["Falso"], "type": "single", "explanation": "Aunque el 'post-pruning' hace algo similar, la definición dada en el test es marcada como Falsa por ser inexacta con el procedimiento estándar." },
                    { "q": "Siempre es mejor un árbol que un modelo lineal:", "options": ["Verdadero", "Falso"], "answer": ["Falso"], "type": "single", "explanation": "Depende del problema (No Free Lunch)." }
                ]
            },
            {
                "id": "Microtest 5.4",
                "questions": [
                    { "q": "Es cierto sobre árboles grandes:", "options": ["Son fáciles de interpretar", "Son difíciles de interpretar", "Nunca deben podarse"], "answer": ["Son difíciles de interpretar"], "type": "single", "explanation": "Demasiadas ramas hacen imposible seguir la lógica humana." },
                    { "q": "Fortaleza de los árboles:", "options": ["Se pueden utilizar con pocos o muchos datos", "Son cajas negras", "Requieren muchos recursos"], "answer": ["Se pueden utilizar con pocos o muchos datos"], "type": "single", "explanation": "Son muy versátiles." },
                    { "q": "Los árboles utilizan:", "options": ["Todas las variables", "Solo las variables importantes", "Solo variables numéricas"], "answer": ["Solo las variables importantes"], "type": "single", "explanation": "Realizan selección implícita de características al elegir los mejores splits." }
                ]
            }
        ]
    },
    {
        "tema": "Tema 6. Random Forests",
        "tests": [
            { "id": "Microtest 6.2", "questions": [
                { "q": "La selección en Bagging se realiza:", "options": ["Dividiendo train en subconjuntos aleatorios con misma cantidad", "Dividiendo en diferentes tamaños"], "answer": ["Dividiendo train en subconjuntos aleatorios con misma cantidad"], "type": "single", "explanation": "Muestreo con reemplazo (bootstrap) del mismo tamaño N." },
                { "q": "Con cada subconjunto:", "options": ["Se entrena un modelo con todos los individuos del subconjunto", "Se entrena y evalúa"], "answer": ["Se entrena un modelo con todos los individuos del subconjunto"], "type": "single", "explanation": "Cada árbol ve solo su 'bag' de datos." },
                { "q": "Bagging significa:", "options": ["Bootstrap aggregating", "Bosques aleatorios"], "answer": ["Bootstrap aggregating"], "type": "single", "explanation": "Es el acrónimo correcto." }
            ]},
            { "id": "Microtest 6.3", "questions": [
                { "q": "Razón para usar gran número de árboles:", "options": ["Para que cada característica tenga oportunidad de aparecer", "Para evaluar mismas características"], "answer": ["Para que cada característica tenga oportunidad de aparecer"], "type": "single", "explanation": "Y reducir varianza." },
                { "q": "Out of bag error es:", "options": ["Método de medida de predicción cuando se usa bagging", "Error de sensibilidad"], "answer": ["Método de medida de predicción cuando se usa bagging"], "type": "single", "explanation": "Usa los datos no vistos para validar." },
                { "q": "Selección de predictores en split:", "options": ["Selección aleatoria de m predictores", "Selección secuencial"], "answer": ["Selección aleatoria de m predictores"], "type": "single", "explanation": "Diferencia clave con Bagging normal." }
            ]},
            { "id": "Microtest 6.4", "questions": [
                { "q": "Al entrenar RF se obtiene:", "options": ["El error de cada árbol", "La importancia de las características", "La decisión de cada árbol"], "answer": ["El error de cada árbol", "La importancia de las características"], "type": "multi", "explanation": "RF permite calcular feature importance y OOB error." },
                { "q": "RF funciona con variables:", "options": ["Categóricas", "Continuas", "Discretas", "Todas"], "answer": ["Categóricas", "Continuas", "Discretas"], "type": "multi", "explanation": "Maneja todo tipo de datos." },
                { "q": "Falso sobre RF:", "options": ["Es fácilmente interpretable", "Trabaja solamente con pocos datos", "Gestiona bien datos faltantes"], "answer": ["Es fácilmente interpretable", "Trabaja solamente con pocos datos"], "type": "multi", "explanation": "RF es caja negra y funciona bien con muchos datos." }
            ]}
        ]
    },
    {
        "tema": "Tema 7. Ensembles (Bagging/Boosting)",
        "tests": [
             { "id": "Microtest 7.2", "questions": [
                { "q": "Técnicas de ensamble hacen referencia a:", "options": ["Construir varios modelos y combinar resultados", "Crear un modelo y ejecutarlo varias veces"], "answer": ["Construir varios modelos y combinar resultados"], "type": "single", "explanation": "La fuerza está en la combinación." },
                { "q": "Varianza de un modelo:", "options": ["Cuánto cambia el modelo dependiendo de los datos de entrenamiento", "Cuánto cambia la predicción"], "answer": ["Cuánto cambia el modelo dependiendo de los datos de entrenamiento"], "type": "single", "explanation": "Alta varianza = Overfitting." },
                { "q": "Bootstrapping significa:", "options": ["Estimación por muestreo con reemplazamiento", "Muestreo sin reemplazo"], "answer": ["Estimación por muestreo con reemplazamiento"], "type": "single", "explanation": "Concepto estadístico base." }
            ]},
            { "id": "Microtest 7.3", "questions": [
                { "q": "Bagging permite:", "options": ["Reducir la varianza", "Calcular varianza"], "answer": ["Reducir la varianza"], "type": "single", "explanation": "Al promediar modelos." },
                { "q": "Falso sobre bagging trees:", "options": ["Se entrenan B conjuntos de entrenamiento distintos", "Es un modelo que ensambla"], "answer": ["Se entrenan B conjuntos de entrenamiento distintos"], "type": "single", "explanation": "Falso porque NO son conjuntos distintos externos, son muestras del MISMO conjunto original." },
                { "q": "Predicción test en bagging:", "options": ["Voto mayoritario o promedio", "Mediana"], "answer": ["Voto mayoritario o promedio"], "type": "single", "explanation": "Clasificación = Voto, Regresión = Promedio." }
            ]},
             { "id": "Microtest 7.4", "questions": [
                { "q": "Boosting construye modelos secuenciales:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Cada modelo corrige al anterior." },
                { "q": "Boosting reduce el sesgo:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Se enfoca en los casos difíciles (bias)." },
                { "q": "Boosting crea copias usando bootstrap:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Usa pesos que equivalen a un remuestreo." }
            ]}
        ]
    },
    {
         "tema": "Tema 8. SVM (Máquinas de Soporte Vectorial)",
         "tests": [
             { "id": "Microtest 8.2", "questions": [
                { "q": "En SVM es cierto:", "options": ["Crea espacio de características", "El espacio es superior en dimensiones"], "answer": ["Crea espacio de características", "El espacio es superior en dimensiones"], "type": "multi", "explanation": "Proyecta a dimensiones altas (Kernel trick)." },
                { "q": "Hiperplano es:", "options": ["Recta en 2D", "Plano en 3D", "Recta en 3D"], "answer": ["Recta en 2D", "Plano en 3D"], "type": "multi", "explanation": "Generalización de recta/plano." },
                { "q": "Falso sobre SVM:", "options": ["Inventadas por Bayes", "Solo pocos datos", "Inventadas por Vapnik"], "answer": ["Inventadas por Bayes", "Solo pocos datos"], "type": "multi", "explanation": "Fueron inventadas por Vapnik." }
            ]},
            { "id": "Microtest 8.3", "questions": [
                { "q": "Mejor hiperplano:", "options": ["Mayor espacio entre dos clases", "Menor espacio"], "answer": ["Mayor espacio entre dos clases"], "type": "single", "explanation": "Máximo margen." },
                { "q": "Parámetro C:", "options": ["Cuanto más grande, menos errores permite", "Cuanto más grande, más errores"], "answer": ["Cuanto más grande, menos errores permite"], "type": "single", "explanation": "C penaliza los errores (Margen duro)." },
                { "q": "Expansión características:", "options": ["Espacio p a D donde D > p", "D < p"], "answer": ["Espacio p a D donde D > p"], "type": "single", "explanation": "Aumenta la dimensionalidad." }
            ]},
            { "id": "Microtest 8.4", "questions": [
                { "q": "Kernel:", "options": ["Función que transforma a espacio mayor", "Truco algoritmo"], "answer": ["Función que transforma a espacio mayor"], "type": "single", "explanation": "Calcula productos escalares en alta dimensión." },
                { "q": "Kernel común:", "options": ["Base radial (RBF)", "Ingenuo"], "answer": ["Base radial (RBF)"], "type": "single", "explanation": "Es el más estándar." },
                { "q": "Debilidad SVM:", "options": ["Lento de entrenar con muchos datos", "Rápido siempre"], "answer": ["Lento de entrenar con muchos datos"], "type": "single", "explanation": "Complejidad O(n^2) o O(n^3)." }
            ]}
         ]
    },
    {
        "tema": "Tema 9. Redes Neuronales",
        "tests": [
            { "id": "Microtest 9.2", "questions": [
                { "q": "Función de activación:", "options": ["Define la salida de una neurona", "Utiliza regresión logística"], "answer": ["Define la salida de una neurona"], "type": "single", "explanation": "Introduce no linealidad." },
                { "q": "Perceptrón conformado por:", "options": ["Nodos entrada, pesos, función activación", "Solo neuronas"], "answer": ["Nodos entrada, pesos, función activación"], "type": "single", "explanation": "Estructura básica." },
                { "q": "Década perceptrón:", "options": ["1950", "1990", "2000"], "answer": ["1950"], "type": "single", "explanation": "Rosenblatt, 1957." }
            ]},
            { "id": "Microtest 9.3", "questions": [
                { "q": "Funciones lineales, tangente, gaussiana son funciones de activación:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Son tipos válidos." },
                { "q": "Número capas depende del número de características:", "options": ["Verdadero", "Falso"], "answer": ["Falso"], "type": "single", "explanation": "Depende de la complejidad del problema (hiperparámetro), no del input." },
                { "q": "Número neuronas entrada depende de características:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "La capa de entrada debe coincidir con la dimensión del input." }
            ]},
            { "id": "Microtest 9.4", "questions": [
                { "q": "Fases backpropagation:", "options": ["Fase forward", "Fase backward", "Reentrenamiento"], "answer": ["Fase forward", "Fase backward"], "type": "multi", "explanation": "Predicción hacia adelante, propagación de error hacia atrás." },
                { "q": "Modificar pesos:", "options": ["Derivada función activación", "Dirección reducción error", "Gradiente descendente"], "answer": ["Derivada función activación", "Dirección reducción error", "Gradiente descendente"], "type": "multi", "explanation": "Todo es parte de la optimización." },
                { "q": "Fortalezas:", "options": ["Se adaptan a todo problema", "Pocas suposiciones"], "answer": ["Se adaptan a todo problema", "Pocas suposiciones"], "type": "multi", "explanation": "Aproximadores universales." }
            ]}
        ]
    },
    {
        "tema": "Tema 10. Clustering",
        "tests": [
            { "id": "Microtest 10.2", "questions": [
                { "q": "Clustering divide sin etiquetas:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Aprendizaje no supervisado." },
                { "q": "Algoritmos se dividen en Agrupación y Jerárquicos:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Familias principales (K-means vs Dendrogramas)." },
                { "q": "Ayudan a reducir grandes datasets:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Resumen datos en prototipos." }
            ]},
            { "id": "Microtest 10.3", "questions": [
                { "q": "Objetivo K-medias: max diferencias entre grupos, min dentro grupo:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Cohesión interna y separación externa." },
                { "q": "Fases: asignar y actualizar:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Algoritmo EM." },
                { "q": "Diagramas Voronoi delimitan espacio:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Representación geométrica." }
            ]},
            { "id": "Microtest 10.4", "questions": [
                { "q": "Desventajas clustering:", "options": ["Raramente proveen buena solución", "Mala interpretación"], "answer": ["Raramente proveen buena solución", "Mala interpretación"], "type": "multi", "explanation": "Es subjetivo y difícil de validar." },
                { "q": "Iteración jerárquico:", "options": ["Elemento a clúster más cercano", "Dibuja conexión y altura"], "answer": ["Elemento a clúster más cercano", "Dibuja conexión y altura"], "type": "multi", "explanation": "Construcción dendrograma." },
                { "q": "Tipos jerárquico:", "options": ["Agglomerative", "Divisive"], "answer": ["Agglomerative", "Divisive"], "type": "multi", "explanation": "Ascendente y Descendente." }
            ]}
        ]
    },
    {
        "tema": "Tema 11. Anomalías",
        "tests": [
            { "id": "Microtest 11.2", "questions": [
                { "q": "Anomalía se debe a:", "options": ["Dato fuera de rango", "Fallo medición", "Naturaleza dato"], "answer": ["Dato fuera de rango", "Fallo medición", "Naturaleza dato"], "type": "multi", "explanation": "Pueden ser errores o fraudes reales." },
                { "q": "Tipos distribuciones:", "options": ["Bimodal", "Asimétrica positiva", "Asimétrica negativa"], "answer": ["Bimodal", "Asimétrica positiva", "Asimétrica negativa"], "type": "multi", "explanation": "Formas histograma." },
                { "q": "Tipos anomalías:", "options": ["Colectivas", "Contexto"], "answer": ["Colectivas", "Contexto"], "type": "multi", "explanation": "Y puntuales." }
            ]},
            { "id": "Microtest 11.3", "questions": [
                { "q": "Aproximación gráfica visual:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Boxplots, Scatter." },
                { "q": "Isolation forest usa isolation trees:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Corta aleatoriamente hasta aislar." },
                { "q": "ML se usa porque datos no siempre son normales:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Métodos estadísticos asumen normalidad." }
            ]},
            { "id": "Microtest 11.4", "questions": [
                { "q": "Supervisado necesita:", "options": ["Datos para aprender", "Definir límite"], "answer": ["Datos para aprender"], "type": "single", "explanation": "Necesita etiquetas." },
                { "q": "Característica dataset supervisado:", "options": ["Muy pocos ejemplos clase anómala"], "answer": ["Muy pocos ejemplos clase anómala"], "type": "single", "explanation": "Desbalance severo." },
                { "q": "Ejemplo anomalía:", "options": ["Fallos en cadena montaje"], "answer": ["Fallos en cadena montaje"], "type": "single", "explanation": "Evento raro." }
            ]},
            { "id": "Microtest 11.5", "questions": [
                { "q": "Algoritmos NO supervisados:", "options": ["Vecinos cercanos", "Isolation Forest", "Clúster"], "answer": ["Vecinos cercanos", "Isolation Forest", "Clúster"], "type": "multi", "explanation": "No requieren etiquetas." },
                { "q": "Antes de crear modelo:", "options": ["Análisis descriptivo", "Boxplot", "Exploratorio"], "answer": ["Análisis descriptivo", "Boxplot", "Exploratorio"], "type": "multi", "explanation": "EDA es clave." },
                { "q": "Predicción Isolation Forest:", "options": ["Score -1 o 1", "Score normalizado"], "answer": ["Score -1 o 1", "Score normalizado"], "type": "multi", "explanation": "Salida estándar." }
            ]}
        ]
    },
    {
        "tema": "Tema 12. Aprendizaje por Refuerzo",
        "tests": [
            { "id": "Microtest 12.2", "questions": [
                { "q": "Elementos agente:", "options": ["Sensores", "Actuadores"], "answer": ["Sensores", "Actuadores"], "type": "multi", "explanation": "Percibe y actúa." },
                { "q": "Procesos Markov:", "options": ["Estado inicial", "Conjunto acciones"], "answer": ["Estado inicial", "Conjunto acciones"], "type": "multi", "explanation": "MDP Components." },
                { "q": "Algoritmos utilidad:", "options": ["Aditiva", "Ponderada", "Descontada"], "answer": ["Aditiva", "Ponderada", "Descontada"], "type": "multi", "explanation": "Suma de recompensas." }
            ]},
            { "id": "Microtest 12.3", "questions": [
                { "q": "Tipos Pasivo y Activo:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Pasivo observa, Activo actúa." },
                { "q": "Pasivo fuerza bruta usa política variable:", "options": ["Verdadero", "Falso"], "answer": ["Falso"], "type": "single", "explanation": "Usa política fija." },
                { "q": "Pasivo calcula media:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Promedio recompensas." }
            ]},
            { "id": "Microtest 12.4", "questions": [
                { "q": "Q-learning busca:", "options": ["Asignar valores Q", "Suma recompensas"], "answer": ["Asignar valores Q", "Suma recompensas"], "type": "multi", "explanation": "Calidad par Estado-Acción." },
                { "q": "Q-learning 3 en raya esfuerzo depende:", "options": ["Acción realizada", "Estado actual", "Acción pasada"], "answer": ["Acción realizada", "Estado actual", "Acción pasada"], "type": "multi", "explanation": "Exploración espacio estados." },
                { "q": "Tabla recompensas guarda:", "options": ["Recompensas", "Estados", "Acciones"], "answer": ["Recompensas", "Estados", "Acciones"], "type": "multi", "explanation": "Q-Table." }
            ]}
        ]
    },
    {
        "tema": "Tema 13. Optimización",
        "tests": [
            { "id": "Microtest 13.2", "questions": [
                { "q": "Conceptos claros antes optimizar:", "options": ["Sesgo", "Varianza"], "answer": ["Sesgo", "Varianza"], "type": "multi", "explanation": "Bias-Variance Tradeoff." },
                { "q": "Corregir alto sesgo (underfitting):", "options": ["Aumentar hiperparámetros", "Aumentar atributos"], "answer": ["Aumentar hiperparámetros", "Aumentar atributos"], "type": "multi", "explanation": "Modelo más complejo." },
                { "q": "Algoritmos búsqueda hiperparámetros:", "options": ["Búsqueda cartesiana", "Optimización evolutiva"], "answer": ["Búsqueda cartesiana", "Optimización evolutiva"], "type": "multi", "explanation": "Grid search, genetic algos." }
            ]},
            { "id": "Microtest 13.3", "questions": [
                { "q": "Búsqueda aleatoria solventa problemas cartesiana:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Más eficiente." },
                { "q": "Criterio parada umbral:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Evita bucles infinitos." },
                { "q": "Aleatoria poco útil con muchos hiperparámetros:", "options": ["Verdadero", "Falso"], "answer": ["Falso"], "type": "single", "explanation": "Al contrario, es donde mejor funciona." }
            ]},
            { "id": "Microtest 13.4", "questions": [
                { "q": "Función Python Grid Search:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "GridSearchCV." },
                { "q": "GridSearch crea tantos modelos como combinaciones:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Fuerza bruta." },
                { "q": "RandomizedSearch necesita definir valores:", "options": ["Verdadero", "Falso"], "answer": ["Verdadero"], "type": "single", "explanation": "Necesita distribución o lista." }
            ]}
        ]
    }
]

if "theme" not in st.session_state:
    st.session_state.theme = "light"

# CSS para forzar estilos limpios
st.markdown("""
    <style>
    :root {
        --primary-color: #ff4b4b;
        --background-color: #f5f7f9;
        --secondary-background-color: #ffffff;
        --text-color: #000000;
        --font: "sans-serif";
    }
    .stApp {
        background-color: #f5f7f9;
        color: #000000 !important;
    }
    .question-card {
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    div[data-testid="stMarkdownContainer"] p {
        color: #000000 !important;
        font-size: 1.1rem;
    }
    h1, h2, h3, h4, p, span, div, label {
        color: #000000 !important;
    }
    div.stButton > button {
        color: white !important;
        background-color: #ff4b4b;
        border: none;
        font-weight: bold;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ff2b2b;
        transform: scale(1.02);
    }
    .status-bar {
        color: #666 !important;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. GESTIÓN DEL ESTADO (SESSION STATE) ---
# Inicializamos variables si no existen
default_values = {
    'q_index': 0,
    'score': 0,
    'quiz_finished': False,
    'last_answer_correct': None,
    'show_explanation': False,
    'active_questions_list': [],     # Aquí guardaremos la lista de preguntas activas (sea 3 o 100)
    'current_mode_id': None          # Para detectar cambios de microtest/examen
}

for key, val in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- 4. FUNCIONES DE LÓGICA ---

def iniciar_quiz(lista_preguntas, mode_id):
    """Reinicia el quiz con una nueva lista de preguntas"""
    st.session_state.active_questions_list = lista_preguntas
    st.session_state.current_mode_id = mode_id
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.quiz_finished = False
    st.session_state.show_explanation = False
    st.session_state.last_answer_correct = None

def submit_answer(user_selection, correct_answers, q_type):
    # Corrección estricta
    is_correct = False
    if q_type == "single":
        if user_selection == correct_answers[0]:
            is_correct = True
    else: # Multi
        # El usuario debe marcar TODAS las correctas y NINGUNA incorrecta
        if set(user_selection) == set(correct_answers):
            is_correct = True
    
    if is_correct:
        st.session_state.score += 1
        st.session_state.last_answer_correct = True
    else:
        st.session_state.last_answer_correct = False
    
    st.session_state.show_explanation = True

def next_question():
    total = len(st.session_state.active_questions_list)
    if st.session_state.q_index < total - 1:
        st.session_state.q_index += 1
        st.session_state.show_explanation = False
        st.session_state.last_answer_correct = None
    else:
        st.session_state.quiz_finished = True

# --- 5. INTERFAZ: BARRA LATERAL ---
with st.sidebar:
    st.title("🧠 Configuración")
    
    # SELECTOR DE MODO
    modo = st.radio("Modo de Estudio:", ["🎯 Práctica por Temas", "🔥 Examen General"], index=0)
    
    preguntas_a_cargar = []
    identificador_nuevo = None
    
    if modo == "🎯 Práctica por Temas":
        # Lógica original: Elegir Tema -> Elegir Microtest
        temas = [t["tema"] for t in FULL_DATA]
        tema_sel = st.selectbox("Elige un Módulo:", temas)
        
        datos_tema = next(item for item in FULL_DATA if item["tema"] == tema_sel)
        tests_ids = [t["id"] for t in datos_tema["tests"]]
        test_sel = st.radio("Elige Microtest:", tests_ids)
        
        # Recuperamos las preguntas de ese test específico
        datos_test = next(t for t in datos_tema["tests"] if t["id"] == test_sel)
        preguntas_a_cargar = datos_test["questions"]
        identificador_nuevo = test_sel # Usamos el nombre del microtest como ID
        
        st.info(f"Microtest de {len(preguntas_a_cargar)} preguntas.")

    else: # MODO EXAMEN GENERAL
        st.warning("⚠️ El examen general incluye TODAS las preguntas mezcladas.")
        
        # Aplanar la lista: sacar todas las preguntas de todos los temas
        todas_las_preguntas = []
        for tema in FULL_DATA:
            for test in tema["tests"]:
                todas_las_preguntas.extend(test["questions"])
        
        identificador_nuevo = "EXAMEN_GENERAL"
        
        # Solo barajamos si estamos iniciando (para no barajar en cada clic)
        if st.session_state.current_mode_id != identificador_nuevo:
             random.shuffle(todas_las_preguntas)
        
        preguntas_a_cargar = todas_las_preguntas
        st.write(f"Total de preguntas: **{len(preguntas_a_cargar)}**")

    # DETECCIÓN DE CAMBIO DE MODO
    # Si el usuario cambió de selección en el menú, reiniciamos el quiz automáticamente
    if st.session_state.current_mode_id != identificador_nuevo:
        iniciar_quiz(preguntas_a_cargar, identificador_nuevo)
        st.rerun()

    st.divider()
    st.metric("Puntuación Actual", f"{st.session_state.score}")
    
    if st.button("🔄 Reiniciar desde cero"):
        # Forzamos recarga con el mismo ID pero barajando de nuevo si es examen
        if modo == "🔥 Examen General":
             random.shuffle(preguntas_a_cargar)
        iniciar_quiz(preguntas_a_cargar, identificador_nuevo)
        st.rerun()

# --- 6. ÁREA PRINCIPAL (QUIZ) ---

# Verificamos que haya preguntas cargadas
if not st.session_state.active_questions_list:
    st.error("No se han cargado preguntas. Selecciona un módulo.")
    st.stop()

# Pantalla de Resultados
if st.session_state.quiz_finished:
    st.balloons()
    st.markdown("<div class='question-card'>", unsafe_allow_html=True)
    st.title("🏁 Resultado Final")
    
    total_q = len(st.session_state.active_questions_list)
    nota = (st.session_state.score / total_q) * 10
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.metric("Nota Final (Base 10)", f"{nota:.2f} / 10")
        st.write(f"Acertaste **{st.session_state.score}** de **{total_q}** preguntas.")
        
        if nota >= 9:
            st.success("¡Excelente! Dominio total.")
        elif nota >= 6:
            st.warning("Aprobado, pero hay margen de mejora.")
        else:
            st.error("Necesitas repasar más.")
            
    if st.button("Intentar de nuevo", key="btn_final_retry"):
        if modo == "🔥 Examen General":
             # En examen general, "Intentar de nuevo" debería re-barajar
             lista_nueva = st.session_state.active_questions_list.copy()
             random.shuffle(lista_nueva)
             iniciar_quiz(lista_nueva, identificador_nuevo)
        else:
             iniciar_quiz(st.session_state.active_questions_list, identificador_nuevo)
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# Pantalla de Pregunta Activa
else:
    idx = st.session_state.q_index
    q_actual = st.session_state.active_questions_list[idx]
    total_q = len(st.session_state.active_questions_list)
    
    # Barra de Progreso
    progreso = (idx + 1) / total_q
    st.progress(progreso)
    st.markdown(f"<div class='status-bar'>Pregunta {idx + 1} de {total_q}</div>", unsafe_allow_html=True)

    # Tarjeta de Pregunta
    st.markdown(f"""
    <div class='question-card'>
        <h3>{q_actual['q']}</h3>
    </div>
    """, unsafe_allow_html=True)

    # Lógica de respuesta
    if not st.session_state.show_explanation:
        with st.form(key=f"form_q_{idx}"): # Key única por índice para limpiar selección al avanzar
            
            user_response = None
            
            if q_actual["type"] == "single":
                user_response = st.radio("Elige una opción:", q_actual["options"], index=None)
            else:
                st.write("**Selección Múltiple** (Marca todas las correctas):")
                # Checkboxes manuales
                user_response = []
                for opt in q_actual["options"]:
                    if st.checkbox(opt):
                        user_response.append(opt)
            
            st.markdown("<br>", unsafe_allow_html=True)
            submit = st.form_submit_button("Comprobar ➔")
            
            if submit:
                if not user_response:
                    st.warning("Debes seleccionar una respuesta.")
                else:
                    submit_answer(user_response, q_actual["answer"], q_actual["type"])
                    st.rerun()

    else:
        # Mostrar Feedback
        if st.session_state.last_answer_correct:
            st.success("✅ ¡Correcto!")
        else:
            st.error("❌ Incorrecto")
            st.write(f"**Solución correcta:** {', '.join(q_actual['answer'])}")
        
        st.info(f"📖 **Explicación:** {q_actual['explanation']}")
        
        if st.button("Siguiente ➔", key=f"next_btn_{idx}"):
            next_question()
            st.rerun()
            
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
