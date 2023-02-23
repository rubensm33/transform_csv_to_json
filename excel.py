from pathlib import Path
import csv
import json
import api

PATH_CSV = Path(__file__).parent / "Nome do seu arquivo CSV"
PATH_JSON = Path(__file__).parent / "Nome do seu arquivo JSON"

print(PATH_CSV)


def converter_csv_para_json(caminho_csv, caminho_json):
    lista_dict_json = []

    # Lê arquivo csv
    with open(caminho_csv, encoding="utf-8") as csv_arquivo:
        leitor_csv = csv.DictReader(csv_arquivo)

        # Converte cada linha csv em um dicionário
        for linha in leitor_csv:
            lista_dict_json.append(linha)

    # Converte a lista de dicionário em JSON String e escreve o arquivo
    with open(caminho_json, "w", encoding="utf-8") as json_arquivo:
        json_string = json.dumps(lista_dict_json, indent=4)
        json.write(json_string)


if __name__ == "__main__":
    api.upload_file()
    converter_csv_para_json(api.UPLOAD_PASTA, api.CAMINHO_JSON)
