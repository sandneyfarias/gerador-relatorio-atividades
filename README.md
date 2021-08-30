# Gerador Relatorio de atividades

Projeto criado a partir do repositório https://github.com/alexandreqo/gerador-relatorio-atividades

Este script auxilia na geração do relatorio de atividades de empresas terceirizadas no Banco do Brasil, retornando um texto com arquivos criados e modificados pelo autor a partir da data informada.
Se o arquivo foi criado e então modificado, o modificado será eliminado da listagem.
Os arquivos são retornados organizados através da sua extensão agrupados por Arquivos Novos e Arquivos Modificados.

O script recebe recebe os parâmetros:

--start-date: Considera os commits a partir da data indicada. Formato yyyy-mm-dd;

--end-data: Considera os commits até a data indicada. Formato yyyy-mm-dd;

--key: Chave C do autor do commit;

--hash: Considera apenas os commits feitos com o hash específicado. Este filtro é exclusivo, quando informado os demais parâmetros 
são desconsiderados.

O projeto utiliza biblioteca GitPython, as orientações para instalação estão disponíveis em https://pypi.org/project/GitPython/. Mais informações sobre a biblioteca podem ser encontradas em https://github.com/gitpython-developers/GitPython e https://gitpython.readthedocs.io/en/stable/

Dentro do repositorio (pasta do projeto clonado):

(LINUX)
```
python3 /home/gerador-relatorio-atividades.py [<--start-date DATA INICIAL> <--end-date DATA FINAL> <--key CHAVE>] [<--hash HASH>]
 ```

(WINDOWS)
```
python c:\Projetos\gerador-relatorio-atividades\gerador-relatorio-atividades.py [<--start-date DATA INICIAL> <--end-date DATA FINAL> <--key CHAVE>] [<--hash HASH>]
 ```

 Exemplo:

 (LINUX)
```
python3 /home/gerador-relatorio-atividades --start-date 2021-06-01 --end-date 2021-06-17 --key C12345678
```
 (WINDOWS)
```
python c:\Projetos\gerador-relatorio-atividades\gerador-relatorio-atividades.py --start-date 2021-06-01 --end-date 2021-06-17 --key C12345678
```
Retorno: 
```
_______________Arquivos Novos_______________
##Arquivos com extensão .html
diretorio/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/modais/modal-detalhamento-validacao.html#bc895ad6
##Arquivos com extencao .js
diretorio/spec/src/app/services/validacao-service-spec.js#bc895ad6
diretorio/src/app/services/validacao-service.js#bc895ad6
_______________Arquivos Modificados_______________
##Arquivos com extensão .html
diretorio/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/modais/modal-erros-validacao.html#0983ca28
diretorio/src/app/spas/fluxo-deploy/fluxo-deploy-app.html#0983ca28
diretorio/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/modais/modal-erros-validacao.html#bc895ad6
diretorio/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/solicitacao/solicitacao-deploy.html#bc895ad6
##Arquivos com extencao .js
diretorio/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/solicitacao/solicitacao-deploy-controller.js#bc895ad6
diretorio/spec/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/solicitacao/solicitacao-deploy-controller-spec.js#bc895ad6
diretorio/src/app/spas/fluxo-deploy/fluxo-deploy-app.js#bc895ad6
diretorio/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/solicitacao/solicitacao-deploy-controller.js#bc895ad6
```
