import git
import sys
import os
import datetime
from re import search

def validateDate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except Exception as e:
        raise Exception("Formato de data inválido, deve ser YYYY-MM-DD")

def validateChave(chave):
    if (chave.startswith("C") != True or len(chave) != 8):
        raise Exception("Formato de chave inválido!")


inputArgs = sys.argv

dirpath = os.getcwd()
foldername = os.path.basename(dirpath) + "/"
arquivosNovos = []
arquivosModificados = []

g = git.Git(dirpath.replace("\\","/"))

if (len(inputArgs) < 3):
    print("É necessário informar da data inicial e chave C do usuário para filtrar os commits")
else:
    validateDate(inputArgs[1])
    validateDate(inputArgs[2])
    validateChave(inputArgs[3].upper())

    try:
        logCommits = g.log('--after=' + inputArgs[1] + 'T00:00:01','--until=' + inputArgs[2] + 'T23:59:59', '--pretty=format:%H', '--author=' + inputArgs[3])
        commitsList = logCommits.split('\n')

        print("Coletando dados dos arquivos criados...")
        for commit in commitsList:
            loginfoAdicionados = g.execute(["git", "show", commit,"--name-status","--pretty=oneline","--abbrev-commit","--diff-filter=A"])
            linhasAdicionados = loginfoAdicionados.split('\n')

            if len(linhasAdicionados) > 0:
                arquivosNovos = arquivosNovos + list(map(lambda x: foldername + x.replace('A\t','') + '#' + commit[0:10], linhasAdicionados))

        print("Coletando dados dos arquivos modificados...")
        for commit in commitsList:
            loginfoModificados = g.execute(["git", "show", commit,"--name-status","--pretty=oneline","--abbrev-commit","--diff-filter=M"])
            linhasModificados = loginfoModificados.split('\n')

            if len(linhasModificados) > 0:
                arquivosModificados = arquivosModificados + list(map(lambda x: foldername + x.replace('MM\t','').replace('M\t','') + '#' + commit[0:10], linhasModificados))

        arquivosNovosSet = set(arquivosNovos)
        arquivosModificadosSet = set(arquivosModificados)

        for novo in arquivosNovos:
            arquivo = novo[:novo.index("#")]

            if (arquivo != foldername and arquivo.find(".")):
                iguais = set(filter(lambda nome: search(arquivo, nome), arquivosModificados))
                try:
                    arquivosModificadosSet = arquivosModificadosSet.difference(iguais)
                except ValueError:
                    pass

        arquivosNovos = list(arquivosNovosSet)
        arquivosModificados = list(arquivosModificadosSet)

        arquivosNovos.sort(key=lambda f: os.path.splitext(f)[1])
        arquivosModificados.sort(key=lambda f: os.path.splitext(f)[1])

        print('_______________Arquivos Novos_______________')
        extensaoAnterior = ''
        for x in arquivosNovos:
            extensao = os.path.splitext(x)[1].split('#')[0]
            if extensao != extensaoAnterior:
                extensaoAnterior = extensao;
                print('##Arquivos com extensão ' + extensaoAnterior)
            if (extensao != ""):
                print(x.strip(" "))

        print('_______________Arquivos Modificados_______________')
        extensaoAnterior = ''
        for x in arquivosModificados:
            extensao = os.path.splitext(x)[1].split('#')[0]
            if extensao != extensaoAnterior:
                extensaoAnterior = extensao;
                print('##Arquivos com extensão ' + extensaoAnterior)
            if (extensao != ""):
                print(x)

    except Exception as e:
      print("Ocorreu uma exceção durante a execução do programa, provavelmente o filtro informado não retornou dados")