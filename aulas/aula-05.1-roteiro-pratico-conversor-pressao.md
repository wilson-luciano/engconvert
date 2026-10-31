# Aula 05.1 — Roteiro Prático

## Implementando a Sprint 04 — Conversor de Pressão

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Correspondência:** roteiro prático da **Aula 05.0 — Conversor de Pressão**.

---

## 🎯 Objetivo

Na Aula 05.0 estudamos como evoluir o EngConvert de uma conversão fixa:

```text
bar → kPa
```

para um conversor de pressão capaz de trabalhar com múltiplas unidades.

Agora iremos implementar, passo a passo, a:

```text
SPRINT 04 — CONVERSOR DE PRESSÃO
```

Ao final desta aula, o EngConvert deverá ser capaz de:

```text
receber um valor de pressão
        ↓
selecionar a unidade "De"
        ↓
selecionar a unidade "Para"
        ↓
converter a origem para Pa
        ↓
converter de Pa para o destino
        ↓
apresentar o resultado
        ↓
inverter as unidades com ↔
        ↓
tratar entradas inválidas
```

As unidades utilizadas nesta etapa serão:

```text
Pa
kPa
MPa
bar
mbar
kgf/cm²
psi
atm
m.c.a.
```

---

# 🧭 Visão geral do roteiro

```text
abrir o projeto
      ↓
conferir o Roadmap
      ↓
registrar a Sprint 04
      ↓
abrir main.py
      ↓
criar fatores_pressao
      ↓
criar unidades_pressao
      ↓
evoluir converter()
      ↓
criar inverter_unidades()
      ↓
atualizar o subtítulo
      ↓
atualizar a entrada
      ↓
criar frame_unidades
      ↓
criar ComboBox "De"
      ↓
criar botão ↔
      ↓
criar ComboBox "Para"
      ↓
executar o programa
      ↓
realizar os testes
      ↓
atualizar Sprint 04
      ↓
CONCLUÍDA
      ↓
atualizar Roadmap
      ↓
Etapa 5 — CONCLUÍDA
```

---

# 1. Abrir o projeto no VSCode

No terminal, confirme que está trabalhando na pasta do EngConvert:

```powershell
cd C:\Projetos\engconvert
```

Depois:

```powershell
code .
```

O VSCode deverá abrir:

```text
C:\Projetos\engconvert
```

---

# 2. Conferir o Roadmap

Abra:

```text
docs/roadmap.md
```

Neste momento, as quatro primeiras etapas deverão estar concluídas:

```markdown
- [x] **Etapa 1 — Ambiente e estrutura**
- [x] **Etapa 2 — Primeira interface gráfica**
- [x] **Etapa 3 — Widgets e eventos**
- [x] **Etapa 4 — Primeiro conversor**
- [ ] **Etapa 5 — Conversor de pressão**
- [ ] **Etapa 6 — Novas grandezas**
- [ ] **Etapa 7 — Modularização**
- [ ] **Etapa 8 — Testes**
- [ ] **Etapa 9 — Interface completa**
- [ ] **Etapa 10 — Distribuição**
```

Nosso objetivo agora é concluir:

```text
Etapa 5 — Conversor de pressão
```

---

# 3. Criar o arquivo da Sprint 04

Na pasta:

```text
docs/sprints/
```

crie:

```text
sprint-04-conversor-pressao.md
```

A estrutura ficará:

```text
docs/
│
├── roadmap.md
│
└── sprints/
    │
    ├── sprint-00-ambiente.md
    ├── sprint-01-interface.md
    ├── sprint-02-widgets.md
    ├── sprint-03-primeiro-conversor.md
    └── sprint-04-conversor-pressao.md
```

---

# 4. Registrar o planejamento da Sprint 04

Abra:

```text
docs/sprints/sprint-04-conversor-pressao.md
```

e utilize:

```markdown
# Sprint 04 — Conversor de Pressão

## Objetivo

Evoluir o primeiro conversor do EngConvert para permitir a conversão entre múltiplas unidades de pressão, utilizando o pascal como unidade de referência.

## Tarefas

- [ ] criar o dicionário de fatores de pressão;
- [ ] criar a lista de unidades;
- [ ] criar o ComboBox "De";
- [ ] criar o ComboBox "Para";
- [ ] obter as unidades selecionadas;
- [ ] converter a unidade de origem para Pa;
- [ ] converter de Pa para a unidade de destino;
- [ ] apresentar o símbolo da unidade no resultado;
- [ ] criar o botão para inverter unidades;
- [ ] testar diferentes pares de conversão;
- [ ] testar entrada inválida;
- [ ] testar campo vazio.

## Critério de conclusão

O usuário deverá ser capaz de informar um valor de pressão, selecionar a unidade de origem e a unidade de destino e obter o valor convertido.

O programa também deverá permitir a inversão das unidades e tratar entradas que não possam ser convertidas para número.

## Resultado

A preencher após a implementação.

## Status

**PLANEJADA**
```

Salve o arquivo.

---

# 5. Abrir o `main.py`

Abra:

```text
main.py
```

Ao final da Aula 04.1, o EngConvert já possui uma função semelhante a:

```python
# Define a função responsável pela conversão.
def converter():

    # Tenta executar as instruções que podem gerar ValueError.
    try:

        # Obtém o conteúdo digitado e converte a string para float.
        pressao_bar = float(entrada.get())

        # Converte a pressão de bar para kPa.
        pressao_kpa = pressao_bar * 100

        # Atualiza o texto do resultado com duas casas decimais.
        resultado.configure(
            text=f"{pressao_kpa:.2f} kPa"
        )

    # Executa este bloco se a entrada não puder ser convertida para float.
    except ValueError:

        # Apresenta uma mensagem de orientação ao usuário.
        resultado.configure(
            text="Digite um valor numérico válido."
        )
```

Até aqui, a conversão está fixa:

```text
bar → kPa
```

Agora iremos generalizá-la.

---

# 6. Criar o dicionário `fatores_pressao`

Logo depois de:

```python
import customtkinter as ctk
```

adicione:

```python
# Dicionário com os fatores de conversão para pascal.
# Cada valor indica quantos Pa correspondem a uma unidade.
fatores_pressao = {
    "Pa": 1,
    "kPa": 1_000,
    "MPa": 1_000_000,
    "bar": 100_000,
    "mbar": 100,
    "kgf/cm²": 98_066.5,
    "psi": 6_894.757,
    "atm": 101_325,
    "m.c.a.": 9_806.65
}
```

Observe novamente a lógica:

```text
 CHAVE              VALOR
   ↓                  ↓
unidade          fator em Pa
```

Exemplos:

```text
"bar"       → 100_000
"psi"       → 6_894.757
"m.c.a."    → 9_806.65
```

> 📌 Nos textos e fórmulas de engenharia podemos escrever `9 806,65`. No código Python, o separador decimal é o ponto: `9_806.65`.

---

# 7. Criar a lista de unidades

Logo depois do dicionário, adicione:

```python
# Cria uma lista com as chaves do dicionário.
# Essa lista será utilizada nos dois ComboBox.
unidades_pressao = list(fatores_pressao.keys())
```

O fluxo é:

```text
fatores_pressao
       ↓
     .keys()
       ↓
chaves do dicionário
       ↓
     list()
       ↓
lista de unidades
```

A lista será equivalente a:

```python
[
    "Pa",
    "kPa",
    "MPa",
    "bar",
    "mbar",
    "kgf/cm²",
    "psi",
    "atm",
    "m.c.a."
]
```

Não precisamos escrever essa lista novamente nos dois `CTkComboBox`.

---

# 8. Evoluir a função `converter()`

Agora substitua a função `converter()` da Aula 04 por:

```python
# Define a função responsável pela conversão.
def converter():

    # Tenta executar as instruções que podem gerar ValueError.
    try:

        # Obtém o conteúdo digitado e converte a string para float.
        valor = float(entrada.get())

        # Obtém a unidade de origem selecionada.
        unidade_de = combo_de.get()

        # Obtém a unidade de destino selecionada.
        unidade_para = combo_para.get()

        # Converte o valor da unidade de origem para pascal.
        valor_pa = (
            valor * fatores_pressao[unidade_de]
        )

        # Converte o valor em pascal para a unidade de destino.
        valor_convertido = (
            valor_pa / fatores_pressao[unidade_para]
        )

        # Atualiza o resultado com duas casas decimais
        # e acrescenta o símbolo da unidade de destino.
        resultado.configure(
            text=f"{valor_convertido:.2f} {unidade_para}"
        )

    # Executa este bloco se a entrada não puder ser convertida para float.
    except ValueError:

        # Apresenta uma mensagem de orientação ao usuário.
        resultado.configure(
            text="Digite um valor numérico válido."
        )
```

---

# 9. Entender a nova sequência da conversão

A função agora realiza:

```text
entrada.get()
      ↓
float()
      ↓
valor
      ↓
combo_de.get()
      ↓
unidade_de
      ↓
fatores_pressao[unidade_de]
      ↓
origem → Pa
      ↓
combo_para.get()
      ↓
unidade_para
      ↓
fatores_pressao[unidade_para]
      ↓
Pa → destino
      ↓
valor_convertido
      ↓
resultado.configure()
```

A primeira etapa é:

```python
valor_pa = (
    valor * fatores_pressao[unidade_de]
)
```

A segunda etapa é:

```python
valor_convertido = (
    valor_pa / fatores_pressao[unidade_para]
)
```

Portanto:

```text
ORIGEM
   ↓
  Pa
   ↓
DESTINO
```

---

# 10. Criar a função `inverter_unidades()`

Depois da função `converter()`, adicione:

```python
# Define a função responsável por inverter as unidades.
def inverter_unidades():

    # Guarda temporariamente a unidade selecionada em "De".
    unidade_de = combo_de.get()

    # Guarda temporariamente a unidade selecionada em "Para".
    unidade_para = combo_para.get()

    # Coloca em "De" a unidade que estava em "Para".
    combo_de.set(unidade_para)

    # Coloca em "Para" a unidade que estava em "De".
    combo_para.set(unidade_de)
```

Essa função utiliza dois métodos que estudamos na Aula 05.0:

```text
.get()  → obtém o valor atual
.set()  → define um novo valor
```

Exemplo:

```text
ANTES

De:   bar
Para: psi
```

Depois do clique em `↔`:

```text
DEPOIS

De:   psi
Para: bar
```

---

# 11. Conferir o início do arquivo

Neste momento, o início de `main.py` deverá estar semelhante a:

```python
# Importa a biblioteca CustomTkinter.
import customtkinter as ctk


# Dicionário com os fatores de conversão para pascal.
# Cada valor indica quantos Pa correspondem a uma unidade.
fatores_pressao = {
    "Pa": 1,
    "kPa": 1_000,
    "MPa": 1_000_000,
    "bar": 100_000,
    "mbar": 100,
    "kgf/cm²": 98_066.5,
    "psi": 6_894.757,
    "atm": 101_325,
    "m.c.a.": 9_806.65
}


# Cria uma lista com as chaves do dicionário.
# Essa lista será utilizada nos dois ComboBox.
unidades_pressao = list(fatores_pressao.keys())


# Define a função responsável pela conversão.
def converter():

    try:

        valor = float(entrada.get())

        unidade_de = combo_de.get()
        unidade_para = combo_para.get()

        valor_pa = (
            valor * fatores_pressao[unidade_de]
        )

        valor_convertido = (
            valor_pa / fatores_pressao[unidade_para]
        )

        resultado.configure(
            text=f"{valor_convertido:.2f} {unidade_para}"
        )

    except ValueError:

        resultado.configure(
            text="Digite um valor numérico válido."
        )


# Define a função responsável por inverter as unidades.
def inverter_unidades():

    unidade_de = combo_de.get()
    unidade_para = combo_para.get()

    combo_de.set(unidade_para)
    combo_para.set(unidade_de)
```

> 📌 Na versão final desta aula manteremos os comentários completos. O trecho acima serve apenas para conferir a organização geral.

---

# 12. Atualizar o tamanho da janela

Localize:

```python
app.geometry("600x430")
```

Substitua por:

```python
# Define as dimensões iniciais.
app.geometry("700x520")
```

O aumento oferece espaço para os novos seletores de unidade.

---

# 13. Atualizar o subtítulo

Localize o subtítulo utilizado na Aula 04:

```python
subtitulo = ctk.CTkLabel(
    container,
    text="Pressão: bar → kPa"
)
```

Substitua por:

```python
# Cria o subtítulo da categoria atual.
subtitulo = ctk.CTkLabel(
    container,
    text="Conversor de Pressão"
)
```

Agora o programa não está mais limitado a:

```text
bar → kPa
```

Ele representa uma categoria:

```text
Conversor de Pressão
```

---

# 14. Atualizar o campo de entrada

Localize:

```python
entrada = ctk.CTkEntry(
    container,
    width=260,
    placeholder_text="Pressão em bar"
)
```

Substitua por:

```python
# Cria o campo para entrada do valor.
entrada = ctk.CTkEntry(
    container,
    width=300,
    placeholder_text="Digite o valor da pressão"
)
```

A unidade não deve mais aparecer no `placeholder_text`, porque será escolhida no seletor `De`.

---

# 15. Criar o `frame_unidades`

Depois de posicionar o campo de entrada:

```python
entrada.pack(pady=10)
```

adicione:

```python
# Cria um frame para organizar os seletores de unidade.
frame_unidades = ctk.CTkFrame(
    container,
    fg_color="transparent"
)

# Posiciona o frame das unidades.
frame_unidades.pack(pady=15)
```

A estrutura começa a ficar:

```text
container
   │
   ├── titulo
   ├── subtitulo
   ├── entrada
   │
   └── frame_unidades
```

O `frame_unidades` será o agrupamento responsável por:

```text
De       ↔       Para
```

---

# 16. Criar o `frame_de`

Adicione:

```python
# Cria o frame da unidade de origem.
frame_de = ctk.CTkFrame(
    frame_unidades,
    fg_color="transparent"
)

# Posiciona o frame da unidade de origem à esquerda.
frame_de.pack(
    side="left",
    padx=10
)
```

Observe:

```python
side="left"
```

Agora queremos colocar elementos lado a lado dentro de:

```text
frame_unidades
```

---

# 17. Criar o rótulo `De`

Adicione:

```python
# Cria o rótulo "De".
label_de = ctk.CTkLabel(
    frame_de,
    text="De"
)

# Posiciona o rótulo.
label_de.pack(pady=(0, 5))
```

A estrutura será:

```text
frame_de
   │
   └── De
```

---

# 18. Criar o `CTkComboBox` de origem

Logo depois, adicione:

```python
# Cria o ComboBox da unidade de origem.
combo_de = ctk.CTkComboBox(
    frame_de,
    values=unidades_pressao,
    width=180
)

# Posiciona o ComboBox.
combo_de.pack()
```

Agora temos:

```text
De
[ unidade ▼ ]
```

O parâmetro:

```python
values=unidades_pressao
```

fornece as opções do seletor.

---

# 19. Definir `bar` como unidade inicial

Depois de:

```python
combo_de.pack()
```

adicione:

```python
# Define "bar" como unidade inicial de origem.
combo_de.set("bar")
```

Ao abrir o programa:

```text
De
[ bar ▼ ]
```

A escolha mantém continuidade com a Aula 04.

---

# 20. Criar o botão de inversão

Agora adicione:

```python
# Cria o botão para inverter as unidades.
botao_inverter = ctk.CTkButton(
    frame_unidades,
    text="↔",
    width=50,
    command=inverter_unidades
)

# Posiciona o botão entre os dois seletores.
botao_inverter.pack(
    side="left",
    padx=5,
    pady=(25, 0)
)
```

Observe:

```python
command=inverter_unidades
```

Quando o usuário clicar:

```text
↔
```

o CustomTkinter chamará:

```python
inverter_unidades()
```

---

# 21. Criar o `frame_para`

Adicione:

```python
# Cria o frame da unidade de destino.
frame_para = ctk.CTkFrame(
    frame_unidades,
    fg_color="transparent"
)

# Posiciona o frame da unidade de destino.
frame_para.pack(
    side="left",
    padx=10
)
```

Agora o `frame_unidades` contém:

```text
frame_de
   +
botao_inverter
   +
frame_para
```

---

# 22. Criar o rótulo `Para`

Adicione:

```python
# Cria o rótulo "Para".
label_para = ctk.CTkLabel(
    frame_para,
    text="Para"
)

# Posiciona o rótulo.
label_para.pack(pady=(0, 5))
```

---

# 23. Criar o `CTkComboBox` de destino

Adicione:

```python
# Cria o ComboBox da unidade de destino.
combo_para = ctk.CTkComboBox(
    frame_para,
    values=unidades_pressao,
    width=180
)

# Posiciona o ComboBox.
combo_para.pack()
```

Teremos:

```text
Para
[ unidade ▼ ]
```

---

# 24. Definir `kPa` como unidade inicial

Depois de:

```python
combo_para.pack()
```

adicione:

```python
# Define "kPa" como unidade inicial de destino.
combo_para.set("kPa")
```

A interface deverá iniciar com:

```text
De          Para
bar    ↔    kPa
```

Assim, a conversão inicialmente exibida continua sendo a mesma da Aula 04.

---

# 25. Conferir a organização dos seletores

O trecho referente às unidades deverá estar semelhante a:

```python
# Cria um frame para organizar os seletores de unidade.
frame_unidades = ctk.CTkFrame(
    container,
    fg_color="transparent"
)

frame_unidades.pack(pady=15)


# Cria o frame da unidade de origem.
frame_de = ctk.CTkFrame(
    frame_unidades,
    fg_color="transparent"
)

frame_de.pack(
    side="left",
    padx=10
)


# Cria o rótulo "De".
label_de = ctk.CTkLabel(
    frame_de,
    text="De"
)

label_de.pack(pady=(0, 5))


# Cria o ComboBox da unidade de origem.
combo_de = ctk.CTkComboBox(
    frame_de,
    values=unidades_pressao,
    width=180
)

combo_de.pack()
combo_de.set("bar")


# Cria o botão para inverter as unidades.
botao_inverter = ctk.CTkButton(
    frame_unidades,
    text="↔",
    width=50,
    command=inverter_unidades
)

botao_inverter.pack(
    side="left",
    padx=5,
    pady=(25, 0)
)


# Cria o frame da unidade de destino.
frame_para = ctk.CTkFrame(
    frame_unidades,
    fg_color="transparent"
)

frame_para.pack(
    side="left",
    padx=10
)


# Cria o rótulo "Para".
label_para = ctk.CTkLabel(
    frame_para,
    text="Para"
)

label_para.pack(pady=(0, 5))


# Cria o ComboBox da unidade de destino.
combo_para = ctk.CTkComboBox(
    frame_para,
    values=unidades_pressao,
    width=180
)

combo_para.pack()
combo_para.set("kPa")
```

---

# 26. Manter o botão `Converter`

O botão principal continua utilizando:

```python
command=converter
```

Portanto, mantenha:

```python
# Cria o botão principal de conversão.
botao_converter = ctk.CTkButton(
    container,
    text="Converter",
    command=converter
)

# Posiciona o botão.
botao_converter.pack(pady=15)
```

Agora a mesma função `converter()` trabalha com as unidades escolhidas pelo usuário.

---

# 27. Manter o campo de resultado

Mantenha:

```python
# Cria o campo de resultado.
resultado = ctk.CTkLabel(
    container,
    text="Resultado",
    font=("Arial", 20, "bold")
)

# Posiciona o resultado.
resultado.pack(pady=20)
```

O texto será alterado pela função:

```python
resultado.configure(
    text=f"{valor_convertido:.2f} {unidade_para}"
)
```

---

# 28. Código completo da Sprint 04

Ao final das alterações, o `main.py` deverá estar assim:

```python
# Importa a biblioteca CustomTkinter.
import customtkinter as ctk


# Dicionário com os fatores de conversão para pascal.
# Cada valor indica quantos Pa correspondem a uma unidade.
fatores_pressao = {
    "Pa": 1,
    "kPa": 1_000,
    "MPa": 1_000_000,
    "bar": 100_000,
    "mbar": 100,
    "kgf/cm²": 98_066.5,
    "psi": 6_894.757,
    "atm": 101_325,
    "m.c.a.": 9_806.65
}


# Cria uma lista com as chaves do dicionário.
# Essa lista será utilizada nos dois ComboBox.
unidades_pressao = list(fatores_pressao.keys())


# Define a função responsável pela conversão.
def converter():

    # Tenta executar as instruções que podem gerar ValueError.
    try:

        # Obtém o conteúdo digitado e converte a string para float.
        valor = float(entrada.get())

        # Obtém a unidade de origem selecionada.
        unidade_de = combo_de.get()

        # Obtém a unidade de destino selecionada.
        unidade_para = combo_para.get()

        # Converte o valor da unidade de origem para pascal.
        valor_pa = (
            valor * fatores_pressao[unidade_de]
        )

        # Converte o valor em pascal para a unidade de destino.
        valor_convertido = (
            valor_pa / fatores_pressao[unidade_para]
        )

        # Atualiza o resultado com duas casas decimais
        # e acrescenta o símbolo da unidade de destino.
        resultado.configure(
            text=f"{valor_convertido:.2f} {unidade_para}"
        )

    # Executa este bloco se a entrada não puder ser convertida para float.
    except ValueError:

        # Apresenta uma mensagem de orientação ao usuário.
        resultado.configure(
            text="Digite um valor numérico válido."
        )


# Define a função responsável por inverter as unidades.
def inverter_unidades():

    # Guarda temporariamente a unidade selecionada em "De".
    unidade_de = combo_de.get()

    # Guarda temporariamente a unidade selecionada em "Para".
    unidade_para = combo_para.get()

    # Coloca em "De" a unidade que estava em "Para".
    combo_de.set(unidade_para)

    # Coloca em "Para" a unidade que estava em "De".
    combo_para.set(unidade_de)


# Define o modo de aparência da aplicação.
ctk.set_appearance_mode("system")

# Define o tema inicial.
ctk.set_default_color_theme("blue")


# Cria a janela principal.
app = ctk.CTk()

# Define o título da janela.
app.title("EngConvert")

# Define as dimensões iniciais.
app.geometry("700x520")


# Cria o frame principal.
container = ctk.CTkFrame(app)

# Posiciona o frame principal.
container.pack(
    padx=30,
    pady=30,
    fill="both",
    expand=True
)


# Cria o título principal.
titulo = ctk.CTkLabel(
    container,
    text="EngConvert",
    font=("Arial", 28, "bold")
)

# Posiciona o título.
titulo.pack(pady=(30, 5))


# Cria o subtítulo da categoria atual.
subtitulo = ctk.CTkLabel(
    container,
    text="Conversor de Pressão"
)

# Posiciona o subtítulo.
subtitulo.pack(pady=(0, 20))


# Cria o campo para entrada do valor.
entrada = ctk.CTkEntry(
    container,
    width=300,
    placeholder_text="Digite o valor da pressão"
)

# Posiciona o campo de entrada.
entrada.pack(pady=10)


# Cria um frame para organizar os seletores de unidade.
frame_unidades = ctk.CTkFrame(
    container,
    fg_color="transparent"
)

# Posiciona o frame das unidades.
frame_unidades.pack(pady=15)


# Cria o frame da unidade de origem.
frame_de = ctk.CTkFrame(
    frame_unidades,
    fg_color="transparent"
)

# Posiciona o frame da unidade de origem à esquerda.
frame_de.pack(
    side="left",
    padx=10
)


# Cria o rótulo "De".
label_de = ctk.CTkLabel(
    frame_de,
    text="De"
)

# Posiciona o rótulo.
label_de.pack(pady=(0, 5))


# Cria o ComboBox da unidade de origem.
combo_de = ctk.CTkComboBox(
    frame_de,
    values=unidades_pressao,
    width=180
)

# Posiciona o ComboBox.
combo_de.pack()

# Define "bar" como unidade inicial de origem.
combo_de.set("bar")


# Cria o botão para inverter as unidades.
botao_inverter = ctk.CTkButton(
    frame_unidades,
    text="↔",
    width=50,
    command=inverter_unidades
)

# Posiciona o botão entre os dois seletores.
botao_inverter.pack(
    side="left",
    padx=5,
    pady=(25, 0)
)


# Cria o frame da unidade de destino.
frame_para = ctk.CTkFrame(
    frame_unidades,
    fg_color="transparent"
)

# Posiciona o frame da unidade de destino.
frame_para.pack(
    side="left",
    padx=10
)


# Cria o rótulo "Para".
label_para = ctk.CTkLabel(
    frame_para,
    text="Para"
)

# Posiciona o rótulo.
label_para.pack(pady=(0, 5))


# Cria o ComboBox da unidade de destino.
combo_para = ctk.CTkComboBox(
    frame_para,
    values=unidades_pressao,
    width=180
)

# Posiciona o ComboBox.
combo_para.pack()

# Define "kPa" como unidade inicial de destino.
combo_para.set("kPa")


# Cria o botão principal de conversão.
botao_converter = ctk.CTkButton(
    container,
    text="Converter",
    command=converter
)

# Posiciona o botão.
botao_converter.pack(pady=15)


# Cria o campo de resultado.
resultado = ctk.CTkLabel(
    container,
    text="Resultado",
    font=("Arial", 20, "bold")
)

# Posiciona o resultado.
resultado.pack(pady=20)


# Inicia o loop principal de eventos.
app.mainloop()
```

Salve o arquivo.

---

# 29. Executar o EngConvert

No terminal integrado do VSCode, confirme que o ambiente virtual está ativo.

Exemplo:

```text
(.venv) PS C:\Projetos\engconvert>
```

Execute:

```powershell
python main.py
```

A janela deverá apresentar aproximadamente:

```text
┌────────────────────────────────────────────┐
│                                            │
│                 EngConvert                 │
│                                            │
│            Conversor de Pressão            │
│                                            │
│       [ Digite o valor da pressão ]        │
│                                            │
│          De        ↔        Para           │
│       [ bar ▼ ]           [ kPa ▼ ]        │
│                                            │
│              [ Converter ]                 │
│                                            │
│                 Resultado                  │
│                                            │
└────────────────────────────────────────────┘
```

---

# 30. Teste 1 — `bar → kPa`

Digite:

```text
2.5
```

Mantenha:

```text
De:   bar
Para: kPa
```

Clique:

```text
Converter
```

Resultado esperado:

```text
250.00 kPa
```

O fluxo é:

```text
2.5 bar
   ↓
250000 Pa
   ↓
250.00 kPa
```

---

# 31. Teste 2 — `bar → Pa`

Digite:

```text
1
```

Selecione:

```text
De:   bar
Para: Pa
```

Resultado esperado:

```text
100000.00 Pa
```

---

# 32. Teste 3 — `MPa → bar`

Digite:

```text
1
```

Selecione:

```text
De:   MPa
Para: bar
```

Resultado esperado:

```text
10.00 bar
```

---

# 33. Teste 4 — `kgf/cm² → m.c.a.`

Digite:

```text
1
```

Selecione:

```text
De:   kgf/cm²
Para: m.c.a.
```

Resultado esperado:

```text
10.00 m.c.a.
```

Isso ocorre porque os fatores adotados são:

```text
1 kgf/cm² = 98 066,5 Pa

1 m.c.a.  = 9 806,65 Pa
```

Logo:

```text
98 066,5
───────── = 10
9 806,65
```

---

# 34. Teste 5 — `atm → kPa`

Digite:

```text
1
```

Selecione:

```text
De:   atm
Para: kPa
```

Resultado esperado:

```text
101.33 kPa
```

O valor calculado é:

```text
101.325 kPa
```

Como estamos utilizando:

```python
:.2f
```

a apresentação será:

```text
101.33 kPa
```

---

# 35. Teste 6 — mesma unidade

Digite:

```text
25
```

Selecione:

```text
De:   psi
Para: psi
```

Resultado esperado:

```text
25.00 psi
```

O programa não precisa de uma condição especial.

Conceitualmente:

```text
25
 ×
fator de psi
 ÷
fator de psi
 =
25
```

---

# 36. Teste 7 — entrada inválida

Digite:

```text
dez
```

Clique:

```text
Converter
```

Resultado esperado:

```text
Digite um valor numérico válido.
```

O fluxo será:

```text
"dez"
   ↓
float()
   ↓
ValueError
   ↓
except
   ↓
mensagem ao usuário
```

---

# 37. Teste 8 — campo vazio

Apague o conteúdo do campo de entrada.

Clique:

```text
Converter
```

Resultado esperado:

```text
Digite um valor numérico válido.
```

O campo vazio também não pode ser convertido por:

```python
float()
```

Portanto, o `except ValueError` será executado.

---

# 38. Teste 9 — inverter as unidades

Selecione:

```text
De:   bar
Para: psi
```

Clique:

```text
↔
```

A interface deverá mudar para:

```text
De:   psi
Para: bar
```

Clique novamente:

```text
↔
```

Deverá retornar para:

```text
De:   bar
Para: psi
```

---

# 39. Teste 10 — valor negativo

Digite:

```text
-0.5
```

Por exemplo:

```text
De:   bar
Para: kPa
```

O programa deverá calcular:

```text
-50.00 kPa
```

Nesta etapa, não iremos bloquear automaticamente valores negativos.

A discussão é:

```text
VALIDAÇÃO COMPUTACIONAL
        ↓
o valor pode ser convertido para número?


VALIDAÇÃO FÍSICA
        ↓
o valor faz sentido para o problema?
```

O tratamento físico de diferentes referências de pressão poderá ser aprofundado posteriormente.

---

# 40. Conferir a lista de unidades

Clique no seletor:

```text
De
```

Confirme que aparecem:

```text
Pa
kPa
MPa
bar
mbar
kgf/cm²
psi
atm
m.c.a.
```

Faça o mesmo no seletor:

```text
Para
```

Os dois devem apresentar a mesma lista.

Isso ocorre porque ambos utilizam:

```python
values=unidades_pressao
```

---

# 41. Conferir o dicionário como fonte dos dados

Observe:

```python
unidades_pressao = list(fatores_pressao.keys())
```

Portanto:

```text
fatores_pressao
       ↓
possui as unidades e os fatores
       ↓
.keys()
       ↓
fornece os nomes das unidades
       ↓
unidades_pressao
       ↓
alimenta os ComboBox
```

Temos:

```text
DADOS
  ↓
fatores_pressao

ALGORITMO
  ↓
converter()

INTERFACE
  ↓
CTkComboBox
```

Esse é um passo importante na evolução da estrutura do EngConvert.

---

# 42. Conferir a conversão genérica

A função não contém:

```python
if unidade_de == "bar" and unidade_para == "kPa":
```

nem:

```python
elif unidade_de == "psi" and unidade_para == "bar":
```

Ela utiliza:

```python
valor_pa = (
    valor * fatores_pressao[unidade_de]
)

valor_convertido = (
    valor_pa / fatores_pressao[unidade_para]
)
```

Portanto, o mesmo algoritmo atende diferentes combinações:

```text
bar → kPa
MPa → bar
psi → atm
mbar → Pa
m.c.a. → kgf/cm²
...
```

---

# 43. Conferir o resultado da Sprint

Se os testes foram executados corretamente, o EngConvert agora possui:

```text
entrada numérica
      ↓
seleção "De"
      ↓
seleção "Para"
      ↓
conversão genérica
      ↓
resultado formatado
      ↓
tratamento de ValueError
      ↓
inversão das unidades
```

A interface deixou de representar apenas:

```text
bar → kPa
```

e passou a representar:

```text
CONVERSOR DE PRESSÃO
```

---

# 44. Atualizar o arquivo da Sprint 04

Abra:

```text
docs/sprints/sprint-04-conversor-pressao.md
```

Marque as tarefas concluídas:

```markdown
# Sprint 04 — Conversor de Pressão

## Objetivo

Evoluir o primeiro conversor do EngConvert para permitir a conversão entre múltiplas unidades de pressão, utilizando o pascal como unidade de referência.

## Tarefas

- [x] criar o dicionário de fatores de pressão;
- [x] criar a lista de unidades;
- [x] criar o ComboBox "De";
- [x] criar o ComboBox "Para";
- [x] obter as unidades selecionadas;
- [x] converter a unidade de origem para Pa;
- [x] converter de Pa para a unidade de destino;
- [x] apresentar o símbolo da unidade no resultado;
- [x] criar o botão para inverter unidades;
- [x] testar diferentes pares de conversão;
- [x] testar entrada inválida;
- [x] testar campo vazio.

## Critério de conclusão

O usuário deverá ser capaz de informar um valor de pressão, selecionar a unidade de origem e a unidade de destino e obter o valor convertido.

O programa também deverá permitir a inversão das unidades e tratar entradas que não possam ser convertidas para número.

## Resultado

O EngConvert agora permite converter valores entre múltiplas unidades de pressão utilizando o pascal como unidade intermediária.

A interface possui seletores de unidade de origem e destino, botão de inversão, apresentação do resultado e tratamento de entradas inválidas.

## Status

**CONCLUÍDA**
```

Salve o arquivo.

---

# 45. Atualizar o Roadmap

Abra:

```text
docs/roadmap.md
```

Altere:

```markdown
- [ ] **Etapa 5 — Conversor de pressão**
```

para:

```markdown
- [x] **Etapa 5 — Conversor de pressão**
```

O Roadmap ficará:

```markdown
- [x] **Etapa 1 — Ambiente e estrutura**
- [x] **Etapa 2 — Primeira interface gráfica**
- [x] **Etapa 3 — Widgets e eventos**
- [x] **Etapa 4 — Primeiro conversor**
- [x] **Etapa 5 — Conversor de pressão**
- [ ] **Etapa 6 — Novas grandezas**
- [ ] **Etapa 7 — Modularização**
- [ ] **Etapa 8 — Testes**
- [ ] **Etapa 9 — Interface completa**
- [ ] **Etapa 10 — Distribuição**
```

Salve o arquivo.

---

# 46. Estado da Sprint

Agora podemos registrar:

```text
SPRINT 04 — CONVERSOR DE PRESSÃO

STATUS:

CONCLUÍDA
```

e:

```text
ETAPA 5 — CONVERSOR DE PRESSÃO

STATUS:

CONCLUÍDA
```

---

# 47. O que o EngConvert já faz?

Neste ponto do projeto:

```text
EngConvert
   │
   ├── possui interface gráfica
   │
   ├── recebe entrada do usuário
   │
   ├── responde a eventos
   │
   ├── trata entrada inválida
   │
   ├── utiliza dados estruturados
   │
   ├── apresenta unidades em ComboBox
   │
   ├── converte entre múltiplas unidades
   │
   └── inverte origem e destino
```

O projeto deixou de ser apenas uma demonstração de GUI.

Agora temos uma aplicação de engenharia funcional.

---

# 48. Conceitos praticados nesta aula

Nesta implementação utilizamos conceitos já conhecidos:

```text
funções
variáveis
float()
dicionários
listas
f-string
try
except
ValueError
CTkFrame
CTkLabel
CTkEntry
CTkButton
pack()
command
.get()
.configure()
```

E praticamos novos elementos:

```text
.keys()
list()
CTkComboBox
values
.set()
side="left"
unidade de referência
conversão genérica
```

---

# 49. Fluxo final da Sprint 04

```text
SPRINT 04 — PLANEJADA
        ↓
criar fatores_pressao
        ↓
criar unidades_pressao
        ↓
CTkComboBox "De"
        ↓
CTkComboBox "Para"
        ↓
.get()
        ↓
origem → Pa
        ↓
Pa → destino
        ↓
f-string
        ↓
.configure()
        ↓
criar inverter_unidades()
        ↓
.set()
        ↓
botão ↔
        ↓
executar testes
        ↓
entrada inválida
        ↓
campo vazio
        ↓
atualizar Sprint 04
        ↓
SPRINT 04 — CONCLUÍDA
        ↓
atualizar Roadmap
        ↓
ETAPA 5 — CONCLUÍDA
```

---

# 50. ✅ Checklist final

Antes de encerrar a aula, confirme:

```text
[ ] o projeto abre no VSCode

[ ] o ambiente virtual está ativo

[ ] fatores_pressao foi criado

[ ] unidades_pressao foi criada

[ ] existem 9 unidades de pressão

[ ] combo_de foi criado

[ ] combo_para foi criado

[ ] bar aparece inicialmente em "De"

[ ] kPa aparece inicialmente em "Para"

[ ] converter() utiliza a unidade de origem

[ ] converter() utiliza a unidade de destino

[ ] a conversão passa por Pa

[ ] o resultado mostra a unidade de destino

[ ] inverter_unidades() funciona

[ ] o botão ↔ funciona

[ ] 2.5 bar → 250.00 kPa

[ ] 1 MPa → 10.00 bar

[ ] 1 kgf/cm² → 10.00 m.c.a.

[ ] 1 atm → 101.33 kPa

[ ] psi → psi mantém o valor

[ ] "dez" apresenta mensagem de erro

[ ] campo vazio apresenta mensagem de erro

[ ] Sprint 04 está CONCLUÍDA

[ ] Etapa 5 do Roadmap está CONCLUÍDA
```

---

# 51. 📌 Resumo da Aula 05.1

Nesta aula implementamos:

```text
DICIONÁRIO DE FATORES
        ↓
fatores_pressao

LISTA DE UNIDADES
        ↓
unidades_pressao

SELEÇÃO
        ↓
CTkComboBox

ORIGEM
        ↓
combo_de

DESTINO
        ↓
combo_para

CONVERSÃO
        ↓
origem → Pa → destino

INVERSÃO
        ↓
.get() + .set()

RESULTADO
        ↓
.configure()

VALIDAÇÃO
        ↓
try / except / ValueError
```

O EngConvert evoluiu de:

```text
bar → kPa
```

para:

```text
              CONVERSOR DE PRESSÃO

                    valor
                      ↓
            ┌─────────┴─────────┐
            ↓                   ↓
       unidade "De"        unidade "Para"
            ↓                   ↑
            └───── → Pa ────────┘
                      ↓
                  resultado
```

---

# 52. 🔜 Próxima etapa

Com a Sprint 04 concluída:

```text
Etapa 5 — Conversor de pressão
            ↓
         CONCLUÍDA
```

o Roadmap aponta para:

```text
Etapa 6 — Novas grandezas
```

O EngConvert poderá começar a crescer além da pressão.

A lógica desenvolvida nesta aula será importante para compreender como novas categorias de conversão poderão ser incorporadas ao projeto.

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
Aula 03
Widgets + interação
   ↓
Aula 04
Primeiro conversor
   ↓
Aula 05.0
Conversor de Pressão
   ↓
Aula 05.1
Implementação da Sprint 04
   ↓
Sprint 04 — CONCLUÍDA
   ↓
Etapa 5 — CONCLUÍDA
   ↓
próxima evolução
Novas grandezas
```

> 🎯 **Ideia final:** nesta Sprint, o EngConvert deixou de possuir uma conversão fixa e passou a utilizar um conjunto de dados e um algoritmo genérico para converter múltiplas unidades de pressão. A interface também evoluiu, permitindo ao usuário escolher as unidades de origem e destino e invertê-las quando necessário.

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
