import sys

def main():
  if len(sys.argv)==2:
    if sys.argv[1][0] == "1":
      print("Apache Hadoop selected. Go to http://34.71.159.122/ for the application.")
      exit()
    if sys.argv[1][0] == "2":
      print("Apache Spark selected. Go to http://35.232.52.139/ for the application.")
      exit()
    if sys.argv[1][0] == "3":
      print("Jupyter Notebook selected. Go to http://35.222.102.35/ for the application.")
      exit()
    if sys.argv[1][0] == "4":
      print("SonarQube and SonnarScanner selected. Go to http://34.122.96.82/ for the application.")
      exit()
  print("command not recognized")
  exit()

main()