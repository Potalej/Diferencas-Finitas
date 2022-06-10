#!/usr/bin/env python3
"""
  LEGENDRE

  Neste exemplo estaremos usando a função:
        
       f(x) = -105 (33x^4 - 18x^2 + 1) / 8

  Com a condição de contorno do diricléia no intervalo [-1, 1] tal que f(-1)=f(1)=1, para os seguintes esquemas centrados:

    -> -1/(12h²) (-u_{k-2} + 16u_{k-1} - 30u_{k} + 16u_{k+1} - u_{k+2}) = f_{k}
    -> -1/h² (u_{k-1} - 2u_{k} + u_{k+1}) = f_{k}

  Sendo a segunda utilizada nas linhas 1, 2, n-1 e n e a primeira utilizada nas linhas restantes.

  Podemos integrar duas vezes e vamos descobrir que a função verdadeira é:

        u(x) = (231x^6 - 315x^4 + 105x^2 - 5) / 16

  então dá para comparar o obtido com o esperado.
"""

from diferencas_finitas import DiferencasFinitas
import resolver

# funçãozinha
f = lambda x: -105*(33*x**4 - 18*x**2 + 1)/8
u = lambda x: (1/16)*(231*x**6 - 315*x**4 + 105*x**2 - 5)

# tmaanho da matriz etc.
n = 960

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
dif = DiferencasFinitas(f, coefsU, coefsh, -1, 1, [1, 1])
# aplica
A, c = dif.matrizes(n)
# resolve
x = resolver.resolver_spsolvebanded(A, c)[0]

#x = resolver.resolver_spsolvebanded(A, c)
import matplotlib.pyplot as plt

plt.scatter([i*2/n-1 for i in range(n)], x, label="Obtido", s=5, c="b")
plt.plot([i*2/n-1 for i in range(n)], [u(i*2/n-1) for i in range(n)], label="Esperado", c="red")
plt.legend()
plt.title("SP Banded (n=960)")
plt.show()