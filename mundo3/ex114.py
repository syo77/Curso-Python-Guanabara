"""
Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
"""

import requests
import re
import validators
from time import sleep
from os import system
system('cls')

def verificar_site(url, nome_site):
    """
    Verifica se o site está acessível.
    :param url: URL do site a ser testado (padrão: Pudim)
    :return: True se o site estiver acessível, False caso contrário.
    """
    padrao_url = re.compile(r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-z]{2,6}(/.*)?$")
    if not padrao_url.match(url) or not validators.url(url):
        print("❌ ERRO: URL inválida! Certifique-se de digitar um link válido.")
        return None
    print(f"🔎 Verificando a acessibilidade do site {nome_site}...")
    try:
        resposta = requests.get(url, timeout=5)
        return resposta.status_code == 200
    except requests.RequestException:
        return False

nome_site = str(input("Digite o nome do site a ser testado: ")).strip()
while True:
    url = str(input(f"Digite a URL do site {nome_site} que vai ser testado: ")).strip()

    status = verificar_site(url, nome_site)

    if status is not None:
        break
    else:
        print("🔄 \033[0;31mTente novamente...\033[m")

sleep(1)
if status:
    print(f"✅ \033[0;32mO site {nome_site} está acessível!\033[m")
else:
    print(f"❌ \033[0;31mO site {nome_site} não está acessível no momento.\033[m")
print()
