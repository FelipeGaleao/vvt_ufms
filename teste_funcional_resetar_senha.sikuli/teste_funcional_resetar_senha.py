# Importar módulos necessários
from sikuli import *
import time 
import webbrowser

def abrir_sistema():
    # Definir as imagens
    navegador_icone = "navegador_icone-1.png"
    campo_url = "campo_url-1.png"
    logo_site = "logo_site-1.png"
    btn_fechar_popup = "1679764976975-1.png"
    
    # Iniciar o aplicativo do navegador
    
    url = "https://sys.projetomedalha.org"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

    
    # Digitar a URL do site
    type(Key.ENTER)
    
    # Esperar o carregamento do site
    time.sleep(2)
    wait(btn_fechar_popup)
    click(btn_fechar_popup)
    wait(logo_site)
    if exists(logo_site):
        print("Sistema aberto corretamente")
    else:
        print("O sistema não foi aberto corretamente")
        return False
    
    return True

def resetar_senha(email):
    btn_reset = "btn_rest.png"
    btn_txt_email = "btn_txt_email.png"
    btn_receber_email = "btn_receber_email.png"
    tela_confirmacao = "tela_confirmacao.png"
    btn_ok = "btn_ok.png"

    click(btn_reset)
    click(btn_txt_email)
    type(email)
    click(btn_receber_email)

    time.sleep(5)
    wait(tela_confirmacao)
    
    if exists (tela_confirmacao):
        click(btn_ok)
        print("Troca de senha enviada.")
    else:
        print("Falha no envio.")
        return False

    return True

abrir_sistema()
resetar_senha("teste@gmail.com")