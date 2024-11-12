#!/usr/bin/env python3

import os


# Função para detectar o ambiente virtual no diretório base do projeto
def activate_virtualenv():
    # Obtém o diretório base onde o script está sendo executado
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho para o ambiente virtual dentro do diretório base
    venv_path = os.path.join(script_dir, 'env')

    # Verifica se o diretório do ambiente virtual existe
    if os.path.exists(venv_path) and os.path.isdir(venv_path):
        activate_this = os.path.join(venv_path, 'bin', 'activate_this.py')

        # Ativa o ambiente virtual se o arquivo de ativação existir
        if os.path.exists(activate_this):
            exec(open(activate_this).read(), dict(__file__=activate_this))
            print(f"Ambiente virtual {venv_path} ativado com sucesso!")
        else:
            print("Não foi possível ativar o ambiente virtual.")
    else:
        print("Ambiente virtual não encontrado, instale as dependências.")


# Função para baixar o vídeo
def download_video(url, download_folder='/home/valdeir/Vídeos'):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',  # Define o caminho de saída
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# Função para baixar música
def download_music(link, download_folder='/home/valdeir/Músicas'):

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',  # Define o caminho de saída
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


def choose_download_folder():
    # Cria uma janela de diálogo para escolher uma pasta
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    folder_selected = filedialog.askdirectory(title="Escolha o diretório de destino")
    return folder_selected


def main():
    parser = argparse.ArgumentParser(
        description="Exemplo de script Python com argumentos"
    )

    # Adiciona um argumento do tipo string
    parser.add_argument('url', type=str, help="A string que você quer passar")

    parser.add_argument('-m', '--music', action='store_true', help="Ativa o sinalizador de música")
    parser.add_argument('-d', '--dir', action='store_true', help="Define se vai usar uma pasta personalizada")
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
    import argparse
    from yt_dlp import YoutubeDL  # type: ignore
    import tkinter as tk
    from tkinter import filedialog

    activate_virtualenv()
    main()
