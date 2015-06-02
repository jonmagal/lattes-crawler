# -*- coding: utf8 -*-
__author__ = 'Marcus V.G. Pestana'

from lattes_crawler.crawler.lattes import get_cv_lattes
from xml.dom import minidom

def extract_information(research)
'''
Extracts valuable information from a Researcher CV Lattes
@param research: Research class object

'''
    parsedinfo          = minidom.parseString(research.lattes_information).encode('utf8'))
    curriculo_lattes    = parsedinfo.getElementsByTagName("curriculo_lattes")[0]
    pesquisador         = curriculo_lattes.getElementsByTagName("pesquisador")[0]
    formacao_academica  = pesquisador.getElementsByTagName("formacao_academica")[0]
    formacao            = formacao_academica.getElementsByTagName("formacao")

    #   Doutorado, Mestrado e Graduação
    print"Formação:\n"

    for form in formacao:
        ano_inicio          = form.getElementsByTagName("ano_inicio")
        ano_conclusao       = form.getElementsByTagName("ano_conclusao")
        tipo                = form.getElementsByTagName("tipo")

        #   Check if is None
        if ano_inicio[0].firstChild is None:
            ano_inicio_info = "None"
        else:
            ano_inicio_info     = ano_inicio[0].firstChild.data

        if ano_conclusao[0].firstChild is None:
            ano_conclusao_info = "None"
        else:
            ano_conclusao_info  = ano_conclusao[0].firstChild.data

        if tipo[0].firstChild is None:
            tipo_info = "None"
        else:
            tipo_info           = tipo[0].firstChild.data.split(' ')[0]


        print tipo_info+": "+ano_inicio_info+" - "+ano_conclusao_info

    #   Projetos
    projetos_pesquisa = pesquisador.getElementsByTagName("projetos_pesquisa")[0]
    projetos           = projetos_pesquisa.getElementsByTagName("projeto")

    print "\nProjetos:\n"

    for proj in projetos:
        nome = proj.getElementsByTagName("nome")[0].firstChild.data
        projeto_ano_inicio = proj.getElementsByTagName("ano_inicio")[0].firstChild.data
        projeto_ano_conclusao = proj.getElementsByTagName("ano_conclusao")[0].firstChild.data

        print nome+' '+'('+projeto_ano_inicio+' - '+projeto_ano_conclusao+')'

    #   Livros
    capitulos_livros = pesquisador.getElementsByTagName("capitulos_livros")[0]
    capitulo         = capitulos_livros.getElementsByTagName("capitulo")
    print"\nLivros:\n"

    for cap in capitulo:
        titulo_livro = cap.getElementsByTagName("titulo")[0].firstChild.data

        print titulo_livro+'\n'

    #   Texto em Jornals
    texto_em_jornal = pesquisador.getElementsByTagName("texto_em_jornal")[0]
    texto           = texto_em_jornal.getElementsByTagName("texto")
    print"\nTexto em Jornals:\n"

    for text in texto:
        titulo_text = text.getElementsByTagName("titulo")[0].firstChild.data
        ano    = text.getElementsByTagName("ano")[0].firstChild.data

        print titulo_text+' ('+ano+')\n'

    #   Papers
    trabalho_completo_congresso = pesquisador.getElementsByTagName("trabalho_completo_congresso")[0]
    trabalho_completo           = trabalho_completo_congresso.getElementsByTagName("trabalho_completo")
    print"\nPapers:\n"

    for trabalho in trabalho_completo:
        titulo_trabalho = trabalho.getElementsByTagName("titulo")[0].firstChild.data
        nome_evento     = trabalho.getElementsByTagName("nome_evento")[0].firstChild.data
        ano_trabalho    = trabalho.getElementsByTagName("ano")[0].firstChild.data

        print titulo_trabalho+" ("+ano_trabalho+")"
        print nome_evento+"\n"

     #   Resumo Expandido Congresso
    resumo_expandido_congresso = pesquisador.getElementsByTagName("resumo_expandido_congresso")[0]
    resumo_expandido           = resumo_expandido_congresso.getElementsByTagName("resumo_expandido")
    print"\nResumos expandidos:\n"

    for resumo in resumo_expandido:
        titulo_resumo_expandido          = resumo.getElementsByTagName("titulo")[0].firstChild.data
        nome_evento_resumo_expandido     = resumo.getElementsByTagName("nome_evento")[0].firstChild.data
        ano_resumo_expandido             = resumo.getElementsByTagName("ano")[0].firstChild.data

        print titulo_resumo_expandido+" ("+ano_resumo_expandido+")"
        print nome_evento_resumo_expandido+"\n"

    #   Resumo Congresso
    resumo_congresso = pesquisador.getElementsByTagName("resumo_congresso")[0]
    resum           = resumo_congresso.getElementsByTagName("resumo")
    print"\nResumos:\n"

    for r in resum:
        titulo_resumo          = r.getElementsByTagName("titulo")[0].firstChild.data
        nome_evento_resumo     = r.getElementsByTagName("nome_evento")[0].firstChild.data
        ano_resumo             = r.getElementsByTagName("ano")[0].firstChild.data

        print titulo_resumo+" ("+ano_resumo+")"
        print nome_evento_resumo+"\n"

    #   Apresentação de Trabalhos
    apresentacao_trabalho         = pesquisador.getElementsByTagName("apresentacao_trabalho")[0]
    trabalho_apresentado          = apresentacao_trabalho.getElementsByTagName("trabalho_apresentado")
    print"\nTrabalhos Apresentados:\n"

    for trab in trabalho_apresentado:
        titulo_trabalho_apresentado     = trab.getElementsByTagName("titulo")[0].firstChild.data
        ano_trabalho_apresentado        = trab.getElementsByTagName("ano")[0].firstChild.data

        print titulo_trabalho_apresentado+" ("+ano_trabalho_apresentado+")"
        print "\n"