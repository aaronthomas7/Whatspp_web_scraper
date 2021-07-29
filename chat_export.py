import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('spreadsheetdata-321315-fc1e730d581b.json',scope)

gc = gspread.authorize(credentials)

wks = gc.open('universal adventures sheet').sheet1

#print(wks.get_all_records())

i = 'hi there people i am aaron how do you do?'

wks.append_row([i.split()])