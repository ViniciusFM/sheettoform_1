import pandas
import requests
from tqdm import tqdm

#======== INPUT

# Inserir a url do formulario
FORM_URL = 'http://127.0.0.1:5000/form/submit'
# ID do arquivo de planilhas (workbook)
SHEET_ID = '1EKXkCrWfV8avj_3mOInwqUvNC_a5P1b3J6d6HhcswwQ'
# Nome da planilha
SHEET_NAME = 'Dados'
# Mapeamento dos campos da planilha com os campos do formulário 
# (atributo 'name' de cada input)
SHEET_FIELDMAP = {
    'Nome': 'name', 
    'Sobrenome': 'lastname', 
    'Telefone': 'phone', 
    'Empresa': 'company'
}

#==============

SHEET_URL = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

def register_to_form(form_record:dict):
    response = requests.post(FORM_URL, data=form_record)
    if response.status_code != 200:
        print(f'err: could not complete request for: {form_record}')

def main(frame:pandas.DataFrame):
    for i in tqdm(range(len(frame))):
        form_record = {}
        for k, v in SHEET_FIELDMAP.items():
            data = frame.at[i, k]
            form_record.update({v:data})
        register_to_form(form_record)

if __name__ == '__main__':
    print('fetching sheet rows and registering in form...')
    frame = pandas.read_csv(SHEET_URL)
    main(frame)
