# Diferenças Finitas

Quando se trabalha com equações diferenciais em problemas reais, geralmente não se possui formas analíticas de encontrar as soluções - às vezes soluções absolutas nem mesmo existem. Nesses momentos, fazem-se necessários os métodos numéricos de resolução, e um deles é o Método por Diferenças Finitas.

Este repositório foi feito com o propósito de estudar um pouco mais a fundo o estudado em aulas de Aplicações de Álgebra Linear de uma forma um pouco geral, e, ao menos em um primeiro momento, se propõe a encontrar soluções para E.D.O.s do tipo $-u''(x) = f(x)$ com condições de contorno de Dirichlet.

<h2>Exemplo de uso</h2>

Uma facilidade desse tipo de E.D.O. enunciada é que encontrar soluções analiticamente é possível, então analisar a relação da aproximação com o resultado real é bem simples. 

Assim, suponhamos uma $f(x) = (cos(x) - sen^2(x)) exp(cos(x))$, para $0 < x < 2\pi$, e valendo que $f(0) = f(2\pi) = e$.

Utilizando $n$ iterações (aumentando), com esquema centrado 
$$-\frac{1}{h^2}(u_{k-1}-2u_k+u_{k+1})=f_{k}$$ 
para as linhas $0$, $1$, $n-1$ e $n$ e o esquema 
$$-\frac{1}{12h^2}(-u_{k-2}+16u_{k-1}-30u_k+16u_{k+1}-u_{k+2})=f_k$$
para as demais linhas, pode-se obter o seguinte resultado:

![Alt Text](https://media3.giphy.com/media/qhcXdGdck55NF1Cetn/giphy.gif?cid=6c09b9524ded011a25eaec508b7594607285770e5f87d612&rid=giphy.gif&ct=g)

Se observando mais perto:

![Alt Text](https://media4.giphy.com/media/mFOsG4pN8d8DqG2uFM/giphy.gif?cid=6c09b9529949bfee12ca40a6e596bd79c4909e504f6807b6&rid=giphy.gif&ct=g)

Isto utilizando que a matriz $A$ obtida em $Au = c$ na hora da discretização é inversível e logo $u = A^{-1}c$. Outros métodos de solução mais precisos e menos custosos hão de ser adicionados.

Onde o gráfico verde é a função $u(x) = exp(cos(x))$, solução analítica de $-u''(x) = f(x)$ (considerando as constantes de integração nulas).

Este exemplo, para determinado $n$, pode ter seu código encontrado abaixo:

```python
from math import sin, cos, exp, pi
import numpy as np

# coeficientes das discretizações
coefsU = {
  (0,1): {-1: 1, 0: -2, 1: 1},
  (2, n-3): {-2: -1, -1: 16, 0: -30, 1: 16, 2: -1},
  (n-2,n-1): {-1: 1, 0: -2, 1: 1},
}

# coeficientes do h nas discretizações
coefsh = {
  (0,1): 1,
  (2, n-3): 12,
  (n-2, n-1): 1
}

# condições de contorno
contorno = [exp(1), exp(1)]

# função
f = lambda x: (cos(x) - sin(x)**2)*exp(cos(x))

# intervalo
a = 0
b = 2*pi

# chama a função
A, c = matrizes_difFin(f, coefsU, coefsh, a, b, n, contorno)

u = np.linalg.inv(A)*np.matrix(c)
```
