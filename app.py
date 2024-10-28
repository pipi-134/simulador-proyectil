import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Simulador de Trayectoria de un Proyectil")

# Entradas del usuario
angle = st.slider("Selecciona el ángulo de tiro (grados):", 0, 90, 45)
force = st.slider("Selecciona la fuerza de tiro (m/s):", 1, 100, 50)

# Convertir ángulo a radianes
angle_rad = np.radians(angle)

# Gravedad
g = 9.81  # m/s^2

# Calcular la distancia máxima
def calcular_distancia(angle, force):
    return (force**2 * np.sin(2 * angle_rad)) / g

distancia = calcular_distancia(angle_rad, force)

# Mostrar la distancia calculada
st.write(f"Distancia máxima alcanzada: {distancia:.2f} metros")

# Gráfico de la trayectoria
def graficar_trayectoria(angle, force):
    t_total = (2 * force * np.sin(angle_rad)) / g
    t = np.linspace(0, t_total, num=100)
    
    x = force * np.cos(angle_rad) * t
    y = force * np.sin(angle_rad) * t - (0.5 * g * t**2)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, y)
    plt.title('Trayectoria del Proyectil')
    plt.xlabel('Distancia (m)')
    plt.ylabel('Altura (m)')
    plt.xlim(0, np.max(x) + 10)
    plt.ylim(0, np.max(y) + 10)
    plt.grid()
    plt.axhline(0, color='black', lw=2)
    plt.axvline(0, color='black', lw=2)
    plt.show()
    
    st.pyplot(plt)

# Graficar la trayectoria
graficar_trayectoria(angle_rad, force)
