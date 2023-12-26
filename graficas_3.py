
import pandas as pd
import plotly.express as px

# Dataset
data = {
    'id': list(range(1, 21)),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí',
                 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Crear el boxplot con Plotly
fig = px.box(df, x='materia', y='nota', color='aprobado', points='all',
             title='Distribución de Notas por Materia', labels={'materia': 'Materia', 'nota': 'Nota'})

# Mostrar el gráfico
fig.show()



# Dataset
data = {
    'id': list(range(1, 21)),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí',
                 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Obtener la distribución de aprobados y no aprobados
aprobados = df['aprobado'].value_counts()

# Crear el pie chart con Plotly
fig = px.pie(aprobados, values='aprobado', names=aprobados.index, 
             title='Proporción de Estudiantes Aprobados y No Aprobados')

# Mostrar el gráfico
fig.show()
