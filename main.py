# This is the main file for the Bedtime Kata for Northwoods
import timeCalc

print("Please enter your times in the following format: 8pm")
begT = input("Please enter the start time: ")
finT = input("Please enter the end time: ")
bT = input("Please enter bedtime: ")

timeCalc.calc_charge(begT, finT, bT)
