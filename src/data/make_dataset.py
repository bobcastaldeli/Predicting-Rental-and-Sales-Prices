import logging
import subprocess
import yaml
from kaggle.api import KaggleApi


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


with open("params.yaml", "r", encoding="utf-8") as file:
    params = yaml.load(file, Loader=yaml.SafeLoader)
    dataset_name = params["dataset"]["name"]
    output_path = params["dataset"]["raw_folder"]


def download_data():
    """Authenticate and downloading train and test data from Kaggle
    São Paulo real estate sale and rent (april 2019) competition."""

    api = KaggleApi()
    api.authenticate()

    logger.info("Downloading train data")
    subprocess.run(
        [
            "kaggle",
            "datasets",
            "download",
            "-d",
            f"{dataset_name}",
            "--p",
            f"{output_path}",
            "--force",
        ],
        check=True,
    )


if __name__ == "__main__":
    download_data()
