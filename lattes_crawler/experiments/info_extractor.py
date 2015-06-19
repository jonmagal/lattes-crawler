# -*- coding: utf8 -*-
'''
@author: Marcus V.G. Pestana
'''

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'lattes_crawler.settings'

import django
django.setup()

from xml.dom import minidom
from lattes_crawler.apps.research.models import Research, ResearchInfo

def save_info(research, data_type, description, year):
    """
    Saves a row of information from a Researcher
    """
    info = ResearchInfo()
    info.research      = research
    info.data_type     = data_type
    info.description   = description
    info.year          = year
    info.save()

def extract_information(research):
    """
    Extracts valuable information from a Researcher CV Lattes
    @param research: Research class object.
    """
    parsedinfo          = minidom.parseString(research.lattes_information.encode('utf8'))
    curriculo_lattes    = parsedinfo.getElementsByTagName("curriculo_lattes")[0]
    pesquisador         = curriculo_lattes.getElementsByTagName("pesquisador")[0]
    formacao_academica  = pesquisador.getElementsByTagName("formacao_academica")[0]
    formacao            = formacao_academica.getElementsByTagName("formacao")

    #   Doutorado, Mestrado e Graduação
    for form in formacao:
        ano_inicio          = form.getElementsByTagName("ano_inicio")
        ano_conclusao       = form.getElementsByTagName("ano_conclusao")
        tipo                = form.getElementsByTagName("tipo")
        
        if tipo[0].firstChild is None:
            pass
        
        else:
            if ano_inicio[0].firstChild is None:
                ano_inicio_info     = None
            else:
                ano_inicio_info     = ano_inicio[0].firstChild.data
        
            if ano_conclusao[0].firstChild is None:
                ano_conclusao_info  = None
            else:
                ano_conclusao_info  = ano_conclusao[0].firstChild.data

            tipo_info            = tipo[0].firstChild.data.split(' ')[0]
            area                 = ''.join(tipo[0].firstChild.data[1:])
        
        save_info(research = research, data_type = tipo_info, description = area, year = ano_conclusao_info)    
            
    #   Projetos
    projetos_pesquisa = pesquisador.getElementsByTagName("projetos_pesquisa")[0]
    projetos           = projetos_pesquisa.getElementsByTagName("projeto")

    print "\nProjetos:\n"

    for proj in projetos:
        nome                      = proj.getElementsByTagName("nome")[0].firstChild.data
        projeto_ano_inicio        = proj.getElementsByTagName("ano_inicio")[0].firstChild.data
        projeto_ano_conclusao     = proj.getElementsByTagName("ano_conclusao")[0].firstChild.data

        save_info(research = research, data_type = 'Projeto', description = nome, year = projeto_ano_conclusao)
        
    #   Livros
    capitulos_livros              = pesquisador.getElementsByTagName("capitulos_livros")[0]
    capitulo                      = capitulos_livros.getElementsByTagName("capitulo")
    print"\nLivros:\n"

    for cap in capitulo:
        titulo_livro              = cap.getElementsByTagName("titulo")[0].firstChild.data
        ano_livro                 = cap.getElementsByTagName("ano")[0].firstChild.data
        
        save_info(research = research, data_type = 'Livro', description = titulo_livro, year = ano_livro)
        
    #   Texto em Jornals
    texto_em_jornal = pesquisador.getElementsByTagName("texto_em_jornal")[0]
    texto           = texto_em_jornal.getElementsByTagName("texto")
    print"\nTexto em Jornals:\n"

    for text in texto:
        titulo_text               = text.getElementsByTagName("titulo")[0].firstChild.data
        ano                       = text.getElementsByTagName("ano")[0].firstChild.data

        save_info(research = research, data_type = 'Texto em Jornal', description = titulo_text, year = ano)

    #   Papers
    trabalho_completo_congresso = pesquisador.getElementsByTagName("trabalho_completo_congresso")[0]
    trabalho_completo           = trabalho_completo_congresso.getElementsByTagName("trabalho_completo")
    print"\nPapers:\n"

    for trabalho in trabalho_completo:
        titulo_trabalho = trabalho.getElementsByTagName("titulo")[0].firstChild.data
        nome_evento     = trabalho.getElementsByTagName("nome_evento")[0].firstChild.data
        ano_trabalho    = trabalho.getElementsByTagName("ano")[0].firstChild.data

        save_info(research = research, data_type = 'Paper', description = titulo_trabalho+' '+'('+nome_evento+')', year = ano_trabalho)

    #   Resumo Expandido Congresso
    resumo_expandido_congresso = pesquisador.getElementsByTagName("resumo_expandido_congresso")[0]
    resumo_expandido           = resumo_expandido_congresso.getElementsByTagName("resumo_expandido")
    print"\nResumos expandidos:\n"

    for resumo in resumo_expandido:
        titulo_resumo_expandido          = resumo.getElementsByTagName("titulo")[0].firstChild.data
        nome_evento_resumo_expandido     = resumo.getElementsByTagName("nome_evento")[0].firstChild.data
        ano_resumo_expandido             = resumo.getElementsByTagName("ano")[0].firstChild.data
        
        save_info(research = research, data_type = 'Resumo Expandido', description = titulo_resumo_expandido+' '+'('+nome_evento_resumo_expandido+')', year = ano_resumo_expandido)
                
    #   Resumo Congresso
    resumo_congresso = pesquisador.getElementsByTagName("resumo_congresso")[0]
    resum            = resumo_congresso.getElementsByTagName("resumo")
    print"\nResumos:\n"

    for r in resum:
        titulo_resumo          = r.getElementsByTagName("titulo")[0].firstChild.data
        nome_evento_resumo     = r.getElementsByTagName("nome_evento")[0].firstChild.data
        ano_resumo             = r.getElementsByTagName("ano")[0].firstChild.data
        
        save_info(research = research, data_type = 'Resumo Congresso', description = titulo_resumo+' '+'('+nome_evento_resumo+')', year = ano_resumo)

    #   Apresentação de Trabalhos
    apresentacao_trabalho         = pesquisador.getElementsByTagName("apresentacao_trabalho")[0]
    trabalho_apresentado          = apresentacao_trabalho.getElementsByTagName("trabalho_apresentado")
    print"\nTrabalhos Apresentados:\n"

    for trab in trabalho_apresentado:
        titulo_trabalho_apresentado     = trab.getElementsByTagName("titulo")[0].firstChild.data
        ano_trabalho_apresentado        = trab.getElementsByTagName("ano")[0].firstChild.data

        save_info(research = research, data_type = 'Trabalho Apresentado', description = titulo_trabalho_apresentado, year = ano_trabalho_apresentado)
    

def main():
    research_list = Research.objects.exclude(lattes_information = None)
    if not research_list:
        return
    for research in research_list:
        extract_information(research)
    
if __name__ == '__main__':
    main()
    
    