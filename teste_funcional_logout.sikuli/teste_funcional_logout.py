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

def deslogar_sistema():
    btn_usuario = "btn_usuario.png"
    btn_logout = "btn_logout.png"
    tela_logout = "1679949805780.png"

    click(btn_usuario)
    time.sleep(2)
    click(btn_usuario)
    click(btn_logout)
    time.sleep(3)
    if exists(tela_logout):
        print("Usuário deslogou com sucesso")
    else:
        print("O usuário não conseguiu deslogar")

   
    
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
    else:
        print("O usuário não conseguiu fazer login")

def fazer_logout_sistema():
    btn_perfil = "btn_perfil.png"
    btn_sair = "btn_sair.png"
    tela_home = "tela_home.png"

    click(btn_perfil)
    click(btn_sair)
    time.sleep(5)
    wait(tela_home)
    
    if exists(tela_home):
        print("O usuario conseguiu deslogar")
    else:
        print("O usuario nao conseguiu deslogar")
        return False
    return True
    
abrir_sistema()
fazer_login_sistema("074200300152", "senha123")
fazer_logout_sistema()