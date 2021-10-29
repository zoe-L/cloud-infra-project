import sys

def main():
  if len(sys.argv)==2:
    print(len(sys.argv[1]))
    if sys.argv[1][0] == "1":
      print("Apache Hadoop selected.")
      exit()
    if sys.argv[1][0] == "2":
      print("Apache Spark selected.")
      exit()
    if sys.argv[1][0] == "3":
      print("Jupyter Notebook selected.")
      exit()
    if sys.argv[1][0] == "4":
      print("SonarQube and SonnarScanner selected.")
      exit()
  print("command not recognized")
  exit()

main()