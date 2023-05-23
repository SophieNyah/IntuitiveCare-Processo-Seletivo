import shutil
import files
from os import mkdir, path

def main():
    # Cria o diretório `tmp/` para armazenar temporariamente os arquivos baixad
    #   Exclui o diretório e todos os arquivos dentro, caso já exista
    download_dir = 'tmp'
    if path.exists(download_dir):
        shutil.rmtree(download_dir)
    mkdir(download_dir)

    # Lê do site as urls para download dos arquivos, junto de seu nome e extensão
    files_url: [str, (str, str)] = files.get_file_urls()
    files.download_files(files_url, download_dir)

    file_names: [str] = []
    for file in files_url:
        file_names.append(f"{file[1][0]}{file[1][1]}")

    # Comprime os arquivos baixados, e exclui o diretório `tmp/`
    files.compress_files(file_names, download_dir)
    shutil.rmtree(download_dir)


if __name__ == '__main__':
    main()
