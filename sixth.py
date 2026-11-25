import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []

    response = requests.get(url)
    if response.status_code == 200:
        html = response.content.decode('utf-8')

        casti = html.split('<a href="')

        i = 1
        while i < len(casti):
            cast = casti[i]
            odkaz = cast.split('"')[0]
            hrefs.append(odkaz)
            i += 1
    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)
        print(odkazy)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
