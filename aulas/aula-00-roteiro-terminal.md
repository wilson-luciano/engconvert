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
│   ├── aula-01.1-roteiro-pratico.md
    ├── aula-02.0-roadmap-sprint-gui.md
    ├── aula-03.0-widgets-eventos.md
    ├── aula-04.0-primeiro-conversor.md
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
            ├── aula-02.0-roadmap-sprint-gui.md
            ├── aula-03.0-widgets-eventos.md
            ├── aula-04.0-primeiro-conversor.md
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

- **`pwd`** (*Print Working Directory*) → mostra o diretório de trabalho atual.
- **`cd`** (*Change Directory*) → permite entrar ou mudar de pasta.
- **`dir` / `ls`** → mostram os arquivos e pastas existentes no diretório atual.
- **`mkdir`** (*Make Directory*) → cria uma nova pasta.

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
│   ├── aula-02.0-roadmap-sprint-gui.md
│   ├── aula-03.0-widgets-eventos.md
│   ├── aula-04.0-primeiro-conversor.md
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

Em alguns computadores, o PowerShell pode impedir a execução do script por causa da política de execução do Windows.

Especialmente em computadores institucionais, **não altere configurações de segurança sem autorização**.

Uma alternativa é utilizar o Prompt de Comando (`cmd`) e executar:

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

# 16. Instalar o CustomTkinter

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

# 17. Registrar as dependências

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

# 18. Criar o primeiro programa

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

# 19. Executar o EngConvert

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

# 20. Marco da Aula 00

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
ativar .venv
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
