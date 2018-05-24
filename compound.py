import sys

# basis = int(input("Enter initial investment: "))
# rate = int(input("Enter interest rate: "))
# compound = int(input("How many times is it compounded?(Ex. 365 if daily, 12 if monthly, etc.): "))

def calculateInvestment():
  basis = int(input("Enter initial investment: "))
  rate = int(input("Enter interest rate: "))
  compound = int(input("How many times is it compounded?(Ex. 365 if daily, 12 if monthly, etc.): "))
  count = 0
  adjustedRate = rate/100
  earnings = 0
  while(count < compound):
    earnings = basis * adjustedRate
    basis = basis + earnings
    count += 1
  print(basis)


def main():
  calculateInvestment()

if __name__ =='__main__':
  main()
