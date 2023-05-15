import os
import zipfile

from kaggle.api.kaggle_api_extended import KaggleApi


class KaggleDatasetDownloader:
    def __init__(self, kaggle_json_path):
        self.api = KaggleApi()
        self.api.authenticate()

        # Define o caminho para o arquivo kaggle.json
        self.kaggle_json_path = kaggle_json_path

    def download_dataset(self, dataset_name, extract_dir):
        # Verifica se o diretório de destino existe; se não, cria o diretório
        if not os.path.exists(extract_dir):
            os.makedirs(extract_dir)

        # Faz o download do conjunto de dados
        self.api.dataset_download_files(
            dataset_name, path=extract_dir, quiet=False)

        # Localiza o arquivo ZIP baixado
        zip_file = [file for file in os.listdir(
            extract_dir) if file.endswith('.zip')][0]
        zip_file_path = os.path.join(extract_dir, zip_file)

        # Extrai o arquivo ZIP baixado
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
