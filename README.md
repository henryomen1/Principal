# Principal
#  Limpeza saída de arquivos hadoop streaming (mrjob)
echo " "
echo "============================="
echo "hdfs dfs -rm -R saida1"
echo "hdfs dfs -rm -R saida2"
echo "hdfs dfs -rm -R contagemartigos"
echo " "

hdfs dfs -rm -R saida1
hdfs dfs -rm -R saida2
hdfs dfs -rm -R contagemartigos

# Carregar conjunto de dados para HDFS Hadoop
echo " "
echo "============================="
hdfs dfs -put contagemartigos/<dblp-100k-articles> contagemartigos

# Executar contagem artigos com Hadoop via python mrjob (stdin) Ex.1) mapreduce-python_periodicos.py 
echo " "
echo "============================="
python mapreduce-python_periodicos.py -r hadoop -D mapred.reduce.tasks=5  hdfs://contagemartigos/dblp-100k-articles.txt
