# -*- coding: utf-8 -*-
"""LAB-PythonBianary

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lc7PU1e3INL7SuXmuKTtuBXZ_4UDxmRs
"""

def main():
    while True:
        print("Press 1 to convert binary into numerical")
        print("Press 0 to convert numerical into binary")
        selection = input("Input your selection: ")

        try:
            selection = int(selection)  # Convert input to integer

            if selection == 1:
                BTON()  # Call the binary-to-decimal function
            elif selection == 0:
                NTOB()  # Call the decimal-to-binary function
            else:
                print("Please enter a valid response (0 or 1)")
        except ValueError:
            print("Invalid input. Please enter 0 or 1")

def NTOB():
    while True:
        try:
            number = int(input("Enter your number: "))
            if number == 0:
                print("Binary: 0")
                continue

            binary = ""
            num = number
            while num > 0:
                remainder = num % 2  # Get remainder (0 or 1)
                binary = str(remainder) + binary  # Build the binary string
                num //= 2  # Integer division by 2

            print(f"Binary: {binary}")
            break

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def BTON():
  while True:
      Bianary = input("Enter your Bianary code: ")
      if not all(digit in '01' for digit in Bianary):
          print("invalid")
      else:
          curVal = 0
          length = len(Bianary)
          for i in range(length):
              digit = Bianary[length - i - 1]

              if digit == '1':
                  curVal += (2**i)
          print(f'{Bianary} translates into {curVal}')
          break

if __name__ == "__main__":
    main()

