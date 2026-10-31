# Aula 07.1 — Roteiro Prático

## Primeiro Versionamento e Publicação do EngConvert no GitHub

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Correspondência:** roteiro prático da **Aula 07.0 — Git, GitHub e Controle de Versão**.  
> **Etapa do Roadmap:** Etapa 7 — Git e GitHub.  
> **Sprint:** Sprint 06 — Primeiro Versionamento e Publicação.

---

# 🎯 Objetivo

Nesta aula transformaremos o projeto EngConvert em um repositório Git e publicaremos sua primeira versão no GitHub.

O fluxo será:

```text
ENGCONVERT LOCAL
      ↓
verificar Git
      ↓
configurar identidade
      ↓
criar .gitignore
      ↓
git init
      ↓
git status
      ↓
git add
      ↓
git commit
      ↓
criar repositório no GitHub
      ↓
conectar origin
      ↓
git push
      ↓
ENGCONVERT NO GITHUB
```

Ao final, o aluno terá:

```text
repositório Git local
        +
histórico de commits
        +
repositório remoto no GitHub
        +
primeiro push realizado
```

---

# 1. Antes de começar

Confirme que você possui:

```text
[ ] Windows funcionando
[ ] VSCode instalado
[ ] projeto EngConvert funcionando
[ ] pasta C:\Projetos\engconvert
[ ] acesso à internet
[ ] navegador
[ ] Git instalado ou permissão para instalá-lo
[ ] conta no GitHub ou possibilidade de criá-la
```

> ⚠️ Não apague nem recrie o EngConvert. Utilizaremos o projeto desenvolvido nas aulas anteriores.

---

# 2. Abrir o projeto

Abra o PowerShell e navegue até:

```powershell
cd C:\Projetos\engconvert
```

Confira:

```powershell
pwd
```

Depois:

```powershell
dir
```

Abra a pasta no VSCode:

```powershell
code .
```

A ideia é trabalhar sempre com:

```text
C:\Projetos\engconvert
```

e não com uma pasta diferente criada apenas para o GitHub.

---

# 3. Conferir se o EngConvert funciona

Antes de iniciar o controle de versão, execute o programa.

Ative o ambiente virtual, se necessário:

```powershell
.\.venv\Scripts\Activate.ps1
```

Depois:

```powershell
python main.py
```

Faça pelo menos alguns testes:

```text
1 bar → 100 kPa
1 m → 1000 mm
1 L → 1000 mL
0 °C → 32 °F
```

Feche a aplicação após confirmar o funcionamento.

> 📌 Estamos prestes a registrar uma versão importante. Primeiro confirmamos que ela funciona.

---

# 4. Criar a Sprint 06

Na pasta:

```text
docs/sprints/
```

crie:

```text
sprint-06-git-github.md
```

Utilize:

```markdown
# Sprint 06 — Primeiro Versionamento e Publicação

## Objetivo

Colocar o EngConvert sob controle de versão com Git e publicar o repositório no GitHub.

## Tarefas

- [ ] verificar a instalação do Git;
- [ ] configurar nome e e-mail;
- [ ] criar/verificar a conta no GitHub;
- [ ] criar o `.gitignore`;
- [ ] verificar os arquivos que serão versionados;
- [ ] inicializar o repositório Git;
- [ ] definir a branch principal como `main`;
- [ ] preparar os arquivos;
- [ ] criar o primeiro commit;
- [ ] criar o repositório remoto no GitHub;
- [ ] conectar o remoto `origin`;
- [ ] realizar a autenticação;
- [ ] executar o primeiro `push`;
- [ ] conferir o projeto no GitHub;
- [ ] realizar um segundo ciclo de alteração, commit e push.

## Status

**PLANEJADA**
```

---

# 5. Verificar a instalação do Git

No terminal do VSCode:

```bash
git --version
```

Se o Git estiver instalado, será exibido algo semelhante a:

```text
git version 2.x.x.windows.x
```

O número exato pode ser diferente.

Se aparecer uma mensagem informando que:

```text
git
```

não foi reconhecido, o Git ainda não está disponível naquele terminal.

---

# 6. Se o Git ainda não estiver instalado

Abra o navegador e acesse o site oficial:

```text
https://git-scm.com/download/win
```

Baixe o **Git for Windows**.

Durante a instalação, para esta primeira experiência, mantenha as opções recomendadas, incluindo o **Git Credential Manager**.

Depois de concluir:

```text
feche o terminal
      ↓
abra um novo terminal
      ↓
execute:
git --version
```

Isso é importante porque um terminal que já estava aberto pode não reconhecer imediatamente uma instalação recém-concluída.

---

# 7. Conhecer o Git Bash

Pesquise no Windows:

```text
Git Bash
```

Abra-o.

Você deverá encontrar algo semelhante a:

```text
aluno@COMPUTADOR MINGW64 ~
$
```

Não precisamos executar toda a aula no Git Bash.

Nosso trabalho continuará principalmente no terminal do VSCode, mas é importante reconhecer essa ferramenta instalada junto com o Git.

---

# 8. Configurar o nome do autor

No terminal:

```bash
git config --global user.name "Seu Nome"
```

Exemplo:

```bash
git config --global user.name "Maria Silva"
```

Use seu nome real ou a forma profissional que deseja associar aos commits.

---

# 9. Configurar o e-mail

Digite:

```bash
git config --global user.email "seu@email.com"
```

Exemplo:

```bash
git config --global user.email "maria@email.com"
```

Esse endereço fica associado à autoria dos commits.

> 📌 Para associação adequada no GitHub, utilize um endereço apropriado associado à conta ou a opção de privacidade/noreply disponibilizada pela plataforma.

---

# 10. Conferir a identidade

Execute:

```bash
git config --global user.name
```

Depois:

```bash
git config --global user.email
```

Você também pode usar:

```bash
git config --list
```

Confirme cuidadosamente os dados antes do primeiro commit.

---

# 11. Configurar o VSCode como editor do Git

Execute:

```bash
git config --global core.editor "code --wait"
```

Isso informa ao Git:

```text
quando precisar abrir um editor
        ↓
utilize o VSCode
```

O parâmetro:

```text
--wait
```

faz o Git aguardar o fechamento do arquivo utilizado na edição.

---

# 12. Criar ou conferir a conta no GitHub

Abra:

```text
https://github.com
```

Se ainda não possui conta:

```text
criar conta
    ↓
escolher username
    ↓
informar e-mail
    ↓
concluir cadastro
    ↓
verificar e-mail
```

Se já possui conta, faça login.

> 📌 O `username` do GitHub não precisa ser igual ao `user.name` configurado no Git.

---

# 13. Escolher um username adequado

O username poderá aparecer publicamente em:

```text
perfil
repositórios
URLs
atividades
```

Por isso, para uma conta acadêmica/profissional, prefira um nome que possa continuar utilizando posteriormente.

Evite, se possível, nomes excessivamente informais ou difíceis de identificar.

---

# 14. Verificar o e-mail da conta

Se o GitHub solicitar confirmação:

```text
caixa de e-mail
      ↓
mensagem do GitHub
      ↓
verificar endereço
```

Conclua essa etapa antes de prosseguir.

---

# 15. Segurança da conta

Se disponível durante o processo, configure a autenticação de dois fatores:

```text
2FA
```

Fluxo conceitual:

```text
senha
  +
segundo fator
```

> ⚠️ Guarde os métodos/códigos de recuperação em local seguro. Não coloque códigos de recuperação dentro do projeto EngConvert.

---

# 16. Voltar ao projeto

No terminal integrado do VSCode, confirme:

```powershell
pwd
```

O diretório deve corresponder a:

```text
C:\Projetos\engconvert
```

Antes de executar comandos Git, tenha certeza de que está na pasta correta.

---

# 17. Verificar se já existe um repositório Git

Execute:

```bash
git status
```

Se a pasta ainda não for um repositório, o Git apresentará uma mensagem informando que não encontrou um repositório Git.

Isso é esperado nesta primeira configuração.

> ⚠️ Se `git status` já mostrar uma branch e o estado dos arquivos, **não execute `git init` novamente por rotina**. O projeto já está sob controle do Git.

---

# 18. Criar o `.gitignore` antes de `git add .`

Na raiz do projeto, crie:

```text
.gitignore
```

Conteúdo:

```gitignore
# Ambiente virtual
.venv/
venv/

# Cache do Python
__pycache__/
*.pyc

# Variáveis de ambiente e segredos
.env

# Logs
*.log
```

Salve o arquivo.

---

# 19. Por que criar o `.gitignore` agora?

Porque queremos impedir que arquivos desnecessários sejam preparados quando utilizarmos:

```bash
git add .
```

Especialmente:

```text
.venv/
```

O fluxo correto é:

```text
criar .gitignore
       ↓
conferir
       ↓
git add .
```

e não:

```text
git add .
       ↓
perceber que enviou .venv
```

---

# 20. Nunca colocar segredos no repositório

Antes de continuar, procure no projeto por informações como:

```text
senha
token
chave de API
credencial
```

Esses dados não devem ser versionados.

Nosso `.gitignore` já contém:

```gitignore
.env
```

Mas o `.gitignore` não substitui a responsabilidade de verificar o que está sendo publicado.

---

# 21. Inicializar o repositório

Somente se o projeto ainda não estiver sob controle do Git, execute:

```bash
git init
```

O terminal deverá indicar que um repositório foi inicializado.

Agora existe uma pasta oculta:

```text
.git/
```

O EngConvert deixou de ser apenas uma pasta comum.

---

# 22. Definir `main` como branch principal

Execute:

```bash
git branch -M main
```

Esse comando define/renomeia a branch atual para:

```text
main
```

Agora teremos:

```text
EngConvert
   ↓
repositório Git
   ↓
branch principal:
main
```

---

# 23. Primeiro `git status`

Execute:

```bash
git status
```

Leia a saída.

Neste momento, vários arquivos poderão aparecer como:

```text
Untracked files
```

ou seja:

```text
arquivos que existem
mas ainda não são acompanhados pelo Git
```

---

# 24. Observe o `.venv`

Verifique a saída de:

```bash
git status
```

A pasta:

```text
.venv/
```

**não deve aparecer entre os arquivos que serão versionados**, pois foi incluída no `.gitignore`.

Se aparecer, não prossiga mecanicamente.

Revise:

```text
nome do arquivo .gitignore
localização do .gitignore
conteúdo do .gitignore
```

---

# 25. Verificar arquivos ignorados

Se quiser confirmar regras de ignore, uma opção útil é:

```bash
git status --ignored
```

Os arquivos ignorados podem aparecer em uma seção específica.

Não precisamos versioná-los.

---

# 26. Preparar os arquivos

Depois de conferir o projeto:

```bash
git add .
```

Agora execute novamente:

```bash
git status
```

Observe a diferença.

Antes:

```text
Untracked files
```

Depois:

```text
Changes to be committed
```

---

# 27. O que acabou de acontecer?

```text
Working Directory
        ↓
    git add .
        ↓
Staging Area
```

Ainda **não criamos um commit**.

Apenas selecionamos as alterações que farão parte dele.

---

# 28. Conferir antes do commit

Leia a lista apresentada por:

```bash
git status
```

Procure especialmente por:

```text
main.py
README.md
requirements.txt
docs/
aulas/
.gitignore
```

e confirme que não existem arquivos privados ou desnecessários.

> 🎯 O hábito profissional é conferir antes de registrar.

---

# 29. Primeiro commit

Execute:

```bash
git commit -m "feat: registra versão multicategorias do EngConvert"
```

Esse será o primeiro ponto formal do histórico Git do projeto.

---

# 30. Conferir o histórico

Execute:

```bash
git log --oneline
```

Você deverá visualizar algo semelhante a:

```text
a1b2c3d feat: registra versão multicategorias do EngConvert
```

O código inicial será diferente em cada repositório.

---

# 31. Conferir novamente o estado

Execute:

```bash
git status
```

Se tudo estiver correto, a saída deverá indicar que não há alterações pendentes.

Conceitualmente:

```text
Working Directory
      ↓
sem mudanças pendentes
      ↓
versão registrada
```

---

# 32. Agora criar o repositório remoto

Abra o GitHub no navegador.

Na interface da conta, escolha a opção para criar um novo repositório.

O nome será:

```text
engconvert
```

---

# 33. Nome do repositório

Utilize:

```text
engconvert
```

Por que?

```text
curto
+
descritivo
+
minúsculo
+
sem espaços
```

Esse padrão é adequado para o projeto.

---

# 34. Descrição

Uma descrição possível:

```text
Conversor de unidades de engenharia desenvolvido em Python e CustomTkinter.
```

A descrição pode ser refinada posteriormente.

---

# 35. Público ou privado?

Escolha a visibilidade de acordo com a orientação definida para a disciplina.

Conceitualmente:

```text
Public
  ↓
qualquer pessoa pode visualizar
```

```text
Private
  ↓
somente pessoas autorizadas
```

A visibilidade não muda o funcionamento básico do Git.

---

# 36. Atenção: não inicializar o remoto com arquivos extras

Como o EngConvert **já possui um repositório local e um primeiro commit**, nesta atividade deixe desmarcadas as opções de criação automática de arquivos como:

```text
README
.gitignore
License
```

Por quê?

Porque já temos um histórico local.

Queremos criar inicialmente:

```text
REPOSITÓRIO REMOTO VAZIO
```

e então enviar nosso histórico local.

Isso reduz a possibilidade de criar dois históricos iniciais diferentes.

---

# 37. Criar o repositório

Confirme:

```text
Create repository
```

O GitHub exibirá instruções para conectar um repositório existente.

Não feche essa página.

---

# 38. Copiar a URL HTTPS

Na página do repositório, utilize a URL HTTPS.

Ela terá formato semelhante a:

```text
https://github.com/SEU-USUARIO/engconvert.git
```

Não copie literalmente o exemplo.

Utilize a URL fornecida pelo seu próprio repositório.

---

# 39. Conectar o `origin`

Volte ao terminal.

Execute:

```bash
git remote add origin URL_DO_SEU_REPOSITORIO
```

Exemplo apenas de formato:

```bash
git remote add origin https://github.com/SEU-USUARIO/engconvert.git
```

Substitua:

```text
SEU-USUARIO
```

pelo username correto.

---

# 40. Conferir o remoto

Execute:

```bash
git remote -v
```

Você deverá encontrar referências para:

```text
origin
```

em operações de:

```text
fetch
push
```

Agora:

```text
repositório local
       ↓
conhece o endereço
       ↓
repositório remoto
```

---

# 41. O que significa `origin`?

Lembre:

```text
origin
```

é o nome convencional que atribuímos ao remoto principal.

Ele não é sinônimo de GitHub.

Poderíamos tecnicamente utilizar outro nome, mas:

```text
origin
```

é a convenção mais comum.

---

# 42. Primeiro `push`

Execute:

```bash
git push -u origin main
```

Interpretação:

```text
git push
   ↓
enviar commits

-u
   ↓
registrar a relação de acompanhamento

origin
   ↓
repositório remoto

main
   ↓
branch enviada
```

---

# 43. Primeira autenticação

Na primeira comunicação com o GitHub, o Git Credential Manager poderá solicitar autenticação.

Dependendo da versão instalada, poderá:

```text
abrir uma janela
       ou
abrir o navegador
```

Siga o fluxo apresentado para autenticar sua própria conta.

> ⚠️ Não forneça sua senha, token ou códigos de recuperação a colegas, professor ou arquivos do projeto.

---

# 44. Se o navegador abrir

O fluxo poderá ser semelhante a:

```text
Git
 ↓
Git Credential Manager
 ↓
navegador
 ↓
GitHub
 ↓
autorizar
 ↓
voltar ao terminal
```

As telas podem mudar ao longo do tempo.

O importante é compreender o processo, não decorar a aparência de cada botão.

---

# 45. Conferir o resultado do `push`

Se tudo funcionar, o terminal mostrará informações sobre o envio.

Agora volte ao navegador e atualize a página do repositório.

Você deverá visualizar os arquivos do EngConvert.

---

# 46. Conferir o que foi publicado

Procure:

```text
main.py
docs/
aulas/
README.md
requirements.txt
.gitignore
```

conforme a estrutura existente no seu projeto.

E confirme principalmente que:

```text
.venv/
```

não foi publicado.

---

# 47. Conferir o commit no GitHub

Na interface do repositório, abra o histórico de commits.

Localize:

```text
feat: registra versão multicategorias do EngConvert
```

Agora o mesmo commit existe:

```text
LOCALMENTE
     +
REMOTAMENTE
```

---

# 48. O que acabamos de construir?

```text
COMPUTADOR
C:\Projetos\engconvert
       │
       │ Git
       │
       ├── .git
       ├── commit
       └── main
       │
       │ git push
       ▼
GITHUB
engconvert
       │
       ├── arquivos
       ├── commit
       └── main
```

---

# 49. Primeiro ciclo completo

Já realizamos:

```text
git init
   ↓
git add
   ↓
git commit
   ↓
git remote
   ↓
git push
```

Agora faremos um **segundo ciclo**, porque o aluno precisa perceber que Git não é algo utilizado apenas uma vez.

---

# 50. Fazer uma pequena alteração

Abra:

```text
README.md
```

Se ele já possui conteúdo, acrescente uma seção simples, adequada ao estado atual do projeto:

```markdown
## Controle de versão

Este projeto utiliza Git para controle de versão e GitHub como repositório remoto.
```

Salve:

```text
Ctrl + S
```

---

# 51. Observar a alteração

Execute:

```bash
git status
```

Agora o Git deverá identificar:

```text
README.md
```

como modificado.

Temos:

```text
arquivo salvo no disco
       ≠
novo commit
```

---

# 52. Ver a diferença

Antes de preparar o arquivo, execute:

```bash
git diff
```

O Git mostrará as diferenças ainda não preparadas.

Isso permite responder:

```text
o que exatamente eu alterei?
```

---

# 53. Preparar apenas o README

Desta vez, em vez de:

```bash
git add .
```

utilize:

```bash
git add README.md
```

Isso mostra que podemos selecionar arquivos individualmente.

---

# 54. Conferir a Staging Area

Execute:

```bash
git status
```

Agora `README.md` deverá aparecer entre as alterações preparadas para commit.

Temos:

```text
Working Directory
       ↓
git add README.md
       ↓
Staging Area
```

---

# 55. Ver o que está preparado

Podemos utilizar:

```bash
git diff --staged
```

Assim visualizamos as alterações que farão parte do próximo commit.

Compare:

```text
git diff
```

com:

```text
git diff --staged
```

O primeiro mostra, em geral, alterações ainda não preparadas.

O segundo mostra alterações já colocadas na Staging Area.

---

# 56. Segundo commit

Execute:

```bash
git commit -m "docs: adiciona informação sobre controle de versão"
```

Agora:

```bash
git log --oneline
```

deverá mostrar dois commits.

---

# 57. O GitHub já recebeu o segundo commit?

Ainda não.

Temos:

```text
LOCAL
  ↓
2 commits
```

enquanto o remoto ainda pode estar com:

```text
GITHUB
  ↓
1 commit
```

Isso demonstra que:

```text
commit ≠ push
```

---

# 58. Segundo `push`

Execute:

```bash
git push
```

Como utilizamos anteriormente:

```bash
git push -u origin main
```

a relação entre a branch local e a remota já foi configurada.

Por isso, agora:

```bash
git push
```

é suficiente.

---

# 59. Conferir no GitHub

Atualize a página do repositório.

Confirme:

```text
README atualizado
        +
segundo commit
```

Agora o aluno executou o ciclo completo duas vezes.

---

# 60. O fluxo que deverá virar hábito

```text
EDITAR
  ↓
SALVAR
  ↓
git status
  ↓
git diff
  ↓
git add
  ↓
git status
  ↓
git commit
  ↓
git push
```

Não é necessário executar `git diff` em absolutamente toda alteração, mas ele é muito útil para revisar o que mudou.

---

# 61. `git status` como ponto de retorno

Se você se perder durante a atividade:

```bash
git status
```

Leia a mensagem.

Ela normalmente informa:

```text
branch atual
arquivos modificados
arquivos preparados
arquivos não rastreados
situação em relação ao remoto
```

> 🎯 Antes de tentar "consertar o Git", descubra primeiro o estado do repositório.

---

# 62. Visualizar o histórico

Execute:

```bash
git log --oneline
```

Resultado conceitual:

```text
bbbbbbb docs: adiciona informação sobre controle de versão
aaaaaaa feat: registra versão multicategorias do EngConvert
```

Os hashes reais serão diferentes.

---

# 63. Abrir um commit no GitHub

No navegador, acesse o histórico de commits.

Clique em um dos commits.

Observe que o GitHub permite visualizar:

```text
arquivos alterados
linhas adicionadas
linhas removidas
autor
data
hash
```

O histórico não é apenas uma lista de cópias completas dos arquivos.

Ele permite compreender a evolução do projeto.

---

# 64. Conhecer a branch `main`

No terminal:

```bash
git branch
```

Você deverá encontrar:

```text
* main
```

O asterisco indica a branch atual.

---

# 65. Conhecer a branch remota

Execute:

```bash
git branch -a
```

Dependendo do estado do repositório, poderá aparecer algo como:

```text
* main
  remotes/origin/main
```

Isso ajuda a visualizar:

```text
main
        ↓
branch local

origin/main
        ↓
referência da branch remota
```

---

# 66. Primeiro contato com `pull`

Como nesta atividade estamos trabalhando em um único computador e acabamos de fazer o `push`, provavelmente não existem alterações novas no remoto.

Mesmo assim, podemos compreender:

```bash
git pull
```

Fluxo:

```text
GitHub
   ↓
buscar alterações
   ↓
integrar
   ↓
branch local
```

Não precisamos criar artificialmente uma alteração no navegador apenas para forçar esse cenário.

---

# 67. Primeiro contato com `clone`

Não execute `git clone` dentro de:

```text
C:\Projetos\engconvert
```

O projeto já existe ali.

O `clone` será utilizado quando quisermos obter um repositório existente em outro local ou computador.

Exemplo conceitual:

```text
GITHUB
   ↓
git clone
   ↓
NOVO COMPUTADOR
```

---

# 68. Como obter o EngConvert em outro computador

Em outro computador, depois de instalar Git e Python, poderíamos utilizar:

```bash
git clone URL_DO_REPOSITORIO
```

Depois:

```bash
cd engconvert
```

Criar o ambiente virtual:

```bash
python -m venv .venv
```

Ativar:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar dependências:

```bash
python -m pip install -r requirements.txt
```

Isso explica por que não precisamos enviar:

```text
.venv/
```

para o GitHub.

---

# 69. O papel do `requirements.txt`

O GitHub recebe:

```text
requirements.txt
```

e não precisa receber todo o ambiente virtual.

Assim:

```text
requirements.txt
       ↓
descreve dependências
       ↓
novo computador
       ↓
pip install -r requirements.txt
       ↓
recria dependências
```

---

# 70. Verificar o `requirements.txt`

Com o ambiente virtual ativo, podemos conferir:

```bash
python -m pip freeze
```

Se for necessário atualizar o arquivo:

```bash
python -m pip freeze > requirements.txt
```

> 📌 Só atualize o arquivo se isso fizer sentido para o estado real do projeto. Não execute comandos apenas para alterar arquivos sem necessidade.

---

# 71. Se `origin` já existir

Se ao executar:

```bash
git remote add origin ...
```

aparecer uma mensagem semelhante a:

```text
remote origin already exists
```

não tente repetir o comando várias vezes.

Primeiro execute:

```bash
git remote -v
```

Confira o endereço existente.

Se ele estiver correto, não há nada a adicionar.

---

# 72. Se a URL do `origin` estiver errada

Depois de confirmar o problema, podemos alterar a URL:

```bash
git remote set-url origin URL_CORRETA
```

Depois:

```bash
git remote -v
```

Confirme novamente.

---

# 73. Se o `push` for rejeitado

Não utilize comandos destrutivos por tentativa e erro.

Primeiro leia a mensagem apresentada pelo Git.

Possíveis causas incluem:

```text
autenticação
URL incorreta
branch diferente
repositório remoto com histórico próprio
falta de permissão
alterações remotas ainda não integradas
```

Use:

```bash
git status
git remote -v
git branch
```

para diagnosticar.

---

# 74. Evitar `--force` nesta etapa

O aluno poderá encontrar na internet:

```bash
git push --force
```

Não utilize esse comando como solução genérica.

Ele pode reescrever referências no repositório remoto.

Nesta etapa:

```text
ERRO
 ↓
LER
 ↓
DIAGNOSTICAR
 ↓
CORRIGIR A CAUSA
```

e não:

```text
ERRO
 ↓
--force
```

---

# 75. Se um arquivo foi adicionado por engano antes do commit

Suponha que um arquivo tenha ido para a Staging Area, mas ainda não desejamos incluí-lo.

Podemos retirá-lo da Staging Area com:

```bash
git restore --staged nome_do_arquivo
```

Depois:

```bash
git status
```

Isso não significa necessariamente apagar o arquivo do computador.

---

# 76. Se alteramos um arquivo e queremos descartar a alteração

Antes de qualquer comando, execute:

```bash
git status
```

Se a alteração ainda não foi commitada e realmente queremos descartá-la:

```bash
git restore nome_do_arquivo
```

> ⚠️ Isso pode apagar alterações locais não registradas. Use somente quando tiver certeza.

---

# 77. Não apagar `.git`

Agora existe:

```text
.git/
```

na raiz do projeto.

Não a exclua.

Ela contém o histórico e as configurações do repositório local.

O fato de existir uma cópia no GitHub não transforma `.git` em uma pasta descartável durante o trabalho normal.

---

# 78. Não enviar credenciais

Nunca faça:

```text
token.txt
senha.txt
credenciais.txt
.env com segredos
```

e depois:

```bash
git add .
git commit
git push
```

Se uma credencial real for publicada, ela deve ser considerada comprometida e substituída.

---

# 79. GitHub não substitui backup de tudo

Git e GitHub são excelentes para arquivos apropriados ao controle de versão.

Mas não devemos transformar o repositório em depósito indiscriminado de:

```text
ambientes virtuais
arquivos temporários
credenciais
arquivos gigantes sem necessidade
cópias redundantes
```

O repositório deve ser organizado.

---

# 80. Visualizar o Git pelo VSCode

Clique no ícone:

```text
Source Control
```

na barra lateral do VSCode.

Agora você poderá relacionar a interface visual com os conceitos já praticados:

```text
Changes
        ↓
Working Directory

Staged Changes
        ↓
Staging Area

Commit
        ↓
registro no histórico

Sync / Push
        ↓
sincronização com remoto
```

---

# 81. Por que começamos pelo terminal?

Porque agora, ao olhar a interface do VSCode, sabemos o que está acontecendo.

Sem esse conhecimento, botões como:

```text
Stage
Commit
Sync
Push
Pull
```

seriam apenas ações gráficas decoradas.

Com o modelo mental:

```text
Working Directory
        ↓
Staging Area
        ↓
Local Repository
        ↓
Remote Repository
```

a interface passa a fazer sentido.

---

# 82. Conferir o repositório no navegador

No GitHub, verifique:

```text
[ ] nome: engconvert
[ ] branch principal: main
[ ] arquivos visíveis
[ ] commits visíveis
[ ] README visível
[ ] .gitignore visível
[ ] .venv ausente
```

Se o repositório for público, não publique qualquer dado que não deva ser público.

---

# 83. Atualizar a Sprint 06

Abra:

```text
docs/sprints/sprint-06-git-github.md
```

Depois de concluir a prática, marque:

```markdown
- [x] verificar a instalação do Git;
- [x] configurar nome e e-mail;
- [x] criar/verificar a conta no GitHub;
- [x] criar o `.gitignore`;
- [x] verificar os arquivos que serão versionados;
- [x] inicializar o repositório Git;
- [x] definir a branch principal como `main`;
- [x] preparar os arquivos;
- [x] criar o primeiro commit;
- [x] criar o repositório remoto no GitHub;
- [x] conectar o remoto `origin`;
- [x] realizar a autenticação;
- [x] executar o primeiro `push`;
- [x] conferir o projeto no GitHub;
- [x] realizar um segundo ciclo de alteração, commit e push.
```

---

# 84. Registrar o resultado da Sprint

No mesmo arquivo:

```markdown
## Resultado

O EngConvert passou a utilizar Git para controle de versão e GitHub como repositório remoto.

Foi criado o primeiro histórico do projeto, configurada a branch `main`, definido o remoto `origin` e realizados os primeiros ciclos de `add`, `commit` e `push`.

## Status

**CONCLUÍDA**
```

---

# 85. Atualizar o Roadmap

Abra:

```text
docs/roadmap.md
```

A partir desta reorganização, o Roadmap deverá representar:

```markdown
- [x] **Etapa 1 — Ambiente e estrutura**
- [x] **Etapa 2 — Primeira interface gráfica**
- [x] **Etapa 3 — Widgets e eventos**
- [x] **Etapa 4 — Primeiro conversor**
- [x] **Etapa 5 — Conversor de pressão**
- [x] **Etapa 6 — Novas grandezas**
- [x] **Etapa 7 — Git e GitHub**
- [ ] **Etapa 8 — Modularização**
- [ ] **Etapa 9 — Testes**
- [ ] **Etapa 10 — Interface completa**
- [ ] **Etapa 11 — Distribuição**
```

---

# 86. Estado da Sprint

```text
SPRINT 06 — PRIMEIRO VERSIONAMENTO E PUBLICAÇÃO

STATUS:

CONCLUÍDA
```

E:

```text
ETAPA 7 — GIT E GITHUB

STATUS:

CONCLUÍDA
```

---

# 87. O que o projeto possui agora?

```text
EngConvert
   │
   ├── código Python
   ├── interface gráfica
   ├── múltiplas grandezas
   ├── documentação
   ├── Roadmap
   ├── Sprints
   │
   ├── Git
   │      ├── histórico
   │      ├── commits
   │      └── main
   │
   └── GitHub
          ├── repositório remoto
          ├── commits
          └── origin/main
```

---

# 88. Conceitos praticados

Nesta Sprint utilizamos:

```text
Git
GitHub
repositório
repositório local
repositório remoto
Working Directory
Staging Area
commit
hash
branch
main
remote
origin
push
pull
clone
.gitignore
Git Credential Manager
HTTPS
README.md
requirements.txt
```

E comandos como:

```bash
git --version
git config
git init
git branch
git status
git add
git diff
git commit
git log
git remote
git push
git pull
```

---

# 89. O ciclo que deverá acompanhar o restante do projeto

A partir de agora, as próximas etapas do EngConvert deverão ser desenvolvidas com controle de versão.

Fluxo básico:

```text
COMEÇAR UMA EVOLUÇÃO
        ↓
git status
        ↓
editar
        ↓
testar
        ↓
git status
        ↓
git diff
        ↓
git add
        ↓
git commit
        ↓
git push
```

Isso significa que Git e GitHub deixam de ser apenas o assunto de uma aula.

Eles passam a fazer parte do processo de desenvolvimento.

---

# 90. Antes da próxima grande alteração

A próxima etapa será:

```text
Etapa 8 — Modularização
```

Antes de iniciá-la, devemos possuir:

```text
main funcional
        ↓
commit realizado
        ↓
push realizado
        ↓
GitHub atualizado
```

Isso cria um ponto seguro antes da reorganização do código.

---

# 91. Possível fluxo com branch na próxima etapa

Quando o conceito estiver consolidado, poderemos evoluir para:

```text
main
  │
  └── feature-modularizacao
            ↓
        desenvolver
            ↓
          testar
            ↓
           merge
            ↓
           main
```

Assim o uso de branches surgirá a partir de uma necessidade real do projeto.

---

# 92. Checklist final

Confirme:

```text
[ ] git --version funciona
[ ] user.name configurado
[ ] user.email configurado
[ ] VSCode configurado como editor
[ ] conta GitHub acessível
[ ] e-mail verificado
[ ] projeto abre em C:\Projetos\engconvert

[ ] .gitignore criado
[ ] .venv ignorado
[ ] git init executado quando necessário
[ ] branch main definida
[ ] git status compreendido
[ ] arquivos preparados
[ ] primeiro commit criado
[ ] git log mostra o commit

[ ] repositório engconvert criado no GitHub
[ ] origin configurado
[ ] git remote -v correto
[ ] autenticação concluída
[ ] primeiro push concluído
[ ] arquivos aparecem no GitHub
[ ] .venv NÃO aparece no GitHub

[ ] README alterado
[ ] segundo commit criado
[ ] segundo push realizado

[ ] Sprint 06 CONCLUÍDA
[ ] Etapa 7 CONCLUÍDA
```

---

# 93. 📌 Resumo da Aula 07.1

Transformamos:

```text
PASTA LOCAL
C:\Projetos\engconvert
```

em:

```text
REPOSITÓRIO GIT
       +
REPOSITÓRIO NO GITHUB
```

Executamos:

```text
.gitignore
    ↓
git init
    ↓
git status
    ↓
git add
    ↓
git commit
    ↓
git remote
    ↓
git push
```

E repetimos o ciclo:

```text
editar
  ↓
git diff
  ↓
git add
  ↓
git commit
  ↓
git push
```

---

# 94. 🔜 Próxima etapa

Agora podemos avançar para:

```text
Etapa 8 — Modularização
```

Até aqui, grande parte do EngConvert ainda está concentrada em:

```text
main.py
```

A próxima necessidade será separar responsabilidades.

Por exemplo:

```text
dados de conversão
        ↓
regras de conversão
        ↓
interface gráfica
        ↓
arquivo de entrada
```

A diferença é que agora faremos essa mudança com:

```text
Git
+
commits
+
GitHub
```

protegendo e documentando a evolução do projeto.

---

# 🧭 Visão do percurso

```text
Aula 06.1
EngConvert Multicategorias
        ↓
versão funcional
        ↓
Aula 07.0
Git, GitHub e Controle de Versão
        ↓
Aula 07.1
Primeiro Versionamento e Publicação
        ↓
Sprint 06 — CONCLUÍDA
        ↓
Etapa 7 — CONCLUÍDA
        ↓
Etapa 8
Modularização
```

> 🎯 **Ideia final:** a partir desta aula, o EngConvert não será apenas desenvolvido. Sua evolução também será **registrada, identificada e sincronizada**. Git e GitHub passam a fazer parte do fluxo de trabalho das próximas etapas do projeto.

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
