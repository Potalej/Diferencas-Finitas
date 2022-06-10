"""
  Neste exemplo estaremos usando a função:
        
       f(x) = (cosx - sin²x)exp(cosx)

  Com a condição de contorno do Dirichlet no intervalo [0, 2pi] tal que f(0)=f(2pi)=e, para os seguintes esquemas centrados:

    -> -1/(12h²) (-u_{k-2} + 16u_{k-1} - 30u_{k} + 16u_{k+1} - u_{k+2}) = f_{k}
    -> -1/h² (u_{k-1} - 2u_{k} + u_{k+1}) = f_{k}

  Sendo a segunda utilizada nas linhas 1, 2, n-1 e n e a primeira utilizada nas linhas restantes.

  Podemos integrar duas vezes e vamos descobrir que a função verdadeira é:

        u(x) = exp(cosx)

  então dá para comparar o obtido com o esperado.
"""

from math import sin, cos, exp, pi
from diferencas_finitas import DiferencasFinitas
import resolver

# funçãozinha
f = lambda x: (cos(x) - sin(x)**2)*exp(cos(x))
u = lambda x: exp(cos(x))

# tmaanho da matriz etc.
n = 500

# coeficientes da U
coefsU = {
  (0,1): {-1:1, 0:-2, 1:1},
  (2, n-3): {-2:-1, -1:16, 0:-30, 1:16, 2:-1},
  (n-2, n-1): {-1:1, 0:-2, 1:1}
}
# coeficientes do h (depende da discretização)
coefsh = {
  (0,1): 1,
  (2,n-3): 12,
  (n-2, n-1): 1
}
# instancia 
dif = DiferencasFinitas(f, coefsU, coefsh, 0, 2*pi, [exp(1), exp(1)])
# aplica
A, c = dif.matrizes(n)
# resolve
x = resolver.resolver_npsolve(A, c)

import matplotlib.pyplot as plt

plt.scatter([i*2*pi/n for i in range(n)], x, label="Obtido", s=5, c="b")
plt.plot([i*2*pi/n for i in range(n)], [u(i*2*pi/n) for i in range(n)], label="Esperado", c="red")
plt.legend()
plt.show()