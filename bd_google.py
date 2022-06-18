import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def create_table():
    print('Подгрузка Базы Данных')
    CREDENTIALS_FILE = 'credentials.json'  # Имя файла с закрытым ключом
    # Читаем ключи из файла
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
    service = build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API

    spreadsheet = service.spreadsheets().create(body = {
        'properties': {'title': 'База данных о поставках', 'locale': 'ru_RU'},
        'sheets': [{'properties': {'sheetType': 'GRID',
                                   'sheetId': 0,
                                   'title': 'Лист номер один',
                                   'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
    }).execute()
    spreadsheetId = spreadsheet['spreadsheetId'] # сохраняем идентификатор файла
    our_table = 'https://docs.google.com/spreadsheets/d/' + spreadsheetId
    print(our_table)

    driveService = build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
    access = driveService.permissions().create(
        fileId = spreadsheetId,
        body = {'type': 'user', 'role': 'writer', 'emailAddress': 'rafil.galimzyanov.00@bk.ru'},  # Открываем доступ на редактирование
        fields = 'id'
    ).execute()
    return service, spreadsheetId, our_table

'''
Чтение данных 

'''
def verify_data():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId,
        range='2:100',
        majorDimension='ROWS'
    ).execute()
    try:
        data_list = values['values']
        return data_list
    except:
        print(f'База не заполнена')
        pass

service, spreadsheetId, our_table = create_table()