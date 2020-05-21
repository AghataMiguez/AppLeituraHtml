from bs4 import BeautifulSoup
import glob


def busca_arquivos(path): 
       
    return glob.glob(path + '*.html')

def busca_capa_processo(html_principal):

    capa_processo = {}
    
    capa_processo['Processo'] = html_principal.find(id='txtNumProcesso').text
    capa_processo['Orgão Julgador'] = html_principal.find(id='txtOrgaoJulgador').text
    capa_processo['Classe da ação'] = html_principal.find(id='txtClasse').text
    capa_processo['Data da Autuação'] = html_principal.find(id='txtAutuacao').text
    capa_processo['Situação'] = html_principal.find(id='txtSituacao').text
    capa_processo['Juiz'] = html_principal.find(id='txtMagistrado').text
     
    return capa_processo

def busca_processos_relacionados(html_principal):

    line_list_tr = html_principal.select('#tableRelacionado tr') 

    processos_relacionados = {}
    processos = []
    for line_tr in line_list_tr:
        concatenacaoDosTds = ''
        lista_de_tds = line_tr.select('td')
        if line_tr.find('td') is not None:
            for td_unico in lista_de_tds:                
                concatenacaoDosTds = concatenacaoDosTds + ' ' + td_unico.get_text()                
            processos.append(concatenacaoDosTds)  

    processos_relacionados['Processos Relacionados'] = processos

    return processos_relacionados

def busca_partes_e_representandes(html_principal):

    partes_e_representantes = {}
    lista_titulo_th = html_principal.select('#fldPartes table tr th')
    linhas_tabela_td = html_principal.select('#fldPartes table tr td')
    index = 0
    while index < len(lista_titulo_th):
        partes_e_representantes[lista_titulo_th[index].get_text()] = linhas_tabela_td[index].get_text().replace(u'\xa0', ' ')        
        index = index + 1   
    
    return partes_e_representantes

def busca_eventos(html_principal):

    lista_eventos = []
    evento = {}
    tables_html = html_principal.find(id='divInfraAreaProcesso').find_all('table')    
    linhas_titulo_th = tables_html[-1].select('tr th')
    linhas_tabela_tr = tables_html[-1].select('tr')
    
    for i, line_tr in enumerate(linhas_tabela_tr):
        if i > 0:
            lista_de_tds = line_tr.select('td')
            j = 0
            for td_unico in lista_de_tds:
                evento[linhas_titulo_th[j].get_text()] = td_unico.get_text()
                j = j + 1
            
            lista_eventos.append(evento.copy())

    return lista_eventos


##### PROGRAMA PRINCIPAL #######

# dados_capa_processo = {}
# partes_e_representantes = {}       
# dados = {}  
# lista_dados = []     
# lista_eventos = [] 
# path_principal = '/home/aghata/Documentos/impactatest/data/'
# lista_de_arquivos = busca_arquivos(path_principal)

# for caminho_arquivo in lista_de_arquivos:

#     arquivo_html = open(caminho_arquivo ,'r', encoding='ISO 8859-1')
#     html_principal = BeautifulSoup(arquivo_html.read(), 'lxml')
#     dados_capa_processo = busca_capa_processo(html_principal)       
#     partes_e_representantes = busca_partes_e_representandes(html_principal)
#     lista_eventos = busca_eventos(html_principal)

#     print(busca_processos_relacionados(html_principal))

#     lista_dados.append(dados_capa_processo)
#     lista_dados.append(partes_e_representantes)
#     lista_dados.append(lista_eventos)
    
#     dados['Dados do arquivo: ' + caminho_arquivo[len(path_principal)-1:]] = lista_dados
#     lista_dados = []

# print(dados)

