from bs4 import BeautifulSoup
import zipfile
import requests


# Lê o html da página
# Filtra todas as tags <p> com classe `callout`, grandemente reduzindo o escopo de busca dos arquivos
# Para as tags <a> que possuem o texto 'Anexo', insere em um vetor o link dessa tag, junto de seu nome e extensão
def get_file_urls() -> [str, (str, str)]:
    ans_url = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'
    ans_html = requests.get(ans_url).text

    soup = BeautifulSoup(ans_html, 'html.parser')

    file_links: [str, (str, str)] = []
    for link in soup.find_all('p', class_='callout'):
        name: str = link.a.text
        if name[0:5] == "Anexo":
            name_no_extension = name.rpartition(' ')[0]
            extension = name[name.find("(") + 1: name.find(")")]
            link = link.a.get('href')
            file_links.append([link, (name_no_extension, extension)])

    return file_links


# Cria novos arquivos, e os popula com o conteúdo das urls
def download_files(urls: [str, (str, str)], target_dir: str):
    for url in urls:
        file_name = f"{target_dir}/{url[1][0]}{url[1][1]}"
        file = open(file_name, 'wb')
        downloaded_content = requests.get(url[0]).content
        file.write(downloaded_content)


# Cria um arquivo zip
# Insere os arquivos passados nesse .zip
def compress_files(file_names: [str], source_dir: str):
    zip_name = 'Anexos.zip'
    target_zip = zipfile.ZipFile(zip_name, mode='w')
    try:
        for name in file_names:
            target_zip.write(f"{source_dir}/{name}", name, compress_type=zipfile.ZIP_DEFLATED)

    except FileNotFoundError:
        print("Algum dos arquivos não foi encontrado")

    finally:
        target_zip.close()
