from flask import Flask, render_template, request, redirect
import leituraArquivo as la

app = Flask(__name__)

 
partes_e_representantes = {}     
lista_eventos = [] 
lista_de_arquivos = []

@app.route('/')
def index():
    
    return render_template('index.html', titulo='Extração de dados de arquivos html')


@app.route('/leitura', methods=['POST',])
def leitura():

    path_principal = request. form['caminho_arquivos']
    lista_arquivos = la.busca_arquivos(path_principal)    
    lista_dados_processos = {}
    lista_informacoes = []

    for caminho_arquivo in lista_arquivos:

        arquivo_html = open(caminho_arquivo ,'r', encoding='ISO 8859-1')
        html_principal = la.BeautifulSoup(arquivo_html.read(), 'lxml')

        
        lista_informacoes.append(la.busca_capa_processo(html_principal))
        lista_informacoes.append(la.busca_processos_relacionados(html_principal))
        lista_informacoes.append(la.busca_partes_e_representandes(html_principal))
        lista_informacoes.append(la.busca_eventos(html_principal))
        

        lista_dados_processos['Informações do ' + caminho_arquivo[len(path_principal):]] = lista_informacoes
        lista_informacoes = [] 
    
    return render_template('dados.html', lista_dados = lista_dados_processos)

if __name__ == '__main__':
    app.run()                         

