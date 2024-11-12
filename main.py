#!/usr/bin/env python3
import os
import argparse
from yt_dlp import YoutubeDL  # type: ignore
import tkinter as tk
from tkinter import filedialog


def activate_virtualenv():

    script_dir = os.path.dirname(os.path.abspath(__file__))

    venv_path = os.path.join(script_dir, 'env')

    if os.path.exists(venv_path) and os.path.isdir(venv_path):
        activate_this = os.path.join(venv_path, 'bin', 'activate_this.py')

        if os.path.exists(activate_this):
            exec(open(activate_this).read(), dict(__file__=activate_this))
            print(f"Ambiente virtual {venv_path} ativado com sucesso!")
        else:
            print("Não foi possível ativar o ambiente virtual.")
    else:
        print("Ambiente virtual não encontrado, instale as dependências.")


def download_video(url, download_folder='/home/valdeir/Vídeos'):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_music(link, download_folder='/home/valdeir/Músicas'):

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


def choose_download_folder():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    folder_selected = filedialog.askdirectory(
        title="Escolha o diretório de destino"
        )
    return folder_selected


def main():
    parser = argparse.ArgumentParser(
        description="Exemplo de script Python com argumentos"
    )

    parser.add_argument('url', type=str, help="A string que você quer passar")

    parser.add_argument('-m', '--music',
                        action='store_true',
                        help="Ativa o sinalizador de música")

    parser.add_argument('-d', '--dir',
                        action='store_true',
                        help="Define se vai usar uma pasta personalizada")

    args = parser.parse_args()

    download_folder = None
    if args.dir:
        download_folder = choose_download_folder()

    if args.music:
        if args.url:
            if download_folder:
                download_music(args.url, download_folder)
            else:
                download_music(args.url)

    else:
        if args.url:
            if download_folder:
                download_video(args.url, download_folder)
            else:
                download_video(args.url)


if __name__ == "__main__":
    activate_virtualenv()
    main()
