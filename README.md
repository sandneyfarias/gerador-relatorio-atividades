# Gerador Relatorio de atividades

Projeto criado a partir do repositório https://github.com/alexandreqo/gerador-relatorio-atividades

Este script auxilia na geração do relatorio de atividades de empresas terceirizadas no Banco do Brasil, retornando um texto com arquivos criados e modificados pelo autor a partir da data informada.
Se o arquivo foi criado e então modificado, o modificado será eliminado da listagem.
Os arquivos são retornados organizados através da sua extensão agrupados por Arquivos Novos e Arquivos Modificados.

O script recebe como parâmetros a data a partir da qual os commits devem ser tratados e a chave C do usuário.

O projeto utiliza biblioteca GitPython, as orientações para instalação estão disponíveis em https://pypi.org/project/GitPython/. Mais informações sobre a biblioteca podem ser encontradas em https://github.com/gitpython-developers/GitPython e https://gitpython.readthedocs.io/en/stable/

Dentro do repositorio:

(LINUX)
```
python3 /home/gerador-relatorio-atividades.py <data-do-commit-inicial> <chavec>
 ```
(WINDOWS)
```
python c:\Projetos\gerador-relatorio-atividades\gerador-relatorio-atividades.py <data-do-commit-inicial> <chavec>
 ```

 Exemplo:

 (LINUX)
```
python3 /home/gerador-relatorio-atividades 2021-06-16 C12345678
```
 (WINDOWS)
```
python c:\Projetos\gerador-relatorio-atividades\gerador-relatorio-atividades.py 2021-06-16 C12345678
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
