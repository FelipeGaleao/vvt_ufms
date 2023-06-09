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
    
    click(txt_campo_cpf)
    type(usuario)
    click(txt_campo_senha) 
    type(senha)
    click(btn_fazer_login)
    time.sleep(5) 
    wait(tela_inicial_sistema)
    
    if exists(tela_inicial_sistema):
        print("Usuário logou com sucesso")
        btn_fechar_popup = "1679764976975.png"
        click(btn_fechar_popup)
    else:
        print("O usuário não conseguiu fazer login")

def preencher_quest_lesao():
    input_selecione = "input_selecione.png" 
    btn_submit_questionario = "Salvar.png"
    popup_cadastro = "popup_cadastro.png"
    
    type("l", Key.CTRL)
    type("https://sys.projetomedalha.org/perfil/lesoes/")
    type(Key.ENTER)
    time.sleep(5)
    click(input_selecione)
    type("s")
    type(Key.ENTER)
    type("\t")
    time.sleep(2)
    type("Joelho")
    type("\t")
    type("s")
    type("\t")
    time.sleep(2)
    type("Joelho")
    type("\t")
    type("s")
    type("\t")
    time.sleep(2)
    type("Joelho")
    type("\t")
    type("s")
    type("\t")
    type("s")
    type("\t")
    type("s")
    click(btn_submit_questionario)
    time.sleep(5)
    if(exists(popup_cadastro):
        print("Questionário de lesões cadastrado com sucesso!")
    else:
        print("Questionário de lesões não cadastrado!")

    
abrir_sistema()
fazer_login_sistema("074200300152", "senha123")
preencher_quest_lesao()
