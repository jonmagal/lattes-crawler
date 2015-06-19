#!/usr/bin/python
# encoding: utf-8
#
#
#  scriptLattes V8
#  Copyright 2005-2013: Jesús P. Mena-Chalco e Roberto M. Cesar-Jr.
#  http://scriptlattes.sourceforge.net/
#
#
#  Este programa é um software livre; você pode redistribui-lo e/ou 
#  modifica-lo dentro dos termos da Licença Pública Geral GNU como 
#  publicada pela Fundação do Software Livre (FSF); na versão 2 da 
#  Licença, ou (na sua opinião) qualquer versão.
#
#  Este programa é distribuído na esperança que possa ser util, 
#  mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
#  MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#  Licença Pública Geral GNU para maiores detalhes.
#
#  Você deve ter recebido uma cópia da Licença Pública Geral GNU
#  junto com este programa, se não, escreva para a Fundação do Software
#  Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

import os


# ---------------------------------------------------------------------------- #
def criarDiretorio(dir):
	if not os.path.exists(dir):
		try:
			os.makedirs(dir)
		### except OSError as exc:
		except:
			print "\n[ERRO] Não foi possível criar ou atualizar o diretório: "+dir.encode('utf8')
			print "[ERRO] Você conta com as permissões de escrita? \n"
			return 0
	return 1

def get_cv_lattes(lattes_id):
	from scriptLattes.grupo import Grupo

	novoGrupo = Grupo(lattes_id, './', True)

	if criarDiretorio(novoGrupo.obterParametro('global-diretorio_de_saida')):
		novoGrupo.carregarDadosCVLattes() #obrigatorio
		return novoGrupo.gerarXMLdeGrupo(save = False)

def get_member(lattes_id):
	from scriptLattes.grupo import Grupo
	
	grupo = Grupo(lattes_id, './', True)

	if criarDiretorio(grupo.obterParametro('global-diretorio_de_saida')):
		grupo.carregarDadosCVLattes() #obrigatorio
		return grupo.listaDeMembros[0]