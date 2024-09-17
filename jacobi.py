import numpy as np

# Definir la matriz A y el vector b
A = np.array([[0.52, 0.20, 0.25],
              [0.30, 0.50, 0.20],
              [0.18, 0.30, 0.55]])
b = np.array([4800, 5810, 5600])

# Número máximo de iteraciones y tolerancia
max_iterations = 100
tolerance = 1e-10

# Inicializar la solución inicial
x = np.zeros_like(b)

# Iteraciones de Jacobi
for iteration in range(max_iterations):
    x_new = np.zeros_like(x)

    # Calcular la nueva solución
    for i in range(len(b)):
        sum_ax = np.dot(A[i, :], x) - A[i, i] * x[i]
        x_new[i] = (b[i] - sum_ax) / A[i, i]
    
    # Mostrar la iteración
    print(f"Iteración {iteration + 1}: {x_new}")

    # Verificar la convergencia
    if np.all(np.abs(x_new - x) < tolerance):
        print("Convergencia alcanzada.")
        break
    
    x = x_new

# Resultado final
print(f"\nSolución final: {x}")
