# Aula 00 — Construindo o EngConvert pelo Terminal

## Roteiro direto de preparação e construção do projeto no VSCode

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Objetivo:** preparar o ambiente inicial do projeto e começar sua construção utilizando o terminal integrado do VSCode.

---

## 🎯 Como utilizar esta Aula 00

Esta aula funciona como um **roteiro prático de execução**.

Diferentemente de um projeto iniciado completamente do zero, você receberá do professor um arquivo `.zip` contendo a pasta `engconvert` e os materiais iniciais da disciplina.

A proposta será:

```text
receber o arquivo .zip
        ↓
descompactar o material
        ↓
colocar engconvert em C:\Projetos
        ↓
abrir engconvert no VSCode
        ↓
acompanhar a Aula 00
        ↓
criar a estrutura do software
        ↓
criar a .venv
        ↓
instalar as dependências
        ↓
criar o primeiro programa
        ↓
executar o EngConvert
```

> 💡 Nesta Aula 00, o objetivo principal é **fazer**.  
> Nas aulas seguintes, cada comando, pasta, arquivo e conceito será estudado com mais detalhes.

### 👁️ Como visualizar este arquivo Markdown

Os arquivos das aulas utilizam a extensão `.md`, isto é, são arquivos **Markdown**. No VSCode, podemos visualizar o texto e também sua apresentação formatada.

Com o arquivo `.md` aberto, pressione:

```text
Ctrl + Shift + V
```

para abrir o **Markdown Preview**.

Para visualizar a edição e o resultado lado a lado, utilize:

```text
Ctrl + K
depois
V
```

Também é possível clicar com o botão direito dentro do arquivo e escolher **Open Preview** ou **Open Preview to the Side**.

> 💡 **Ideia-chave:** o arquivo `.md` continua sendo texto. O Preview apenas mostra como esse conteúdo será apresentado de forma formatada.

---

## 📦 Material inicial fornecido

Para iniciar o projeto, será disponibilizado pelo professor um arquivo compactado contendo a pasta:

```text
engconvert/
```

Inicialmente, ela conterá principalmente o material didático:

```text
engconvert/
│
└── aulas/
    ├── aula-00-roteiro-terminal.md
    ├── aula-01.0-vscode-estrutura-ambiente.md
    ├── aula-01.1-roteiro-pratico.md
    ├── aula-02.0-gui-roadmap-sprints.md
    ├── aula-02.1-roteiro-pratico.md
    ├── aula-03.0-widgets-eventos.md
    ├── aula-03.1-roteiro-pratico.md
    ├── aula-04.0-primeiro-conversor.md
    ├── aula-04.1-roteiro-pratico.md
    └── ...
```

A pasta `aulas/` contém os arquivos Markdown que acompanharão a construção do projeto.

> 🎯 **Importante:** o material das aulas será fornecido, mas o **software será construído progressivamente pelo aluno**.

---

## 🏗️ Antes de começar: como se organiza um projeto de software?

Um programa profissional normalmente não é formado por apenas um arquivo `.py`.

À medida que um software cresce, precisamos organizar diferentes tipos de conteúdo: **código-fonte, documentação, testes, recursos visuais, dependências e arquivos de configuração**.

Uma estrutura simplificada pode ser representada assim:

```text
projeto/
│
├── src/                  → código-fonte do programa
│
├── tests/                → testes do software
│
├── assets/               → imagens, ícones e outros recursos
│
├── docs/                 → documentação e planejamento
│
├── main.py               → ponto inicial de execução
│
├── README.md             → apresentação e instruções do projeto
│
├── requirements.txt      → dependências Python
│
└── .gitignore            → arquivos que não devem ser versionados
```

Não significa que todos os projetos Python terão exatamente essa estrutura.

A organização depende do **tamanho, finalidade e complexidade do software**.

No EngConvert, utilizaremos uma estrutura semelhante porque queremos acompanhar a evolução de um programa simples até um **projeto de software organizado**.

### 🔎 O que representa cada parte?

```text
PROJETO
│
├── src/
│     └── Onde ficará o código-fonte da aplicação.
│
├── tests/
│     └── Onde ficarão os testes utilizados para verificar
│         se o programa continua funcionando corretamente.
│
├── assets/
│     └── Recursos utilizados pelo programa, como imagens,
│         ícones e outros elementos visuais.
│
├── docs/
│     └── Documentação técnica, Roadmap, Sprints e
│         outras informações sobre o desenvolvimento.
│
├── main.py
│     └── Ponto de entrada inicial do programa.
│
├── README.md
│     └── Apresenta o projeto e explica como utilizá-lo.
│
├── requirements.txt
│     └── Registra as bibliotecas Python necessárias.
│
└── .gitignore
      └── Informa ao Git quais arquivos e pastas
          não deverão ser versionados.
```

> 💡 **Não precisamos preencher ou utilizar tudo imediatamente.**  
> Algumas dessas estruturas ganharão importância somente quando o EngConvert crescer.

### 🎓 E a pasta `aulas/`?

No nosso projeto também teremos:

```text
aulas/
```

Ela possui uma finalidade **didática**.

```text
EngConvert
│
├── aplicação
│     ├── src/
│     ├── tests/
│     ├── assets/
│     └── ...
│
└── material didático
      └── aulas/
```

A pasta `aulas/` armazenará os arquivos Markdown utilizados para acompanhar o desenvolvimento do EngConvert durante a disciplina.

Ela não é uma pasta obrigatória de um projeto Python profissional. Está presente porque o **EngConvert também é uma aula-projeto**.

### 🧠 Uma analogia com Engenharia Mecânica

Podemos comparar a organização do software com a documentação de um projeto de engenharia:

```text
PROJETO DE ENGENHARIA                 PROJETO DE SOFTWARE

desenhos e modelos             →      código-fonte
memorial/documentação          →      docs/
procedimentos de ensaio        →      tests/
catálogos e recursos           →      assets/
lista de materiais             →      requirements.txt
documento geral do projeto     →      README.md
```

Em ambos os casos, organizar corretamente as informações facilita o **desenvolvimento, a manutenção, os testes, a documentação, o trabalho em equipe e a evolução do projeto**.

> 🎯 **Ideia-chave:** um software profissional não é apenas código. Ele também envolve **organização, documentação, testes, dependências e controle de sua evolução**.

---

### 📚 Padrão de nomenclatura das aulas

A partir da **Aula 01**, utilizaremos dois materiais complementares para cada etapa:

```text
Aula XX.0  → conteúdo completo e aprofundado
Aula XX.1  → roteiro prático de implementação
```

Assim:

```text
01.0  → estudar e compreender
01.1  → implementar

02.0  → estudar e compreender
02.1  → implementar
```

A **Aula 00** permanece como caso especial, pois sua função é preparar e construir a estrutura inicial do projeto.

> 🎯 **Ideia-chave:** os arquivos `.0` apresentam os conceitos e explicações completas; os arquivos `.1` orientam a execução prática, sem repetir desnecessariamente etapas já concluídas.

---

# 1. Preparar a pasta geral de projetos

Durante o curso utilizaremos:

```text
C:\Projetos
```

Se essa pasta ainda não existir, abra o terminal e execute:

```powershell
mkdir C:\Projetos
```

Depois:

```powershell
cd C:\Projetos
```

Podemos confirmar onde estamos com:

```powershell
pwd
```

Resultado esperado:

```text
C:\Projetos
```

> 📌 Se `C:\Projetos` já existir, não é necessário criá-la novamente.

---

# 2. Descompactar o material fornecido

Descompacte o arquivo `.zip` fornecido pelo professor.

Depois, coloque a pasta:

```text
engconvert
```

dentro de:

```text
C:\Projetos
```

A estrutura deverá ficar semelhante a:

```text
C:\
└── Projetos/
    └── engconvert/
        └── aulas/
            ├── aula-00-roteiro-terminal.md
            ├── aula-01.0-vscode-estrutura-ambiente.md
            ├── aula-01.1-roteiro-pratico.md
            ├── aula-02.0-gui-roadmap-sprints.md
            ├── aula-02.1-roteiro-pratico.md
            ├── aula-03.0-widgets-eventos.md
            ├── aula-03.1-roteiro-pratico.md
            ├── aula-04.0-primeiro-conversor.md
            ├── aula-04.1-roteiro-pratico.md
            └── ...
```

Assim, o material didático já estará disponível dentro do próprio projeto.

---

# 3. Entrar na pasta do EngConvert

No terminal:

```powershell
cd C:\Projetos\engconvert
```

Confirme:

```powershell
pwd
```

Resultado esperado:

```text
C:\Projetos\engconvert
```

Para visualizar o que existe na pasta:

```powershell
dir
```

Você deverá encontrar, inicialmente, a pasta:

```text
aulas
```

### 🧭 Comandos básicos para navegar pelo terminal

Vale diferenciar alguns comandos que aparecerão bastante durante o desenvolvimento:

```text
pwd          → Onde estou?
cd           → Quero mudar de pasta.
dir / ls     → O que existe nesta pasta?
mkdir        → Quero criar uma pasta.
```

- **`pwd`** (_Print Working Directory_) → mostra o diretório de trabalho atual.
- **`cd`** (_Change Directory_) → permite entrar ou mudar de pasta.
- **`dir` / `ls`** → mostram os arquivos e pastas existentes no diretório atual.
- **`mkdir`** (_Make Directory_) → cria uma nova pasta.

> 💡 Esses comandos ajudam a **localizar, navegar e visualizar** a estrutura do projeto diretamente pelo terminal.

---

# 4. E se a pasta `engconvert` não tivesse sido fornecida?

Neste curso, a pasta `engconvert` já foi fornecida no arquivo `.zip`, juntamente com os materiais das aulas.

Por isso, **não precisamos criá-la novamente**.

Entretanto, é importante compreender como iniciaríamos um projeto completamente do zero.

Se estivéssemos em:

```text
C:\Projetos
```

poderíamos executar:

```powershell
mkdir engconvert
```

Depois:

```powershell
cd engconvert
```

Teríamos:

```text
C:\Projetos\engconvert
```

Portanto:

```text
mkdir engconvert
      ↓
cria a pasta do projeto

cd engconvert
      ↓
entra na pasta criada
```

> 🎯 **Ideia-chave:** mantemos este exemplo porque `mkdir` e `cd` serão comandos importantes durante todo o desenvolvimento, embora a pasta principal do EngConvert já tenha sido fornecida nesta disciplina.

---

# 5. Abrir a pasta do projeto no VSCode

Neste momento, devemos estar em:

```text
C:\Projetos\engconvert
```

Podemos confirmar:

```powershell
pwd
```

Se o VSCode ainda **não estiver aberto com a pasta `engconvert` como projeto**, execute:

```powershell
code .
```

Nesse comando:

```text
code .
│    │
│    └── . = diretório atual
│
└── code = abrir no Visual Studio Code
```

Portanto:

```powershell
code .
```

significa:

> **"Abra no VSCode a pasta em que o terminal está localizado neste momento."**

### 🔎 E se o terminal estiver em outra pasta?

É importante perceber que:

```powershell
code .
```

**não significa "abra o EngConvert".**

O comando significa:

> **"Abra no VSCode a pasta em que estou agora."**

Por exemplo, se o terminal estiver em:

```text
PS C:\Projetos>
```

e executarmos:

```powershell
code .
```

o VSCode abrirá:

```text
C:\Projetos
```

porque, naquele momento:

```text
. = C:\Projetos
```

Para abrir o EngConvert, podemos primeiro entrar nele:

```powershell
cd engconvert
```

Agora:

```text
PS C:\Projetos\engconvert>
```

Então:

```powershell
code .
```

abrirá:

```text
C:\Projetos\engconvert
```

Também poderíamos, estando em `C:\Projetos`, executar diretamente:

```powershell
code engconvert
```

ou informar o caminho completo:

```powershell
code C:\Projetos\engconvert
```

> 🎯 **Ideia-chave:** o ponto `.` representa o **diretório atual**. Portanto, `code .` pede ao VSCode que abra como projeto a pasta em que o terminal está localizado naquele momento.

> 📌 Se a pasta `engconvert` já estiver aberta no VSCode, não é necessário executar `code .` novamente.

---

# 6. Criar as pastas iniciais do software

A pasta `aulas/` já veio no material fornecido.

Agora começaremos a construir a estrutura do software.

Execute:

```powershell
mkdir assets
mkdir docs
mkdir src
mkdir tests
```

Teremos:

```text
engconvert/
│
├── assets/
├── aulas/        ← fornecida pelo professor
├── docs/
├── src/
└── tests/
```

Observe a diferença:

```text
aulas/
   ↓
material didático fornecido

assets/ docs/ src/ tests/
   ↓
estrutura construída pelo aluno
```

---

# 7. Preparar a documentação do projeto

Crie a pasta destinada às Sprints:

```powershell
mkdir docs\sprints
```

Agora:

```text
docs/
└── sprints/
```

Crie os documentos iniciais:

```powershell
New-Item docs\roadmap.md -ItemType File
New-Item docs\git-github.md -ItemType File
New-Item docs\arquitetura.md -ItemType File
```

Crie os arquivos iniciais das Sprints:

```powershell
New-Item docs\sprints\sprint-00-ambiente.md -ItemType File
New-Item docs\sprints\sprint-01-interface.md -ItemType File
New-Item docs\sprints\sprint-02-widgets.md -ItemType File
New-Item docs\sprints\sprint-03-conversor.md -ItemType File
```

A estrutura ficará:

```text
docs/
├── roadmap.md
├── git-github.md
├── arquitetura.md
└── sprints/
    ├── sprint-00-ambiente.md
    ├── sprint-01-interface.md
    ├── sprint-02-widgets.md
    └── sprint-03-conversor.md
```

> 💡 **Roadmap** apresenta a direção geral do projeto.  
> **Sprints** representam etapas menores de desenvolvimento. Esses conceitos serão aprofundados nas aulas seguintes.

---

# 8. Criar a estrutura inicial de `src`

Crie:

```powershell
mkdir src\engconvert
```

Neste momento teremos:

```text
src/
└── engconvert/
```

Agora crie:

```powershell
New-Item src\engconvert\__init__.py -ItemType File
```

Teremos:

```text
src/
└── engconvert/
    └── __init__.py
```

Mais adiante, quando o programa crescer e surgir a necessidade de modularização, essa estrutura poderá evoluir para algo semelhante a:

```text
src/
└── engconvert/
    ├── converters/
    ├── gui/
    ├── data/
    └── utils/
```

Por enquanto, **não criaremos essas quatro subpastas**.

> 💡 Primeiro construiremos o programa. Depois, quando o código começar a crescer, entenderemos por que separar suas responsabilidades se torna necessário.

---

# 9. Preparar a pasta `tests`

A pasta:

```text
tests/
```

já foi criada.

Neste momento, criaremos apenas um arquivo de orientação:

```powershell
New-Item tests\README.md -ItemType File
```

O primeiro arquivo de teste será criado somente quando chegarmos à etapa de **testes automatizados**.

Assim, os testes surgirão quando existir uma necessidade concreta de verificar o comportamento do software.

---

# 10. Entender a evolução futura de `assets`

Neste momento temos apenas:

```text
assets/
```

Quando o EngConvert começar a utilizar recursos visuais, poderemos organizá-la, por exemplo, assim:

```text
assets/
├── icons/
├── images/
└── screenshots/
```

Ainda **não criaremos essas subpastas**, porque não existem ícones, imagens ou capturas de tela para armazenar.

> 💡 Podemos conhecer antecipadamente a estrutura para a qual o projeto poderá evoluir, mas criaremos cada pasta quando ela passar a ter uma responsabilidade real.

---

# 11. Criar os arquivos da raiz do projeto

`mkdir` cria **diretórios**.

Para criar arquivos vazios no PowerShell, utilizaremos:

```text
New-Item
```

Execute:

```powershell
New-Item main.py -ItemType File
New-Item README.md -ItemType File
New-Item requirements.txt -ItemType File
New-Item .gitignore -ItemType File
```

Agora teremos também:

```text
engconvert/
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

> 📌 Os arquivos das aulas **não são criados aqui**, pois já vieram no material fornecido pelo professor.

---

# 12. Conferir a estrutura construída

Execute:

```powershell
tree /F
```

A opção `/F` faz com que `tree` apresente também os **arquivos**.

A estrutura deverá se aproximar de:

```text
engconvert/
│
├── assets/
│
├── aulas/
│   ├── aula-00-roteiro-terminal.md
│   ├── aula-01.0-vscode-estrutura-ambiente.md
│   ├── aula-01.1-roteiro-pratico.md
│   ├── aula-02.0-gui-roadmap-sprints.md
│   ├── aula-02.1-roteiro-pratico.md
│   ├── aula-03.0-widgets-eventos.md
│   ├── aula-03.1-roteiro-pratico.md
│   ├── aula-04.0-primeiro-conversor.md
│   ├── aula-04.1-roteiro-pratico.md
│   └── ...
│
├── docs/
│   ├── roadmap.md
│   ├── git-github.md
│   ├── arquitetura.md
│   └── sprints/
│       ├── sprint-00-ambiente.md
│       ├── sprint-01-interface.md
│       ├── sprint-02-widgets.md
│       └── sprint-03-conversor.md
│
├── src/
│   └── engconvert/
│       └── __init__.py
│
├── tests/
│   └── README.md
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

Observe que algumas estruturas profissionais apresentadas no início ainda não possuem conteúdo.

Isso é intencional.

---

# 13. Verificar o Python

Execute:

```powershell
python --version
```

No Windows, também podemos verificar o Python Launcher:

```powershell
py --version
```

Para consultar as instalações reconhecidas pelo Launcher:

```powershell
py -0p
```

> 💡 Esse comando é especialmente útil quando existem várias versões do Python instaladas.

### 🐍 E se eu entrar no Python REPL sem querer?

Se executarmos apenas:

```powershell
python
```

sem informar um arquivo, o Python poderá abrir seu modo interativo, chamado **REPL**. O terminal passa a apresentar:

```text
>>>
```

Nesse momento, estamos dentro do interpretador Python, e não no PowerShell.

Para sair do REPL no Windows, digite:

```python
exit()
```

ou utilize:

```text
Ctrl + Z
depois
Enter
```

O prompt normal deverá reaparecer:

```text
PS C:\Projetos\engconvert>
```

> 🎯 **Regra prática:** se você esperava usar comandos como `cd`, `dir` ou `python main.py`, mas está vendo `>>>`, saia primeiro do REPL.

Neste momento, não é necessário decorar todos esses comandos.

---

# 14. Criar o ambiente virtual

Na raiz do projeto:

```powershell
python -m venv .venv
```

Caso seja necessário selecionar explicitamente uma versão instalada, por exemplo:

```powershell
py -3.12 -m venv .venv
```

Agora teremos também:

```text
engconvert/
└── .venv/
```

> ⚠️ A pasta `.venv/` pertence ao ambiente local do projeto. Posteriormente veremos por que ela **não deverá ser versionada pelo Git**.

---

# 15. Ativar a `.venv`

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

O terminal deverá apresentar algo semelhante a:

```text
(.venv) PS C:\Projetos\engconvert>
```

Confirme:

```powershell
python --version
```

Para verificar exatamente qual interpretador está sendo utilizado:

```powershell
python -c "import sys; print(sys.executable)"
```

O resultado deverá apontar para algo semelhante a:

```text
C:\Projetos\engconvert\.venv\Scripts\python.exe
```

### ⚠️ E se o PowerShell impedir a ativação?

Em alguns computadores, o PowerShell pode impedir a execução do `Activate.ps1` por causa da **política de execução** (_Execution Policy_) do Windows.

Pode aparecer uma mensagem informando que a execução de scripts está desabilitada.

Em um **computador pessoal**, uma solução comum é permitir scripts locais para o usuário atual:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

O comando não mostra mensagem de sucesso, ele apenas executa e retorna ao prompt.

Se o PowerShell solicitar confirmação, confirme a alteração. Depois, **feche e abra** novamente o terminal do VSCode e tente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Nesse comando:

```text
CurrentUser
    ↓
alteração somente para o usuário atual

RemoteSigned
    ↓
permite scripts locais e mantém restrições
para scripts obtidos da Internet
```

> ⚠️ **Computadores institucionais ou de laboratório:** não altere políticas de segurança sem autorização. A configuração pode ser administrada pela instituição.

Se a alteração não for permitida, utilize o **Prompt de Comando (`cmd`)**:

```bat
.venv\Scripts\activate.bat
```

O objetivo continua sendo o mesmo:

```text
ativar .venv
      ↓
usar o Python específico do projeto
```

---

## 15.1. Selecionar o interpretador Python no VSCode

A ativação da `.venv` no terminal e a seleção do **interpretador do VSCode** são configurações relacionadas, mas diferentes. O terminal pode estar usando um Python enquanto o botão de execução utiliza outro.

1. Com a pasta `C:\Projetos\engconvert` aberta no VSCode, pressione **Ctrl + Shift + P** para abrir a **Paleta de Comandos**.
2. Pesquise **`Python: Select Interpreter`** (ou **Python: Selecionar Interpretador**) e pressione **Enter**.
3. Escolha o interpretador localizado em **`C:\Projetos\engconvert\.venv\Scripts\python.exe`**. A identificação pode aparecer como `Python 3.12.x ('.venv')` ou de outra forma, conforme a versão e a extensão instalada.
4. Abra o terminal integrado em **Terminal → New Terminal** ou use **Ctrl + `** (a tecla de acento grave, normalmente próxima de Esc).
5. Confira os comandos:

```powershell
python --version
python -c "import sys; print(sys.executable)"
```

O caminho exibido pelo segundo comando deve terminar em `engconvert\.venv\Scripts\python.exe`. **Não confie apenas no texto `(.venv)` do prompt:** ele ajuda a identificar a ativação, mas o caminho de `sys.executable` é uma verificação mais precisa.

> **Regra didática:** um projeto → um ambiente virtual próprio → o interpretador correspondente selecionado no VSCode.

## 15.2. Configurar o interpretador padrão do projeto

Para que o VSCode encontre mais facilmente o Python correto ao reabrir o projeto, crie a pasta `.vscode` na raiz, caso ainda não exista:

```powershell
New-Item -ItemType Directory -Force .vscode
```

Dentro dela, crie ou abra o arquivo **`.vscode/settings.json`** e utilize:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
  "python.terminal.activateEnvironment": true
}
```

**Importante:** o arquivo `settings.json` configura o VSCode, mas não instala o Python nem cria o ambiente virtual. Se o editor continuar utilizando outro interpretador, abra **Python: Select Interpreter (Python: Selecionar Interpretador)** e selecione o Python localizado em `.venv\Scripts\python.exe`.

> Se `.vscode/settings.json` já existir, **não substitua indiscriminadamente** seu conteúdo: acrescente as duas propriedades ao objeto JSON existente, respeitando vírgulas e chaves.

## 15.3. O botão Run não funciona ou usa outro Python?

Quando `python main.py` funciona no terminal, mas a execução pelo botão **▶** falha, o VSCode pode estar utilizando um interpretador diferente. Também pode existir outro problema no código; por isso, confira primeiro o Python selecionado na Seção 15.1.

Com o arquivo `main.py` aberto, clique na **seta para baixo (⌄), ao lado do botão ▶**, localizada no canto superior direito do editor do VSCode. Essa seta abre o menu com as opções disponíveis. **Escolha preferencialmente a primeira opção: Executar Arquivo do Python.**

As opções exibidas no menu podem incluir:

1. **Run Python File (Executar Arquivo do Python):** opção recomendada para executar `main.py` com o interpretador selecionado na extensão Python do VSCode.
2. **Run Python File in Dedicated Terminal (Executar Arquivo Python no Terminal Dedicado):** executa o programa em um terminal dedicado ao Python; também pode ser utilizada no EngConvert.
3. **Run Current File in Interactive Window (Executar Arquivo Atual na Janela Interativa):** executa o código na janela interativa, geralmente associada ao Jupyter. Não é necessária para nossa aplicação gráfica com CustomTkinter.
4. **Run as Task (Executar como Tarefa):** permite executar tarefas configuradas no VSCode, por exemplo, por meio do arquivo `.vscode/tasks.json`. Não é necessária nesta etapa.
5. **Python Debugger: Debug Python File (Depurar Arquivo Python):** inicia a depuração do arquivo para investigar erros e acompanhar sua execução.
6. **Python Debugger: Debug using launch.json (Depurar usando launch.json):** inicia a depuração conforme uma configuração definida no arquivo `.vscode/launch.json`.

> 📌 **Para esta aula:** utilize **Executar Arquivo do Python**, a primeira opção. As opções de janela interativa, tarefas e depuração serão úteis em outros contextos, mas não são necessárias para iniciar o EngConvert.

### 🔎 Outros comandos que não aparecem necessariamente nesse menu

- **Run Without Debugging (Executar sem Depuração):** normalmente acessível pelo menu **Executar → Executar sem Depuração** ou pelo atalho **Ctrl + F5**. Não é uma das opções mostradas na captura de tela do menu da seta.
- **Run Code (Executar Código):** comando da extensão *Code Runner*, quando instalada. Pode utilizar um interpretador diferente do selecionado na extensão Python; por isso, evite essa opção nesta aula.

> ⚠️ **Atenção:** o símbolo **▶** pode ser utilizado por diferentes comandos e extensões. Para abrir a lista mostrada, clique especificamente **na seta para baixo (⌄), ao lado do botão ▶**.

Para verificar o interpretador utilizado pelo terminal, execute:

```powershell
python -c "import sys; print(sys.executable)"
```

Se houver dúvida, utilize o caminho explícito apresentado na próxima seção. **`python main.py` só utiliza a `.venv` quando o comando `python` do terminal aponta para ela**; digitar `python` não força automaticamente o uso desse ambiente.

## 15.4. Executar sem ativar a `.venv` — alternativa útil

Mesmo que o prompt mostre apenas `PS C:\Projetos\engconvert>`, é possível chamar diretamente o Python do ambiente virtual, sem executar `Activate.ps1`:

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe main.py
```

Isso também ajuda em computadores de laboratório nos quais a política de execução impede a ativação por script. **O arquivo `main.py` receberá seu primeiro conteúdo na Seção 19; volte a este comando depois de criá-lo.**

Outra opção, **após concluir a Seção 19**, é criar na raiz do projeto um arquivo **`run.ps1`** com o seguinte conteúdo completo:

```powershell
# Executa o EngConvert usando o Python da .venv do próprio projeto.
$raiz = Split-Path -Parent $MyInvocation.MyCommand.Path
& (Join-Path $raiz '.venv\Scripts\python.exe') (Join-Path $raiz 'main.py')
```

Para executar, estando na raiz do projeto:

```powershell
.\run.ps1
```

O script utiliza caminhos relativos à sua própria localização, mesmo quando o terminal estiver em outra pasta. **Importante:** `run.ps1` também está sujeito à política de execução do PowerShell; portanto, não é uma solução para contornar bloqueios institucionais. Nesses casos, prefira o comando direto `.\.venv\Scripts\python.exe main.py` (sem o espaço inicial/final) ou solicite orientação ao responsável pelo laboratório.

---

# 16. Verificando e atualizando o `pip`

Antes de instalar bibliotecas no ambiente virtual, vamos verificar se o `pip` está disponível.

Com a `.venv` ativada, execute:

```powershell
python -m pip --version
```

Uma resposta semelhante a esta deverá aparecer:

```text
pip 25.x from C:\Projetos\engconvert\.venv\Lib\site-packages\pip
```

Observe que o caminho deve apontar para:

```text
engconvert\.venv
```

Isso indica que estamos utilizando o `pip` associado ao **Python do ambiente virtual do projeto**.

## 16.1 Atualizando o `pip`

Podemos atualizar o `pip` com:

```powershell
python -m pip install --upgrade pip
```

Depois, podemos verificar novamente:

```powershell
python -m pip --version
```

> 💡 Utilizamos `python -m pip` porque dessa forma o módulo `pip` é executado pelo mesmo interpretador chamado pelo comando `python`. Com a `.venv` ativa, isso ajuda a garantir que estamos trabalhando no ambiente virtual do projeto.

O fluxo é:

```text
python
   ↓
Python da .venv
   ↓
-m pip
   ↓
pip da .venv
   ↓
instalação das bibliotecas
```

> 📌 **Importante:** verificar o `pip` faz parte da conferência do ambiente. A atualização é recomendável, mas não é uma condição obrigatória para instalar o CustomTkinter.

Agora o ambiente está preparado para instalar a primeira biblioteca externa utilizada pelo EngConvert.

---

# 17. Instalar o CustomTkinter

Com a `.venv` ativa:

```powershell
python -m pip install customtkinter
```

Verifique:

```powershell
python -m pip show customtkinter
```

> 💡 Utilizamos `python -m pip` para executar o `pip` através do mesmo interpretador chamado pelo comando `python`. Esse conceito será detalhado posteriormente.

---

# 18. Registrar as dependências

Execute:

```powershell
python -m pip freeze > requirements.txt
```

Confira:

```powershell
Get-Content requirements.txt
```

O arquivo `requirements.txt` passa a registrar as dependências instaladas no ambiente.

---

# 19. Criar o primeiro programa

Abra:

```text
main.py
```

e digite:

```python
print("EngConvert iniciado com sucesso!")
```

Salve o arquivo.

---

# 20. Executar o EngConvert

No terminal:

```powershell
python main.py
```

Resultado esperado:

```text
EngConvert iniciado com sucesso!
```

Temos agora o primeiro programa executável do projeto.

---

# 21. Marco da Aula 00

Ao final deste roteiro devemos ter:

- [ ] material das aulas descompactado;
- [ ] pasta `engconvert` em `C:\Projetos`;
- [ ] projeto aberto no VSCode;
- [ ] pasta `assets/`;
- [ ] estrutura `docs/`;
- [ ] Roadmap e Sprints preparados;
- [ ] estrutura inicial `src/engconvert/`;
- [ ] pasta `tests/` preparada;
- [ ] `main.py`;
- [ ] `README.md`;
- [ ] `requirements.txt`;
- [ ] `.gitignore`;
- [ ] `.venv` criada;
- [ ] `.venv` ativada;
- [ ] interpretador da `.venv` selecionado no VSCode;
- [ ] `.vscode/settings.json` configurado;
- [ ] alternativa de execução direta compreendida;
- [ ] `pip` verificado;
- [ ] `pip` atualizado, quando necessário;
- [ ] CustomTkinter instalado;
- [ ] dependências registradas;
- [ ] primeiro programa executado.

---

# 🧭 Visão geral da Aula 00

```text
engconvert.zip
      ↓
descompactar
      ↓
C:\Projetos\engconvert
      ↓
aulas/
      ↓
abrir no VSCode
      ↓
code .
      ↓
criar a estrutura inicial
      ↓
assets/ docs/ src/ tests/
      ↓
criar arquivos do projeto
      ↓
main.py + README.md + requirements.txt + .gitignore
      ↓
python -m venv .venv
      ↓
ativar .venv e selecionar interpretador no VSCode
      ↓
python -m pip --version
      ↓
python -m pip install --upgrade pip
      ↓
python -m pip install customtkinter
      ↓
registrar dependências
      ↓
python main.py
      ↓
EngConvert iniciado com sucesso!
```

---

## 🚦 O que ainda não criamos — e por quê?

Ao observar a visão profissional apresentada no início da aula, você pode perceber que algumas estruturas futuras ainda não existem.

Isso é intencional.

```text
visão do projeto
      ↓
sabemos para onde queremos evoluir

implementação atual
      ↓
criamos somente o que já possui uma função

novas necessidades
      ↓
novas pastas, módulos e testes aparecem
```

Nas próximas aulas, o EngConvert crescerá gradualmente.

Quando o `main.py` começar a acumular responsabilidades, surgirá a necessidade de modularização.

Quando tivermos comportamentos que precisam ser verificados automaticamente, criaremos os primeiros testes.

> 💡 Dessa forma, a estrutura do software não é decorada: ela é **compreendida a partir das necessidades do próprio projeto**.

---

> 🎯 **Ideia-chave:** nesta Aula 00 preparamos o ambiente e começamos a construir o EngConvert a partir do material didático fornecido. A partir da Aula 01, compreenderemos com mais profundidade **por que cada pasta, arquivo, comando e ferramenta existe**.

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
