# Aula 02.0 — Fundamentos das Interfaces Gráficas e Planejamento do EngConvert

## GUI, Tcl/Tk, Tkinter, CustomTkinter, Roadmap e Sprints

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Objetivo desta etapa:** compreender com maior profundidade como funciona a interface gráfica que já construímos e organizar a evolução do EngConvert por meio de Roadmap e Sprints.

---

## 🎯 Objetivos

Ao final desta aula, o aluno deverá ser capaz de:

- retomar a primeira janela construída na Aula 01;
- compreender com maior profundidade o conceito de **GUI**;
- diferenciar um programa sequencial de uma aplicação orientada a eventos;
- compreender o significado de **Tcl/Tk**;
- compreender o papel do **Tkinter** na comunicação entre Python e Tcl/Tk;
- compreender onde o **CustomTkinter** se posiciona nessa arquitetura;
- reconhecer a relação entre Tkinter e CustomTkinter;
- compreender o conceito de **widget**;
- compreender o conceito de **evento**;
- compreender o papel do `mainloop()`;
- compreender como esses elementos se relacionam no EngConvert;
- diferenciar **Roadmap** de **Sprint**;
- reconhecer as etapas do Roadmap inicial do EngConvert;
- registrar retrospectivamente as etapas já concluídas;
- identificar a próxima etapa de desenvolvimento do projeto.

---

# 1. Retomando a primeira janela do EngConvert

Na Aula 01 construímos nossa primeira interface gráfica.

O arquivo `main.py` passou a conter uma estrutura semelhante a:

```python
# Importa a biblioteca CustomTkinter.
# "as ctk" cria o apelido ctk para facilitar seu uso no código.
import customtkinter as ctk

# Define o modo de aparência da aplicação.
# "system" acompanha o modo claro/escuro configurado no sistema operacional.
ctk.set_appearance_mode("system")

# Define o tema de cores padrão utilizado pelos widgets do CustomTkinter.
ctk.set_default_color_theme("blue")

# Cria a janela principal da aplicação.
app = ctk.CTk()

# Define o texto apresentado na barra de título da janela.
app.title("EngConvert")

# Define o tamanho inicial da janela.
app.geometry("700x450")

# Inicia o loop principal de eventos da interface gráfica.
app.mainloop()
```

Naquele momento, nosso objetivo principal era **fazer a primeira janela funcionar**.

Agora faremos uma pergunta diferente:

> **O que existe por trás dessa janela e como uma aplicação gráfica funciona?**

---

# 2. Do script para a GUI

Um programa simples pode seguir uma sequência como:

```text
   Início
      ↓
   Entrada
      ↓
Processamento
      ↓
    Saída
      ↓
     Fim
```

Nesse modelo, as instruções são executadas em sequência.

Por exemplo:

```python
pressao_bar = float(input("Digite a pressão em bar: "))
pressao_kpa = pressao_bar * 100
print(pressao_kpa)
```

O programa:

```text
solicita um valor
        ↓
  recebe o valor
        ↓
realiza o cálculo
        ↓
mostra o resultado
        ↓
     termina
```

Uma aplicação gráfica funciona de maneira diferente.

Depois de aberta, ela normalmente permanece ativa aguardando acontecimentos:

```text
             ┌── clique
             ├── digitação
Aplicação ───┼── seleção
             ├── redimensionamento
             └── fechar janela
```

Isso introduz um conceito fundamental:

> **Programação orientada a eventos.**

---

# 3. O que é GUI?

**GUI** significa:

```text
Graphical User Interface
```

ou:

> **Interface Gráfica do Usuário (IGU).**

Uma GUI permite que o usuário interaja com o programa por meio de elementos gráficos.

Exemplos:

- janelas;
- botões;
- campos de entrada;
- textos;
- menus;
- listas;
- caixas de seleção.

### Terminal × GUI

```text
Terminal                     GUI

Digite a pressão: 10        Valor: [ 10       ]

Resultado: 1000 kPa         [ CONVERTER ]

                              Resultado: 1000 kPa
```

A lógica matemática pode ser exatamente a mesma.

O que muda é principalmente:

> **a forma de interação entre o usuário e o software.**

No EngConvert, continuaremos utilizando Python para implementar a lógica do programa, mas construiremos uma interface gráfica para tornar essa interação mais organizada e intuitiva.

---

# 4. Programação sequencial × programação orientada a eventos

Compare os dois modelos.

### Programa sequencial

```text
  Início
     ↓
  Entrada
     ↓
Processamento
     ↓
   Saída
     ↓
    Fim
```

### Aplicação gráfica

```text
             ┌── evento A
             ├── evento B
Aplicação ───┼── evento C
             ├── evento D
             └── evento E
```

Em uma aplicação gráfica, nem sempre sabemos antecipadamente qual será a próxima ação do usuário.

Ele pode:

```text
       digitar
          ↓
       clicar
          ↓
 alterar uma seleção
          ↓
redimensionar a janela
          ↓
   clicar novamente
```

ou realizar essas ações em outra ordem.

A aplicação precisa permanecer disponível para responder a esses acontecimentos.

> 🎯 **Ideia-chave:** uma GUI é fortemente baseada em eventos. O programa permanece ativo e responde às ações que ocorrem durante sua execução.

---

# 5. Tkinter

O **Tkinter** é a interface padrão do Python para o toolkit gráfico **Tk**, pertencente ao ecossistema **Tcl/Tk**.

Um exemplo simples utilizando Tkinter seria:

```python
# Importa o Tkinter e utiliza "tk" como apelido.
import tkinter as tk

# Cria a janela principal.
app = tk.Tk()

# Define o título da janela.
app.title("Minha primeira interface")

# Define as dimensões iniciais.
app.geometry("500x300")

# Cria um texto dentro da janela.
label = tk.Label(
    app,
    text="Programação para Engenharia Mecânica"
)

# Posiciona o texto.
label.pack(pady=20)

# Cria um botão.
botao = tk.Button(
    app,
    text="Executar"
)

# Posiciona o botão.
botao.pack()

# Mantém a interface ativa.
app.mainloop()
```

Mas, para compreender melhor o papel do Tkinter, precisamos entender primeiro o que significa **Tcl/Tk**.

---

# 6. 🔎 O que significa Tcl/Tk?

O Tkinter fornece ao Python acesso aos recursos gráficos do **Tk**.

O Tk, por sua vez, está historicamente associado à linguagem **Tcl**.

Por isso encontramos frequentemente a expressão:

```text
Tcl/Tk
```

Vamos separar os dois conceitos.

---

## 6.1 Tcl — Tool Command Language

**Tcl** significa:

```text
Tool Command Language
```

É uma **linguagem de programação** criada para ser simples e facilmente incorporada a outras aplicações.

Para nosso projeto, não precisamos aprender a programar diretamente em Tcl.

O importante é compreender onde essa tecnologia se encontra na arquitetura gráfica que estamos utilizando.

---

## 6.2 Tk — toolkit gráfico

O **Tk** é um **toolkit gráfico**.

Um toolkit gráfico fornece recursos utilizados na construção de interfaces.

Por exemplo:

```text
Tk
│
├── janelas
├── botões
├── campos de texto
├── menus
├── caixas de seleção
└── outros widgets
```

Podemos representar a relação entre Tcl e Tk de forma didática:

```text
Tcl
│
└── linguagem de programação
        │
        └── Tk
            │
            └── toolkit para interfaces gráficas
                │
                ├── janelas
                ├── botões
                ├── campos de texto
                ├── menus
                ├── caixas de seleção
                └── outros widgets
```

> 💡 **Widget** é o nome utilizado para componentes que formam uma interface gráfica, como botões, campos de entrada, textos, menus e caixas de seleção.

---

# 7. 🐍 Onde entra o Tkinter?

O **Tkinter funciona como uma ponte entre o Python e o Tcl/Tk**.

Isso permite utilizar recursos gráficos do Tk escrevendo código Python.

Podemos representar essa relação de forma simplificada:

```text
  Código Python
        ↓
     Tkinter
        ↓
     Tcl/Tk
        ↓
Sistema Operacional
        ↓
 Interface Gráfica
```

Quando escrevemos:

```python
import tkinter as tk

app = tk.Tk()
```

não precisamos programar diretamente em Tcl.

O Tkinter fornece uma **interface Python** para acessar os recursos gráficos disponibilizados pelo Tk.

> 🎯 **Ideia-chave:** não precisamos aprender Tcl para desenvolver a interface do EngConvert. Precisamos compreender que o Tkinter atua como uma camada de comunicação entre nosso código Python e a infraestrutura gráfica Tcl/Tk.

---

## 7.1 🧩 De onde vem o nome Tkinter?

Didaticamente, podemos associar o nome à ideia de:

```text
Tk + Interface
      ↓
   Tkinter
```

Isso ajuda a lembrar sua função:

> fornecer ao Python uma interface para utilização do Tk.

---

# 8. 🎨 Onde entra o CustomTkinter?

No EngConvert escolhemos utilizar **CustomTkinter**.

Ele mantém conceitos muito próximos dos encontrados no Tkinter, mas oferece widgets estilizados e recursos convenientes para construção de interfaces com aparência mais moderna.

Podemos representar nossa arquitetura assim:

```text
Python
   │
   └── CustomTkinter
          ↓
       Tkinter
          ↓
        Tcl/Tk
          ↓
   Sistema Operacional
          ↓
   Interface Gráfica
```

Portanto:

> **utilizar CustomTkinter não significa abandonar os fundamentos do Tkinter.**

Continuamos trabalhando sobre a infraestrutura Tkinter/Tcl/Tk.

---

# 9. Tkinter × CustomTkinter

Observe alguns componentes equivalentes:

| Tkinter  | CustomTkinter | Função           |
| -------- | ------------- | ---------------- |
| `Tk()`   | `CTk()`       | janela principal |
| `Label`  | `CTkLabel`    | texto            |
| `Button` | `CTkButton`   | botão            |
| `Entry`  | `CTkEntry`    | campo de entrada |
| `Frame`  | `CTkFrame`    | agrupamento      |

A sintaxe também permanece conceitualmente próxima.

### Tkinter

```python
import tkinter as tk

app = tk.Tk()
```

### CustomTkinter

```python
import customtkinter as ctk

app = ctk.CTk()
```

Podemos resumir:

```text
Tkinter                     CustomTkinter
   │                              │
 janela                         janela
 widgets                        widgets
 eventos                        eventos
 pack/grid                      pack/grid
 mainloop                       mainloop
   │                              │
   └──── fundamentos comuns ──────┘
```

A escolha do CustomTkinter no EngConvert não é apenas estética.

Ela nos permite estudar conceitos tradicionais de GUI enquanto construímos uma aplicação desktop com uma apresentação mais atual.

---

# 10. Por que CustomTkinter no EngConvert?

Podemos resumir nossa escolha:

```text
Fundamentos de GUI
        +
Sintaxe próxima do Tkinter
        +
Widgets estilizados
        +
Modo claro/escuro
        +
Aplicação desktop
        ↓
    EngConvert
```

Na Aula 01 já utilizamos:

```python
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
```

e criamos:

```python
app = ctk.CTk()
```

Agora entendemos melhor onde esses comandos se encaixam.

---

# 11. O que são widgets?

Uma interface gráfica é formada por componentes.

Esses componentes são chamados de:

> **widgets**

No EngConvert utilizaremos progressivamente:

```text
CTk()
   ↓
janela principal

CTkFrame
   ↓
área para agrupar componentes

CTkLabel
   ↓
texto

CTkEntry
   ↓
campo de entrada

CTkButton
   ↓
botão

CTkComboBox
   ↓
seleção entre opções
```

Podemos imaginar uma interface como uma estrutura composta por widgets:

```text
JANELA
│
├── FRAME
│   │
│   ├── LABEL
│   ├── ENTRY
│   ├── BUTTON
│   └── LABEL
│
└── outros componentes
```

Na próxima aula começaremos a construir essa estrutura no EngConvert.

---

# 12. O que são eventos?

Um **evento** é um acontecimento que pode ser detectado pela aplicação.

Exemplos:

```text
 usuário clica em um botão
            ↓
          evento

      usuário digita
            ↓
          evento

usuário seleciona uma opção
            ↓
          evento

  usuário fecha a janela
            ↓
          evento
```

Um botão pode, por exemplo, ser associado a uma função Python.

Mais adiante utilizaremos uma estrutura semelhante a:

```python
# A função será executada quando o botão for acionado.
botao = ctk.CTkButton(
    app,
    text="Converter",
    command=converter
)
```

Observe:

```text
usuário
   ↓
clica no botão
   ↓
evento
   ↓
função converter()
   ↓
processamento
   ↓
interface atualizada
```

Não implementaremos ainda o conversor nesta aula.

Nosso objetivo aqui é compreender o mecanismo.

---

# 13. O papel do `mainloop()`

Na Aula 01 utilizamos:

```python
app.mainloop()
```

Agora podemos compreender melhor sua função.

```text
                 ┌── clique
                 ├── digitação
mainloop() ──────┼── seleção
                 ├── redimensionamento
                 └── fechar janela
```

O `mainloop()` inicia o **loop principal de eventos da interface**.

De forma didática:

```text
janela criada
     ↓
mainloop()
     ↓
interface permanece ativa
     ↓
aguarda eventos
     ↓
processa acontecimentos
     ↓
continua aguardando
```

Por isso uma interface gráfica não funciona apenas como um script linear que termina depois da última instrução de processamento.

> 🎯 **Ideia-chave:** o `mainloop()` mantém a GUI ativa e permite que ela continue recebendo e processando eventos.

---

# 14. Juntando os conceitos

Agora podemos visualizar o funcionamento geral da aplicação:

```text
Código Python
      ↓
CustomTkinter
      ↓
Tkinter
      ↓
Tcl/Tk
      ↓
Sistema Operacional
      ↓
Janela do EngConvert
      ↓
mainloop()
      ↓
aguarda eventos
      ↓
usuário interage
      ↓
funções Python respondem
      ↓
interface é atualizada
```

Essa estrutura será a base das próximas aulas.

---

# 15. Onde estamos no desenvolvimento do EngConvert?

Até agora realizamos duas grandes etapas:

```text
Preparação do projeto
        ↓
estrutura de diretórios
        ↓
ambiente virtual
        ↓
VSCode e interpretador
        ↓
dependências
        ↓
primeira janela gráfica
```

Já temos, portanto, algo maior do que exercícios isolados.

Estamos construindo um **projeto de software**.

A partir deste ponto, precisamos visualizar:

```text
onde estamos
     ↓
para onde vamos
     ↓
o que faremos em seguida
```

É aqui que entram:

```text
ROADMAP
   +
SPRINTS
```

---

# 16. 🗺️ O que é um Roadmap?

Um **Roadmap** apresenta uma visão mais ampla da evolução planejada do projeto.

Ele responde principalmente:

> **Para onde o projeto vai?**

No EngConvert, o Roadmap pode representar grandes etapas:

```text
Etapa 1
Ambiente e estrutura
        ↓
Etapa 2
Primeira interface gráfica
        ↓
Etapa 3
Widgets e eventos
        ↓
Etapa 4
Primeiro conversor
        ↓
Etapa 5
Conversor de pressão
        ↓
Etapa 6
Novas grandezas
        ↓
Etapa 7
Modularização
        ↓
Etapa 8
Testes
        ↓
Etapa 9
Interface completa
        ↓
Etapa 10
Distribuição
```

O Roadmap não precisa descrever cada pequena tarefa.

Ele fornece a **direção geral**.

---

# 17. 🏃 O que é uma Sprint?

Uma **Sprint** representa um trecho menor e mais concreto do desenvolvimento.

Ela responde:

> **O que construiremos agora?**

Podemos visualizar:

```text
ROADMAP
   ↓
mostra a estrada
   ↓
SPRINT
   ↓
define o trecho que será percorrido agora
```

Enquanto o Roadmap apresenta várias etapas do projeto, uma Sprint concentra-se em um objetivo mais próximo.

---

# 18. Roadmap × Sprint

Compare:

| Roadmap                      | Sprint                          |
| ---------------------------- | ------------------------------- |
| visão ampla                  | foco de curto prazo             |
| mostra a evolução do projeto | define um incremento            |
| contém grandes etapas        | contém tarefas concretas        |
| responde “para onde vamos?”  | responde “o que faremos agora?” |

Uma analogia simples:

```text
ROADMAP
   ↓
mapa da viagem

SPRINT
   ↓
trecho percorrido agora
```

> 🎯 **Ideia-chave:** o Roadmap mostra a direção; as Sprints organizam os trechos do desenvolvimento.

---

# 19. 🗺️ Roadmap inicial do EngConvert

Neste momento, nosso Roadmap didático pode ser registrado assim:

```text
ROADMAP — ENGCONVERT

Etapa 1 — Ambiente e estrutura             ✓

Etapa 2 — Primeira interface gráfica       ✓

Etapa 3 — Widgets e eventos                ← PRÓXIMA

Etapa 4 — Primeiro conversor

Etapa 5 — Conversor de pressão

Etapa 6 — Novas grandezas

Etapa 7 — Modularização

Etapa 8 — Testes

Etapa 9 — Interface completa

Etapa 10 — Distribuição
```

Esse Roadmap poderá evoluir ao longo do projeto.

Isso é normal.

Planejamento de software não significa que todas as decisões precisam permanecer imutáveis.

---

# 20. 📁 Onde registrar o Roadmap?

Na estrutura do projeto já reservamos:

```text
docs/
│
├── roadmap.md
├── git-github.md
├── arquitetura.md
└── sprints/
```

Portanto:

```text
docs/roadmap.md
       ↓
visão geral da evolução do EngConvert
```

e:

```text
docs/sprints/
       ↓
registro das Sprints do projeto
```

A estrutura começa a ganhar uma função concreta.

---

# 21. 🔄 Registrando retrospectivamente o que já fizemos

Nós começamos a construir o EngConvert antes de formalizar as Sprints.

Isso não é um problema para nosso objetivo didático.

Podemos registrar retrospectivamente os primeiros ciclos de trabalho.

---

## Sprint 00 — Preparação do ambiente

### Objetivo

Preparar o ambiente e a estrutura inicial do EngConvert.

```text
SPRINT 00 — PREPARAÇÃO DO AMBIENTE

[x] criar a estrutura inicial do projeto

[x] criar a .venv

[x] ativar a .venv

[x] instalar as dependências iniciais

[x] criar requirements.txt

[x] configurar o VSCode

[x] selecionar o interpretador

[x] executar main.py

STATUS: CONCLUÍDA
```

---

## Sprint 01 — Primeira GUI

### Objetivo

Criar a primeira janela gráfica do EngConvert.

```text
SPRINT 01 — PRIMEIRA GUI

[x] importar CustomTkinter

[x] definir aparência

[x] definir tema

[x] criar CTk()

[x] definir título

[x] definir geometry()

[x] iniciar mainloop()

[x] executar a aplicação

STATUS: CONCLUÍDA
```

Agora temos duas Sprints já percorridas.

---

# 22. 🚀 Próxima Sprint

Nosso próximo objetivo será começar a construir os componentes visuais da aplicação.

```text
SPRINT 02 — WIDGETS E INTERAÇÃO

[ ] criar CTkFrame

[ ] criar CTkLabel

[ ] criar CTkEntry

[ ] criar CTkButton

[ ] organizar widgets com pack()

[ ] associar uma ação ao botão

STATUS: PLANEJADA
```

Observe que não estamos implementando tudo nesta aula.

Estamos **planejando o próximo incremento**.

---

# 23. Roadmap → Sprint → Código

A partir deste ponto, adotaremos progressivamente uma lógica de desenvolvimento:

```text
ROADMAP
   ↓
Para onde o EngConvert vai?
   ↓
SPRINT
   ↓
O que construiremos agora?
   ↓
CÓDIGO
   ↓
Implementamos
   ↓
TESTES
   ↓
Verificamos
   ↓
DOCUMENTAÇÃO
   ↓
Registramos a evolução
```

Mais adiante acrescentaremos formalmente o versionamento com Git.

```text
planejar
   ↓
implementar
   ↓
testar
   ↓
documentar
   ↓
versionar
   ↓
evoluir
```

Assim, o EngConvert passa a funcionar também como um projeto-guia para introduzir práticas de desenvolvimento de software.

---

# 24. 🧠 O que mudou desde a Aula 01?

Na Aula 01 nossa pergunta era:

> **Como criar a primeira janela?**

Nesta aula a pergunta mudou para:

> **Como essa interface funciona e como planejaremos sua evolução?**

Podemos resumir:

```text
AULA 01
   ↓
fazer funcionar
   ↓
primeira janela

AULA 02
   ↓
compreender
   +
planejar
   ↓
fundamentos da GUI
   +
Roadmap e Sprints

AULA 03
   ↓
implementar novos componentes
   ↓
widgets e eventos
```

---

# 25. 🧪 Atividade de compreensão

Sem alterar o código, responda:

1. O que significa GUI?
2. Qual a diferença básica entre um programa sequencial e uma aplicação orientada a eventos?
3. O que significa Tcl?
4. Qual é o papel do Tk?
5. Qual é o papel do Tkinter?
6. Onde o CustomTkinter se posiciona nessa arquitetura?
7. O que é um widget?
8. O que é um evento?
9. Qual é a função de `mainloop()`?
10. Qual é a diferença entre Roadmap e Sprint?
11. Quais etapas do Roadmap do EngConvert já foram concluídas?
12. Qual é a próxima Sprint planejada?

---

# 26. 📌 Resumo da Aula 02.0

Nesta aula aprofundamos os fundamentos necessários para compreender a interface gráfica do EngConvert.

```text
GUI
   ↓
interface gráfica

Tcl
   ↓
linguagem de programação

Tk
   ↓
toolkit gráfico

Tkinter
   ↓
interface Python para Tcl/Tk

CustomTkinter
   ↓
camada utilizada no EngConvert

Widgets
   ↓
componentes da interface

Eventos
   ↓
acontecimentos da aplicação

mainloop()
   ↓
loop principal de eventos
```

Também passamos a visualizar o desenvolvimento do software como um processo:

```text
ROADMAP
   ↓
direção do projeto

SPRINT
   ↓
próximo incremento

CÓDIGO
   ↓
implementação

TESTES
   ↓
verificação

DOCUMENTAÇÃO
   ↓
registro da evolução
```

---

# 27. 🔜 Próxima aula

Na próxima etapa começaremos a transformar a janela vazia em uma interface realmente interativa.

Estudaremos e utilizaremos:

```text
CTkFrame
   ↓
CTkLabel
   ↓
CTkEntry
   ↓
CTkButton
   ↓
pack()
   ↓
command
   ↓
eventos
```

A pergunta da próxima aula será:

> **Como adicionar componentes à janela e fazer a interface responder ao usuário?**

---

# 🧭 Visão do percurso

```text
AULA 00
Preparação do projeto
        ↓
AULA 01
Ambiente + primeira GUI
        ↓
AULA 02
Fundamentos da GUI
+
Roadmap e Sprints
        ↓
AULA 03
Widgets e eventos
        ↓
AULA 04
Primeiro conversor
        ↓
EVOLUÇÃO DO ENGCONVERT
```

---

> 🎯 **Ideia final:** antes de aumentar a interface, precisamos compreender a tecnologia que estamos utilizando e saber qual será o próximo passo do projeto.
