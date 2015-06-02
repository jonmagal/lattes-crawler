# -*- coding: utf8 -*-
'''
Created on 21/05/2014

@author: Jonathas Magalhães
'''

from lattes_crawler.crawler.lattes       import get_cv_lattes, get_member
from recsys.util.util   import year_now

class LattesCrawler(object):
    
    def __get_production(self, element, content_type = 'bibliography'):
        information = []
        if element:
            for elem in element:
                content     = {}
                try:
                    content['description']  = elem.titulo
                    content['year']         = self.__fix_year(elem.ano)
                    content['type']         = content_type
                    information.append(content)
                except:
                    pass
        return information
    
    def __fix_year(self, year):
        if year < 1950:
            year = year_now()
        return year
        
    def __get_member(self, lattes_id):
        return get_member(lattes_id) 
    
    def get_lattes(self, lattes_id):
        return get_cv_lattes(lattes_id)
    
    def lattes_parser(self, lattes_xml):
        pass
            
    def get_user_information(self, lattes_id):
        lattes_id   = lattes_id.split('/')[-1]
        member      = self.__get_member(lattes_id)
        information = []
        y_now       = year_now()
        #Setting the resumé
        try:
            content     = {}
            content['description']  = member.textoResumo.replace("Texto informado pelo autor", "")
            content['year']         = y_now
            content['type']         = 'cv'
            information.append(content)
        except:
            pass
        
        #Formation
        if member.listaFormacaoAcademica:
            for formation in member.listaFormacaoAcademica:
                content     = {}
                try:
                    description = formation.descricao
                    description = description.split("Bolsista do(a):")[0]
                    description = description.split("Orientador:")[0]
                    description = description.split("Título:")[1]
                    content['description']  = description.split("Ano de Obtenção:")[0]
                    content['year']         = self.__fix_year(int(formation.anoConclusao))
                    content['type']         = 'formation'
                    information.append(content)
                except:
                    pass   
        
        #Projects            
        if member.listaProjetoDePesquisa:
            for pesquisa in member.listaProjetoDePesquisa:
                content     = {}
                try:                    
                    description = pesquisa.descricao[0]
                    if "Situação: Concluído" in description:
                        content['year'] = self.__fix_year(int(pesquisa.anoConclusao))
                    else:
                        content['year'] = y_now
                    description = description.split("Alunos envolvidos:")[0]
                    description = description.split("Situação:")[0]
                    description = description.split("Descrição:")[1]
                    content['description']  = pesquisa.nome + description
                    content['type']         = 'project'
                    information.append(content)
                except :
                    pass 
        
        #Bibliography
        information += self.__get_production(member.listaArtigoEmPeriodico)
        information += self.__get_production(member.listaLivroPublicado)
        information += self.__get_production(member.listaCapituloDeLivroPublicado)
        information += self.__get_production(member.listaTextoEmJornalDeNoticia)
        information += self.__get_production(member.listaTrabalhoCompletoEmCongresso)
        information += self.__get_production(member.listaResumoExpandidoEmCongresso)
        information += self.__get_production(member.listaResumoEmCongresso)
        information += self.__get_production(member.listaArtigoAceito)
        information += self.__get_production(member.listaApresentacaoDeTrabalho)
        information += self.__get_production(member.listaOutroTipoDeProducaoBibliografica)
        
        #Technical
        content_type = 'technical'
        information += self.__get_production(member.listaSoftwareComPatente, content_type)
        information += self.__get_production(member.listaSoftwareSemPatente, content_type)
        information += self.__get_production(member.listaProdutoTecnologico, content_type)
        information += self.__get_production(member.listaProcessoOuTecnica, content_type)
        information += self.__get_production(member.listaTrabalhoTecnico, content_type)
        information += self.__get_production(member.listaOutroTipoDeProducaoTecnica, content_type)        
        
        return information

if __name__ == '__main__':
    x = LattesCrawler()
    x.lattes_id = "7151033935149782"
    get_user_information(x.lattes_id)    
