#!/usr/bin/env python3
"""
  LEGENDRE

  Neste exemplo estaremos usando a função:
        
       f(x) = exp(sin(x))cos(x)(-3sin(x)+cos²(x)-1)

  Com a condição de contorno do diricléia no intervalo [-pi/2, pi/2] tal que f(-pi/2)=f(pi/2)=0, para os seguintes esquemas centrados:

    -> -1/(12h²) (-u_{k-2} + 16u_{k-1} - 30u_{k} + 16u_{k+1} - u_{k+2}) = f_{k}
    -> -1/h² (u_{k-1} - 2u_{k} + u_{k+1}) = f_{k}

  Sendo a segunda utilizada nas linhas 1, 2, n-1 e n e a primeira utilizada nas linhas restantes.

  Podemos integrar duas vezes e vamos descobrir que a função verdadeira é:

        u(x) = -exp(sin(x))cos(x)

  então dá para comparar o obtido com o esperado.
"""

from diferencas_finitas import DiferencasFinitas
import resolver
from math import exp, sin, cos, pi
# funçãozinha
f = lambda x: exp(sin(x))*cos(x)*(-3*sin(x)+cos(x)**2-1)
u = lambda x: -exp(sin(x))*cos(x)

# tmaanho da matriz etc.
n = 240

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
dif = DiferencasFinitas(f, coefsU, coefsh, -pi/2, pi/2, [0,0])
# aplica
A, c = dif.matrizes(n)
# resolve
x = resolver.resolver_spsolvebanded(A, c)[0]

#x = resolver.resolver_spsolvebanded(A, c)
import matplotlib.pyplot as plt

plt.scatter([i*(pi)/n-(pi/2) for i in range(n)], x, label="Obtido", s=5, c="b")
plt.plot([i*(pi)/n-(pi/2) for i in range(n)], [u(i*(pi)/n-(pi/2)) for i in range(n)], label="Esperado", c="red")
plt.legend()
plt.title(f"SP Banded (n={n})")
plt.show()