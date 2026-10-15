# Aula 07.0 — Git, GitHub e Controle de Versão

## Do Projeto Local ao Primeiro Repositório Remoto do EngConvert

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Etapa do Roadmap:** Etapa 7 — Git e GitHub: Controle de Versão e Repositório Remoto  
> **Pré-requisito:** Aulas 06.0 e 06.1 concluídas.  
> **Objetivo:** compreender Git e GitHub desde o primeiro contato, instalar e configurar as ferramentas, criar uma conta no GitHub e entender o fluxo que será utilizado para versionar e publicar o EngConvert.

---

# 🎯 Objetivos da aula

Ao final desta aula, o aluno deverá ser capaz de:

- compreender por que projetos de software precisam de controle de versão;
- distinguir **Terminal**, **Git** e **GitHub**;
- compreender a diferença entre repositório local e remoto;
- baixar e instalar o **Git for Windows**;
- reconhecer o **Git Bash**;
- verificar se o Git está instalado;
- criar uma conta pessoal no **GitHub**;
- compreender a importância da verificação do e-mail e da autenticação em dois fatores;
- configurar nome e e-mail utilizados nos commits;
- compreender `git init`, `git status`, `git add` e `git commit`;
- compreender **Working Directory**, **Staging Area** e **Repository**;
- compreender o que são `branch`, `merge`, `remote` e `origin`;
- compreender `push`, `pull`, `fetch` e `clone`;
- criar um `.gitignore` adequado a um projeto Python;
- entender como o EngConvert será enviado para o GitHub;
- reconhecer formas seguras de desfazer alterações;
- compreender o ciclo básico de trabalho com Git e GitHub.

---

# 1. Por que introduzir Git e GitHub agora?

Até aqui, o EngConvert evoluiu de uma janela simples para uma aplicação capaz de trabalhar com diferentes grandezas:

```text
EngConvert
   │
   ├── Pressão
   ├── Comprimento
   ├── Área
   ├── Volume
   └── Temperatura
```

O projeto já possui uma versão funcional que desejamos preservar.

A partir deste ponto começaremos a realizar alterações estruturais cada vez maiores.

Surge então uma nova necessidade:

```text
PROJETO FUNCIONAL
       ↓
queremos preservar versões
       ↓
queremos saber o que mudou
       ↓
queremos poder voltar
       ↓
queremos trabalhar com segurança
       ↓
CONTROLE DE VERSÃO
```

É exatamente nesse problema que entra o **Git**.

Depois surge outra necessidade:

```text
REPOSITÓRIO LOCAL
       ↓
queremos uma cópia remota
       ↓
queremos compartilhar
       ↓
queremos colaborar
       ↓
queremos construir um portfólio
       ↓
GITHUB
```

> 📌 **Ideia-chave:** primeiro precisamos compreender o controle de versão. Depois compreendemos como esse histórico local se relaciona com uma plataforma remota.

---

# 2. O problema de trabalhar sem controle de versão

É comum encontrar projetos organizados assim:

```text
main.py
main_final.py
main_final_agora_vai.py
main_final_definitivo.py
main_final_definitivo2.py
main_final_definitivo_agora_vai.py
```

Isso parece preservar versões, mas cria problemas:

```text
Qual é a versão correta?

O que mudou entre duas versões?

Quem fez determinada alteração?

Como voltar apenas uma modificação?

Como trabalhar em equipe?

Como testar uma ideia sem destruir a versão funcional?
```

O controle de versão resolve esses problemas de maneira sistemática.

---

# 3. O que é controle de versão?

Um **Sistema de Controle de Versão** registra a evolução de arquivos ao longo do tempo.

Podemos imaginar:

```text
VERSÃO 1
   ↓
VERSÃO 2
   ↓
VERSÃO 3
   ↓
VERSÃO 4
```

Cada versão importante pode ser identificada e registrada.

Isso permite:

```text
acompanhar alterações
        +
preservar histórico
        +
comparar versões
        +
recuperar estados anteriores
        +
trabalhar em paralelo
        +
colaborar
```

No nosso projeto:

```text
EngConvert inicial
        ↓
Conversor de pressão
        ↓
Múltiplas unidades
        ↓
Múltiplas grandezas
        ↓
futuras versões
```

Agora essa evolução passará a ser registrada formalmente.

---

# 4. O que é Git?

**Git** é um sistema distribuído de controle de versão.

Ele registra a evolução dos arquivos de um projeto e permite criar um histórico de desenvolvimento.

Entre suas principais funções estão:

```text
rastrear alterações
registrar versões
comparar mudanças
criar branches
mesclar alterações
recuperar versões
trabalhar localmente
sincronizar com repositórios remotos
```

O Git foi criado por **Linus Torvalds em 2005**, inicialmente para atender às necessidades de desenvolvimento do kernel Linux.

---

# 5. O que significa "distribuído"?

No Git, cada desenvolvedor pode possuir em seu computador uma cópia do repositório com seu histórico.

Didaticamente:

```text
COMPUTADOR A
repositório completo
       │
       │
       ├──────────────┐
       │              │
       ▼              ▼
SERVIDOR REMOTO    COMPUTADOR B
                   repositório completo
```

Isso significa que muitas operações do Git podem ser executadas localmente.

Por exemplo:

```text
git status
git add
git commit
git log
git branch
```

não dependem do GitHub para funcionar.

---

# 6. O que é GitHub?

**GitHub** é uma plataforma on-line que hospeda repositórios Git.

Além de armazenar repositórios remotos, oferece recursos de colaboração, documentação e gerenciamento de projetos.

Entre eles:

```text
repositórios
branches
Pull Requests
Issues
revisão de código
documentação
Actions / automação
perfil profissional
colaboração
```

O GitHub não substitui o Git.

A relação é:

```text
Git
│
├── controla versões
├── funciona localmente
└── cria o histórico

GitHub
│
├── hospeda repositórios Git
├── permite compartilhamento
├── permite colaboração
└── mantém uma cópia remota
```

---

# 7. Terminal, Git e GitHub não são a mesma coisa

Essa distinção é fundamental:

```text
Terminal / PowerShell / Git Bash
        │
        ├── permite digitar comandos
        │
        ▼
       Git
        │
        ├── controla as versões do projeto
        │
        ▼
      GitHub
        │
        └── hospeda e compartilha o repositório remoto
```

Em resumo:

| Tecnologia | Função |
|---|---|
| Terminal | Interface para executar comandos |
| Git | Sistema de controle de versão |
| GitHub | Plataforma on-line para hospedar e colaborar em repositórios Git |

> 📌 **Git pode existir sem GitHub. GitHub utiliza Git.**

---

# 8. Local × remoto

Outra distinção essencial:

```text
LOCAL
```

é aquilo que está no computador do aluno.

```text
C:\Projetos\engconvert
```

Já:

```text
REMOTO
```

é o repositório hospedado em um servidor, como o GitHub.

A relação será:

```text
COMPUTADOR DO ALUNO                    GITHUB

C:\Projetos\engconvert
        │
        │ git push
        ├──────────────────────────────► repositório remoto
        │
        │ git pull
        ◄───────────────────────────────
```

---

# 9. O que instalaremos?

Para esta disciplina utilizaremos:

```text
Windows
   │
   ├── VSCode
   ├── Python
   ├── Git
   ├── Git Bash
   └── navegador
          ↓
        GitHub
```

O **Git Bash** é instalado juntamente com o Git for Windows.

---

# 10. Download do Git for Windows

Abra o navegador e acesse o site oficial do Git:

```text
https://git-scm.com/download/win
```

Baixe a versão atual do **Git for Windows** adequada ao computador.

> ⚠️ **Boa prática:** prefira sempre a página oficial do projeto para baixar instaladores.

Depois do download, execute o instalador.

---

# 11. Instalação do Git no Windows

O instalador apresenta várias telas de configuração.

Para o primeiro contato, a orientação geral é:

```text
manter as opções recomendadas
        ↓
continuar a instalação
        ↓
manter o Git Credential Manager
        ↓
concluir
```

O **Git Credential Manager (GCM)** acompanha o Git for Windows e auxilia na autenticação segura com serviços como o GitHub.

Não é necessário decorar todas as opções do instalador.

Nosso objetivo é obter:

```text
Git
+
Git Bash
+
Git Credential Manager
```

---

# 12. Verificar se o Git foi instalado

Abra o **PowerShell**, o terminal integrado do VSCode ou o **Git Bash**.

Digite:

```bash
git --version
```

O resultado será semelhante a:

```text
git version 2.x.x.windows.x
```

O número exato depende da versão instalada.

O importante é que o comando seja reconhecido.

---

# 13. Como abrir o Git Bash

No Windows:

```text
Pesquisa do Windows
        ↓
digitar:
Git Bash
        ↓
abrir o aplicativo
```

Será exibido algo semelhante a:

```text
aluno@DESKTOP-ABC123 MINGW64 ~
$
```

---

# 14. Entendendo o prompt do Git Bash

Considere:

```text
aluno@DESKTOP-ABC123 MINGW64 ~
$
```

Podemos interpretar:

```text
aluno @ DESKTOP-ABC123   MINGW64   ~
  │          │              │      │
  │          │              │      └── diretório atual
  │          │              └───────── ambiente do terminal
  │          └──────────────────────── computador
  └─────────────────────────────────── usuário
```

`MINGW64` identifica o ambiente utilizado pelo Git Bash no Windows.

O símbolo:

```text
~
```

representa o diretório pessoal do usuário.

O símbolo:

```text
$
```

indica que o terminal está pronto para receber um comando.

> 📌 Ao copiar exemplos, **não digite o `$`**.

---

# 15. Comandos de terminal que já conhecemos

Antes de usar Git, precisamos chegar à pasta correta.

Comandos importantes:

```bash
pwd
```

Mostra o diretório atual.

```bash
ls
```

Lista arquivos e pastas.

```bash
cd pasta
```

Entra em uma pasta.

```bash
cd ..
```

Volta um nível.

No nosso projeto:

```powershell
cd C:\Projetos\engconvert
```

---

# 16. Git Bash × PowerShell × Terminal do VSCode

O Git pode ser utilizado em diferentes terminais:

```text
Git Bash
PowerShell
Prompt de Comando
Terminal integrado do VSCode
```

Nesta disciplina, o aluno poderá utilizar principalmente:

```text
PowerShell
+
Terminal do VSCode
```

e conhecerá também o Git Bash.

O Git não está preso a uma única janela de terminal.

---

# 17. Antes do GitHub: criar uma conta

Para utilizar os recursos pessoais do GitHub, cada aluno deverá possuir uma conta.

Abra:

```text
https://github.com
```

Selecione a opção de cadastro e siga as etapas apresentadas pela plataforma.

O aluno deverá escolher um:

```text
username
```

Esse nome fará parte da identidade pública do perfil e poderá aparecer nos endereços dos repositórios.

> 📌 Escolha um nome de usuário que possa ser utilizado profissionalmente.

---

# 18. Conta gratuita

Para o trabalho inicial da disciplina, uma conta pessoal gratuita é suficiente.

O objetivo é permitir que o aluno:

```text
crie repositórios
publique projetos
acompanhe commits
utilize branches
compartilhe código
construa seu perfil
```

Recursos pagos não são necessários para as atividades introdutórias do EngConvert.

---

# 19. Verificação do e-mail

Após criar a conta, verifique o endereço de e-mail utilizado no cadastro.

A verificação é importante para o uso adequado dos recursos da plataforma.

Fluxo:

```text
criar conta
    ↓
receber mensagem de verificação
    ↓
confirmar e-mail
    ↓
conta preparada
```

---

# 20. Segurança da conta: 2FA

O GitHub recomenda configurar **autenticação de dois fatores — 2FA**.

A ideia é acrescentar uma segunda camada de segurança:

```text
senha
  +
segundo fator
```

Isso reduz o risco de acesso indevido à conta.

> ⚠️ Guarde com segurança os métodos e códigos de recuperação fornecidos durante a configuração.

---

# 21. Conhecendo o perfil do GitHub

Depois de entrar na conta, o aluno encontrará seu perfil.

O perfil pode apresentar:

```text
nome
username
foto
bio
repositórios
contribuições
projetos destacados
organizações
```

Ao longo da disciplina, o GitHub poderá se tornar também parte do portfólio técnico do aluno.

---

# 22. Repositório

Um **repositório** é o ambiente no qual um projeto é acompanhado pelo Git.

Podemos pensar:

```text
REPOSITÓRIO
    │
    ├── arquivos
    ├── pastas
    ├── histórico
    ├── commits
    ├── branches
    └── configurações
```

No nosso caso:

```text
engconvert/
```

será transformado em um repositório Git.

---

# 23. Repositório local

O repositório local ficará no computador:

```text
C:\Projetos\engconvert
```

Quando executarmos:

```bash
git init
```

o Git criará internamente:

```text
.git/
```

A pasta `.git` contém os dados necessários ao controle de versão.

Podemos representar:

```text
pasta comum
    │
    │ git init
    ▼
repositório Git local
```

---

# 24. O que é `.git`?

A pasta:

```text
.git
```

é o núcleo do repositório local.

Ela mantém informações como:

```text
histórico
commits
branches
referências
configurações
metadados
```

> ⚠️ **Não apague nem altere manualmente a pasta `.git`** durante as atividades.

Se ela for removida, a pasta deixa de possuir aquele histórico Git local.

---

# 25. Configurar a identidade do Git

Antes do primeiro commit, precisamos informar ao Git quem está registrando as alterações.

Digite:

```bash
git config --global user.name "Seu Nome"
```

Depois:

```bash
git config --global user.email "seu@email.com"
```

Exemplo:

```bash
git config --global user.name "Maria Silva"
git config --global user.email "maria@email.com"
```

---

# 26. `--global`

Em:

```bash
git config --global user.name "Seu Nome"
```

a opção:

```text
--global
```

indica que essa configuração será utilizada, por padrão, nos repositórios daquele usuário no computador.

Podemos pensar:

```text
CONFIGURAÇÃO GLOBAL
        ↓
vale como padrão
para os repositórios
do usuário
```

---

# 27. Nome do Git × username do GitHub

Eles não são obrigatoriamente a mesma coisa.

Temos:

```text
Git:
user.name
        ↓
identificação gravada nos commits
```

e:

```text
GitHub:
username
        ↓
identidade da conta na plataforma
```

Essa diferença evita uma confusão muito comum entre iniciantes.

---

# 28. E-mail dos commits

O e-mail configurado no Git também fica associado aos commits.

Para que o GitHub associe adequadamente um commit à conta, é importante utilizar um endereço apropriado associado à conta ou uma opção de privacidade disponibilizada pela plataforma.

Mais adiante poderemos discutir:

```text
e-mail público
        ×
e-mail privado / noreply
```

Nesta primeira etapa, o aluno deve compreender que:

```text
commit
   ↓
possui autor
   ↓
nome + e-mail
```

---

# 29. Conferir a configuração

Execute:

```bash
git config --global user.name
```

Depois:

```bash
git config --global user.email
```

Também podemos visualizar configurações com:

```bash
git config --list
```

---

# 30. O conceito mais importante do Git

O fluxo fundamental é:

```text
┌───────────────────┐
│ Working Directory │
│ arquivos em edição│
└─────────┬─────────┘
          │
          │ git add
          ▼
┌───────────────────┐
│   Staging Area    │
│ alterações        │
│ selecionadas      │
└─────────┬─────────┘
          │
          │ git commit
          ▼
┌───────────────────┐
│ Local Repository  │
│ histórico salvo   │
└───────────────────┘
```

Compreender isso é mais importante do que decorar comandos.

---

# 31. Working Directory

O **Working Directory** é a área de trabalho.

É onde normalmente editamos:

```text
main.py
README.md
docs/
aulas/
```

Por exemplo:

```text
alteramos main.py
        ↓
arquivo modificado
        ↓
Working Directory
```

A alteração ainda não é um novo commit.

---

# 32. Staging Area

A **Staging Area** é uma área intermediária.

Nela selecionamos o que deverá entrar no próximo commit.

Fluxo:

```text
main.py modificado
       ↓
git add main.py
       ↓
main.py preparado
para o próximo commit
```

---

# 33. Local Repository

Quando executamos:

```bash
git commit
```

as alterações preparadas são registradas no histórico local.

Assim:

```text
EDITAR
  ↓
PREPARAR
  ↓
REGISTRAR
```

equivale a:

```text
Working Directory
       ↓ git add
Staging Area
       ↓ git commit
Local Repository
```

---

# 34. `git status`: o comando de orientação

Um dos comandos mais importantes para iniciantes é:

```bash
git status
```

Ele ajuda a responder:

```text
Em qual branch estou?

Há arquivos novos?

Há arquivos modificados?

O que ainda não foi preparado?

O que já está na Staging Area?

Minha branch está sincronizada com o remoto?
```

> 🎯 **Regra didática:** use `git status` sempre que tiver dúvida sobre o estado do repositório.

---

# 35. `git add`

Para preparar um arquivo:

```bash
git add main.py
```

Para preparar as alterações da pasta atual:

```bash
git add .
```

Importante:

```text
git add
```

**não cria um commit**.

Ele apenas prepara as alterações.

---

# 36. `git commit`

Depois de preparar as alterações:

```bash
git commit -m "mensagem do commit"
```

Exemplo para o EngConvert:

```bash
git commit -m "feat: adiciona conversor multicategorias"
```

Um commit funciona como um ponto identificado no histórico.

---

# 37. Commit não é simplesmente "salvar"

Quando pressionamos:

```text
Ctrl + S
```

salvamos o arquivo no disco.

Quando executamos:

```bash
git commit
```

registramos uma versão no histórico do Git.

Portanto:

```text
Ctrl + S
   ↓
salva o arquivo

git commit
   ↓
registra um estado no histórico
```

---

# 38. Boas mensagens de commit

Evite:

```text
mudança
teste
coisas
final
agora vai
```

Prefira mensagens que expressem a alteração:

```text
feat: adiciona conversão de volume
fix: corrige fator do galão imperial
docs: atualiza instruções do projeto
refactor: separa regras de conversão
test: adiciona testes de temperatura
```

Prefixos como:

```text
feat
fix
docs
refactor
test
```

ajudam a tornar o histórico mais legível.

---

# 39. `git log`

Para consultar o histórico:

```bash
git log
```

Uma versão compacta:

```bash
git log --oneline
```

Exemplo:

```text
a82f911 feat: adiciona temperatura
47bd210 feat: adiciona volume
c13e602 initial commit
```

O conjunto inicial de caracteres identifica o commit de forma abreviada.

---

# 40. O que é hash?

Cada commit possui um identificador.

Didaticamente, podemos imaginar:

```text
commit
   ↓
conteúdo + metadados
   ↓
identificador
   ↓
hash
```

Exemplo abreviado:

```text
a82f911
```

Esse identificador permite referenciar um commit específico.

---

# 41. O que é uma branch?

Uma **branch** é uma linha de desenvolvimento.

Imagine:

```text
main
  │
  ●────●────●────────────●
             \
              ●────●────●
                  nova-feature
```

Podemos desenvolver uma funcionalidade sem alterar imediatamente a linha principal.

---

# 42. A branch `main`

Usaremos:

```text
main
```

como branch principal do projeto.

Ela deverá representar a linha principal de desenvolvimento.

Podemos verificar branches com:

```bash
git branch
```

---

# 43. Criar uma branch

Uma forma moderna de criar e entrar em uma nova branch é:

```bash
git switch -c nome-da-branch
```

Exemplo futuro:

```bash
git switch -c feature-modularizacao
```

A ideia é:

```text
main
  │
  └── criar branch
          ↓
feature-modularizacao
```

---

# 44. Trocar de branch

Para voltar à `main`:

```bash
git switch main
```

Para entrar em outra branch já existente:

```bash
git switch nome-da-branch
```

Em materiais antigos, o aluno também encontrará:

```bash
git checkout
```

Hoje podemos usar `git switch` para tornar a intenção de troca de branch mais explícita.

---

# 45. `merge`

Depois de concluir e validar uma funcionalidade, podemos integrá-la à branch principal.

Exemplo:

```bash
git switch main
git merge feature-modularizacao
```

Conceitualmente:

```text
main              ●────────────●
                    \          /
feature              ●──●──●
                         ↑
                       merge
```

---

# 46. Conflito de merge

Se duas linhas de desenvolvimento alterarem partes incompatíveis de um mesmo arquivo, poderá ocorrer:

```text
MERGE CONFLICT
```

Isso não significa que o Git "quebrou".

Significa que ele não consegue decidir sozinho qual conteúdo deve prevalecer.

O desenvolvedor precisa analisar e resolver o conflito.

Nesta primeira etapa, nosso objetivo é apenas reconhecer o conceito.

---

# 47. `.gitignore`

Nem tudo que existe na pasta do projeto deve ser enviado para o repositório.

No EngConvert temos um exemplo importante:

```text
.venv/
```

O ambiente virtual é local e pode ser reconstruído.

Não devemos versioná-lo.

---

# 48. `.gitignore` para o EngConvert

Na raiz do projeto, criaremos futuramente:

```text
.gitignore
```

Uma base adequada é:

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

Neste curso, não ignoraremos automaticamente toda a pasta `.vscode/` sem discutir antes se alguma configuração do projeto merece ser compartilhada.

---

# 49. Por que `.venv` não vai para o GitHub?

A pasta `.venv` pode conter muitos arquivos e depende do ambiente local.

O que queremos preservar é:

```text
código
+
documentação
+
dependências declaradas
```

e não:

```text
cópia completa
do ambiente virtual
```

Assim:

```text
.venv/
    ↓
.gitignore
```

Enquanto as dependências podem ser registradas em:

```text
requirements.txt
```

---

# 50. Repositório remoto

Até agora falamos principalmente do Git local.

O próximo conceito é:

```text
REMOTE
```

Um repositório remoto é uma referência para um repositório hospedado fora da máquina local.

No nosso caso, utilizaremos o GitHub.

---

# 51. O que é `origin`?

Quando conectamos o repositório local ao remoto, é comum chamar esse remoto de:

```text
origin
```

Importante:

```text
origin ≠ GitHub
```

`origin` é apenas um nome convencional atribuído ao repositório remoto principal.

Podemos verificar os remotos com:

```bash
git remote -v
```

---

# 52. Criar um repositório no GitHub

Na interface do GitHub, o aluno poderá criar um novo repositório.

Para o projeto utilizaremos futuramente um nome como:

```text
engconvert
```

Ao criar um repositório para receber um projeto local já existente, precisamos ter cuidado para não criar desnecessariamente históricos diferentes no local e no remoto.

Na Aula 07.1 faremos o procedimento completo passo a passo.

---

# 53. Público × privado

Ao criar um repositório, uma decisão importante é sua visibilidade.

```text
PUBLIC
   ↓
o conteúdo pode ser visualizado publicamente
```

```text
PRIVATE
   ↓
o acesso é restrito às pessoas autorizadas
```

A escolha depende do objetivo do projeto.

No curso, o professor poderá definir qual visibilidade deverá ser utilizada para a atividade.

---

# 54. Conectar local e remoto

Conceitualmente, teremos:

```text
C:\Projetos\engconvert
        │
        │ git remote add origin ...
        ▼
GitHub / engconvert
```

O comando possui a forma:

```bash
git remote add origin URL_DO_REPOSITORIO
```

Depois podemos conferir:

```bash
git remote -v
```

---

# 55. HTTPS e autenticação

Para iniciantes no Windows, trabalharemos preferencialmente com repositórios remotos via:

```text
HTTPS
```

O Git for Windows inclui o **Git Credential Manager**, que pode auxiliar no processo seguro de autenticação.

Quando necessário, a autenticação pode ser concluída pelo navegador.

> ⚠️ A senha comum da conta do GitHub não deve ser tratada como senha de autenticação Git no terminal. Os mecanismos atuais utilizam formas mais seguras, como autenticação pelo navegador/credential manager, tokens ou SSH.

Nesta disciplina começaremos com o fluxo HTTPS + Git Credential Manager.

---

# 56. `git push`

O comando:

```bash
git push
```

envia commits locais para o repositório remoto.

No primeiro envio da `main`, é comum utilizar:

```bash
git push -u origin main
```

Podemos ler:

```text
git push  -u  origin  main
   │            │      │
   │            │      └── branch
   │            └───────── remoto
   └────────────────────── enviar commits
```

Depois da configuração inicial, frequentemente será suficiente:

```bash
git push
```

---

# 57. `git pull`

O comando:

```bash
git pull
```

busca alterações do remoto e tenta integrá-las à branch local.

Didaticamente:

```text
GITHUB
   │
   │ git pull
   ▼
REPOSITÓRIO LOCAL
```

---

# 58. `git fetch`

O comando:

```bash
git fetch
```

busca informações do remoto sem integrar automaticamente essas alterações à branch atual.

Assim:

```text
git fetch
    ↓
buscar
    ↓
analisar
    ↓
decidir como integrar
```

Enquanto:

```text
git pull
    ↓
buscar + integrar
```

---

# 59. `git clone`

Quando o projeto já existe em um repositório remoto, podemos copiá-lo para outro computador:

```bash
git clone URL_DO_REPOSITORIO
```

O clone normalmente traz:

```text
arquivos
histórico
branches
configuração do remoto
```

Assim:

```text
GITHUB
   │
   │ git clone
   ▼
NOVO COMPUTADOR
```

---

# 60. `git init` × `git clone`

Essa diferença deve ficar clara:

```text
PROJETO JÁ EXISTE LOCALMENTE
        ↓
git init
```

```text
PROJETO JÁ EXISTE NO REMOTO
        ↓
git clone
```

Em geral, não iniciamos o mesmo fluxo executando os dois indiscriminadamente.

Para o EngConvert:

```text
o projeto já existe em
C:\Projetos\engconvert
        ↓
git init
```

---

# 61. GitHub não é Google Drive

Um erro conceitual comum é pensar no GitHub apenas como uma pasta na nuvem.

O GitHub trabalha com:

```text
repositório
+
histórico
+
commits
+
branches
+
colaboração
```

Não estamos simplesmente copiando arquivos.

Estamos sincronizando um **histórico de desenvolvimento**.

---

# 62. `push` não significa "salvar"

Outro erro comum:

```text
git push
```

não é o comando que cria o commit.

O fluxo correto é:

```text
editar
  ↓
git add
  ↓
git commit
  ↓
git push
```

Portanto:

```text
git add
   ↓
prepara

git commit
   ↓
registra localmente

git push
   ↓
envia commits ao remoto
```

---

# 63. Fluxo completo: local → GitHub

Nosso primeiro fluxo será:

```text
C:\Projetos\engconvert
        ↓
git init
        ↓
.gitignore
        ↓
git status
        ↓
git add .
        ↓
git commit
        ↓
criar repositório no GitHub
        ↓
git remote add origin ...
        ↓
git push -u origin main
```

---

# 64. Fluxo cotidiano depois da configuração

Depois que local e remoto estiverem conectados:

```text
editar arquivos
      ↓
git status
      ↓
git add
      ↓
git commit
      ↓
git push
```

Uma sequência curta para memorizar:

```text
EDITAR
VERIFICAR
PREPARAR
REGISTRAR
SINCRONIZAR
```

---

# 65. O papel do `git status`

Durante o aprendizado, utilizaremos `git status` repetidamente:

```text
editar
  ↓
git status
  ↓
git add
  ↓
git status
  ↓
git commit
  ↓
git status
```

Isso permite observar as mudanças de estado dos arquivos.

O aluno não deve enxergar `git status` como um comando redundante.

Ele funciona como um painel de diagnóstico do repositório.

---

# 66. Como desfazer: primeiro descubra o estado

Antes de desfazer qualquer coisa, pergunte:

```text
A alteração foi commitada?
        │
        ├── NÃO
        │
        └── SIM
             │
             ├── somente local?
             └── já compartilhada?
```

Não existe um único comando universal para "voltar tudo".

---

# 67. `git restore`

Para descartar alterações locais ainda não commitadas em um arquivo:

```bash
git restore main.py
```

Antes:

```bash
git status
```

> ⚠️ Esse comando pode descartar trabalho local. Não o utilize mecanicamente.

---

# 68. `git reset`

O `git reset` pode reposicionar o histórico local.

Exemplo:

```bash
git reset --soft HEAD~1
```

pode remover o commit mais recente da ponta atual, preservando suas alterações para que possam ser reorganizadas.

Já:

```bash
git reset --hard HEAD~1
```

pode descartar alterações.

> ⚠️ `--hard` é potencialmente destrutivo e não será usado como comando rotineiro por iniciantes.

---

# 69. `git revert`

Para um commit que já foi compartilhado, frequentemente é mais apropriado preservar o histórico e criar um novo commit que desfaça o anterior:

```bash
git revert ID_DO_COMMIT
```

Conceitualmente:

```text
A → B → C → D
        ↑
        C permanece no histórico
        D desfaz seu efeito
```

---

# 70. Mapa mental para desfazer

```text
QUERO DESFAZER
      │
      ▼
Já existe commit?
   /        \
 NÃO        SIM
  │          │
  ▼          ▼
restore    já foi compartilhado?
              /       \
            NÃO       SIM
             │         │
             ▼         ▼
           reset     revert
```

Esse mapa é conceitual.

Sempre analise o estado real antes de executar um comando destrutivo.

---

# 71. `git stash`

Imagine que existe trabalho ainda não concluído, mas precisamos mudar temporariamente de contexto.

Podemos guardar as alterações:

```bash
git stash
```

Depois recuperá-las:

```bash
git stash pop
```

Fluxo:

```text
trabalho incompleto
       ↓
git stash
       ↓
alterações guardadas
temporariamente
       ↓
git stash pop
       ↓
alterações recuperadas
```

Esse recurso será explorado quando começarmos a trabalhar mais intensamente com branches.

---

# 72. Quando o Git abrir um editor

Em algumas situações, o Git pode abrir um editor de texto para receber uma mensagem.

Se o editor for o **Vim**, o aluno pode achar que o terminal travou.

Comandos mínimos:

| Ação | Comando |
|---|---|
| Entrar no modo de edição | `i` |
| Sair do modo de edição | `Esc` |
| Salvar e sair | `:wq` + `Enter` |
| Sair sem salvar | `:q!` + `Enter` |

Não faremos um curso de Vim.

O objetivo é apenas reconhecer a situação.

---

# 73. Configurar o VSCode como editor do Git

Como já utilizamos VSCode, podemos configurá-lo como editor:

```bash
git config --global core.editor "code --wait"
```

Aqui:

```text
code
  ↓
abre o VSCode

--wait
  ↓
faz o Git aguardar
até o arquivo ser fechado
```

Isso reduz a possibilidade de o iniciante ser surpreendido por um editor desconhecido.

---

# 74. Git no VSCode

O VSCode possui integração visual com Git.

Depois que a pasta se torna um repositório, podemos visualizar:

```text
arquivos modificados
staging
commits
branches
sincronização
```

Entretanto, nesta primeira etapa utilizaremos principalmente comandos.

Por quê?

Porque queremos compreender o processo:

```text
Working Directory
        ↓
Staging Area
        ↓
Repository
        ↓
Remote
```

Depois a interface gráfica do VSCode ficará muito mais fácil de entender.

---

# 75. GitHub no navegador

No GitHub, o aluno deverá aprender a reconhecer pelo menos:

```text
perfil
repositórios
Code
Issues
Pull requests
Actions
Settings
```

Nem todos esses recursos serão utilizados imediatamente.

A prioridade será:

```text
Repository
Code
Commits
Branches
```

---

# 76. `README.md`

Um repositório pode possuir:

```text
README.md
```

Esse arquivo apresenta o projeto.

Para o EngConvert, futuramente poderemos informar:

```text
nome do projeto
objetivo
tecnologias
como instalar
como executar
funcionalidades
estrutura
licença
```

O README funciona como uma porta de entrada para quem visita o repositório.

---

# 77. O GitHub como portfólio

Além de colaboração, o GitHub pode funcionar como registro público da evolução técnica do aluno.

Um perfil bem organizado pode demonstrar:

```text
projetos
documentação
frequência de desenvolvimento
boas práticas
capacidade de colaboração
evolução técnica
```

Mas o objetivo principal nesta aula continua sendo:

```text
aprender controle de versão
+
publicar corretamente um projeto
```

---

# 78. Issues

Uma **Issue** pode ser utilizada para registrar:

```text
tarefa
problema
bug
melhoria
discussão
```

Exemplo futuro:

```text
Issue:
Adicionar configuração de precisão dos resultados
```

Isso se conecta diretamente ao Roadmap do EngConvert.

---

# 79. Pull Request

Uma **Pull Request** propõe integrar alterações de uma branch a outra.

Fluxo simplificado:

```text
branch de funcionalidade
        ↓
alterações concluídas
        ↓
Pull Request
        ↓
revisão
        ↓
merge
        ↓
main
```

Esse conceito será mais útil quando trabalharmos com branches e colaboração.

---

# 80. GitHub Actions e uma primeira ideia de CI/CD

O GitHub também possui mecanismos de automação.

Um dos principais é o:

```text
GitHub Actions
```

Com ele, um repositório pode ser configurado para executar automaticamente tarefas como:

```text
testes
verificações
build
empacotamento
deploy
```

Isso está relacionado ao conceito de:

```text
CI/CD
```

**CI/CD** é a sigla utilizada para práticas de automação do processo de desenvolvimento e entrega de software.

### CI — Continuous Integration

Em português:

```text
Integração Contínua
```

A ideia é integrar alterações ao projeto com frequência e verificar automaticamente se o código continua funcionando.

Por exemplo:

```text
ALTERAÇÃO NO CÓDIGO
        ↓
     git push
        ↓
      GitHub
        ↓
  GitHub Actions
        ↓
executar testes automaticamente
        ↓
verificar se o projeto continua funcionando
```

No futuro, poderíamos configurar o EngConvert para executar seus testes automaticamente após determinadas alterações enviadas ao GitHub.

### CD — Continuous Delivery / Continuous Deployment

Em português, encontramos principalmente:

```text
Entrega Contínua
```

ou:

```text
Implantação Contínua
```

Essas práticas automatizam etapas posteriores à integração, como preparar uma nova versão e, dependendo do fluxo adotado, disponibilizá-la em um ambiente de uso.

De forma simplificada:

```text
CÓDIGO
  ↓
CI
  ↓
testar e verificar
  ↓
CD
  ↓
preparar / entregar / implantar
uma nova versão
```

Aplicando a ideia ao EngConvert:

```text
git push
    ↓
GitHub
    ↓
GitHub Actions
    ↓
executar testes do EngConvert
    ↓
      ┌───────────────┐
      │               │
    PASS             FAIL
      │               │
      ▼               ▼
verificação       problema
concluída         detectado
```

Mais adiante, esse processo poderia ser ampliado para:

```text
testar
   ↓
gerar o executável
   ↓
preparar uma nova versão
   ↓
disponibilizar a versão
```

> 📌 **Ideia-chave:** Git e GitHub registram e compartilham a evolução do projeto. O **CI/CD acrescenta automação a esse fluxo**, permitindo verificar, preparar e eventualmente distribuir novas versões do software.

Nesta etapa, precisamos apenas compreender o conceito.

**Não implementaremos CI/CD agora.**

Também não entraremos ainda em arquivos de workflow, YAML ou configuração do GitHub Actions. Esses assuntos fazem mais sentido depois que o EngConvert possuir testes automatizados.

A ideia, neste momento, é perceber que o GitHub pode ir muito além de simplesmente armazenar código.

---

# 81. O EngConvert antes do primeiro commit

Antes de versionar, deveremos conferir a estrutura.

Conceitualmente:

```text
engconvert/
│
├── aulas/
├── docs/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── .venv/          ← local, não versionar
```

A estrutura real do aluno deverá ser conferida antes do primeiro `git add .`.

---

# 82. Atenção antes de `git add .`

Nunca execute mecanicamente:

```bash
git add .
```

sem primeiro verificar:

```bash
git status
```

e confirmar que arquivos sensíveis ou desnecessários não serão adicionados.

Fluxo seguro:

```text
.gitignore
    ↓
git status
    ↓
conferir
    ↓
git add .
```

---

# 83. Nunca versionar segredos

Arquivos que podem conter:

```text
senhas
tokens
chaves de API
credenciais
```

não devem ser publicados em repositórios.

Um arquivo comum para variáveis locais é:

```text
.env
```

Por isso incluímos:

```gitignore
.env
```

no `.gitignore`.

> ⚠️ Se um segredo for enviado a um repositório, simplesmente apagá-lo em um commit posterior pode não removê-lo do histórico. O segredo deve ser considerado comprometido e substituído.

---

# 84. Autenticação: senha da conta não é senha do Git

No navegador, o aluno entra em sua conta do GitHub utilizando os mecanismos oferecidos pela plataforma.

Já o Git no terminal utiliza mecanismos próprios de autenticação segura.

Para nosso ambiente Windows:

```text
Git
  ↓
HTTPS
  ↓
Git Credential Manager
  ↓
autenticação
  ↓
GitHub
```

Isso evita ensinar um fluxo antigo baseado em senha comum da conta para operações Git.

---

# 85. Primeiro contato com autenticação pelo navegador

No primeiro `push`, dependendo da configuração, o Git Credential Manager poderá abrir uma janela ou o navegador.

O aluno deverá:

```text
confirmar a conta
        ↓
autorizar a autenticação
        ↓
retornar ao terminal
        ↓
continuar o push
```

Depois, as credenciais podem ser gerenciadas de forma segura pelo sistema.

A aparência exata das telas pode mudar com atualizações da plataforma.

---

# 86. O que o aluno NÃO precisa decorar agora

Não é necessário memorizar imediatamente:

```text
todos os comandos Git
todos os tipos de reset
todos os modos de merge
SSH
tokens avançados
rebase
cherry-pick
GitHub Actions
GitHub CLI
```

O primeiro objetivo é dominar:

```text
git status
git add
git commit
git log
git push
git pull
```

e compreender o que cada etapa faz.

---

# 87. Os seis comandos fundamentais desta etapa

```bash
git status
git add .
git commit -m "mensagem"
git log --oneline
git push
git pull
```

Mas lembre:

> 🎯 **Mais importante do que decorar os comandos é compreender onde estão as alterações e o que cada comando faz com elas.**

---

# 88. Vocabulário essencial

| Termo | Significado didático |
|---|---|
| Repository | Projeto controlado pelo Git |
| Working Directory | Arquivos em edição |
| Staging Area | Alterações preparadas para o próximo commit |
| Commit | Registro de uma versão no histórico |
| Branch | Linha de desenvolvimento |
| Merge | Integração entre linhas de desenvolvimento |
| Remote | Referência para um repositório remoto |
| Origin | Nome convencional do remoto principal |
| Push | Enviar commits ao remoto |
| Pull | Buscar e integrar alterações remotas |
| Fetch | Buscar informações sem integrar automaticamente |
| Clone | Copiar um repositório remoto para a máquina |
| `.gitignore` | Regras de arquivos/pastas que o Git deve ignorar |

---

# 89. Comparação rápida dos comandos

```text
git init
   ↓
inicia controle Git

git status
   ↓
mostra o estado

git add
   ↓
prepara alterações

git commit
   ↓
registra versão local

git push
   ↓
envia commits

git pull
   ↓
busca e integra

git clone
   ↓
obtém um repositório existente
```

---

# 90. Fluxo mental do iniciante

```text
ABRIR O PROJETO
      ↓
git status
      ↓
EDITAR
      ↓
git status
      ↓
git add
      ↓
git status
      ↓
git commit
      ↓
git log --oneline
      ↓
git push
```

A repetição de `git status` é intencional.

Ela ajuda o aluno a visualizar a mudança de estado.

---

# 91. O que faremos com o EngConvert

Na Aula 07.1, o roteiro prático utilizará o projeto real.

O fluxo será:

```text
C:\Projetos\engconvert
        ↓
verificar estrutura
        ↓
criar .gitignore
        ↓
git init
        ↓
git branch -M main
        ↓
git status
        ↓
git add .
        ↓
primeiro commit
        ↓
criar repositório no GitHub
        ↓
conectar origin
        ↓
primeiro push
        ↓
conferir arquivos no navegador
```

---

# 92. O primeiro commit do EngConvert

O primeiro commit não representa o início cronológico do projeto.

O EngConvert já existe.

Ele representa o momento em que começamos a registrar formalmente seu histórico com Git.

Uma mensagem possível será:

```text
feat: registra versão multicategorias do EngConvert
```

A partir desse ponto, cada evolução poderá ser registrada.

---

# 93. Por que versionar antes da modularização?

A próxima grande evolução do EngConvert envolverá reorganizar o código.

Hoje:

```text
main.py
   │
   ├── dados
   ├── regras
   ├── funções
   └── interface
```

Na modularização, parte desse conteúdo será distribuída em arquivos diferentes.

Antes de fazer isso:

```text
VERSÃO FUNCIONAL
       ↓
COMMIT
       ↓
GITHUB
       ↓
MODULARIZAÇÃO
```

Assim teremos um ponto seguro no histórico.

---

# 94. Novo Roadmap a partir desta etapa

A evolução passa a ser:

```text
Etapa 1 — Ambiente e estrutura              ✓
Etapa 2 — Primeira interface gráfica        ✓
Etapa 3 — Widgets e eventos                 ✓
Etapa 4 — Primeiro conversor                ✓
Etapa 5 — Conversor de pressão              ✓
Etapa 6 — Novas grandezas                   ✓
Etapa 7 — Git e GitHub                      ← ATUAL
Etapa 8 — Modularização
Etapa 9 — Testes
Etapa 10 — Interface completa
Etapa 11 — Distribuição
```

Na interface completa entraremos posteriormente em recursos como:

```text
precisão
notação científica
configurações
aparência
refinamentos de UX
```

---

# 95. Sprint prevista

A implementação prática será organizada como:

```text
SPRINT 06 — PRIMEIRO VERSIONAMENTO E PUBLICAÇÃO
```

Objetivos:

```text
[ ] instalar/verificar Git
[ ] criar/verificar conta GitHub
[ ] configurar identidade do Git
[ ] preparar .gitignore
[ ] inicializar repositório
[ ] criar primeiro commit
[ ] criar repositório remoto
[ ] conectar origin
[ ] autenticar com segurança
[ ] realizar primeiro push
[ ] conferir o EngConvert no GitHub
```

A execução será feita na Aula 07.1.

---

# 96. Erros comuns do iniciante

### Erro 1

```text
Git = GitHub
```

Correção:

```text
Git ≠ GitHub
```

---

### Erro 2

```text
git add = salvar versão
```

Correção:

```text
git add
   ↓
prepara

git commit
   ↓
registra
```

---

### Erro 3

```text
git push = criar commit
```

Correção:

```text
git push
   ↓
envia commits existentes
```

---

### Erro 4

Enviar:

```text
.venv/
```

Correção:

```text
.gitignore
```

---

### Erro 5

Publicar:

```text
senha
token
chave de API
.env
```

Correção:

```text
nunca versionar segredos
```

---

### Erro 6

Executar comandos destrutivos sem:

```bash
git status
```

Correção:

```text
primeiro compreender o estado
depois escolher o comando
```

---

# 97. Checklist conceitual

Antes da prática, confirme se você consegue explicar:

```text
[ ] o que é controle de versão
[ ] o que é Git
[ ] o que é GitHub
[ ] diferença entre Git e GitHub
[ ] diferença entre local e remoto
[ ] o que é repositório
[ ] o que é commit
[ ] o que é branch
[ ] o que é merge
[ ] o que é Working Directory
[ ] o que é Staging Area
[ ] o que é origin
[ ] o que faz push
[ ] o que faz pull
[ ] o que faz clone
[ ] para que serve .gitignore
[ ] por que .venv não deve ser versionado
```

---

# 98. Checklist de preparação

Antes da Aula 07.1:

```text
[ ] Git instalado
[ ] git --version funcionando
[ ] Git Bash disponível
[ ] conta GitHub criada
[ ] e-mail da conta verificado
[ ] 2FA considerada/configurada
[ ] username conhecido
[ ] acesso ao GitHub funcionando
[ ] projeto EngConvert funcionando
[ ] pasta C:\Projetos\engconvert localizada
```

---

# 99. Resumo da aula

Nesta aula construímos a visão:

```text
ARQUIVOS DO PROJETO
        ↓
       Git
        ↓
controle de versão local
        ↓
     commits
        ↓
    branches
        ↓
repositório remoto
        ↓
      GitHub
```

O fluxo fundamental do Git é:

```text
Working Directory
        ↓
      git add
        ↓
Staging Area
        ↓
    git commit
        ↓
Local Repository
        ↓
     git push
        ↓
Remote Repository
```

---

# 100. Ideia-chave

```text
Git não é apenas um conjunto de comandos.

Git é uma forma de controlar
a evolução de um projeto.
```

E:

```text
GitHub não substitui o Git.

GitHub amplia o fluxo do Git
para armazenamento remoto,
compartilhamento e colaboração.
```

---

# 101. Próxima aula

## Aula 07.1 — Roteiro Prático

### Primeiro Versionamento e Publicação do EngConvert

Na próxima aula faremos, passo a passo:

```text
instalação/verificação
        ↓
configuração
        ↓
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
GitHub
        ↓
origin
        ↓
autenticação
        ↓
git push
        ↓
EngConvert publicado
```

---

# 🧭 Visão do percurso

```text
Aula 06.0
Novas Grandezas
      ↓
Aula 06.1
Sprint 05
      ↓
Etapa 6 — CONCLUÍDA
      ↓
Aula 07.0
Git, GitHub e Controle de Versão
      ↓
Aula 07.1
Primeiro Versionamento e Publicação
      ↓
Sprint 06
      ↓
Etapa 7 — Git e GitHub
      ↓
Etapa 8 — Modularização
```

> 🎯 **Ideia final:** agora que o EngConvert possui uma versão funcional relevante, começaremos a preservar sua evolução de forma profissional. O Git registrará a história do projeto; o GitHub permitirá armazená-la remotamente, compartilhá-la e utilizá-la como base para as próximas etapas do desenvolvimento.

---

# 📚 Fontes e material de apoio

Esta aula foi estruturada a partir do material didático já utilizado na disciplina — **Guia Didático — Comandos Básicos de Git e Terminal** e **Programação para Engenharia Mecânica — GitHub (Aulas 13 a 16)** — e ampliada para o fluxo atual do projeto EngConvert.

Para procedimentos que podem mudar com o tempo, consulte também a documentação oficial:

```text
Git:
https://git-scm.com/

GitHub:
https://github.com/

GitHub Docs:
https://docs.github.com/
```

> 📌 Interfaces, nomes de botões e telas de cadastro/autenticação podem mudar. Os conceitos de Git apresentados nesta aula permanecem a referência para compreender o fluxo.
