    # Importar módulos necessários
from sikuli import *
import time 
import webbrowser

def abrir_sistema():
    # Definir as imagens
    navegador_icone = "navegador_icone.png"
    campo_url = "campo_url.png"
    logo_site = "logo_site.png"
    btn_fechar_popup = "1679764976975.png"
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
    
def fazer_login_sistema(usuario, senha):
    txt_campo_cpf = "1679948457154.png"
    txt_campo_senha = "txt_campo_senha.png"
    btn_fazer_login = "btn_fazer_login.png"

    tela_inicial_sistema = "tela_inicial_sistema.png"
    btn_ok = "btn_ok.png"
    
    click(txt_campo_cpf)
    type(usuario)
    click(txt_campo_senha) 
    type(senha)
    click(btn_fazer_login)
    time.sleep(5) 
    wait(tela_inicial_sistema)
    
    if exists(tela_inicial_sistema):
        click(btn_ok)
        print("O usuário não conseguiu fazer login")
    else:
        print("O usuário não conseguiu fazer login")

    
abrir_sistema()
fazer_login_sistema("074200300152", "senha1234")
