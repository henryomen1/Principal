# - * - coding: utf-8 - * -
# Mapreduce usando biblioteca python mrjob > por meio do Hadoop Streaming (stdin e stdout)
# Exercicio(1)Computar a quantidade de artigos por periódico

from mrjob.job import MRJob

class MRWordCount(MRJob):

	def mapper(self, _, linha):
		linha = linha.strip() # remove leading and trailing whitespace
		separa = linha.split(" | ") # split linha in words

		ano, periodico, titulo, numero_autores, autor = separa[0], separa[1], separa[2], separa[3], separa[4:]

		yield(periodico, 1)


	def reducer(self, periodico, ocorrencia):
		yield(periodico, sum(ocorrencia))

if __name__ == '__main__':
   MRWordCount.run()
