# Importar módulos necessários
from sikuli import *
import time 

def abrir_sistema():
    # Definir as imagens
    navegador_icone = "navegador_icone.png"
    campo_url = "campo_url.png"
    logo_site = "logo_site.png"
    btn_fechar_popup = "1679764976975.png"
    # Iniciar o aplicativo do navegador
    click(navegador_icone)

    # Esperar o navegador abrir
    wait(campo_url)
    click(campo_url)
    
    # Digitar a URL do site
    type("sys.projetomedalha.org")
    type(Key.ENTER)
    
    # Esperar o carregamento do site
    time.sleep(10)
    wait(btn_fechar_popup)
    click(btn_fechar_popup)
    wait(logo_site)
    if exists(logo_site):
        print("Sistema aberto corretamente")
    else:
        print("O sistema não foi aberto corretamente")
        return False
    
    return True

def cadastrar_novo_atleta():
    link_cadastro = "link_cadastro.png"

    print("Aberto página de cadastro")
    click(link_cadastro)

def gerar_dados_fake():
    from faker import Faker
    faker = Faker("pt_BR")
    print(faker.name)
# Chamar a função para verificar o site

pip install faker
