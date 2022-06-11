import diferencas_finitas

def testeAutomatizado(range_n : list or tuple, f, u, a : float, b : float, coefs_U : list, coefs_h : list, contorno : list, norma, funcaoSolucao, printarTabela=False)->dict:
  """
    Esta função recebe os parâmetros básicos de aplicação das Diferenças Finitas,
    com o porém de que recebe também um range para a quantidade de variáveis e a
    função que é solução do problema inicial, para que sejam feitas as devidas
    comparações.

    Para cada valor dentro do range será aplicado o método e os resultados e
    informações guardados em um dicionário que será retornado.
  """
  # dicionário com as informações divididas em listas em ordem
  infos = [["$n$", "$h = \dfrac{(b-a)}{n}$", "$||e(h)|| = ||u - \eta(h)||$", "$p = log_2(||e(h)||/||e(h/2)||)$"]]

  # caso o range_n seja uma tupla, então é um intervalo
  if isinstance(range_n, tuple): valores_n = [i for i in range(range_n[0], range_n[1]+1)]
  # caso seja uma lista, então deve ser percorrido
  elif isinstance(range_n, list): valores_n = range_n

  # percorre n ∈ valores_n
  for n in valores_n:
    # tamanho da diferença
    h = (b - a)/n
        
    # coeficientes da U
    n_coefsU = dict()
    for func in coefs_U:
      indice, valor = func(n)
      n_coefsU[indice] = valor

    # coeficientes da h
    n_coefsH = dict()
    for func in coefs_h:
      indice, valor = func(n)
      n_coefsH[indice] = valor

    # instancia
    dif = DiferencasFinitas(f, n_coefsU, n_coefsH, a, b, contorno)
    # aplica
    A,c = dif.matrizes(n)

    # resolve
    sol = funcaoSolucao(A, c)
    print('soluções:', sol)

    ### Erros
    erros = [ u(a+i*h)-sol[i] for i in range(len(sol)) ]
    # norma do erro
    normaErro = norma(erros)
    # adiciona à lista
    infos.append([
                  n, h, normaErro, log2(infos[-1][2]/normaErro) if len(infos) > 1 else "-"
    ])

  # printa a tabela se quiser
  if printarTabela:
    print('\nTabela dos valores:\n')
    print(tabulate(infos[1:], headers=infos[0]))

    print('\nLaTeX dos valores:\n')
    
    print("\\begin{table}\n\t\\centering\n\t\\begin{tabular}{c|c|c|c}\n\t\t\\hline\\hline")
    for indice, info in enumerate(infos):
      print("\t\t" + " & ".join([str(i) for i in info]), "\\\\ \n \t\t\hline" + ("" if indice != 0 else "\hline"))
      
    print("\t\\end{tabular}\n\\end{table}")

  return infos
