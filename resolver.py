"""
  Para resolver sistemas lineares, temos algumas opções prontas dentro das bibliotecas NumPy e SciPy que, por terem uma eficiência superior a qualquer método que possa ser feito "na mão", podem ser utilizadas.

  No entanto, com fatorações LU, QR, etc. é possível construir funções que podem não ser tão ágeis quanto as das referidas bibliotecas, mas bastante precisas e, tanto quanto possível, eficientes.
"""

from numpy import matrix
from numpy.linalg import inv, solve as solve_np
from scipy.linalg import solve as solve_sp, solve_banded

def resolver_inversa(A,b):
  """
    Dado `Ax=b`, se `A` tiver inversa, então `x = A'b`, onde `A'` representa a inversa de A.
  """
  invA = inv(matrix(A))
  sol = invA * matrix(b)
  return [i[0,0] for i in sol]

def resolver_npsolve(A,b):
  """
    A função `np.solve` resolve sistemas lineares do tipo `Ax=b`.
  """
  sol = solve_np(A,b)
  return sol

def resolver_spsolve(A,b):
  """
    A função `scipy.linalg.solve` resolve sistemas lineares do tipo `Ax=b`.
  """
  sol = solve_sp(A,b)
  return sol

def formaDiagonal(A, uk, lk):
  """
    Encontra a forma diagonal da matriz `A`.
  """
  m = len(A) # qntd de linhas
  n = len(A[0]) # qntd de colunas
  
  # matriz na forma diagonal
  ab = [[0 for j in range(n)] for linha in range(uk+lk+1)]
  # posições
  posicoes = []

  for i in range(uk, -1, -1):
    # adiciona uma linha
    posicoes.append([])
    for w in range(m-i): posicoes[-1].append((w, w+i))

  for j in range(1, lk+1):
    # adiciona uma linha
    posicoes.append([])
    for w in range(m-j): posicoes[-1].append((w+j, w))

  # percorre as linhas
  for linha, pos in enumerate(posicoes):
    for i,j in pos:
      ab[linha][j] = A[i][j]

  return ab

def resolver_spsolvebanded(A,b,ab=[],uk=2,lk=2,retornarAb=False):
  """
    A `solve_banded` do SciPy resolve sistemas de banda.
  """
  # caso a forma diagonal seja vazia, encontra ela
  if len(ab) == 0:
    ab = formaDiagonal(A, uk, lk)
  # resolve
  sol = solve_banded([lk, uk], ab, b)
  return sol,ab if retornarAb else sol
