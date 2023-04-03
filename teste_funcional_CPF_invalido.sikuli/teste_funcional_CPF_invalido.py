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

def cpf_invalido(nome, sobrenome, cartao_sus, cpf, rg, dt_nascimento, cep, nacionalidade, celular, telefone, clube, face, email, senha, confirmar):
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
    tela_erro = "tela_erro.png"
    btn_ok = "btn_ok.png"
    
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
    type(nacionalidade)
    type("\t")
    type(celular)
    type("\t")
    type(telefone)
    type("\t")
    type(clube)
    type("\t")
    type("\t")
    type("\t")
    type(face)
    type("\t")
    type(email)
    type("\t")
    type(senha)
    type("\t")
    type(confirmar)
    type("\t")
    type("\t")
    type("\n")

    time.sleep(5)
    wait(tela_erro)
    if exists (tela_erro):
        click(btn_ok)
        print("Falha no cadastro")
    else:
        return False
    return True

abrir_sistema()
cpf_invalido("Maycon", "Mota", "0020", "11111111111", "00010", "07/06/2001", "79062370", "Brasileiro", "64999522359", "64999522359", "Palmeiras", "Instagram", "teste2@gmail.com", "senha123", "senha123")
