# Aula 03.1 — Roteiro Prático

## Implementando a Sprint 02 — Widgets e Interação

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Correspondência:** roteiro prático da **Aula 03.0 — Widgets e Eventos**.

---

## 🎯 Objetivo

Na Aula 03.0 estudamos os componentes e mecanismos necessários para construir uma interface interativa.

Agora iremos implementar, passo a passo, a **Sprint 02 — Widgets e Interação** planejada na Aula 02.1.

Ao final desta aula, o EngConvert deverá:

```text
abrir a janela principal
        ↓
apresentar um container
        ↓
apresentar um título
        ↓
receber um valor
        ↓
apresentar um botão
        ↓
responder ao clique
        ↓
ler o conteúdo digitado
        ↓
atualizar o resultado
```

---

# 🧭 Visão geral do roteiro

```text
abrir o projeto
      ↓
conferir a Sprint 02
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
criar converter()
      ↓
associar command
      ↓
usar .get()
      ↓
usar .configure()
      ↓
executar e testar
      ↓
atualizar a Sprint 02
      ↓
CONCLUÍDA
```

---

# 1. Abrir o projeto no VSCode

No terminal:

```powershell
cd C:\Projetos\engconvert
```

Depois:

```powershell
code .
```

Confirme que o VSCode abriu a pasta raiz:

```text
C:\Projetos\engconvert
```

---

# 2. Conferir a Sprint 02

Abra:

```text
docs/sprints/sprint-02-widgets.md
```

Ela deverá estar aproximadamente assim:

```markdown
# Sprint 02 — Widgets e Interação

## Tarefas

- [ ] criar um `CTkFrame`;
- [ ] criar um `CTkLabel`;
- [ ] criar um `CTkEntry`;
- [ ] criar um `CTkButton`;
- [ ] organizar os widgets utilizando `pack()`;
- [ ] associar uma ação ao botão.

## Status

**PLANEJADA**
```

Nesta aula iremos executar essas tarefas.

> 📌 À medida que avançarmos, poderemos acompanhar o que foi planejado e, ao final, registrar a conclusão da Sprint.

---

# 3. Abrir o `main.py`

Abra:

```text
main.py
```

Ele deverá conter a primeira janela construída anteriormente:

```python
# Importa a biblioteca CustomTkinter.
import customtkinter as ctk

# Define o modo de aparência.
ctk.set_appearance_mode("system")

# Define o tema inicial.
ctk.set_default_color_theme("blue")

# Cria a janela principal.
app = ctk.CTk()

# Define o título.
app.title("EngConvert")

# Define as dimensões iniciais.
app.geometry("700x450")

# Inicia o loop principal de eventos.
app.mainloop()
```

Agora evoluiremos esse código.

---

# 4. Criar a função `converter()`

Logo depois do `import`, adicione:

```python
# Define a função que será executada quando o botão for pressionado.
def converter():

    # Obtém o conteúdo digitado no campo de entrada.
    valor = entrada.get()

    # Atualiza o texto apresentado na interface.
    resultado.configure(
        text=f"Você digitou: {valor}"
    )
```

Neste momento, a função faz três coisas:

```text
converter()
    ↓
entrada.get()
    ↓
obtém o conteúdo
    ↓
resultado.configure()
    ↓
atualiza a interface
```

> 📌 A função pode aparecer no arquivo antes da criação dos widgets. Ela só será executada posteriormente, quando o usuário clicar no botão.

---

# 5. Ajustar o tamanho da janela

Localize:

```python
app.geometry("700x450")
```

e altere para:

```python
# Define as dimensões iniciais da janela.
app.geometry("600x400")
```

Essa dimensão será utilizada nesta etapa da interface.

---

# 6. Criar o `CTkFrame`

Antes de:

```python
app.mainloop()
```

adicione:

```python
# Cria um frame para organizar os componentes da interface.
container = ctk.CTkFrame(app)

# Posiciona o frame e permite que ele utilize o espaço disponível.
container.pack(
    padx=30,
    pady=30,
    fill="both",
    expand=True
)
```

Agora temos:

```text
app
 ↓
container
```

O `container` será a área que receberá os demais widgets.

---

# 7. Criar o título com `CTkLabel`

Depois do `container.pack(...)`, adicione:

```python
# Cria o título dentro do container.
titulo = ctk.CTkLabel(
    container,
    text="EngConvert"
)

# Posiciona o título.
titulo.pack(pady=30)
```

A hierarquia passa a ser:

```text
app
 ↓
container
 ↓
titulo
```

---

# 8. Criar o campo de entrada com `CTkEntry`

Depois do título:

```python
# Cria o campo para entrada de dados.
entrada = ctk.CTkEntry(
    container,
    placeholder_text="Digite um valor"
)

# Posiciona o campo de entrada.
entrada.pack(pady=10)
```

Ao executar posteriormente, aparecerá um campo semelhante a:

```text
[ Digite um valor ]
```

---

# 9. Criar o botão com `CTkButton`

Depois do campo de entrada:

```python
# Cria o botão e associa o clique à função converter.
botao = ctk.CTkButton(
    container,
    text="Converter",
    command=converter
)

# Posiciona o botão.
botao.pack(pady=10)
```

Observe novamente:

```python
command=converter
```

Não utilizamos:

```python
command=converter()
```

porque queremos que a função seja executada **quando ocorrer o clique**.

---

# 10. Criar o campo de resultado

Depois do botão:

```python
# Cria o texto que apresentará o resultado.
resultado = ctk.CTkLabel(
    container,
    text="Resultado"
)

# Posiciona o resultado.
resultado.pack(pady=20)
```

Nossa hierarquia agora é:

```text
app
│
└── container
    │
    ├── titulo
    ├── entrada
    ├── botao
    └── resultado
```

---

# 11. Conferir o `main.py` completo

Neste ponto, o arquivo deverá estar assim:

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

Salve o arquivo.

---

# 12. Executar o EngConvert

No terminal:

```powershell
python main.py
```

A interface deverá apresentar aproximadamente:

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

---

# 13. Testar a interação

No campo de entrada, digite:

```text
25
```

Clique:

```text
Converter
```

O resultado deverá mudar para:

```text
Você digitou: 25
```

O fluxo executado foi:

```text
25
 ↓
CTkEntry
 ↓
.get()
 ↓
valor
 ↓
clique
 ↓
command=converter
 ↓
converter()
 ↓
.configure()
 ↓
Você digitou: 25
```

---

# 14. Fazer um segundo teste

Apague o conteúdo e digite:

```text
100
```

Clique novamente em:

```text
Converter
```

Agora deverá aparecer:

```text
Você digitou: 100
```

Isso confirma que a aplicação não executa a função apenas uma vez.

Ela permanece ativa por causa do:

```python
app.mainloop()
```

e responde a novos eventos.

---

# 15. Testar a entrada vazia

Apague todo o conteúdo do campo e clique em:

```text
Converter
```

Observe o resultado.

Neste momento, o programa ainda aceita uma entrada vazia.

Isso é esperado.

Ainda não implementamos:

```text
validação
   ↓
tratamento de erro
   ↓
conversão numérica
```

Esses recursos serão introduzidos progressivamente.

---

# 16. Relacionar o teste com os conceitos

Agora podemos identificar cada parte:

```text
CTkFrame
   ↓
organização

CTkLabel
   ↓
título e resultado

CTkEntry
   ↓
entrada do usuário

.get()
   ↓
leitura da entrada

CTkButton
   ↓
acionamento

command
   ↓
conexão com a função

converter()
   ↓
resposta ao evento

.configure()
   ↓
atualização da GUI

pack()
   ↓
posicionamento
```

---

# 17. Atualizar a Sprint 02

Volte para:

```text
docs/sprints/sprint-02-widgets.md
```

Agora podemos marcar as tarefas realizadas:

```markdown
# Sprint 02 — Widgets e Interação

## Objetivo

Adicionar os primeiros componentes visuais à janela do EngConvert e iniciar a interação com o usuário.

## Tarefas

- [x] criar um `CTkFrame`;
- [x] criar um `CTkLabel`;
- [x] criar um `CTkEntry`;
- [x] criar um `CTkButton`;
- [x] organizar os widgets utilizando `pack()`;
- [x] associar uma ação ao botão.

## Critério de conclusão

A janela deverá apresentar componentes organizados e possuir pelo menos uma interação acionada pelo usuário.

## Resultado

A janela do EngConvert apresenta os primeiros widgets organizados em um `CTkFrame`.

O usuário pode digitar um valor, acionar o botão **Converter** e visualizar o conteúdo digitado no campo de resultado.

## Status

**CONCLUÍDA**
```

Salve o arquivo.

---

# 18. O que mudou na Sprint?

Antes:

```text
SPRINT 02

[ ] CTkFrame
[ ] CTkLabel
[ ] CTkEntry
[ ] CTkButton
[ ] pack()
[ ] ação do botão

STATUS: PLANEJADA
```

Depois:

```text
SPRINT 02

[x] CTkFrame
[x] CTkLabel
[x] CTkEntry
[x] CTkButton
[x] pack()
[x] ação do botão

STATUS: CONCLUÍDA
```

Temos agora o ciclo completo:

```text
PLANEJAR
   ↓
IMPLEMENTAR
   ↓
TESTAR
   ↓
VERIFICAR
   ↓
DOCUMENTAR
   ↓
CONCLUIR
```

---

# 19. Atualizar o Roadmap

Abra:

```text
docs/roadmap.md
```

Na Aula 02.1 tínhamos:

```markdown
- [x] **Etapa 1 — Ambiente e estrutura**
- [x] **Etapa 2 — Primeira interface gráfica**
- [ ] **Etapa 3 — Widgets e eventos**
- [ ] **Etapa 4 — Primeiro conversor**
```

Agora podemos atualizar para:

```markdown
- [x] **Etapa 1 — Ambiente e estrutura**
- [x] **Etapa 2 — Primeira interface gráfica**
- [x] **Etapa 3 — Widgets e eventos**
- [ ] **Etapa 4 — Primeiro conversor**
```

Salve o arquivo.

---

# 20. Conferir o Roadmap

No Preview:

```text
☑ Etapa 1 — Ambiente e estrutura
☑ Etapa 2 — Primeira interface gráfica
☑ Etapa 3 — Widgets e eventos
☐ Etapa 4 — Primeiro conversor
```

Assim:

```text
Sprint 02
   ↓
CONCLUÍDA

Etapa 3
   ↓
CONCLUÍDA

Próximo objetivo
   ↓
PRIMEIRO CONVERSOR
```

---

# 21. Checklist da Aula 03.1

Confirme:

```text
[ ] abri o EngConvert no VSCode

[ ] conferi a Sprint 02

[ ] abri main.py

[ ] criei a função converter()

[ ] criei CTkFrame

[ ] criei CTkLabel

[ ] criei CTkEntry

[ ] criei CTkButton

[ ] utilizei pack()

[ ] associei command=converter

[ ] utilizei entrada.get()

[ ] utilizei resultado.configure()

[ ] executei python main.py

[ ] testei diferentes valores

[ ] testei a entrada vazia

[ ] marquei as tarefas da Sprint 02

[ ] alterei o status para CONCLUÍDA

[ ] atualizei a Etapa 3 no Roadmap
```

---

# 22. Resultado da Aula 03

Agora o EngConvert evoluiu de:

```text
┌──────────────────────────────┐
│                              │
│                              │
│                              │
│        janela vazia          │
│                              │
│                              │
│                              │
└──────────────────────────────┘
```

para:

```text
┌──────────────────────────────┐
│                              │
│          EngConvert          │
│                              │
│   [ Digite um valor       ]  │
│                              │
│        [ Converter ]         │
│                              │
│   Você digitou: 25           │
│                              │
└──────────────────────────────┘
```

A aplicação já possui:

```text
ENTRADA
   ↓
EVENTO
   ↓
FUNÇÃO
   ↓
ATUALIZAÇÃO DA INTERFACE
```

---

# 23. 🔜 Preparação para a Aula 04

A próxima etapa do Roadmap é:

```text
Etapa 4 — Primeiro conversor
```

Agora o botão deixará de apenas repetir o conteúdo digitado.

Ele começará a realizar uma conversão real de engenharia.

O fluxo evoluirá de:

```text
entrada
   ↓
mostrar entrada
```

para:

```text
entrada
   ↓
converter para número
   ↓
aplicar relação de conversão
   ↓
calcular
   ↓
formatar resultado
   ↓
atualizar interface
```

---

# 📌 Resumo do roteiro

```text
Sprint 02 planejada
        ↓
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
.get()
        ↓
.configure()
        ↓
interface interativa
        ↓
testes
        ↓
Sprint 02 concluída
        ↓
Roadmap atualizado
        ↓
próxima etapa:
PRIMEIRO CONVERSOR
```

> 🎯 **Ideia-chave:** nesta aula percorremos pela primeira vez o ciclo completo de uma Sprint planejada antes da implementação: definimos anteriormente o que seria construído, implementamos as tarefas, testamos o resultado e registramos sua conclusão.

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
