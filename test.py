#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
import csv
import re

def readCSV(filename, delimiter=' ',quotechar='|'):
	with open(filename, newline='') as csvfile:
		reader =  csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
		csvArray = []
		i=0
		for row in reader:
			csvArray.append(row)
			# print(', '.join(row))
			# 
		return csvArray


def day1():
	inputArray = readCSV('input1')
	for row1 in inputArray:
		for row2 in inputArray:
			val1=int(row1[0])
			val2=int(row2[0])
			if (val1+val2 == 2020):
				print(val1*val2)

def day1_2():
	inputArray = readCSV('input1')
	for row1 in inputArray:
		for row2 in inputArray:
			for row3 in inputArray:
				val1=int(row1[0])
				val2=int(row2[0])
				val3=int(row3[0])
				if (val1+val2+val3 == 2020):
					print(val1*val2*val3)


def day2():
	inputArray = readCSV('input2')
	valid = 0;
	for row in inputArray:
		letter = row[1][0]
		min_l=int(row[0].split("-")[0])
		max_l=int(row[0].split("-")[1])
		occ = 0
		for l in row[2]:
			if l == letter:
				occ = occ+1
		if occ >= min_l and occ <= max_l :
			valid = valid + 1
	print(valid)

def day2_2():
	inputArray = readCSV('input2')
	valid = 0;
	for row in inputArray:
		letter = row[1][0]
		min_l=int(row[0].split("-")[0])
		max_l=int(row[0].split("-")[1])
		if len(row[2]) >= min_l and row[2][min_l - 1] == letter:
			if len(row[2]) >= max_l :
				if row[2][max_l - 1] != letter:
					valid = valid + 1
			else:
				valid = valid + 1

		elif len(row[2]) >= max_l and row[2][max_l - 1] == letter:
			valid = valid + 1
	print(valid)

def day3():
	inputArray = readCSV('input3')
	position_y= 0 
	trees = 0
	i = 1
	while i < len(inputArray):
	# for row in inputArray:
		row = inputArray[i]
		position_y = position_y + 3
		if(position_y >= len(row[0])):
			position_y = position_y - len(row[0])

		if(row[0][position_y] == "#"):
			trees = trees + 1
		i = i +1
	print(trees) 

def day3_2():
	inputArray = readCSV('input3')
	slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
	number = 1
	for slope in slopes:
		pas_y = slope[0]
		pas_x = slope[1]
		position_y = 0
		trees = 0
		i = pas_x
		while i < len(inputArray):
		# for row in inputArray:
			row = inputArray[i]
			position_y = position_y + pas_y
			if(position_y >= len(row[0])):
				position_y = position_y - len(row[0])

			if(row[0][position_y] == "#"):
				trees = trees + 1
			i = i + pas_x
		print(trees)
		number = number * trees
	print(number)


def day4():
	inputArray = readCSV('input4',delimiter='\n')
	requiredValues = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
	passports = []
	newPassport = ""
	for row in inputArray:
		if len(row) != 0:
			newPassport = newPassport + " " + row[0]
		else:
			passports.append(newPassport)
			newPassport = ""
	passports.append(newPassport)
	validPassports = 0
	for passport in passports:
		valid = True
		for val in requiredValues:
			if passport.find(val) == -1:
				valid = False

				break

		if valid :
			validPassports = validPassports + 1
	print(validPassports)

def day4_2():
	inputArray = readCSV('input4',delimiter='\n')
	requiredValues = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
	passports = []
	newPassport = ""
	for row in inputArray:
		if len(row) != 0:
			newPassport = newPassport + " " + row[0]
		else:
			passports.append(newPassport)
			newPassport = ""
	passports.append(newPassport)
	validPassports = 0
	for passport in passports:
		valid = True
		for val in requiredValues:
			if passport.find(val) == -1:
				valid = False
				break

			passVal = passport.split(val+":")[1].split(" ")[0]
			if val == "byr":
				if(len(passVal) != 4 or int(passVal) < 1920 or int(passVal) > 2002):
					valid = False
					break
			elif val == "iyr":
				if(len(passVal) != 4 or int(passVal) < 2010 or int(passVal) > 2020):
					valid = False
					break
			elif val == "eyr":
				if(len(passVal) != 4 or int(passVal) < 2020 or int(passVal) > 2030):
					valid = False
					break
			elif val == "hgt":
				if passVal.find("cm") != -1:
					hgt = passVal.split('cm')[0]
					if(int(hgt) < 150 or int(hgt) > 193):
						valid = False
						break
				elif passVal.find("in") != -1:
					hgt = passVal.split('in')[0]
					if(int(hgt) < 59 or int(hgt) > 76):
						valid = False
						break
				else:
					valid = False
					break
			elif val == "hcl":
				if not(re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', passVal)):
					valid = False
					break
			elif val == "ecl":
				if not passVal in ["amb","blu","brn","gry","grn","hzl","oth"]:
					valid = False
					break
			elif val == "pid":
				if len(passVal) != 9:
					valid = False
					break
		if valid :
			print(passport)
			validPassports = validPassports + 1
	print(validPassports)


def day5():
	inputArray = readCSV('input5',delimiter='\n')
	maxid = 0
	for row in inputArray:
		boardp = row[0]
		#find row
		minRow = 0
		maxRow = 127
		i = 0
		while i < 7:
			if boardp[i] == "F":
				maxRow = int(minRow + (maxRow-minRow)/2)
			else:
				minRow = int(minRow + (maxRow-minRow)/2) + 1
			i = i+1
		# find columns
		minCol = 0
		maxCol = 7
		while i < 10:
			if boardp[i] == "L":
				maxCol = int(minCol + (maxCol-minCol)/2)
			else:
				minCol = int(minCol + (maxCol-minCol)/2) + 1
			i = i+1
		id = maxRow * 8 + maxCol
		print(maxCol)
		print(minCol)
		print(id)
		print("-------")
		if maxid < id:
			maxid = id
	print(maxid)


def day5_2():
	inputArray = readCSV('input5',delimiter='\n')
	emptySeats = [[i*8+j for j in range(8)] for i in range(128)]
	for row in inputArray:
		boardp = row[0]
		#find row
		minRow = 0
		maxRow = 127
		i = 0
		while i < 7:
			if boardp[i] == "F":
				maxRow = int(minRow + (maxRow-minRow)/2)
			else:
				minRow = int(minRow + (maxRow-minRow)/2) + 1
			i = i+1
		# find columns
		minCol = 0
		maxCol = 7
		while i < 10:
			if boardp[i] == "L":
				maxCol = int(minCol + (maxCol-minCol)/2)
			else:
				minCol = int(minCol + (maxCol-minCol)/2) + 1
			i = i+1
		id = maxRow * 8 + maxCol
		emptySeats[maxRow][maxCol] = False
	idx = 1
	while idx < 127:
		jdx = 1
		while jdx < 7:
			if emptySeats[idx][jdx] != False and emptySeats[idx][jdx + 1] == False and emptySeats[idx][jdx - 1] == False:
				print(emptySeats[idx][jdx])
			jdx = jdx +1
		idx = idx +1

def day6():
	inputArray = readCSV('input6',delimiter='\n')
	answers = 0
	newanswer = ''
	for row in inputArray:
		if len(row) != 0:
			i = 0
			while i < len(row):
				j = 0
				while j < len(row[i]):
					if newanswer.find(row[i][j]) == -1:
						newanswer = newanswer + row[i][j]
						
					j = j+1
				i=i+1
		else:
			print(newanswer)
			answers = answers + len(newanswer)
			newanswer = ''
	answers = answers + len(newanswer)
	print(answers)

def day6_2():
	inputArray = readCSV('input6',delimiter='\n')
	answers = 0
	newanswer = inputArray[0][0]
	rowIdx = 0
	while rowIdx < len(inputArray):
		row = inputArray[rowIdx]
		if len(row) != 0:
			i = 0
			while i < len(row):
				j = 0
				thisanswer = ''
				while j < len(row[i]):
					if newanswer.find(row[i][j]) != -1:
						thisanswer = thisanswer + row[i][j]
					j = j+1
				newanswer = thisanswer			
				i=i+1
		else:
			answers = answers + len(newanswer)
			newanswer = inputArray[rowIdx + 1][0]
		rowIdx = rowIdx + 1
	answers = answers + len(newanswer)
	print(answers)

day6_2()