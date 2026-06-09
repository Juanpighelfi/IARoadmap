import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi, 100)
print(x)
y = np.sin(x)
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, np.cos(x), label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funciones Trigonométricas')
plt.legend()         # Mostrar leyenda
plt.grid(True)       # Activar grilla
plt.tight_layout()   # Ajustar márgenes
plt.show()