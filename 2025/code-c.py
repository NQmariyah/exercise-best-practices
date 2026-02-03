def f(n):return 1 if n==0 else n*f(n-1)
def main():
  num = 5 
  print("Faktorial dari",num, "adalah",f(num))

main()
