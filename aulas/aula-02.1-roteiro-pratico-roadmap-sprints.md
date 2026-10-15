# Aula 02.1 — Roteiro Prático

## Registrando o Roadmap e as Sprints do EngConvert

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Correspondência:** roteiro prático da **Aula 02.0 — Fundamentos das Interfaces Gráficas e Planejamento do EngConvert**.

---

## 🎯 Objetivo

Na Aula 02.0 estudamos GUI, Tcl/Tk, Tkinter, CustomTkinter, widgets, eventos, `mainloop()`, Roadmap e Sprints.

Agora transformaremos o planejamento em documentação real do projeto.

Ao final teremos:

```text
docs/
│
├── roadmap.md
└── sprints/
    ├── sprint-00-ambiente.md
    ├── sprint-01-interface.md
    └── sprint-02-widgets.md
```

> 📌 Nesta aula **não adicionaremos novos widgets ao `main.py`**. Vamos registrar o caminho percorrido e planejar o próximo incremento.

---

# 🧭 Visão geral

```text
abrir o EngConvert no VSCode
        ↓
verificar docs/
        ↓
preencher roadmap.md
        ↓
registrar Sprint 00
        ↓
registrar Sprint 01
        ↓
planejar Sprint 02
        ↓
conferir a documentação
        ↓
executar novamente o EngConvert
        ↓
Aula 02 concluída
```

---

# 1. Abrir o projeto

No terminal:

```powershell
cd C:\Projetos\engconvert
code .
```

O VSCode deverá abrir a pasta raiz do EngConvert.

---

# 2. Verificar `docs/`

No Explorer, localize:

```text
docs/
│
├── roadmap.md
├── sprints/
├── git-github.md
└── arquitetura.md
```

Nesta etapa utilizaremos efetivamente `roadmap.md` e `sprints/`.

---

# 3. Preencher `docs/roadmap.md`

Abra `docs/roadmap.md` e utilize:

`````markdown
# Roadmap — EngConvert

## Engineering Unit Converter

Este documento apresenta a visão geral da evolução planejada do EngConvert.

O Roadmap poderá ser atualizado conforme o projeto evoluir e novas necessidades forem identificadas.

---

## Etapas

- [x] **Etapa 1 — Ambiente e estrutura**
- [x] **Etapa 2 — Primeira interface gráfica**
- [ ] **Etapa 3 — Widgets e eventos**
- [ ] **Etapa 4 — Primeiro conversor**
- [ ] **Etapa 5 — Conversor de pressão**
- [ ] **Etapa 6 — Novas grandezas**
- [ ] **Etapa 7 — Modularização**
- [ ] **Etapa 8 — Testes**
- [ ] **Etapa 9 — Interface completa**
- [ ] **Etapa 10 — Distribuição**

---

## Situação atual

As etapas de preparação do ambiente e criação da primeira interface gráfica foram concluídas.

A próxima etapa será dedicada à introdução de widgets e eventos na interface do EngConvert.
`````

Salve com `Ctrl + S`.

---

# 4. Visualizar o Roadmap

Use:

```text
Ctrl + Shift + V
```

ou:

```text
Ctrl + K  →  V
```

Confira:

```text
☑ Etapa 1 — Ambiente e estrutura
☑ Etapa 2 — Primeira interface gráfica
☐ Etapa 3 — Widgets e eventos
```

> 🎯 **Checkpoint:** o Roadmap agora registra onde estamos e para onde o EngConvert irá evoluir.

---

# 5. Verificar `docs/sprints/`

A estrutura será:

```text
sprints/
│
├── sprint-00-ambiente.md
├── sprint-01-interface.md
└── sprint-02-widgets.md
```

Se algum arquivo não existir:

```text
botão direito em sprints/
        ↓
New File
        ↓
nome_do_arquivo.md
```

---

# 6. Registrar a Sprint 00

Abra `docs/sprints/sprint-00-ambiente.md` e utilize:

````markdown
# Sprint 00 — Preparação do Ambiente

## Objetivo

Preparar o ambiente e a estrutura inicial do EngConvert.

## Tarefas

- [x] criar a estrutura inicial do projeto;
- [x] criar a `.venv`;
- [x] ativar a `.venv`;
- [x] instalar as dependências iniciais;
- [x] criar `requirements.txt`;
- [x] configurar o VSCode;
- [x] selecionar o interpretador Python;
- [x] executar `main.py`.

## Critério de conclusão

O ambiente deve estar preparado para executar o EngConvert utilizando o interpretador Python do projeto.

## Resultado

Sprint concluída. O projeto possui estrutura inicial, ambiente virtual, dependências e configuração necessária para continuar o desenvolvimento.

## Status

**CONCLUÍDA**
````

Salve o arquivo.

---

# 7. Registrar a Sprint 01

Abra `docs/sprints/sprint-01-interface.md` e utilize:

````markdown
# Sprint 01 — Primeira Interface Gráfica

## Objetivo

Criar a primeira janela gráfica do EngConvert utilizando CustomTkinter.

## Tarefas

- [x] importar `customtkinter`;
- [x] definir o modo de aparência;
- [x] definir o tema inicial;
- [x] criar a janela com `CTk()`;
- [x] definir o título;
- [x] definir as dimensões com `geometry()`;
- [x] iniciar o loop de eventos com `mainloop()`;
- [x] executar e verificar a aplicação.

## Critério de conclusão

Ao executar:

```powershell
python main.py
```

a janela principal do EngConvert deve ser aberta corretamente.

## Resultado

Sprint concluída. O EngConvert possui sua primeira interface gráfica funcional.

## Status

**CONCLUÍDA**
````

Salve o arquivo.

---

## 📌 Mudança importante a partir da Sprint 02

As **Sprints 00 e 01** foram registradas retrospectivamente, pois suas tarefas já haviam sido realizadas.

A **Sprint 02** será diferente: ela será **planejada antes da implementação**. Por isso, suas tarefas aparecem inicialmente com `[ ]`, indicando que ainda estão pendentes.

Durante a Aula 03, à medida que essas tarefas forem realizadas, elas poderão ser alteradas para `[x]`, indicando sua conclusão.

---

# 8. Planejar a Sprint 02

Abra `docs/sprints/sprint-02-widgets.md` e utilize:

````markdown
# Sprint 02 — Widgets e Interação

## Objetivo

Adicionar os primeiros componentes visuais à janela do EngConvert e iniciar a interação com o usuário.

## Tarefas

- [ ] criar um `CTkFrame`;
- [ ] criar um `CTkLabel`;
- [ ] criar um `CTkEntry`;
- [ ] criar um `CTkButton`;
- [ ] organizar os widgets utilizando `pack()`;
- [ ] associar uma ação ao botão.

## Critério de conclusão

A janela deverá apresentar componentes organizados e possuir pelo menos uma interação acionada pelo usuário.

## Resultado

A preencher após a implementação.

## Status

**PLANEJADA**
````

Salve o arquivo.

---

# 9. Comparar as Sprints

```text
Sprint 00
   ↓
ambiente preparado
   ↓
CONCLUÍDA

Sprint 01
   ↓
primeira GUI
   ↓
CONCLUÍDA

Sprint 02
   ↓
widgets e interação
   ↓
PLANEJADA
```

Assim registramos:

```text
PASSADO
   ↓
o que já fizemos

PRESENTE
   ↓
onde estamos

PRÓXIMO PASSO
   ↓
o que faremos agora
```

---

# 10. Conferir a estrutura

Ao terminar:

```text
docs/
│
├── roadmap.md
│
├── sprints/
│   ├── sprint-00-ambiente.md
│   ├── sprint-01-interface.md
│   └── sprint-02-widgets.md
│
├── git-github.md
└── arquitetura.md
```

> 📌 `git-github.md` e `arquitetura.md` serão utilizados em etapas posteriores.

---

# 11. Conferir o `main.py`

Nesta aula **não modificaremos o `main.py`**.

Ele deve continuar com a primeira janela construída na Aula 01:

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

> 💡 Preservar o `main.py` nesta etapa evidencia a diferença entre **planejar** o próximo incremento e **implementá-lo**.

---

# 12. Executar novamente o EngConvert

Execute:

```powershell
python main.py
```

Verifique se a janela continua abrindo normalmente.

A documentação foi alterada, mas o comportamento do programa deve permanecer o mesmo.

---

# 13. Checklist

```text
[ ] abri a pasta raiz do EngConvert no VSCode
[ ] localizei docs/
[ ] preenchi docs/roadmap.md
[ ] marquei as Etapas 1 e 2 como concluídas
[ ] mantive a Etapa 3 como próxima etapa
[ ] registrei sprint-00-ambiente.md
[ ] registrei sprint-01-interface.md
[ ] planejei sprint-02-widgets.md
[ ] mantive main.py sem alterações
[ ] executei python main.py
[ ] confirmei que a janela continua funcionando
```

---

# 14. Resultado da Aula 02

```text
CONHECIMENTO
│
├── GUI
├── programação orientada a eventos
├── Tcl/Tk
├── Tkinter
├── CustomTkinter
├── widgets
├── eventos
└── mainloop()

PLANEJAMENTO
│
├── Roadmap
└── Sprints

PROJETO
│
├── Etapa 1 concluída
├── Etapa 2 concluída
└── Etapa 3 planejada
```

---

# 15. 🔜 Preparação para a Aula 03

A Sprint 02 responde:

> **O que construiremos em seguida?**

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
interação
```

Na Aula 03 começaremos sua implementação.

---

# 📌 Resumo do roteiro

```text
Aula 02.0
   ↓
compreender GUI e planejamento
   ↓
Aula 02.1
   ↓
registrar Roadmap e Sprints
   ↓
Sprint 00 — CONCLUÍDA
   ↓
Sprint 01 — CONCLUÍDA
   ↓
Sprint 02 — PLANEJADA
   ↓
Aula 03
   ↓
implementar widgets e eventos
```

> 🎯 **Ideia-chave:** desenvolver software não significa apenas escrever código. Planejar, documentar o que foi realizado e definir claramente o próximo incremento também fazem parte do desenvolvimento de um projeto.
