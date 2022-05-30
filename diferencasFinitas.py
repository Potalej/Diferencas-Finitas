class DiferencasFinitas:
  """
    Esta classe compreende alguns métodos utilizados na resolução numérica de EDOs da forma -u''(x) = f(x) pelo método das diferenças finitas com condições de contorno de Dirichlet
	"""
	def __init__(self, f, coefsU : dict, coefsh : dict, a : float = 0, b : float = 1, contorno : list = []):
		# armazena a função
		self.f = f
		# coeficientes de U
		self.coefsU = coefsU
		# coeficientes de h
		self.coefsh = coefsh
		# limites
		self.a, self.b = a,b
		# condições de contorno
		self.contorno = contorno
		
	def linhaCoeficientes(self, n : int, coluna : int, coeficientes : dict) -> tuple:
		"""
			Cria uma lista de tamanho `n`que contém os coeficientes na posição necessária (a partir da `coluna`).
		"""		
		# caso necessário, será adicionado um vlaor na matriz da direita
		adicional=(0,0)
		# linha
		linha = [0 for i in range(n)]
		# percorre as chaves dos coeficientes
		for pos in coeficientes:
			# verifica se a posição coluna + pos é comportada na matriz
			if not 0 <= coluna+pos < n:
				# se não for, segue o baile, mas com um adendo: adiciona do outro lado
				adicional = (-coeficientes[pos], 0 if coluna+pos < 0 else -1)
			else:
				# caso seja, adiciona
				linha[coluna+pos] = coeficientes[pos]
		# retorna a lista e o adicional
		return linha, adicional
	
	def matrizes(self, n) -> list:
		"""
			Cria as matrizes que aparecem na hora de encontrar a soluçãoi (Au=c).
		"""
		# matriz direita
		c = [[0] for i in range(n)]
		# valor h utilizado
		h = (self.b - self.a)/n
		# matriz de pontos
		x = [self.a + h*k for k in range(n)]
		# percorre as chaves dos coeficientes de h
		for chave in self.coefsh:
			valores = []
			# se a chave for um int, então cria um range de 1 elemento
			if isinstance(chave, int): valores=[chave]
			# se a chave for uma tupla, pode pegar direto os valores
			elif isinstance(chave, tuple): valores[i fro i in range(chave[0], chave[1]+1)]
			
			# percorre as linhas obtidas
			for linha in valores: c[linha][0] = -self.coefsh[chave] * (h**2) * self.f(x[linha])
				
		# matriz A
		A = [[] for i in range(n)]
		# percorre as chaves dos coeficientes de U
		for chave in self.coefsU:
			valores = []
			# se a chave for um int, então apenas uma linha será alterada
			if isinstance(chave, int): valores=[chave]
			# se a chave for uma tupla, então tem um range de valores
			elif isinstance(chave, tuple): valores=[i for i in range(chave[0], chave[1]+1)]
			
			# percorre os valores
			for linha in valores:
				# cria a linha
				novaLinha, adicional = self.linhaCoeficientes(n=n, coluna=linha, coeficientes=self.coefsU[chave])
				# adiciona a nova linha ao A
				A[linha] = novaLinha
				# separa o adicional
				coef, pos_adicional = adicional
				# adiciona o resto a c
				c[linha][0] += coef * self.contorno[pos_adicional]
				
		return A, c
