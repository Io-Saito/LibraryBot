import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import Japan_perse
import kinokuniya_parse
import maruzen_perse
import time
import tqdm


def connect_gspread(jsonf, key):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        jsonf, scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    return worksheet


jsonf = "libbot-307106-caaee1ec4c17.json"
spread_sheet_key = "1Lq8tDDPpLvDJadSYGJldpZXuurYS3VsgXBqENZGtvSY"
ws = connect_gspread(jsonf, spread_sheet_key)


ws.update_acell("A1", "title")
ws.update_acell("B1", "author")
ws.update_acell("C1", "publish")
ws.update_acell("D1", "publish_date")
ws.update_acell("E1", "link")
ws.update_acell("F1", "from")

book_data = maruzen_perse.li
book_data.extend(kinokuniya_parse.data_list)
book_data.extend(Japan_perse.data_list)

new_list = []
for i, x in tqdm.tqdm(enumerate(book_data)):
    new_list.append([x["title"], x["author"], x["publish"],
                     x["publish_date"], x["link"], x["from"]])

ws.update('A9859:F12000', new_list)
