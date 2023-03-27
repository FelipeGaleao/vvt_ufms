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

def cadastrar_novo_atleta(nome, sobrenome, cartao_sus, cpf, rg, dt_nascimento, cep):
    """ Função para cadastrar um novo atleta """
    
    link_cadastro = "link_cadastro.png"

    print("Aberto página de cadastro")
    click(link_cadastro)
    
    txt_campo_nome =  "Nome.png"
    txt_campo_sobrenome = "txt_campo_sobrenome.png"
    txt_campo_sus = "txt_campo_sus.png"
    txt_campo_cpf = "CPF.png" 
    txt_campo_rg = "RG.png"
    txt_campo_dt_nascimento = "txt_campo_dt_nascimento.png"
    txt_campo_cep = "txt_campo_cep.png"
    txt_campo_endereco ="txt_campo_endereco.png"
    txt_campo_complemento = "txt_campo_complemento.png"
    txt_campo_cidade = "Cidade.png"
    txt_campo_estado = "Estado.png"
    txt_campo_nacionalidade = "txt_campo_nacionalidade.png"
    txt_celular = "txt_celular.png"
    txt_campo_telefone_fixo = "txt_campo_telefone_fixo.png"
    txt_time_instituicao = "txt_time_instituicao.png"
    txt_link_facebook = "Facebookfo.png"
    txt_email = "txt_email.png"
    txt_senha_1 = "txt_senha_1.png"
    txt_senha_2 = "txt_senha_2.png"
    
    print("Atleta cadastrado no sistema")
    wait(txt_campo_nome)
    click(txt_campo_nome)


    type(nome)
    type("\t")
    type(sobrenome)
    type("\t")
    type("\t")
    type(cartao_sus)
    type("\t")
    type("\t")
    type(cpf)
    type("\t")
    type(rg)
    type("\t")    
    type(dt_nascimento)
    type("\t")
    type(cep)
    type("\t")
    type("\t")
    type("\t")
    type("\t")
    type("\t")
    type("Brasileiro")

abrir_sistema()
cadastrar_novo_atleta("Maycon", "Mota", "0020", "074200300152", "00010", "07/06/2001", "79062370")
