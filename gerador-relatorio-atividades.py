import git
import os
import datetime
import argparse
from re import search

def validateDate(date_text):
    if (date_text != None):
        try:
            datetime.datetime.strptime(str(date_text), '%Y-%m-%d')
        except Exception as e:
            raise Exception("Formato de data inválido, deve ser YYYY-MM-DD")

def validateChave(chave):
    if (chave != None):
        chave = str(chave)
        if (chave.startswith("C") != True or len(chave) != 8):
            raise Exception("Formato de chave inválido!")

def montarFiltroLog(args):
    filtro = []
    if (args.start_date):
        filtro.append('--after=' + str(args.start_date) + 'T00:00:01')
    if (args.end_date):
        filtro.append('--until=' + args.end_date + 'T23:59:59')
    if (args.key):
        filtro.append('--author=' + args.key)

    if (len(filtro) > 0):
        filtro.append("--pretty=format:%H")

    return filtro

def isArgumentoInformado(args):
    return (args.start_date or args.end_date or args.key or args.hash)



# Definição dos argumentos de filtro
parser = argparse.ArgumentParser()
parser.add_argument("--start-date", "-sd", help="Data inicial do commit padrão (YYYY-mm-dd)")
parser.add_argument("--end-date", "-ed", help="Data final do commit (YYYY-mm-dd)")
parser.add_argument("--key", "-k", help="Chave C do usuário que realizou o commit")
parser.add_argument("--hash", "-ha", help="Hash do commit a ser analisado")

# Leitura dos argumentos
inputArgs = parser.parse_args()

dirpath = os.getcwd()
foldername = os.path.basename(dirpath) + "/"
arquivosNovos = []
arquivosModificados = []

g = git.Git(dirpath.replace("\\","/"))

if (not isArgumentoInformado(inputArgs)):
    print("É necessário informar pelo menos um dos argumentos usados no filtro dos commits. Execute o programa com a opção --help ou -h")
else:

    if (inputArgs.hash):
        print("Coletando dados dos arquivos criados...")

        loginfoAdicionados = g.execute(["git", "show", str(inputArgs.hash), "--name-status", "--pretty=oneline", "--abbrev-commit", "--diff-filter=A"])
        linhasAdicionados = loginfoAdicionados.splitlines()

        if len(linhasAdicionados) > 0:
            arquivosNovos = arquivosNovos + list(
                map(lambda x: foldername + x.replace('A\t', '') + '#' + str(inputArgs.hash)[0:10], linhasAdicionados))

        print("Coletando dados dos arquivos modificados...")

        loginfoModificados = g.execute(["git", "show", str(inputArgs.hash), "--name-status", "--pretty=oneline", "--abbrev-commit", "--diff-filter=M"])
        linhasModificados = loginfoModificados.splitlines()

        if len(linhasModificados) > 0:
            arquivosModificados = arquivosModificados + list(
                map(lambda x: foldername + x.replace('MM\t', '').replace('M\t', '') + '#' + str(inputArgs.hash)[0:10],
                    linhasModificados))

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

    else:
        validateDate(inputArgs.start_date)
        validateDate(inputArgs.end_date)
        validateChave(inputArgs.key)
        filtroLog = montarFiltroLog(inputArgs)

        try:
            logCommits = g.log(tuple(filtroLog))
            commitsList = logCommits.splitlines()
            print("Total de COMMITS encontrados: {}".format(len(commitsList)))

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
          print("Ocorreu uma exceção durante a execução do programa, provavelmente o filtro informado não retornou dados " + e)