#!/usr/bin/python
"""
Name: retrieveDrupalData.py
Author: Cortlan Bainbridge
Description:  This turns *.csv files into Google Spreadsheets
Sources:
	https://crate.io/packages/gspread/
	https://github.com/burnash/gspread"
"""
from oauth2client.client import SignedJwtAssertionCredentials
import json # Used to read in OAuth information from a .JSON file
import gspread # Used to interface with the Google Spreadsheet
import argparse # Used for CLI interface

# Load in JSON Key
PRIVATE_KEY = "cred.json"
json_key = json.load(open(PRIVATE_KEY))

#scope for Oauth2
scope = ['https://spreadsheets.google.com/feeds']

# Set up for arguments
parser = argparse.ArgumentParser(description="Tool that turns csv files to google spreadsheets")
parser.add_argument('-f', action="store",required=True,help="Argument that provides the *.csv filename")
parser.add_argument('-n', action="store",required=True,help="Specifies the name of the Google Spreadsheet you are writing to")
parser.add_argument('-s', action="store",required=False,help="Specifies the index sheet you would like to write on, defaults to 0")
args = parser.parse_args()

def main():
	def intToLetter(number):
		div=number
		string=""
		temp=0
		while div>0:
			module=(div-1)%26
			string=chr(65+module)+string
			div=int((div-module)/26)
		return string
	def clearSheet(worksheetName):
		def getNumOfRows(worksheetName):
			numberOfRows = 0
			columnList = worksheetName.col_values(1)
			for item in columnList:
				if item != "":
					numberOfRows += 1
			return numberOfRows
		def getNumOfCols(worksheetName):
			numberOfCols = 0
			rowList = worksheetName.row_values(1)
			for item in rowList:
				numberOfCols += 1
			return numberOfCols
		numberOfRows = getNumOfRows(worksheetName)
		rangeBuild = 'A1:'+str(intToLetter(getNumOfCols(worksheetName)))+str(numberOfRows+1)
		cells_list = worksheetName.range(rangeBuild)
		for cell in cells_list:
			try:
				cell.value = ""
			except:		
				print("ERROR: An error has occurred when erasing on line "+str(index))
		worksheetName.update_cells(cells_list)
		print("Sheet has been cleared...")
		return
	def getCellRange(tableList):
		def getHeight(list2d):
			# Since this is a list of horizontal lists, this is it!
			return len(list2d)
		def getWidth(list2d):
			maxInt = 0
			for horzLine in list2d:
				if len(horzLine) > maxInt:
					maxInt = len(horzLine)
			return maxInt
		rangeStr = "A1:"+str(intToLetter(getWidth(tableList)))+str(getHeight(tableList))
		return rangeStr
	def buildSheetTable(csvFile):
		vertList = list()
		for line in csvFile:
			horzList = list()
			line = line.split(",")
			for cell in line:
				if "\n" in cell:
					cell = cell.replace("\n","")
				horzList.append(cell)
			vertList.append(horzList)
		return vertList
	def csvToCells(csvTable,listOfCells):
		for cell in listOfCells:
			cell.value = csvTable[cell.row-1][cell.col-1]
		return listOfCells

	credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
	try:
		print("Authorizing account...")
		gclient = gspread.authorize(credentials)
		gclient.login()
		print("Account authorized")
	except:
		print("Failed to authorize the service account, make sure you have the right credentials and permissions")
		return
	try:
		sh = gclient.open(args.n)
		if args.s:
			worksheet = sh.get_worksheet(int(args.s))
			print("Authorization complete!")
		else:
			worksheet = sh.get_worksheet(0)
			print("Authorization complete!")
	except gspread.exceptions.SpreadsheetNotFound:
		print("Failed to open up the Spreadsheet, make sure you are sharing it with the service account")
		return
	# Clear the sheet before writing to it to delete previous information
	clearSheet(worksheet)
	csvFile = open(args.f,"r")
	sheetTable = buildSheetTable(csvFile)
	csvFile.close()
	cellRangeStr = getCellRange(sheetTable)
	cells_list = worksheet.range(cellRangeStr)
	cells_list = csvToCells(sheetTable,cells_list)
	worksheet.update_cells(cells_list)
	print("Worksheet has been successfully written!")
	return

main()