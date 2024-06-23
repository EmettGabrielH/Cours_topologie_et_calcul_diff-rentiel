import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Définir la fonction z=f(x,y)
def f(x, y):
    return x**2 + y**2

def grad_f(x,y):
    return np.array((2*x,2*y))

def scalaire(a,b):
    return a[0]*b[0] + a[1]*b[1]

# Créer une grille de points
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Initialisation
x_a = 0
y_a = 0


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.1, bottom=0.35)


surface = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0)

# Fonction de mise à jour
def update(val):
    global x_a, y_a
    
    x_a = x_0.val
    y_a = y_0.val

    ax.clear()
    ax.set_title("z=f(x,y)")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0)
    
    Z1 = f(x_a,y_a) + scalaire(grad_f(x_a,y_a),(X-x_a,Y-y_a))
    ax.plot_surface(X, Y, Z1, cmap=cm.copper, linewidth=0)
    
    dx_a,dy_a = grad_f(x_a,y_a)
    
    ax.quiver(x_a, y_a, f(x_a, y_a), 1, 0, dx_a, color='r', length=2, normalize=True)
    ax.quiver(x_a, y_a, f(x_a, y_a), 0, 1, dy_a, color='b', length=2, normalize=True)

    
    fig.canvas.draw_idle()

# Créer les axes pour les curseurs, puis les curseurs
axcolor = 'lightgoldenrodyellow'
ax_x = plt.axes([0.1, 0.1, 0.8, 0.03], facecolor=axcolor)
ax_y = plt.axes([0.1, 0.15, 0.8, 0.03], facecolor=axcolor)

x_0 = Slider(ax_x, 'a_x', -2, 2, valinit=x_a)
y_0 = Slider(ax_y, 'a_y', -2, 2, valinit=y_a)
x_0.on_changed(update)
y_0.on_changed(update)

plt.show()
