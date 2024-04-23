import os
import requests
from urllib.parse import unquote
import zipfile


CWD = os.getcwd()


def download_data(url: str, output_filename: str):
    """simpler funciton to download data from url and save it to output_filename, it does not show any progress bar or animation"""
    output_path = os.path.join(CWD, output_filename)
    if os.path.exists(output_path):
        print(f"{output_filename} already exists, skipping download.")
        return
    decoded_url = unquote(url)
    response = requests.get(decoded_url)
    with open(output_filename, "wb") as f:
        f.write(response.content)


def download_data_with_animation(url: str, output_filename: str):
    """function to download data from url and save it to output_filename, it shows progress bar"""
    output_path = os.path.join(CWD, output_filename)
    if os.path.exists(output_path):
        print(f"{output_filename} already exists, skipping download.")
        return

    from tqdm import tqdm

    decoded_url = unquote(url)
    response = requests.get(decoded_url, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))
    chunk = 1
    chunk_size = 1024
    num_bars = int(file_size / chunk_size)

    with open(output_filename, "wb") as fp:
        for chunk in tqdm(
            response.iter_content(chunk_size=chunk_size),
            total=num_bars,
            unit="KB",
            desc=output_filename,
            leave=True,  # progressbar stays
        ):
            fp.write(chunk)


def unzip_data(file_path, output_dir):
    output_path = os.path.join(CWD, output_dir)
    if os.path.exists(output_path):
        print(f"{output_dir} already exists, skipping unzip.")
        return

    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(output_dir)
    print(f"Unzipped {file_path} to {output_dir}")
