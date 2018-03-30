#!/usr/bin/env python3

def main():
  acc = 0

  for x in range(0, 1000000):
    if (isPalindrome(x)):
      acc = acc + x
  print("final sum is", acc)

def dec_to_bin(x):
    return int(bin(x)[2:])

def isPalindrome(num):
  strNum = str(num)
  flipped = strNum[::-1]

  binNum = str(dec_to_bin(num))
  flippedBin = binNum[::-1]

  return (strNum == flipped) and (binNum == flippedBin)

if __name__ == "__main__":
  main()