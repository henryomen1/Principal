# - * - coding: utf-8 - * -
# Mapreduce usando biblioteca python mrjob > por meio do Hadoop Streaming (stdin e stdout)
# Exercicio(2)Computar a quantidade de artigos por autor

from mrjob.job import MRJob

class MRWordCount(MRJob):

	def mapper(self, _, linha):
		linha = linha.strip() # remove spaços
		separa = linha.split(" | ") # separa linhas em palavras

		ano, periodico, titulo, qtde_autores, autores = separa[0], separa[1], separa[2], separa[3], separa[4:]

		for autor in autores:
			yield(autor, 1)


	def reducer(self, autor, ocorrencia):
		yield(autor, sum(ocorrencia))

if __name__ == '__main__':
   MRWordCount.run()
