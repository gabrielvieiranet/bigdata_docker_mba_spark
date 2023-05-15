from kaggle_dataset_downloader import KaggleDatasetDownloader

# Constantes
KAGGLE_JSON_PATH = '~/.kaggle/kaggle.json'  # kaggle token
DATASET_NAME = 'rdoume/beerreviews'
EXTRACT_DIR = 'data/dataset'


class Main:
    def __init__(self):
        self.kaggle_json_path = KAGGLE_JSON_PATH

    def run(self):
        downloader = KaggleDatasetDownloader(self.kaggle_json_path)
        downloader.download_dataset(DATASET_NAME, EXTRACT_DIR)


if __name__ == '__main__':
    main = Main()
    main.run()
