# Aula 03.0 — Widgets e Eventos

## Construindo a primeira interface funcional do EngConvert

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Pré-requisito:** Aulas 02.0 e 02.1 concluídas e **Sprint 02 — Widgets e Interação** planejada.

---

## 🎯 Objetivos

Ao final desta aula, o aluno deverá ser capaz de:

- compreender com maior profundidade o conceito de **widget**;
- compreender a função de um `CTkFrame`;
- utilizar `CTkLabel`, `CTkEntry` e `CTkButton`;
- compreender o funcionamento básico de `pack()`;
- associar uma função a um botão utilizando `command`;
- obter dados de um campo de entrada utilizando `.get()`;
- alterar propriedades de um widget utilizando `.configure()`;
- compreender o fluxo **evento → função → processamento → atualização da GUI**;
- relacionar os novos conteúdos com a **Sprint 02 — Widgets e Interação** planejada na Aula 02.

---

# 1. Retomando a Sprint 02

Na Aula 02.1 planejamos nossa primeira Sprint antes de sua implementação:

```text
SPRINT 02 — WIDGETS E INTERAÇÃO

[ ] criar um CTkFrame
[ ] criar um CTkLabel
[ ] criar um CTkEntry
[ ] criar um CTkButton
[ ] organizar os widgets utilizando pack()
[ ] associar uma ação ao botão

STATUS: PLANEJADA
```

Agora começaremos a compreender os elementos necessários para executar essa Sprint.

```text
Aula 02.1
   ↓
planejamos a Sprint 02
   ↓
Aula 03.0
   ↓
compreendemos widgets e eventos
   ↓
Aula 03.1
   ↓
implementamos a Sprint 02
   ↓
Sprint 02 concluída
```

> 🎯 **Ideia-chave:** primeiro planejamos o incremento; agora estudaremos os recursos necessários para implementá-lo.

---

# 2. O que é um widget?

Um **widget** é um componente gráfico utilizado na construção de uma interface.

```text
CTkFrame   → organiza outros widgets
CTkLabel   → apresenta texto
CTkEntry   → recebe dados
CTkButton  → executa uma ação
```

Podemos imaginar:

```text
JANELA PRINCIPAL
│
└── CTkFrame
    │
    ├── CTkLabel
    ├── CTkEntry
    ├── CTkButton
    └── CTkLabel
```

Cada widget possui uma responsabilidade.

---

# 3. `CTkFrame` — organizando a interface

Antes dos demais componentes, podemos criar uma área para agrupá-los:

```python
# Cria um frame dentro da janela principal.
container = ctk.CTkFrame(app)
```

Nesse comando:

```text
container
    ↓
variável que armazenará o objeto

ctk.CTkFrame(...)
    ↓
cria o frame

app
    ↓
define a janela principal como elemento pai
```

Depois:

```python
# Posiciona o frame dentro da janela.
container.pack(
    padx=30,
    pady=30,
    fill="both",
    expand=True
)
```

Estrutura:

```text
app
│
└── container
    │
    └── receberá os demais widgets
```

> 💡 **Container** é uma área utilizada para agrupar e organizar outros componentes da interface. No EngConvert, criaremos um `CTkFrame` dentro da janela principal e armazenaremos esse objeto na variável `container`.

---

# 4. O que é `pack()`?

O `pack()` é um **gerenciador de geometria**. Ele ajuda a posicionar widgets dentro de uma janela ou de outro componente.

```python
container.pack(
    padx=30,
    pady=30,
    fill="both",
    expand=True
)
```

```text
padx          → espaçamento horizontal externo
pady          → espaçamento vertical externo
fill="both"   → ocupa espaço horizontal e vertical disponível
expand=True   → utiliza espaço adicional disponível
```

Mais adiante conheceremos `grid()`, adequado a layouts estruturados em linhas e colunas.

---

# 5. `CTkLabel` — apresentando informações

Um `CTkLabel` apresenta texto:

```python
# Cria um título dentro do container.
titulo = ctk.CTkLabel(
    container,
    text="EngConvert"
)

# Posiciona o título.
titulo.pack(pady=30)
```

```text
titulo
   ↓
nome da variável

CTkLabel
   ↓
tipo do widget

container
   ↓
elemento pai

text="EngConvert"
   ↓
texto apresentado
```

---

# 6. `CTkEntry` — entrada de dados

Para receber dados digitados pelo usuário:

```python
# Cria um campo para entrada de dados.
entrada = ctk.CTkEntry(
    container,
    placeholder_text="Digite um valor"
)

# Posiciona o campo.
entrada.pack(pady=10)
```

O `placeholder_text` apresenta uma orientação enquanto o campo está vazio.

---

# 7. Obtendo o conteúdo com `.get()`

Depois que o usuário digita um valor:

```python
valor = entrada.get()
```

```text
entrada
   ↓
campo da interface
   ↓
.get()
   ↓
obtém o conteúdo
   ↓
valor
```

> 📌 Um `CTkEntry` fornece inicialmente seu conteúdo como **string**.

Se o usuário digitar `25`, o conteúdo obtido inicialmente será equivalente a `"25"`.

---

# 8. `CTkButton` — criando uma ação

Um botão pode ser criado assim:

```python
# Cria o botão.
botao = ctk.CTkButton(
    container,
    text="Converter"
)

# Posiciona o botão.
botao.pack(pady=10)
```

Mas ainda precisamos definir o que acontecerá quando o usuário clicar nele.

---

# 9. Criando a função do botão

Começamos com uma função:

```python
# Define a função que será executada pelo botão.
def converter():
    print("Botão pressionado")
```

Depois associamos a função ao botão:

```python
# Cria o botão e associa o clique à função converter.
botao = ctk.CTkButton(
    container,
    text="Converter",
    command=converter
)
```

Observe:

```python
command=converter
```

e não:

```python
command=converter()
```

No primeiro caso fornecemos ao botão a **referência da função**, que será chamada no clique. Com `converter()`, a função seria executada imediatamente durante a construção da interface.

> 🎯 **Ideia-chave:** `command=converter` conecta o evento do botão à função que responderá a esse evento.

---

# 10. Evento → função

```text
Usuário
   │
   │ clique
   ↓
CTkButton
   │
   │ command
   ↓
converter()
   │
   ↓
processamento
```

O clique é o **evento**. A função `converter()` define a resposta do programa.

---

# 11. Criando o widget de resultado

Podemos utilizar outro `CTkLabel`:

```python
# Cria o texto que apresentará o resultado.
resultado = ctk.CTkLabel(
    container,
    text="Resultado"
)

# Posiciona o widget.
resultado.pack(pady=20)
```

---

# 12. Atualizando a GUI com `.configure()`

O método `.configure()` permite alterar propriedades de um widget já criado:

```python
# Define a função executada quando o botão for pressionado.
def converter():

    # Obtém o conteúdo digitado no campo de entrada.
    valor = entrada.get()

    # Altera o texto apresentado no widget resultado.
    resultado.configure(
        text=f"Você digitou: {valor}"
    )
```

Fluxo:

```text
Usuário digita
      ↓
   CTkEntry
      ↓
    .get()
      ↓
    valor
      ↓
Usuário clica
      ↓
  CTkButton
      ↓
   command
      ↓
 converter()
      ↓
.configure()
      ↓
GUI atualizada
```

---

# 13. A primeira interface funcional mínima

```text
┌──────────────────────────────┐
│                              │
│          EngConvert          │
│                              │
│   [ Digite um valor       ]  │
│                              │
│        [ Converter ]         │
│                              │
│           Resultado          │
│                              │
└──────────────────────────────┘
```

Ainda não estamos realizando uma conversão real de unidades. O botão demonstra o funcionamento:

```text
entrada
   ↓
evento
   ↓
função
   ↓
atualização
```

---

# 14. Código completo para estudo

> 📌 Este código serve para **estudo da integração dos conceitos**. A execução passo a passo da Sprint 02 será organizada na Aula 03.1.

```python
# Importa a biblioteca CustomTkinter.
# "as ctk" cria um apelido para facilitar seu uso.
import customtkinter as ctk


# Define a função que será executada quando o botão for pressionado.
def converter():

    # Obtém o conteúdo digitado no campo de entrada.
    valor = entrada.get()

    # Atualiza o texto apresentado na interface.
    resultado.configure(
        text=f"Você digitou: {valor}"
    )


# Define o modo de aparência da aplicação.
ctk.set_appearance_mode("system")

# Define o tema inicial utilizado pelos widgets.
ctk.set_default_color_theme("blue")


# Cria a janela principal.
app = ctk.CTk()

# Define o título apresentado na barra da janela.
app.title("EngConvert")

# Define as dimensões iniciais da janela.
app.geometry("600x400")


# Cria um frame para organizar os componentes da interface.
container = ctk.CTkFrame(app)

# Posiciona o frame e permite que ele utilize o espaço disponível.
container.pack(
    padx=30,
    pady=30,
    fill="both",
    expand=True
)


# Cria o título dentro do container.
titulo = ctk.CTkLabel(
    container,
    text="EngConvert"
)

# Posiciona o título.
titulo.pack(pady=30)


# Cria o campo para entrada de dados.
entrada = ctk.CTkEntry(
    container,
    placeholder_text="Digite um valor"
)

# Posiciona o campo de entrada.
entrada.pack(pady=10)


# Cria o botão e associa o clique à função converter.
botao = ctk.CTkButton(
    container,
    text="Converter",
    command=converter
)

# Posiciona o botão.
botao.pack(pady=10)


# Cria o texto que apresentará o resultado.
resultado = ctk.CTkLabel(
    container,
    text="Resultado"
)

# Posiciona o resultado.
resultado.pack(pady=20)


# Inicia o loop principal de eventos da interface.
app.mainloop()
```

---

# 15. Hierarquia da interface

```text
app
│
└── container
    │
    ├── titulo
    │   └── CTkLabel
    │
    ├── entrada
    │   └── CTkEntry
    │
    ├── botao
    │   └── CTkButton
    │
    └── resultado
        └── CTkLabel
```

Os widgets possuem relações de organização e pertencimento. Aqui, os widgets visuais estão dentro do `container`, e o `container` está dentro de `app`.

---

# 16. Relacionando o conteúdo com a Sprint 02

Planejamos:

```text
SPRINT 02 — WIDGETS E INTERAÇÃO

[ ] criar um CTkFrame
[ ] criar um CTkLabel
[ ] criar um CTkEntry
[ ] criar um CTkButton
[ ] organizar os widgets utilizando pack()
[ ] associar uma ação ao botão
```

Todos esses elementos foram estudados nesta aula. Na Aula 03.1 eles serão implementados passo a passo.

Ao final:

```text
SPRINT 02 — WIDGETS E INTERAÇÃO

[x] criar um CTkFrame
[x] criar um CTkLabel
[x] criar um CTkEntry
[x] criar um CTkButton
[x] organizar os widgets utilizando pack()
[x] associar uma ação ao botão

STATUS: CONCLUÍDA
```

---

# 17. 🧪 Desafio de compreensão

Observe:

```python
valor = entrada.get()
```

Responda:

1. O que representa `entrada`?
2. O que faz `.get()`?
3. O que será armazenado em `valor`?
4. Qual será inicialmente o tipo do conteúdo obtido?

Agora observe:

```python
resultado.configure(
    text=f"Você digitou: {valor}"
)
```

Responda:

1. Qual widget está sendo alterado?
2. Qual propriedade está sendo modificada?
3. O que será apresentado ao usuário?

---

# 18. 🧠 Fluxo completo da interação

```text
USUÁRIO
   ↓
digita um valor
   ↓
CTkEntry
   ↓
.get()
   ↓
DADO
   ↓
usuário clica
   ↓
CTkButton
   ↓
command
   ↓
FUNÇÃO
   ↓
processamento
   ↓
.configure()
   ↓
INTERFACE ATUALIZADA
```

---

# 19. 📌 Resumo da Aula 03.0

```text
CTkFrame
   ↓
organiza widgets

CTkLabel
   ↓
apresenta informações

CTkEntry
   ↓
recebe dados

.get()
   ↓
obtém o conteúdo

CTkButton
   ↓
dispara uma ação

command
   ↓
conecta evento e função

.configure()
   ↓
altera propriedades

pack()
   ↓
posiciona widgets
```

Consolidamos:

```text
EVENTO
   ↓
FUNÇÃO
   ↓
PROCESSAMENTO
   ↓
ATUALIZAÇÃO DA GUI
```

---

# 20. 🔜 Próxima etapa — Aula 03.1

Na Aula 03.1 implementaremos a **Sprint 02 — Widgets e Interação**:

```text
abrir o projeto
      ↓
abrir main.py
      ↓
criar CTkFrame
      ↓
criar CTkLabel
      ↓
criar CTkEntry
      ↓
criar CTkButton
      ↓
organizar com pack()
      ↓
criar função
      ↓
associar command
      ↓
usar .get()
      ↓
usar .configure()
      ↓
testar a interação
      ↓
atualizar Sprint 02
      ↓
CONCLUÍDA
```

Depois estaremos preparados para introduzir o **primeiro conversor real do EngConvert**.

---

# 🧭 Visão do percurso

```text
Aula 00
Preparação
   ↓
Aula 01
Primeira GUI
   ↓
Aula 02
Fundamentos + planejamento
   ↓
Aula 03.0
Widgets e eventos
   ↓
Aula 03.1
Implementação da Sprint 02
   ↓
Aula 04
Primeiro conversor
```

> 🎯 **Ideia final:** uma interface gráfica é construída por widgets, mas ganha comportamento quando eventos são associados a funções capazes de processar informações e atualizar a própria interface.

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
