from shutil import copyfile

import requests
import tabula
from bs4 import BeautifulSoup

def main():
    res = requests.get('https://www.mwra.com/biobot/biobotdata.htm')
    base_url = "/".join(res.url.split("/")[:-1]) + '/'

    soup = BeautifulSoup(res.text, 'html.parser')
    link = soup.select('a[href^="2022/MWRAData"][href$="-data.pdf"]')[0].attrs['href']
    date_string = link[13:-9]
    pdf_url = base_url + link

    df = tabula.io.convert_into(pdf_url, pages='all', lattice=True, output_path=f'output/mwra-data-{date_string}.csv', output_format='csv')

    copyfile(f'output/mwra-data-{date_string}.csv', 'output/latest.csv')

if __name__ == '__main__':
    main()