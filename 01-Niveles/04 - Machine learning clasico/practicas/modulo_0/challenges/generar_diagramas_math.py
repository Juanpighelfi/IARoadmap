import os
import matplotlib.pyplot as plt
import numpy as np

# Paleta "Creamy & Brownish"
BG_COLOR = "#F8F5F0"        # Cremoso muy suave
AXIS_COLOR = "#4A3B32"      # Marrón muy oscuro (ejes y texto)
GRID_COLOR = "#E5D9C5"      # Marrón arena/crema oscuro (grilla)
SURFACE_COLOR = "#E9DEC6"   # Arena para superficies 3D
LINE_COLOR = "#8B7355"      # Marrón roble (líneas principales)
HIGHLIGHT_COLOR = "#C16642" # Teja/Terracota para destacar (vectores, W)

plt.rcParams.update({
    "figure.facecolor": BG_COLOR,
    "axes.facecolor": BG_COLOR,
    "savefig.facecolor": BG_COLOR,
    "text.color": AXIS_COLOR,
    "axes.edgecolor": AXIS_COLOR,
    "xtick.color": AXIS_COLOR,
    "ytick.color": AXIS_COLOR,
    "font.family": "serif"
})

def style_axis(ax):
    """Limpia los bordes de los gráficos para que parezcan ejes coordenados clásicos."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_color(AXIS_COLOR)
    ax.spines['bottom'].set_color(AXIS_COLOR)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.set_xticks([])
    ax.set_yticks([])

def slide_1(output_dir):
    print("Generando Diapositiva 1 (Portada)...")
    fig = plt.figure(figsize=(10, 7), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off()
    
    u = np.linspace(-3, 3, 40)
    v = np.linspace(-3, 3, 40)
    U, V = np.meshgrid(u, v)
    
    # Superficie retorciéndose
    Z = np.sin(U/1.5) * np.cos(V/1.5) * 1.5
    
    ax.plot_surface(U, V, Z, color=SURFACE_COLOR, edgecolor=LINE_COLOR, 
                    linewidth=0.5, antialiased=True, alpha=0.9)
    
    ax.view_init(elev=25, azim=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/01_portada_3D.png", bbox_inches='tight')
    plt.close()

def slide_2(output_dir):
    print("Generando Diapositiva 2 (Vectores)...")
    fig, ax = plt.subplots(figsize=(8, 8), dpi=300)
    style_axis(ax)
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    
    # Grilla de fondo
    for i in range(-4, 5):
        if i != 0:
            ax.axhline(i, color=GRID_COLOR, lw=1.2, zorder=0)
            ax.axvline(i, color=GRID_COLOR, lw=1.2, zorder=0)
            
    # Flecha simple
    ax.annotate("", xy=(2, 3), xytext=(0, 0),
                arrowprops=dict(facecolor=HIGHLIGHT_COLOR, edgecolor=HIGHLIGHT_COLOR, 
                                width=3, headwidth=10, headlength=12), zorder=3)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/02_vector.png", bbox_inches='tight')
    plt.close()

def slide_3(output_dir):
    print("Generando Diapositiva 3 (Matrices/Cizalladura)...")
    fig, ax = plt.subplots(figsize=(8, 8), dpi=300)
    style_axis(ax)
    
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    
    # Matriz de cizalladura (Shear) + Ligera dilatación para estética
    transform = np.array([[1.2, 0.8], [0.3, 1.1]])
    
    for i in range(-5, 6):
        # Lineas horizontales transformadas
        p1 = transform @ np.array([-5, i])
        p2 = transform @ np.array([5, i])
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=GRID_COLOR, lw=1.5, zorder=0)
        
        # Lineas verticales transformadas
        p1 = transform @ np.array([i, -5])
        p2 = transform @ np.array([i, 5])
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=LINE_COLOR if i == 0 else GRID_COLOR, 
                lw=2 if i == 0 else 1.5, zorder=1 if i == 0 else 0)
        
    ax.annotate("", xy=transform @ np.array([1, 0]), xytext=(0, 0),
                arrowprops=dict(facecolor=HIGHLIGHT_COLOR, edgecolor=HIGHLIGHT_COLOR, 
                                width=2, headwidth=8), zorder=3)
    ax.annotate("", xy=transform @ np.array([0, 1]), xytext=(0, 0),
                arrowprops=dict(facecolor=LINE_COLOR, edgecolor=LINE_COLOR, 
                                width=2, headwidth=8), zorder=3)

    plt.tight_layout()
    plt.savefig(f"{output_dir}/03_transformacion.png", bbox_inches='tight')
    plt.close()

def slide_4(output_dir):
    print("Generando Diapositiva 4 (El colapso)...")
    fig, ax = plt.subplots(figsize=(8, 8), dpi=300)
    style_axis(ax)
    
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    
    # Matriz colapsante (determinante = 0)
    transform = np.array([[1, 1], [1, 1]])
    
    for i in range(-5, 6):
        p1 = transform @ np.array([-5, i])
        p2 = transform @ np.array([5, i])
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=HIGHLIGHT_COLOR, lw=1, alpha=0.4, zorder=0)
        
        p1 = transform @ np.array([i, -5])
        p2 = transform @ np.array([i, 5])
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=HIGHLIGHT_COLOR, lw=1, alpha=0.4, zorder=0)

    # Espacio 1D resultante sobre el origen
    ax.plot([-5, 5], [-5, 5], color=AXIS_COLOR, lw=3, zorder=2)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/04_colapso.png", bbox_inches='tight')
    plt.close()

def slide_5(output_dir):
    print("Generando Diapositiva 5 (Red Neuronal)...")
    fig, ax = plt.subplots(figsize=(10, 4), dpi=300)
    ax.set_axis_off()
    
    # Renderizamos la fórmula completa en color primario
    ax.text(0.5, 0.65, r"$y \,=\, \mathbf{W_2} \cdot \mathrm{ReLU}(\mathbf{W_1} \cdot x \,+\, b_1)$", 
            fontsize=40, color=AXIS_COLOR, ha='center', va='center', weight='bold')
    
    # Agregamos texto secundario que enfatiza el color teja "W"
    # Esto evita problemas de alineación al tratar de renderizar multicolores en mathtext.
    ax.text(0.5, 0.35, "Las matrices W dictan los aplastamientos e inclinaciones", 
            fontsize=18, color=HIGHLIGHT_COLOR, ha='center', va='center', style='italic')

    plt.tight_layout()
    plt.savefig(f"{output_dir}/05_red_neuronal.png", bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    out_path = "diagramas_creamy_brown"
    os.makedirs(out_path, exist_ok=True)
    
    slide_1(out_path)
    slide_2(out_path)
    slide_3(out_path)
    slide_4(out_path)
    slide_5(out_path)
    
    print(f"\n¡Todos los diagramas (5) fueron generados exitosamente en la carpeta '{os.path.abspath(out_path)}'!")
