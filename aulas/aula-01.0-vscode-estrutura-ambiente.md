# Aula 01.0 — VSCode, Estrutura e Ambiente de Desenvolvimento

## Do Script à Primeira Interface Gráfica do EngConvert

## VSCode, Markdown, terminal e organização inicial do EngConvert

> **Projeto-guia:** EngConvert — Engineering Unit Converter

> 📚 **Organização do material:** esta é a **Aula 01.0**, com o conteúdo completo e aprofundado. A **Aula 01.1** é o roteiro prático correspondente, contendo somente a sequência de implementação necessária para esta etapa.

> **Objetivo desta etapa:** compreender o ambiente preparado na Aula 00, o VSCode, o Markdown, o Python e a organização do EngConvert antes de avançarmos para a interface gráfica.

---

> 📌 **Continuidade com a Aula 00:** esta aula parte do projeto que já foi preparado anteriormente. Portanto, vários comandos aparecerão novamente, mas agora com foco em **compreender seu significado**, e não em repetir desnecessariamente a configuração.

## 🎯 Objetivos da aula

Na **Aula 00**, executamos um roteiro prático: recebemos a estrutura didática, preparamos o projeto, criamos a `.venv`, instalamos a primeira dependência e executamos o `main.py`.

Agora vamos compreender **por que cada uma dessas partes existe e como elas se relacionam em um projeto de software**.

Ao final desta aula, o aluno deverá ser capaz de:

- compreender a diferença entre **script** e **projeto**;
- reconhecer as principais áreas do **VSCode**;
- compreender por que abrimos uma **pasta de projeto**, e não apenas um arquivo isolado;
- utilizar e interpretar o **terminal integrado**;
- compreender o que é **Markdown** e visualizar arquivos `.md`;
- alternar entre a edição Markdown e o **Markdown Preview**;
- compreender a função de `README.md`, `requirements.txt` e `.gitignore`;
- distinguir o terminal do **Python REPL**;
- compreender a diferença entre `python` e `py` no Windows;
- compreender o papel de um **ambiente virtual**;
- verificar se a `.venv` está ativa e qual interpretador está sendo utilizado;
- selecionar o interpretador Python correto no VSCode;
- executar o `main.py`.

> 🎯 **Aula 00 = fazer. Aula 01 = compreender o que fizemos.**

---

# 1. Do arquivo isolado para um projeto

Em exercícios pequenos, é comum trabalhar com um único arquivo. Até agora, muitos dos programas desenvolvidos na disciplina poderiam ser representados simplesmente por:

```text
programa.py
```

No desenvolvimento de uma aplicação, passamos a trabalhar com um **projeto de software**, formado por código, documentação, dependências e outros recursos.

Por isso, desde o início utilizaremos uma estrutura organizada de pastas e arquivos, que evoluirá gradualmente durante várias aulas e Sprints.

Na **Aula 00**, construímos uma estrutura inicial semelhante a:

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
│   └── aula-04.1-roteiro-pratico.md
│
├── docs/
│   ├── roadmap.md
│   ├── sprints/
│   │   ├── sprint-00-ambiente.md
│   │   ├── sprint-01-interface.md
│   │   ├── sprint-02-widgets.md
│   │   └── sprint-03-conversor.md
│   ├── git-github.md
│   └── arquitetura.md
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

Essa é a **estrutura atual** do projeto.

No futuro, conforme surgirem necessidades reais, algumas partes poderão evoluir:

```text
assets/
├── icons/
├── images/
└── screenshots/

src/engconvert/
├── __init__.py
├── converters/
├── gui/
├── data/
└── utils/

tests/
├── test_pressure.py
├── test_temperature.py
└── ...
```

> 💡 **Importante:** a arquitetura futura pode ser apresentada antecipadamente para compreendermos a direção do projeto, mas suas pastas e arquivos serão criados somente quando tiverem uma função concreta.

```text
ESTRUTURA ATUAL
      ↓
o que já precisamos

ESTRUTURA FUTURA
      ↓
para onde o projeto poderá evoluir
```

---

# 🏗️ O que essa estrutura representa?

Um projeto profissional não é constituído apenas pelo código-fonte.

Ele normalmente envolve diferentes responsabilidades:

```text
PROJETO DE SOFTWARE
│
├── Código
├── Recursos
├── Testes
├── Documentação
├── Planejamento
├── Dependências
└── Controle de versão
```

Por isso, organizamos o projeto em diferentes pastas e arquivos.

---

# 📦 `assets/` — Recursos da aplicação

A palavra:

```text
assets
```

pode ser entendida, nesse contexto, como **recursos utilizados pela aplicação**.

São arquivos necessários à interface ou apresentação do programa, mas que **não são código Python**.

Quando esses recursos começarem a ser utilizados, uma possível organização para o EngConvert será:

```text
assets/
│
├── icons/
│   ├── app.ico
│   ├── copy.png
│   ├── swap.png
│   └── favorite.png
│
├── images/
│   ├── logo.png
│   └── engconvert.png
│
└── screenshots/
    ├── interface-principal.png
    └── modo-escuro.png
```

### `assets/icons/`

Armazena pequenos elementos gráficos utilizados pela interface.

Por exemplo:

```text
icons/
├── app.ico
├── copy.png
├── swap.png
└── favorite.png
```

Futuramente esses ícones poderão representar:

```text
📋 copiar resultado
⇄  trocar unidades
★  adicionar favorito
⚙  configurações
```

---

### `assets/images/`

Armazena imagens maiores utilizadas pelo projeto.

Por exemplo:

```text
images/
├── logo.png
└── engconvert.png
```

Podem ser utilizadas em:

- tela inicial;
- cabeçalho;
- documentação;
- identidade visual da aplicação.

---

### `assets/screenshots/`

Pode armazenar capturas de tela do próprio programa:

```text
screenshots/
├── interface-principal.png
├── modo-claro.png
└── modo-escuro.png
```

Essas imagens podem posteriormente ser utilizadas no:

```text
README.md
```

ou na documentação do projeto.

Assim:

```text
assets/
│
├── icons/          → ícones da interface
├── images/         → imagens e logotipos
└── screenshots/    → imagens demonstrativas do software
```

> 📌 Na estrutura atual da Aula 01 temos apenas `assets/`. As subpastas abaixo representam uma **possível evolução futura**. A estrutura interna pode variar de projeto para projeto e deve ser criada somente quando houver recursos reais para organizar.

---

# 📚 `docs/` — Documentação técnica e planejamento

A pasta:

```text
docs/
```

concentra documentação mais detalhada do projeto.

No EngConvert, poderemos ter:

```text
docs/
│
├── roadmap.md
├── sprints/
├── git-github.md
└── arquitetura.md
```

Cada documento possui uma finalidade diferente.

---

# 🗺️ `roadmap.md` — Para onde o projeto vai?

O **Roadmap** apresenta uma visão geral da evolução planejada do EngConvert.

Ele responde principalmente:

> **Onde estamos e para onde queremos levar o projeto?**

Por exemplo:

```text
ROADMAP — ENGCONVERT

Etapa 1
↓
Ambiente de desenvolvimento

Etapa 2
↓
Primeira GUI

Etapa 3
↓
Widgets e eventos

Etapa 4
↓
Primeira conversão

Etapa 5
↓
Múltiplas grandezas

Etapa 6
↓
Arquitetura modular

Etapa 7
↓
Testes

Etapa 8
↓
Interface completa

Etapa 9
↓
Empacotamento

Etapa 10
↓
EngConvert.exe
```

O Roadmap apresenta uma visão **mais ampla** do desenvolvimento.

Podemos pensar nele como:

```text
HOJE
 │
 ├── GUI
 │
 ├── conversões
 │
 ├── testes
 │
 ├── recursos avançados
 │
 └── distribuição
                         → FUTURO
```

---

# 🏃 `sprints/` — Como avançaremos passo a passo?

Dentro de `docs/`, podemos possuir:

```text
sprints/
```

O projeto será desenvolvido por meio de pequenas etapas chamadas **Sprints**.

Uma Sprint representa um **ciclo curto de desenvolvimento com um objetivo definido**.

Por exemplo:

```text
docs/
└── sprints/
    ├── sprint-00-ambiente.md
    ├── sprint-01-interface.md
    ├── sprint-02-widgets.md
    └── sprint-03-conversor.md
```

Cada arquivo pode registrar:

```text
SPRINT
│
├── objetivo
├── tarefas
├── funcionalidades
├── critérios de conclusão
└── resultado alcançado
```

Exemplo:

```markdown
# Sprint 03 — Primeiro Conversor

## Objetivo

Implementar a primeira conversão funcional do EngConvert.

## Tarefas

- criar entrada de valor;
- converter bar para kPa;
- apresentar resultado;
- tratar entrada inválida.

## Critério de conclusão

O usuário deve conseguir inserir uma pressão em bar
e obter corretamente o resultado em kPa.
```

---

# 🗺️ Roadmap × Sprint

Embora estejam relacionados, **Roadmap e Sprint não são a mesma coisa**.

```text
ROADMAP
│
│  visão geral do projeto
│
├── Etapa 1
├── Etapa 2
├── Etapa 3
├── Etapa 4
└── Etapa 5
        │
        ▼
      FUTURO
```

Já uma Sprint possui um objetivo mais específico:

```text
SPRINT
│
├── objetivo
├── tarefas
├── desenvolvimento
├── testes
└── entrega
```

Podemos resumir:

|           | Roadmap           | Sprint                 |
| --------- | ----------------- | ---------------------- |
| Visão     | Ampla             | Específica             |
| Horizonte | Médio/longo prazo | Curto prazo            |
| Pergunta  | Para onde vamos?  | O que faremos agora?   |
| Conteúdo  | Etapas do projeto | Tarefas da etapa       |
| Resultado | Direção           | Incremento do software |

> 🎯 **Ideia-chave:** o **Roadmap mostra a estrada**; as **Sprints representam os trechos que percorremos para chegar ao destino**.

---

# 📄 Outros documentos em `docs/`

Além do Roadmap e das Sprints, podemos armazenar documentação técnica.

```text
docs/
├── roadmap.md
├── sprints/
├── git-github.md
└── arquitetura.md
```

### `git-github.md`

Pode registrar:

- comandos Git;
- criação do repositório;
- commits;
- branches;
- conexão com GitHub;
- `push`;
- `pull`;
- boas práticas de versionamento.

### `arquitetura.md`

Poderá documentar futuramente:

- organização dos módulos;
- responsabilidades das partes do sistema;
- fluxo de dados;
- decisões de arquitetura;
- evolução estrutural do EngConvert.

---

# 💻 `src/` — Código-fonte da aplicação

`src` é uma abreviação de:

```text
source
```

ou seja:

```text
código-fonte
```

No EngConvert:

```text
src/
└── engconvert/
```

A primeira pasta:

```text
engconvert/
```

é a **raiz do projeto**.

Já:

```text
src/engconvert/
```

representará o **pacote Python da aplicação**.

```text
engconvert/
     ↓
PROJETO

src/engconvert/
     ↓
PACOTE PYTHON
```

---

# 🧩 Estrutura futura de `src/engconvert/`

Inicialmente teremos apenas:

```text
src/
└── engconvert/
    └── __init__.py
```

À medida que o programa crescer, poderemos evoluir para algo semelhante a:

```text
src/
└── engconvert/
    │
    ├── __init__.py
    │
    ├── converters/
    │   ├── pressure.py
    │   ├── temperature.py
    │   ├── length.py
    │   └── mass.py
    │
    ├── gui/
    │   ├── main_window.py
    │   ├── sidebar.py
    │   └── result_card.py
    │
    ├── data/
    │   └── units.py
    │
    └── utils/
        └── validators.py
```

Essa estrutura **não será criada toda agora**.

Ela representa uma possível evolução profissional do projeto.

---

## 🔄 `converters/`

Responsável pela **lógica das conversões de unidades**.

```text
converters/
├── pressure.py
├── temperature.py
├── length.py
└── mass.py
```

Exemplo:

```text
pressure.py
     ↓
bar
Pa
kPa
MPa
psi
atm
```

A lógica matemática fica separada da interface gráfica.

---

## 🖥️ `gui/`

Responsável pela **interface gráfica**.

```text
gui/
├── main_window.py
├── sidebar.py
└── result_card.py
```

Poderá conter:

```text
gui/
│
├── janela principal
├── menu lateral
├── campos de entrada
├── botões
└── apresentação dos resultados
```

Assim:

```text
GUI
↓
interage com o usuário

converters
↓
realiza os cálculos
```

---

## 🗃️ `data/`

Pode armazenar dados estruturados utilizados pelo programa.

Por exemplo:

```text
data/
└── units.py
```

Esse arquivo poderá conter informações sobre:

```text
Pressão
├── Pa
├── kPa
├── MPa
├── bar
├── psi
└── atm
```

ou outras grandezas:

```text
Comprimento
Temperatura
Massa
Área
Volume
Energia
Potência
```

---

## 🔧 `utils/`

`utils` vem de:

```text
utilities
```

Pode reunir pequenas funções auxiliares reutilizadas por diferentes partes do programa.

Por exemplo:

```text
utils/
└── validators.py
```

que futuramente poderá verificar:

- entrada vazia;
- número inválido;
- formato numérico;
- limites permitidos.

> 📌 Não devemos utilizar `utils/` como uma pasta para colocar qualquer código sem organização. Ela deve conter apenas funções auxiliares com responsabilidade clara.

---

# 🐍 `__init__.py`

Dentro do pacote:

```text
src/engconvert/
```

encontramos:

```text
__init__.py
```

Ele está relacionado à organização do diretório como um **pacote Python**.

Inicialmente poderá permanecer vazio.

```text
src/
└── engconvert/
    └── __init__.py
          ↓
      pacote Python
```

Módulos, pacotes e `import` serão estudados com mais detalhes quando começarmos a modularizar o EngConvert.

---

# 🧪 `tests/` — Testes automatizados

A pasta:

```text
tests/
```

será destinada aos testes do programa.

Uma possível evolução:

```text
tests/
├── test_pressure.py
├── test_temperature.py
├── test_length.py
└── test_validators.py
```

Imagine que programamos:

```text
1 bar = 100 kPa
```

Um teste automatizado poderá verificar se essa relação continua correta após futuras alterações.

```text
     Alteramos o código
             ↓
    Executamos os testes
             ↓
Resultados continuam corretos?
             │
         ┌───┴───┐
        SIM     NÃO
         │       │
         ↓       ↓
    continuar  corrigir
```

Os testes ajudam a detectar **regressões**, isto é, situações em que uma nova alteração quebra uma funcionalidade que anteriormente funcionava.

---

# ▶️ `main.py` — Ponto de entrada

Nesta fase, iniciaremos o programa com:

```powershell
python main.py
```

Portanto:

```text
main.py
   ↓
inicia o EngConvert
```

Inicialmente teremos boa parte do código nesse arquivo.

Depois:

```text
     main.py
        ↓
   inicialização
        ↓
  src/engconvert/
        ↓
lógica da aplicação
```

> 💡 Começaremos simples e modularizaremos quando a complexidade justificar essa mudança.

---

# 📖 `README.md` — Porta de entrada do projeto

O:

```text
README.md
```

apresenta o projeto.

Normalmente contém:

```text
README.md
│
├── nome
├── descrição
├── objetivo
├── tecnologias
├── instalação
├── execução
├── exemplos
├── documentação
└── autoria
```

Quando o projeto estiver no GitHub, esse documento será apresentado na página principal do repositório.

---

# 📋 `requirements.txt` — Dependências

Registra bibliotecas externas necessárias ao projeto.

Por exemplo:

```text
customtkinter
```

Posteriormente:

```powershell
python -m pip install -r requirements.txt
```

permitirá instalar as dependências registradas.

```text
requirements.txt
       ↓
  dependências
       ↓
      pip
       ↓
ambiente do projeto
```

---

# 🚫 `.gitignore` — Arquivos que não serão versionados

O:

```text
.gitignore
```

informa ao Git quais arquivos ou pastas devem ser ignorados.

Por exemplo:

```gitignore
.venv/
__pycache__/
*.pyc
```

Assim:

```text
Projeto local
│
├── código              → Git
├── documentação        → Git
├── testes              → Git
│
└── .venv               → NÃO
```

Estudaremos esse comportamento quando introduzirmos **Git e GitHub**.

---

# 🎓 `aulas/` — Material didático

Finalmente:

```text
aulas/
```

é uma particularidade do nosso projeto.

Ela existe porque o EngConvert também está sendo utilizado como **projeto didático da disciplina**.

```text
aulas/
├── aula-00-roteiro-terminal.md
├── aula-01.0-vscode-estrutura-ambiente.md
├── aula-01.1-roteiro-pratico.md
├── aula-02.0-gui-roadmap-sprints.md
├── aula-02.1-roteiro-pratico.md
├── aula-03.0-widgets-eventos.md
├── aula-03.1-roteiro-pratico.md
├── aula-04.0-primeiro-conversor.md
└── aula-04.1-roteiro-pratico.md
```

Em uma **aplicação profissional** convencional, essa pasta normalmente **não existiria**.

Aqui temos:

```text
EngConvert
│
├── SOFTWARE
│   ├── src/
│   ├── tests/
│   ├── assets/
│   └── ...
│
└── MATERIAL DIDÁTICO
    └── aulas/
```

---

# 🏭 Estrutura profissional do EngConvert

Se retirarmos a pasta didática `aulas/`, podemos visualizar melhor a organização relacionada ao desenvolvimento do software:

```text
engconvert/
│
├── assets/
│   ├── icons/
│   ├── images/
│   └── screenshots/
│
├── docs/
│   ├── roadmap.md
│   ├── sprints/
│   ├── git-github.md
│   └── arquitetura.md
│
├── src/
│   └── engconvert/
│       ├── __init__.py
│       ├── converters/
│       ├── gui/
│       ├── data/
│       └── utils/
│
├── tests/
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

Podemos resumir as responsabilidades:

| Elemento              | Responsabilidade                       |
| --------------------- | -------------------------------------- |
| `assets/`             | Recursos visuais e arquivos auxiliares |
| `assets/icons/`       | Ícones utilizados pela aplicação       |
| `assets/images/`      | Imagens e identidade visual            |
| `assets/screenshots/` | Capturas de tela para documentação     |
| `docs/`               | Documentação técnica                   |
| `docs/roadmap.md`     | Visão da evolução do projeto           |
| `docs/sprints/`       | Planejamento e registro das Sprints    |
| `docs/git-github.md`  | Documentação de versionamento          |
| `docs/arquitetura.md` | Decisões de arquitetura                |
| `src/`                | Código-fonte                           |
| `src/engconvert/`     | Pacote Python principal                |
| `converters/`         | Lógica das conversões                  |
| `gui/`                | Interface gráfica                      |
| `data/`               | Dados e unidades                       |
| `utils/`              | Funções auxiliares                     |
| `tests/`              | Testes automatizados                   |
| `.gitignore`          | Exclusões do Git                       |
| `main.py`             | Ponto inicial da aplicação             |
| `README.md`           | Apresentação do projeto                |
| `requirements.txt`    | Dependências Python                    |

---

# 🔄 Como essas partes participarão do desenvolvimento?

Agora podemos compreender como a estrutura do projeto poderá participar do processo de desenvolvimento à medida que o EngConvert evoluir:

```text
             ROADMAP
         docs/roadmap.md
                ↓
         define a direção
                ↓
             SPRINT
          docs/sprints/
                ↓
    define o próximo objetivo
                ↓
         DESENVOLVIMENTO
    main.py + src/engconvert/
                ↓
   implementa a funcionalidade
                ↓
             TESTES
             tests/
                ↓
    verificam o comportamento
                ↓
           DOCUMENTAÇÃO
        README.md + docs/
                ↓
       registra a evolução
                ↓
          VERSIONAMENTO
               Git
                ↓
 será introduzido quando tivermos
uma versão funcional para preservar
```

Neste momento, estamos concentrados em **ambiente, organização e desenvolvimento**.

O Git será estudado em uma aula posterior, quando já existir uma versão funcional do EngConvert que faça sentido registrar e preservar.

> 💡 Assim, o controle de versão aparecerá como resposta a uma necessidade real: **o programa já funciona; agora queremos registrar seu estado antes de continuar modificando-o.**

---

> 🎯 **Ideia-chave:** um projeto profissional não é apenas um conjunto de arquivos `.py`.
>
> Ele envolve **planejamento, código, recursos, documentação, testes, dependências e controle de versão**, cada um organizado de acordo com sua responsabilidade.

---

# 2. O que é o VSCode?

O **Visual Studio Code (VSCode)** é um editor de código extensível. Neste projeto ele será nosso ambiente central de desenvolvimento.

Usaremos no mesmo ambiente:

```text
VSCode
├── Editor de código
├── Explorer de arquivos
├── Terminal integrado
├── Markdown Preview
├── Extensões
└── Controle de versão Git
```

## 2.1 Áreas importantes

- **Explorer:** arquivos e pastas do projeto;
- **Editor:** código e documentação;
- **Terminal:** execução de comandos;
- **Source Control:** integração com Git;
- **Extensions:** instalação de extensões.

## 2.2 Extensões recomendadas para o VSCode

Para o EngConvert, utilizaremos inicialmente poucas extensões.  
A ideia é manter o ambiente simples e instalar novas ferramentas à medida que forem necessárias.

### Essenciais

- **Python** — Microsoft  
  Suporte ao desenvolvimento e execução de programas Python.
- **Pylance** — Microsoft  
  Autocomplete, análise do código, identificação de erros e informações sobre funções e variáveis.
- **Jupyter** — Microsoft  
  Útil para os notebooks da disciplina, embora não seja necessário para executar o EngConvert;

### Opcionais

- **Portuguese (Brazil) Language Pack for Visual Studio Code**  
  Permite utilizar a interface do VSCode em português.

> `Live Server` é útil para projetos HTML/CSS/JavaScript, mas **não é necessário para este projeto desktop**.

> 💡 **Importante:** outras extensões serão instaladas posteriormente, quando surgir uma necessidade real durante o desenvolvimento do EngConvert.

Por exemplo:

Git → GitHub → GitLens → testes → empacotamento

## 🎨 2.3 Temas e personalização visual do VSCode

Além das extensões utilizadas para programação, o VSCode permite personalizar sua aparência.

Essa configuração é **opcional** e não interfere no funcionamento dos programas. Cada aluno pode escolher o tema que considerar mais confortável para leitura e programação.

### 🌙 Temas de cores sugeridos

Algumas opções populares são:

- **One Dark Pro**
- **Night Owl**
- **Dracula Theme Official**

Esses temas modificam principalmente:

- cores do editor;
- fundo da área de código;
- cores da sintaxe;
- aparência de comentários, variáveis, funções e palavras reservadas.

> 💡 **Importante:** a escolha do tema é uma preferência pessoal.  
> Ela não altera o código nem interfere na execução do programa.

---

### 🎨 Como instalar um tema

Abra a área de extensões do VSCode:

```text
Ctrl + Shift + X
```

Pesquise pelo nome do tema desejado.

Por exemplo:

```text
One Dark Pro
```

Depois:

```text
Install
```

---

### 🖌️ Como selecionar um tema

Abra a **Paleta de Comandos**:

```text
Ctrl + Shift + P
```

Digite:

```text
Preferences: Color Theme
```

ou, dependendo do idioma da interface:

```text
Preferências: Tema de Cores
```

Selecione o tema desejado.

---

### 📁 Temas de ícones

Também podemos modificar os ícones apresentados no **Explorer** do VSCode.

Duas opções bastante utilizadas são:

- **Material Icon Theme**
- **vscode-icons**

Essas extensões facilitam a identificação visual de diferentes tipos de arquivos e pastas.

Por exemplo:

```text
📁 engconvert
│
├── 🐍 main.py
├── 📝 README.md
├── ⚙️ .gitignore
├── 📁 aulas
├── 📁 docs
├── 📁 src
└── 📁 tests
```

> 📌 **Tema de cores** e **tema de ícones** são recursos diferentes.

```text
Tema de cores
     ↓
aparência do editor e da sintaxe

Tema de ícones
     ↓
aparência dos arquivos e pastas
```

---

### 🖼️ Como selecionar o tema de ícones

Abra novamente:

```text
Ctrl + Shift + P
```

Digite:

```text
Preferences: File Icon Theme
```

ou:

```text
Preferências: Tema de Ícones de Arquivo
```

Escolha, por exemplo:

```text
Material Icon Theme
```

ou:

```text
vscode-icons
```

---

### 💡 Sugestão para este curso

Uma configuração possível para acompanhar as aulas é:

```text
Editor
├── Tema de cores → One Dark Pro, Night Owl ou Dracula
└── Tema de ícones → Material Icon Theme ou vscode-icons
```

A personalização é opcional. O mais importante é escolher uma configuração que proporcione **boa legibilidade e conforto durante a programação**.

---

# 3. Entendendo como o EngConvert foi aberto

Nossa organização recomendada é:

```text
C:\Projetos\engconvert
```

Na Aula 00, colocamos o projeto em:

```text
C:\Projetos\engconvert
```

e abrimos essa **pasta raiz** no VSCode.

Também é possível realizar essa operação pela interface:

```text
File → Open Folder...
```

selecionando:

```text
C:\Projetos\engconvert
```

Ou, estando nessa pasta pelo terminal:

```powershell
code .
```

O importante não é apenas abrir um arquivo `.py` isoladamente, mas abrir a **pasta do projeto**. Assim, o Explorer do VSCode apresenta sua estrutura completa.

Ao abrir o terminal integrado, o prompt deverá indicar aproximadamente:

```powershell
PS C:\Projetos\engconvert>
```

> 🎯 **Regra prática:** cada projeto deve possuir uma pasta raiz claramente identificada.

---

# 4. Terminal integrado

O terminal permite executar comandos sem sair do VSCode.

Abra por:

```text
Terminal → New Terminal
```

Atalhos úteis:

| Ação                             | Atalho             |
| -------------------------------- | ------------------ |
| Abrir/fechar terminal            | `` Ctrl + ` ``     |
| Paleta de comandos               | `Ctrl + Shift + P` |
| Interromper programa em execução | `Ctrl + C`         |
| Limpar o terminal PowerShell     | `cls`              |

## 4.1 Verificando a instalação do Python 🐍

Antes de iniciar o projeto, vamos verificar se o Python está instalado e acessível pelo **terminal integrado do VSCode**.

No Windows, estamos utilizando o **PowerShell**, identificado no terminal por algo semelhante a:

```text
PS C:\Projetos\engconvert>
```

Execute:

```powershell
python --version
```

Uma possível resposta será:

```text
Python 3.12.10
```

No Windows também podemos usar:

```powershell
py --version
```

Para listar as instalações do Python reconhecidas pelo **Python Launcher for Windows**, podemos utilizar:

```powershell
py -0p
```

Esse comando é especialmente útil quando existem **várias versões do Python instaladas** no computador.

---

### 🔎 Mas qual é a diferença entre `python` e `py`?

Apesar de os comandos:

```powershell
python --version
```

e:

```powershell
py --version
```

poderem apresentar resultados semelhantes, `python` e `py` **não representam exatamente a mesma coisa**.

O comando:

```text
python
```

executa um interpretador Python disponível no **ambiente atual**.

Já:

```text
py
```

chama o **Python Launcher for Windows**, uma ferramenta que ajuda a localizar e selecionar instalações do Python disponíveis no computador.

Podemos representar inicialmente essa diferença como:

```text
          python
            ↓
executa o Python disponível
     no ambiente atual
```

enquanto:

```text
            py
            ↓
Python Launcher for Windows
            ↓
  localiza/seleciona uma
   instalação do Python
```

> 💡 **Importante:** `py` não é um comando específico do PowerShell.  
> Ele pertence ao **Python Launcher for Windows**. O PowerShell é apenas o terminal no qual estamos executando esse comando.

Por isso, `py` também pode ser utilizado em outros terminais do Windows, como o **Prompt de Comando (CMD)**.

---

### 🔢 Quando existem várias versões do Python

Imagine que o computador possua:

```text
Python 3.11
Python 3.12
Python 3.13
```

Nesse caso, o Python Launcher é particularmente útil porque podemos solicitar uma versão específica.

Por exemplo:

```powershell
py -3.12 --version
```

Estamos dizendo:

```text
py
│
└── -3.12
       ↓
   utilize o Python 3.12
```

Também podemos executar um programa explicitamente com essa versão:

```powershell
py -3.12 main.py
```

---

### 📋 Consultando as instalações do Python

Como vimos anteriormente, podemos utilizar:

```powershell
py -0p
```

para visualizar as instalações reconhecidas pelo Python Launcher.

De forma simplificada:

```text
py -0p
   ↓
Python Launcher
   ↓
procura as instalações reconhecidas
   ↓
apresenta versões e caminhos
```

Esse recurso é útil para identificar **quais versões do Python estão disponíveis no computador** antes de escolhermos aquela que será utilizada no projeto.

---

### 🛠️ Usando o Launcher para criar a `.venv`

Se quisermos criar o ambiente virtual do EngConvert especificamente com o Python 3.12, podemos executar:

```powershell
py -3.12 -m venv .venv
```

Podemos interpretar o comando por partes:

```text
py
↓
Python Launcher

-3.12
↓
seleciona o Python 3.12

-m venv
↓
executa o módulo venv

.venv
↓
cria o ambiente virtual nessa pasta
```

Depois que a `.venv` estiver criada e ativada, utilizaremos normalmente:

```powershell
python
```

para executar o Python pertencente ao **ambiente virtual do projeto**.

Por exemplo:

```powershell
python --version
python main.py
python -m pip --version
```

---

> 🎯 **Ideia-chave:** no Windows, o `py` é especialmente útil para **localizar ou selecionar uma instalação do Python**. Depois que a `.venv` do projeto estiver criada e ativada, utilizaremos normalmente `python` para trabalhar dentro desse ambiente.

```text
Python instalado no Windows
            ↓
           py
            ↓
 seleciona a versão desejada
            ↓
      cria a .venv
            ↓
      ativa a .venv
            ↓
         python
            ↓
executa o Python do projeto
```

> 📌 **Neste momento, não é necessário decorar todos esses comandos.**  
> O importante é compreender por que podemos encontrar tanto `python` quanto `py` durante o desenvolvimento no Windows.

---

# 5. 📝 Visualizando arquivos Markdown no VSCode

Durante este projeto, parte do conteúdo teórico das aulas será escrita em arquivos **Markdown**, identificados pela extensão:

```text
.md
```

O Markdown é uma linguagem de marcação simples, muito utilizada para criar **documentação de projetos de software**, especialmente em plataformas como o **GitHub**.

Um dos arquivos Markdown mais conhecidos em projetos de software é:

```text
README.md
```

Neste projeto, o próprio material das aulas também será escrito em Markdown.

---

## 5.1 ✏️ Modo de edição

Ao abrir um arquivo `.md` no VSCode, inicialmente vemos o seu **código Markdown**.

Por exemplo:

```markdown
# EngConvert

## Introdução às Interfaces Gráficas — visão inicial

**GUI — Graphical User Interface**

GUI significa Interface Gráfica do Usuário.
```

Esse é o modo utilizado para **escrever e editar** o conteúdo.

---

## 5.2 👁️ Visualizando o Markdown formatado

O VSCode possui um visualizador de Markdown integrado chamado **Markdown Preview**.

Para visualizar o documento formatado, utilize:

```text
Ctrl + Shift + V
```

O conteúdo deixa de aparecer como código Markdown e passa a ser apresentado como um documento formatado.

Por exemplo:

```text
# Título

**texto em negrito**

- Item 1
- Item 2
```

será apresentado visualmente com **títulos, negrito, listas e demais elementos formatados**.

> 💡 **Importante:** o arquivo não foi convertido para outro formato.  
> Ele continua sendo um arquivo `.md`. O VSCode está apenas mostrando uma visualização formatada do seu conteúdo.

---

## 5.3 ↔️ Abrindo o Preview ao lado

Também podemos visualizar simultaneamente o **código Markdown** e o **documento formatado**.

Utilize:

```text
Ctrl + K
```

solte as teclas e, em seguida, pressione:

```text
V
```

Ou seja:

```text
Ctrl + K  →  V
```

O VSCode dividirá a área de trabalho:

```text
┌───────────────────────────┬───────────────────────────┐
│ MARKDOWN                  │ PREVIEW                   │
│                           │                           │
│ # O que é GUI?            │ O que é GUI?              │
│                           │                           │
│ **GUI** significa...      │ GUI significa...          │
│                           │                           │
│ - Tkinter                 │ • Tkinter                 │
│ - CustomTkinter           │ • CustomTkinter           │
│                           │                           │
└───────────────────────────┴───────────────────────────┘
          EDIÇÃO                    VISUALIZAÇÃO
```

Essa opção é particularmente útil durante o aprendizado de Markdown, pois permite observar imediatamente como cada comando é apresentado no documento final.

---

## 5.4 🔙 Voltando para o Markdown

Não é necessário realizar nenhuma conversão.

Para voltar à edição, basta clicar novamente na aba correspondente ao arquivo:

```text
aula-01.0-vscode-estrutura-ambiente.md
```

O arquivo `.md` permanece disponível para edição durante todo o processo.

---

## 5.5 ⌨️ Atalhos importantes

| Ação                    | Atalho                         |
| ----------------------- | ------------------------------ |
| Abrir o Preview         | `Ctrl + Shift + V`             |
| Abrir o Preview ao lado | `Ctrl + K` e depois `V`        |
| Voltar para edição      | Clicar na aba do arquivo `.md` |

---

## 5.6 💡 Por que estamos utilizando Markdown?

O Markdown será utilizado nesta disciplina porque é amplamente empregado na **documentação de projetos de software**.

Ao utilizá-lo nas aulas, estaremos trabalhando simultaneamente com:

```text
  Markdown
     ↓
Documentação
     ↓
 README.md
     ↓
    Git
     ↓
   GitHub
```

Assim, o próprio material didático passa a fazer parte do **projeto de software e do seu controle de versão**.

> 🎯 **Ideia-chave:** documentação não é algo separado do desenvolvimento.  
> Em um projeto profissional, **código e documentação evoluem juntos**.

---

# 6. Python REPL × terminal

Ao executar:

```powershell
python
```

entramos no **Python REPL**:

```text
>>>
```

REPL significa:

```text
Read → Eval → Print → Loop
Ler  → Avaliar → Exibir → Repetir
```

É um ambiente interativo para executar instruções Python rapidamente.

Para sair:

```python
exit()
```

No Windows, também é possível sair usando:

```text
Ctrl + Z
Enter
```

> Se o prompt mostrar `>>>`, você está no Python.  
> Se mostrar `PS C:\...>`, você está no PowerShell.

---

# 7. Arquivos iniciais do projeto

## `main.py`

É o ponto inicial de execução da aplicação nesta primeira etapa.

## `README.md`

Apresenta o projeto para quem acessa o repositório: objetivo, instalação, execução e documentação básica.

## `requirements.txt`

Registra dependências Python necessárias para reproduzir o ambiente do projeto.

## `.gitignore`

Indica arquivos e pastas que o Git não deverá versionar, como a `.venv`.

---

# 🛠 Sprint 00 — Compreendendo o ambiente Python preparado

# 8. Por que usar ambiente virtual?

Uma aplicação pode depender de bibliotecas e versões específicas.

O ambiente virtual cria um Python isolado para o projeto:

```text
Python do sistema
      │
      ├── Projeto A → .venv própria
      └── EngConvert → .venv própria
```

Benefícios:

- reduz conflitos entre bibliotecas;
- facilita reproduzir o projeto;
- mantém as dependências organizadas;
- ajuda o VSCode a utilizar o interpretador correto.

> 📌 **Regra prática para a disciplina:** um projeto Python → uma `.venv`.

---

# 9. Como a `.venv` foi criada

Na Aula 00, dentro de:

```text
C:\Projetos\engconvert
```

executamos:

```powershell
python -m venv .venv
```

Esse comando **já foi executado** durante a preparação do projeto. Aqui estamos entendendo o que ele fez.

> ⚠️ Se a pasta `.venv` já existe e está funcionando, **não é necessário recriá-la**.

A pasta aparece no projeto:

```text
engconvert/
├── .venv/
├── assets/
├── aulas/
├── docs/
├── src/
├── tests/
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

> A `.venv` é local. Ela **não deve ser enviada ao GitHub**.

---

## 9.1 🐍 E se precisarmos utilizar uma versão específica do Python?

Em alguns projetos, determinadas bibliotecas podem apresentar requisitos ou diferenças de compatibilidade entre versões do Python.

Nesses casos, podemos padronizar uma versão específica para toda a turma.

Um exemplo é o **Python 3.12.10**, que pode ser instalado diretamente no Windows utilizando o instalador oficial de 64 bits:

```text
https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe
```

Página oficial da versão:

```text
https://www.python.org/downloads/release/python-31210/
```

> 💡 O link direto para o `.exe` facilita a instalação em sala de aula, evitando que o aluno precise localizar manualmente o instalador correto entre diferentes arquivos disponíveis.

Durante a instalação do Python, verifique se os componentes necessários ao desenvolvimento estão disponíveis, especialmente:

```text
Python
pip
venv
```

Quando a opção estiver disponível no instalador, também é conveniente permitir que o Python seja localizado pelo sistema.

Depois de instalado, podemos conferir as versões reconhecidas pelo Python Launcher:

```powershell
py -0p
```

Se quisermos criar a `.venv` especificamente com a série Python 3.12:

```powershell
py -3.12 -m venv .venv
```

Depois:

```powershell
.\.venv\Scripts\Activate.ps1
```

e:

```powershell
python --version
```

Em uma instalação baseada no Python 3.12.10, esperamos:

```text
Python 3.12.10
```

> 🎯 **Ideia-chave:** não devemos escolher uma versão específica do Python apenas por hábito. A padronização deve existir quando houver uma necessidade de **compatibilidade, reprodutibilidade ou uniformidade do ambiente da turma**.

---

## 9.2 🔎 `venv` ou `.venv`? Qual é a diferença?

Observe novamente o comando utilizado para criar o ambiente virtual:

```powershell
python -m venv .venv
```

À primeira vista, pode parecer estranho termos `venv` e `.venv` no mesmo comando.

Apesar dos nomes semelhantes, eles representam **coisas diferentes**.

Podemos decompor o comando completo:

```text
python -m venv .venv
│      │    │    │
│      │    │    └── nome escolhido para a pasta
│      │    │
│      │    └──────── módulo venv
│      │
│      └───────────── executa um módulo
│
└──────────────────── interpretador Python
```

Portanto:

- **`python`** → executa o interpretador Python;
- **`-m`** → solicita ao Python que execute um módulo;
- **`venv`** → é o módulo do Python utilizado para criar ambientes virtuais;
- **`.venv`** → é o nome que escolhemos para a pasta onde o ambiente será criado.

### 📁 O nome da pasta pode ser diferente?

Sim.

O último elemento do comando representa o **nome da pasta que será criada**.

Por exemplo:

```powershell
python -m venv venv
```

cria:

```text
engconvert/
│
├── venv/
├── main.py
└── ...
```

Enquanto:

```powershell
python -m venv .venv
```

cria:

```text
engconvert/
│
├── .venv/
├── main.py
└── ...
```

Poderíamos até utilizar outro nome:

```powershell
python -m venv ambiente
```

e teríamos:

```text
engconvert/
│
├── ambiente/
├── main.py
└── ...
```

Os três comandos utilizam exatamente o mesmo módulo:

```text
python -m venv
```

O que muda é somente o último elemento:

```text
python -m venv venv
               └──── nome da pasta

python -m venv .venv
               └──── nome da pasta

python -m venv ambiente
               └──── nome da pasta
```

Portanto:

```text
venv       ┐
.venv      ├── nomes possíveis para a pasta
ambiente   ┘
```

> 💡 O ambiente virtual não precisa obrigatoriamente se chamar `venv` ou `.venv`. Esses são apenas nomes e convenções utilizadas nos projetos Python.

### ⚠️ O comando de ativação acompanha o nome da pasta

O nome utilizado na criação também aparecerá no caminho utilizado para ativar o ambiente.

```text
CRIAÇÃO                         PASTA        ATIVAÇÃO NO POWERSHELL

python -m venv venv       →     venv/     →  .\venv\Scripts\Activate.ps1

python -m venv .venv      →     .venv/    →  .\.venv\Scripts\Activate.ps1

python -m venv ambiente   →     ambiente/  →  .\ambiente\Scripts\Activate.ps1
```

Assim, se criarmos:

```powershell
python -m venv .venv
```

devemos ativar:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 9.3 🔎 Por que usamos `.venv` com um ponto no início?

Como vimos, poderíamos chamar a pasta do ambiente virtual de:

```text
venv
```

ou até:

```text
ambiente
```

Então, por que encontramos com frequência:

```text
.venv
```

O ponto `.` no início do nome faz parte de uma **convenção de nomenclatura muito utilizada no desenvolvimento de software**.

Em sistemas como Linux e macOS, arquivos e diretórios cujo nome começa com `.` são tradicionalmente tratados como **ocultos** em muitas formas de listagem.

Por exemplo:

```text
.gitignore
.env
.venv
.vscode
```

No desenvolvimento de software, nomes iniciados por `.` são frequentemente utilizados para arquivos e diretórios **auxiliares**, relacionados ao ambiente, à configuração ou às ferramentas utilizadas pelo projeto.

No EngConvert:

```text
engconvert/
│
├── .venv/        ← ambiente virtual do Python
├── .vscode/      ← configurações do VSCode, se utilizadas
├── .gitignore    ← regras de arquivos ignorados pelo Git
│
├── assets/
├── aulas/
├── docs/
├── src/
├── tests/
└── main.py
```

> 💡 **Importante:** o ponto não modifica o funcionamento do ambiente virtual Python. Ele faz parte apenas do **nome da pasta**.

Por isso:

```powershell
python -m venv venv
```

e:

```powershell
python -m venv .venv
```

criam o mesmo tipo de ambiente virtual.

O que muda é somente o nome da pasta:

```text
               venv
                ↓
            nome comum

              .venv
                ↓
      nome iniciado por ponto
                ↓
   convenção bastante utilizada
para o ambiente virtual do projeto
```

No **EngConvert**, adotaremos:

```text
.venv
```

como padrão para o ambiente virtual.

> 🎯 **Ideia-chave:** `venv` é o módulo do Python responsável por criar ambientes virtuais; `.venv` é o nome que escolhemos para a pasta do ambiente virtual do EngConvert. O `.` não é um comando nem uma característica especial do Python: ele simplesmente faz parte do nome escolhido para a pasta.

---

# 10. Ativando e verificando o ambiente virtual

Quando abrirmos um novo terminal e a `.venv` não estiver ativa, no PowerShell podemos executar:

```powershell
.\.venv\Scripts\Activate.ps1
```

O terminal deverá mudar para algo semelhante a:

```text
(.venv) PS C:\Projetos\engconvert>
```

No CMD:

```cmd
.venv\Scripts\activate.bat
```

No Git Bash:

```bash
source .venv/Scripts/activate
```

Para sair:

```powershell
deactivate
```

Podemos representar:

```text
      .venv existe
           ↓
abrimos um novo terminal
           ↓
    ativamos a .venv
           ↓
         python
           ↓
    Python do projeto
```

---

# 11. Se o PowerShell bloquear a ativação da `.venv`

Ao tentar:

```powershell
.\.venv\Scripts\Activate.ps1
```

pode aparecer uma mensagem semelhante a:

```text
A execução de scripts foi desabilitada neste sistema.
```

Isso não significa necessariamente que exista algum problema com o Python ou com a `.venv`.

O PowerShell possui uma configuração de segurança chamada **Execution Policy**, ou **Política de Execução**, que controla em quais condições scripts podem ser executados.

Como a ativação da `.venv` utiliza o script:

```text
Activate.ps1
```

essa política pode impedir sua execução.

```text
        .venv criada
             ↓
        Activate.ps1
             ↓
PowerShell verifica a política
             ↓
      script permitido?
             │
       ┌─────┴─────┐
      SIM         NÃO
       │           │
       ↓           ↓
     ativa      bloqueia
     .venv      o script
```

---

## 11.1 🔎 Verificando a política atual

Antes de modificar qualquer configuração, consulte:

```powershell
Get-ExecutionPolicy -List
```

O PowerShell apresentará as políticas configuradas para diferentes escopos.

> ⚠️ **Importante:** em computadores institucionais, laboratórios ou equipamentos administrados por uma organização, não altere políticas de segurança sem autorização.

---

## 11.2 🛠️ Alterando a política no computador pessoal

Em um **computador pessoal**, quando apropriado, podemos permitir a execução de scripts locais para o usuário atual com:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Podemos interpretar:

```text
Set-ExecutionPolicy
        ↓
altera a política de execução

-Scope CurrentUser
        ↓
aplica ao usuário atual

-ExecutionPolicy RemoteSigned
        ↓
permite scripts locais e aplica
regras adicionais a scripts remotos
```

Dependendo da configuração, poderá aparecer uma confirmação semelhante a:

```text
Deseja alterar a política de execução?

[S] Sim
[A] Sim para Todos
[N] Não
```

Nesse caso, confirme a alteração conforme solicitado.

Em outras situações, o comando simplesmente será executado e o PowerShell retornará ao prompt.

Depois:

1. feche o terminal PowerShell;
2. abra um novo terminal;
3. volte para a pasta do projeto:

```powershell
cd C:\Projetos\engconvert
```

4. ative novamente a `.venv`:

```powershell
.\.venv\Scripts\Activate.ps1
```

O terminal deverá apresentar:

```text
(.venv) PS C:\Projetos\engconvert>
```

> ⚠️ Em computadores institucionais, prefira solicitar orientação ao responsável pelo equipamento em vez de modificar a política de execução.

---

## 11.3 🛣️ Alternativa sem alterar a política do PowerShell

Também podemos utilizar o **CMD**:

```cmd
.venv\Scripts\activate.bat
```

Ou executar diretamente o Python da `.venv`:

```powershell
.\.venv\Scripts\python.exe --version
```

Portanto:

```text
PowerShell bloqueou Activate.ps1
              │
       ┌──────┴──────┐
       ↓             ↓
  computador    não alterar
   pessoal      a política
       │             │
       ↓             ↓
 RemoteSigned    usar CMD
 CurrentUser         │
       │             ↓
       ↓        activate.bat
 Activate.ps1
```

---

# 12. Verificando se estamos realmente utilizando a `.venv`

Depois da ativação, não precisamos confiar apenas na indicação:

```text
(.venv)
```

Podemos perguntar diretamente ao Python qual interpretador está sendo utilizado:

```powershell
python -c "import sys; print(sys.executable)"
```

O resultado deverá apontar para algo semelhante a:

```text
C:\Projetos\engconvert\.venv\Scripts\python.exe
```

Agora verifique:

```powershell
python --version
```

e:

```powershell
python -m pip --version
```

O `pip` deverá estar associado ao ambiente virtual, por exemplo:

```text
...\engconvert\.venv\Lib\site-packages\pip
```

> 🎯 **Verificação importante:** tanto o Python quanto o `pip` devem estar associados à `.venv` do projeto.

---

## 12.1 🔎 E se `pip --version` não funcionar?

Pode acontecer de:

```powershell
pip --version
```

retornar:

```text
pip : O termo 'pip' não é reconhecido...
```

Isso significa que o terminal não conseguiu localizar diretamente o comando `pip`.

O sistema utiliza o **PATH** como uma lista de locais onde procura programas executáveis:

```text
 digitamos um comando
          ↓
       sistema
          ↓
procura nos diretórios
 registrados no PATH
          ↓
      encontrou?
          │
     ┌────┴────┐
    SIM       NÃO
     │         │
     ↓         ↓
  executa    erro
```

Para o EngConvert adotaremos preferencialmente:

```powershell
python -m pip --version
```

Podemos ler:

```text
python -m pip
│      │  │
│      │  └── módulo pip
│      └───── execute um módulo
└──────────── interpretador Python atual
```

Com a `.venv` ativa:

```text
         python
            ↓
      Python da .venv
            ↓
         -m pip
            ↓
pip associado a esse Python
```

> 🎯 **Regra prática do EngConvert:** prefira `python -m pip` aos comandos executados diretamente com `pip`.

---

## 12.2 📦 Verificando e atualizando o `pip`

Execute:

```powershell
python -m pip --version
```

Também podemos observar os executáveis:

```powershell
dir .venv\Scripts
```

Normalmente encontraremos:

```text
python.exe
pip.exe
pip3.exe
```

Para atualizar o `pip`:

```powershell
python -m pip install --upgrade pip
```

Depois:

```powershell
python -m pip --version
```

Se o módulo `pip` realmente não estiver disponível, situação menos comum, podemos tentar:

```powershell
python -m ensurepip --upgrade
```

e novamente:

```powershell
python -m pip --version
```

---

# 13. Forma recomendada para instalar pacotes

Durante o desenvolvimento do EngConvert, adotaremos:

```powershell
python -m pip install nome_do_pacote
```

Por exemplo:

```powershell
python -m pip install customtkinter
```

A forma:

```powershell
pip install customtkinter
```

também pode funcionar, mas a primeira deixa explícita a relação:

```text
Python selecionado
       ↓
      pip
       ↓
biblioteca instalada
       ↓
ambiente desse Python
```

> 🎯 **Ideia-chave:** `python -m pip` reduz ambiguidades quando existem várias instalações do Python ou vários ambientes virtuais.

---

# 14. 🧯 Recriando a `.venv` — somente quando necessário

A recriação da `.venv` **não deve ser a primeira solução para qualquer problema**.

Ela pode ser útil quando o ambiente estiver realmente corrompido ou quando decidirmos reconstruí-lo.

Primeiro, saia do ambiente:

```powershell
deactivate
```

No PowerShell, remova a pasta:

```powershell
Remove-Item -Recurse -Force .venv
```

No CMD:

```cmd
rmdir /s /q .venv
```

Depois, recrie:

```powershell
python -m venv .venv
```

ou, se quisermos selecionar explicitamente o Python 3.12:

```powershell
py -3.12 -m venv .venv
```

Ative:

```powershell
.\.venv\Scripts\Activate.ps1
```

Verifique:

```powershell
python -c "import sys; print(sys.executable)"
```

e:

```powershell
python -m pip --version
```

Como o projeto possui `requirements.txt`, podemos reinstalar as dependências registradas:

```powershell
python -m pip install -r requirements.txt
```

Assim:

```text
  problema na .venv
         ↓
diagnosticar primeiro
         ↓
precisa reconstruir?
         │
    ┌────┴───────┐
   NÃO          SIM
    │            │
    ↓            ↓
corrigir   remover .venv
problema         ↓
          criar novamente
                 ↓
               ativar
                 ↓
     instalar requirements.txt
                 ↓
             verificar
```

> ⚠️ A `.venv` é um ambiente **recriável**. O código do projeto e o `requirements.txt` são mais importantes do que preservar fisicamente a pasta `.venv`.

---

# 15. Retomando o primeiro programa no VSCode

Na Aula 00, criamos em `main.py`:

```python
print("EngConvert iniciado com sucesso!")
```

Agora podemos alterar o arquivo para:

```python
print("EngConvert")
print("Primeiro programa executado no VSCode.")
```

Execute pelo terminal:

```powershell
python main.py
```

Saída esperada:

```text
EngConvert
Primeiro programa executado no VSCode.
```

---

# 16. ▶️ O botão Run não funciona?

Pode acontecer de o programa funcionar corretamente quando executamos pelo terminal:

```powershell
python main.py
```

mas apresentar algum problema quando utilizamos um botão de execução do VSCode.

Uma das possíveis causas é o VSCode estar utilizando um **interpretador Python diferente daquele utilizado no terminal**.

```text
        TERMINAL
     python main.py
           ↓
     Python da .venv
           ↓
    programa funciona


    BOTÃO DE EXECUÇÃO
           ↓
outro interpretador Python
           ↓
biblioteca não encontrada
ou comportamento diferente
```

> 🎯 **Ideia-chave:** executar um arquivo Python não depende apenas do código. Também precisamos saber qual interpretador Python está executando esse código.

---

## 16.1 🔎 Descobrindo qual Python está sendo utilizado

Com a `.venv` ativa:

```powershell
python -c "import sys; print(sys.executable)"
```

Esperamos algo semelhante a:

```text
C:\Projetos\engconvert\.venv\Scripts\python.exe
```

Esse é o Python que queremos utilizar no projeto.

---

## 16.2 🐍 Selecionando o interpretador correto no VSCode

Abra:

```text
Ctrl + Shift + P
```

Digite:

```text
Python: Select Interpreter
```

Escolha:

```text
C:\Projetos\engconvert\.venv\Scripts\python.exe
```

Podemos representar:

```text
         VSCode
           ↓
Python: Select Interpreter
           ↓
.venv\Scripts\python.exe
           ↓
  Python do EngConvert
```

> 💡 Ativar a `.venv` no terminal e selecionar o interpretador no VSCode são ações relacionadas, mas não são exatamente a mesma coisa.

---

## 16.3 ▶️ Utilize `Run Python File`

Com um arquivo `.py` aberto, a extensão **Python**, da Microsoft, disponibiliza:

```text
▶ Run Python File
```

Também podemos executar pelo terminal:

```powershell
python main.py
```

Durante o curso, essas serão nossas formas preferenciais de execução.

---

## 16.4 ⚠️ `Run Code` não é `Run Python File`

Se a extensão **Code Runner** estiver instalada, poderá aparecer:

```text
Run Code
```

Ela não é a mesma opção que:

```text
Run Python File
```

Dependendo da configuração do Code Runner, a execução pode utilizar um comando ou ambiente diferente daquele esperado para a `.venv`.

Por isso, neste curso, adotaremos preferencialmente:

```text
TERMINAL
python main.py

        ou

VSCODE
Run Python File
```

> 💡 Essa é uma das razões pelas quais não precisamos instalar o **Code Runner** no início do EngConvert.

---

## 16.5 🧪 Diagnóstico com `sys.executable`

Também podemos colocar temporariamente no programa:

```python
import sys

print(sys.executable)
```

Ao executar, o Python mostrará o caminho do interpretador utilizado.

Se aparecer:

```text
C:\Projetos\engconvert\.venv\Scripts\python.exe
```

estamos utilizando a `.venv`.

Se aparecer outro caminho, o programa está sendo executado por outro Python.

```text
sys.executable
      ↓
"Qual Python está executando
este programa?"
```

---

## 16.6 🛠️ Configuração explícita do projeto

O VSCode permite armazenar configurações específicas do projeto em:

```text
.vscode/
└── settings.json
```

Uma configuração possível é:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
  "python.terminal.activateEnvironment": true
}
```

`workspaceFolder` representa a pasta raiz aberta no VSCode:

```text
${workspaceFolder}
        ↓
C:\Projetos\engconvert
```

Assim:

```text
${workspaceFolder}/.venv/Scripts/python.exe
```

aponta para o Python do ambiente virtual do EngConvert.

> 📌 Essa configuração pode ser útil para padronizar o ambiente, mas **não é obrigatória neste momento**. Primeiro aprenderemos a selecionar e verificar corretamente o interpretador pelo VSCode.

---

## 16.7 🧰 Executando diretamente o Python da `.venv`

Mesmo sem ativar o ambiente virtual, podemos chamar diretamente:

```powershell
.\.venv\Scripts\python.exe main.py
```

Nesse caso:

```text
.\.venv\Scripts\python.exe
            ↓
Python específico da .venv
            ↓
          main.py
```

Isso é particularmente útil como técnica de diagnóstico.

> 💡 Ativar a `.venv` facilita o trabalho no terminal, mas não é obrigatório quando chamamos diretamente o interpretador existente dentro dela.

---

## 🎯 Ideia-chave — execução no VSCode

Quando um programa funciona pelo terminal, mas não funciona por algum botão do VSCode, uma das primeiras perguntas deve ser:

> **Qual interpretador Python está executando meu programa?**

Durante o EngConvert utilizaremos principalmente:

```text
python main.py
      ↓
terminal + .venv

ou

Run Python File
      ↓
interpretador selecionado no VSCode
```

e poderemos verificar o interpretador com:

```python
import sys

print(sys.executable)
```

---

# 17. 🧪 Prática orientada

Confirme cada item:

- [ ] abri `C:\Projetos\engconvert` como pasta no VSCode;
- [ ] localizei Explorer, Editor e Terminal;
- [ ] abri `aula-01.0-vscode-estrutura-ambiente.md`;
- [ ] visualizei a aula com `Ctrl + Shift + V`;
- [ ] testei o Preview ao lado com `Ctrl + K → V`;
- [ ] voltei à edição do arquivo `.md`;
- [ ] verifiquei `python --version`;
- [ ] compreendi a diferença entre `python` e `py`;
- [ ] identifiquei terminal × REPL;
- [ ] confirmei a existência da `.venv`;
- [ ] ativei ou confirmei que a `.venv` estava ativa;
- [ ] verifiquei o interpretador com `sys.executable`;
- [ ] executei `python -m pip --version`;
- [ ] selecionei o interpretador correto no VSCode;
- [ ] distingui `Run Python File` de `Run Code`;
- [ ] executei `main.py`.

---

# 18. 🖥️ Do script para uma aplicação

Até aqui, muitos programas Python podem seguir uma sequência direta:

```text
   Início
      ↓
   entrada
      ↓
processamento
      ↓
    saída
      ↓
     fim
```

Por exemplo, um programa executado no terminal pode solicitar um valor, realizar um cálculo, apresentar o resultado e terminar.

Uma aplicação gráfica funciona de maneira diferente.

Depois de abrir sua janela, ela precisa permanecer ativa aguardando ações do usuário:

```text
       abrir a aplicação
              ↓
      exibir a interface
              ↓
      aguardar o usuário
              ↓
   ┌──────────┼──────────┐
   ↓          ↓          ↓
clique    digitação   seleção
   └──────────┼──────────┘
              ↓
      executar uma ação
              ↓
    atualizar a interface
              ↓
    continuar aguardando
```

Essa mudança introduz um conceito importante: **programação orientada a eventos**.

---

# 19. Introdução à interface gráfica do EngConvert

Até este ponto, trabalhamos principalmente com **Python, terminal, ambiente virtual, VSCode e organização do projeto**.

Agora daremos o primeiro passo para transformar o EngConvert em uma **aplicação gráfica**.

## 19.1 O que é GUI?

**GUI** significa:

```text
Graphical User Interface
```

ou:

> **Interface Gráfica do Usuário (IGU).**

Em vez de interagir somente por comandos no terminal, o usuário passa a utilizar elementos visuais, como:

```text
janela
  │
  ├── textos
  ├── campos de entrada
  ├── botões
  ├── menus
  └── outros componentes
```

Compare:

```text
Terminal                     Interface gráfica

Digite a pressão: 10         Valor: [ 10       ]

Resultado: 1000 kPa          [ CONVERTER ]

                              Resultado: 1000 kPa
```

A lógica matemática do programa pode continuar sendo a mesma. O que muda é principalmente **a forma de interação entre o usuário e o software**.

> 🎯 **Ideia-chave:** nesta aula queremos apenas compreender o suficiente para criar e executar a **primeira janela do EngConvert**. O funcionamento de **Tcl/Tk, Tkinter, CustomTkinter, widgets e eventos** será aprofundado na **Aula 02.0**.

---

# 20. A tecnologia que utilizaremos

Para construir a interface gráfica do EngConvert utilizaremos:

```text
CustomTkinter
```

O **CustomTkinter** é uma biblioteca Python voltada à criação de interfaces gráficas com componentes de aparência moderna.

Por enquanto, podemos visualizar nossa aplicação de maneira simplificada:

```text
Python
   ↓
CustomTkinter
   ↓
Interface gráfica do EngConvert
```

Existe uma estrutura importante por trás dessa biblioteca:

```text
Python
   ↓
CustomTkinter
   ↓
Tkinter
   ↓
Tcl/Tk
   ↓
Sistema Operacional
```

Nesta aula, **não precisamos aprofundar cada uma dessas camadas**. Nosso objetivo imediato é utilizar o CustomTkinter para criar a primeira janela.

> 💡 Na **Aula 02.0**, estudaremos com mais detalhes o que são **Tcl, Tk, Tkinter e CustomTkinter**, como essas tecnologias se relacionam e por que escolhemos essa biblioteca para o EngConvert.

---

# 21. Uma primeira noção de widget

Os elementos que compõem uma interface gráfica são frequentemente chamados de **widgets**.

Alguns exemplos que utilizaremos no EngConvert são:

```text
CTk()        → janela principal
CTkFrame     → área para organizar componentes
CTkLabel     → texto
CTkEntry     → campo de entrada
CTkButton    → botão
```

Neste momento, porém, utilizaremos apenas o necessário para criar a **janela principal**.

Os demais widgets serão estudados progressivamente nas próximas aulas.

---

# 22. Uma primeira noção de eventos

Uma aplicação gráfica normalmente permanece aberta esperando ações do usuário ou do próprio sistema.

Por exemplo:

```text
Aplicação
   │
   ├── usuário digita
   ├── usuário clica
   ├── usuário seleciona
   ├── janela é redimensionada
   └── usuário fecha a aplicação
```

Essas ações são chamadas, de forma geral, de **eventos**.

Isso introduz uma característica importante das interfaces gráficas:

> **programação orientada a eventos.**

Não precisamos dominar esse conceito agora. Na **Aula 02.0** ele será explicado com maior profundidade e, posteriormente, veremos sua aplicação nos componentes do EngConvert.

---

# 23. Uma primeira noção de `mainloop()`

Ao final do código da nossa primeira janela encontraremos:

```python
app.mainloop()
```

De forma introdutória, podemos entender `mainloop()` como o comando que mantém a interface gráfica ativa, aguardando os acontecimentos da aplicação.

```text
mainloop()
     ↓
mantém a janela ativa
     ↓
aguarda eventos
     ↓
a aplicação continua funcionando
```

Sem entrar ainda nos detalhes internos:

> 🎯 **Por enquanto:** `mainloop()` inicia o ciclo principal da interface gráfica e mantém a aplicação preparada para responder aos eventos.

O funcionamento desse **loop de eventos** será aprofundado na **Aula 02.0**.

---

# 24. Preparando a primeira janela

Agora já temos o conhecimento mínimo necessário:

```text
GUI
 ↓
interface gráfica

CustomTkinter
 ↓
biblioteca utilizada no EngConvert

widget
 ↓
componente da interface

evento
 ↓
ação que ocorre durante a execução

mainloop()
 ↓
mantém a GUI ativa
```

Com essa visão introdutória, podemos construir nossa primeira janela sem antecipar toda a fundamentação que será desenvolvida na próxima aula.

---

# 25. 🚀 Nossa primeira janela do EngConvert

Agora podemos transformar o `main.py` em nossa primeira aplicação gráfica.

Substitua o conteúdo pelo código:

```python
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("EngConvert")
app.geometry("700x450")

app.mainloop()
```

Execute:

```powershell
python main.py
```

Uma janela deverá ser aberta.

## 25.1 Entendendo cada linha

### Importação

```python
import customtkinter as ctk
```

Importamos a biblioteca `customtkinter` e utilizamos:

```text
ctk
```

como um nome abreviado.

Assim:

```python
customtkinter.CTk()
```

pode ser escrito como:

```python
ctk.CTk()
```

### Aparência

```python
ctk.set_appearance_mode("system")
```

Define o modo de aparência de acordo com o sistema.

Posteriormente poderemos experimentar:

```python
ctk.set_appearance_mode("dark")
```

ou:

```python
ctk.set_appearance_mode("light")
```

### Tema

```python
ctk.set_default_color_theme("blue")
```

Define o tema de cores padrão utilizado pelos widgets do CustomTkinter.

### Janela principal

```python
app = ctk.CTk()
```

Cria a janela principal da aplicação e armazena o objeto na variável:

```text
app
```

### Título

```python
app.title("EngConvert")
```

Define o texto exibido na barra de título.

### Geometria

```python
app.geometry("700x450")
```

Define as dimensões iniciais:

```text
700 × 450
 ↓     ↓
largura altura
```

### Loop de eventos

```python
app.mainloop()
```

Mantém a aplicação aberta e aguardando eventos.

---

# 26. 🧪 Experimente

Altere:

```python
app.geometry("900x600")
```

Execute novamente:

```powershell
python main.py
```

Observe o efeito.

Depois experimente:

```python
ctk.set_appearance_mode("dark")
```

e:

```python
ctk.set_appearance_mode("light")
```

A intenção desta atividade não é decorar comandos.

O objetivo é perceber a relação:

```text
alteramos o código
        ↓
executamos novamente
        ↓
observamos a interface
        ↓
compreendemos o efeito
```

---

# 27. 🧭 Onde estamos no desenvolvimento?

Neste momento, já conseguimos:

```text
EngConvert
    ↓
estrutura do projeto
    ↓
VSCode
    ↓
Python + .venv
    ↓
CustomTkinter
    ↓
primeira janela
```

Ainda não temos:

```text
campos de entrada
botões funcionais
conversões
seleção de unidades
resultado formatado
```

Esses recursos serão acrescentados progressivamente.

> 📌 Na próxima etapa, o Roadmap e os Sprints nos ajudarão a visualizar o caminho completo do EngConvert e o próximo incremento que será desenvolvido.

---

# 📌 Resumo da aula

Nesta aula, partimos do ambiente preparado na Aula 00 e compreendemos os principais elementos que sustentam o desenvolvimento do EngConvert.

Aprendemos que:

- um projeto profissional envolve código, documentação, dependências, testes e organização;
- o VSCode reúne editor, terminal, extensões e ferramentas de desenvolvimento;
- `python` e `py` possuem papéis diferentes no Windows;
- a `.venv` cria um ambiente virtual isolado para o projeto;
- `venv` é o módulo Python e `.venv` é o nome adotado para a pasta do ambiente;
- o ponto inicial de `.venv` faz parte de uma convenção de nomenclatura;
- `python -m pip` ajuda a utilizar o `pip` associado ao interpretador Python selecionado;
- `sys.executable` permite verificar qual Python está executando o programa;
- o VSCode deve utilizar o interpretador correto da `.venv`;
- `Run Python File` não deve ser confundido com `Run Code`;
- GUI significa **Graphical User Interface**;
- Tkinter é a interface padrão do Python para Tcl/Tk;
- CustomTkinter mantém conceitos semelhantes ao Tkinter com uma apresentação moderna;
- componentes gráficos são chamados de **widgets**;
- GUIs trabalham com eventos;
- `mainloop()` mantém o loop de eventos da aplicação;
- criamos e executamos a primeira janela gráfica do EngConvert.

Podemos resumir a evolução:

```text
         Aula 00
     preparamos o projeto
            ↓
         Aula 01.0
   compreendemos o ambiente
            ↓
   Python + .venv + VSCode
            ↓
           GUI
            ↓
   Tkinter / CustomTkinter
            ↓
     eventos + mainloop()
            ↓
primeira janela do EngConvert
```

---

## 🎯 Ideia-chave da Aula 01.0

> **Não estamos apenas aprendendo comandos Python. Estamos começando a compreender como um software desktop é estruturado, executado e preparado para interagir com o usuário por meio de uma interface gráfica.**

---

## ➡️ Próxima aula

Na próxima aula, avançaremos a partir da janela que já construímos.

Vamos relacionar o desenvolvimento ao **Roadmap e aos Sprints** e continuar a evolução da interface gráfica do EngConvert de forma incremental.

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
