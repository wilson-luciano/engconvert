# Aula 06.1 — Roteiro Prático

## Implementando a Sprint 05 — EngConvert Multicategorias

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Correspondência:** roteiro prático da **Aula 06.0 — Novas Grandezas e EngConvert Multicategorias**.  
> **Etapa do Roadmap:** Etapa 6 — Novas Grandezas.

---

# 🎯 Objetivo

Na Aula 06.0 definimos a evolução do EngConvert de um conversor dedicado à pressão para um aplicativo capaz de trabalhar com diferentes grandezas.

Agora iremos implementar:

```text
SPRINT 05 — ENGCONVERT MULTICATEGORIAS
```

Ao final desta aula, o programa deverá trabalhar com:

```text
Pressão
Comprimento
Área
Volume
Temperatura
```

e permitir:

```text
selecionar a grandeza
        ↓
atualizar automaticamente
as unidades disponíveis
        ↓
selecionar a unidade de origem
        ↓
selecionar a unidade de destino
        ↓
digitar o valor
        ↓
converter
        ↓
apresentar a saída
```

A categoria **Temperatura** utilizará:

```text
°C
°F
K
°R
```

e Volume incluirá:

```text
gal (US)
gal (UK)
```

---

# 1. Abrir o projeto

No terminal:

```powershell
cd C:\Projetos\engconvert
```

Depois:

```powershell
code .
```

Confirme que o ambiente virtual está ativo:

```text
(.venv) PS C:\Projetos\engconvert>
```

---

# 2. Conferir o Roadmap

Abra:

```text
docs/roadmap.md
```

O estado esperado é:

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

Nesta aula iremos concluir:

```text
Etapa 6 — Novas grandezas
```

---

# 3. Criar a Sprint 05

Na pasta:

```text
docs/sprints/
```

crie:

```text
sprint-05-engconvert-multicategorias.md
```

Utilize:

```markdown
# Sprint 05 — EngConvert Multicategorias

## Objetivo

Evoluir o EngConvert para trabalhar com Pressão, Comprimento, Área, Volume e Temperatura.

## Tarefas

- [ ] manter os fatores de pressão;
- [ ] criar os fatores de comprimento;
- [ ] criar os fatores de área;
- [ ] criar os fatores de volume;
- [ ] organizar as grandezas multiplicativas;
- [ ] criar as unidades de temperatura;
- [ ] criar a função de conversão de temperatura;
- [ ] criar o seletor de grandeza;
- [ ] atualizar as unidades quando a grandeza mudar;
- [ ] atualizar o conversor para múltiplas grandezas;
- [ ] manter a inversão de unidades;
- [ ] adaptar Entrada e Saída;
- [ ] testar Pressão;
- [ ] testar Comprimento;
- [ ] testar Área;
- [ ] testar Volume;
- [ ] testar gal (US);
- [ ] testar gal (UK);
- [ ] testar °C;
- [ ] testar °F;
- [ ] testar K;
- [ ] testar °R;
- [ ] testar entrada inválida.

## Status

**PLANEJADA**
```

---

# 4. Abrir o `main.py`

Abra:

```text
main.py
```

Na Aula 05.1 possuíamos apenas:

```python
fatores_pressao = {
    ...
}
```

Agora o programa terá vários conjuntos de dados.

---

# 5. Manter os fatores de pressão

Mantenha:

```python
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

O pascal continua sendo a unidade de referência dessa categoria.

---

# 6. Criar os fatores de comprimento

Adicione:

```python
# Fatores em relação ao metro.
fatores_comprimento = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1_000,
    "in": 0.0254,
    "ft": 0.3048
}
```

A referência é:

```text
m
```

---

# 7. Criar os fatores de área

Adicione:

```python
# Fatores em relação ao metro quadrado.
fatores_area = {
    "mm²": 0.000001,
    "cm²": 0.0001,
    "m²": 1,
    "in²": 0.00064516,
    "ft²": 0.09290304
}
```

A referência é:

```text
m²
```

---

# 8. Criar os fatores de volume

Adicione:

```python
# Fatores em relação ao metro cúbico.
fatores_volume = {
    "mL": 0.000001,
    "cm³": 0.000001,
    "L": 0.001,
    "m³": 1,
    "in³": 0.000016387064,
    "ft³": 0.028316846592,
    "gal (US)": 0.003785411784,
    "gal (UK)": 0.00454609
}
```

Observe que:

```text
gal (US) ≠ gal (UK)
```

---

# 9. Criar o dicionário `grandezas`

Agora agruparemos as grandezas que utilizam conversão multiplicativa:

```python
# Organiza as grandezas que utilizam fatores multiplicativos.
grandezas = {
    "Pressão": fatores_pressao,
    "Comprimento": fatores_comprimento,
    "Área": fatores_area,
    "Volume": fatores_volume
}
```

Temos:

```text
grandezas
   │
   ├── Pressão
   ├── Comprimento
   ├── Área
   └── Volume
```

Cada chave aponta para outro dicionário.

---

# 10. Criar as unidades de temperatura

Temperatura não utilizará o mesmo dicionário de fatores.

Adicione:

```python
# Unidades disponíveis para temperatura.
unidades_temperatura = [
    "°C",
    "°F",
    "K",
    "°R"
]
```

---

# 11. Criar a lista de grandezas

Adicione:

```python
# Lista apresentada no seletor de grandeza.
lista_grandezas = [
    "Pressão",
    "Comprimento",
    "Área",
    "Volume",
    "Temperatura"
]
```

Essa lista alimentará o novo `CTkComboBox`.

---

# 12. Estratégia para temperatura

Para evitar criar uma fórmula diferente diretamente para cada par, utilizaremos uma unidade intermediária:

```text
ORIGEM
   ↓
 kelvin
   ↓
DESTINO
```

A ideia é semelhante ao que já fizemos com pressão:

```text
Pressão:
origem → Pa → destino

Temperatura:
origem → K → destino
```

A diferença é que, em temperatura, a passagem para a referência pode envolver multiplicação **e deslocamento**.

---

# 13. Criar `converter_temperatura()`

Adicione antes da função principal `converter()`:

```python
# Converte temperaturas utilizando kelvin como referência.
def converter_temperatura(valor, unidade_de, unidade_para):

    # Primeiro converte a unidade de origem para kelvin.
    if unidade_de == "°C":
        valor_k = valor + 273.15

    elif unidade_de == "°F":
        valor_k = (valor - 32) * 5 / 9 + 273.15

    elif unidade_de == "K":
        valor_k = valor

    elif unidade_de == "°R":
        valor_k = valor * 5 / 9

    # Depois converte de kelvin para a unidade de destino.
    if unidade_para == "°C":
        return valor_k - 273.15

    elif unidade_para == "°F":
        return (valor_k - 273.15) * 9 / 5 + 32

    elif unidade_para == "K":
        return valor_k

    elif unidade_para == "°R":
        return valor_k * 9 / 5
```

O fluxo é:

```text
°C ─┐
°F ─┤
K  ─┼── → K ─── → destino
°R ─┘
```

---

# 14. Exemplos da função de temperatura

Para:

```text
0 °C → °F
```

temos:

```text
0 °C
  ↓
273,15 K
  ↓
32 °F
```

Para:

```text
32 °F → °R
```

temos:

```text
32 °F
   ↓
273,15 K
   ↓
491,67 °R
```

Para:

```text
0 K → °R
```

temos:

```text
0 K
 ↓
0 °R
```

---

# 15. Criar a função `obter_unidades()`

Precisamos descobrir quais unidades pertencem à grandeza selecionada.

Adicione:

```python
# Retorna as unidades da grandeza selecionada.
def obter_unidades(grandeza):

    # Temperatura utiliza uma lista própria.
    if grandeza == "Temperatura":
        return unidades_temperatura

    # As demais grandezas utilizam as chaves
    # de seus respectivos dicionários.
    return list(grandezas[grandeza].keys())
```

Exemplos:

```python
obter_unidades("Pressão")
```

retorna as unidades de pressão.

Enquanto:

```python
obter_unidades("Volume")
```

retorna:

```text
mL
cm³
L
m³
in³
ft³
gal (US)
gal (UK)
```

---

# 16. Criar `atualizar_unidades()`

Quando o usuário alterar a grandeza, os seletores `De` e `Para` também deverão mudar.

Adicione:

```python
# Atualiza os ComboBox quando a grandeza é alterada.
def atualizar_unidades(grandeza_selecionada):

    # Obtém as unidades correspondentes.
    unidades = obter_unidades(grandeza_selecionada)

    # Atualiza as opções do ComboBox "De".
    combo_de.configure(values=unidades)

    # Atualiza as opções do ComboBox "Para".
    combo_para.configure(values=unidades)

    # Define a primeira unidade como origem.
    combo_de.set(unidades[0])

    # Define a segunda unidade como destino.
    combo_para.set(unidades[1])

    # Limpa a saída anterior.
    resultado.configure(text="Resultado")
```

Agora:

```text
mudar a grandeza
        ↓
atualizar_unidades()
        ↓
novas unidades em "De"
        ↓
novas unidades em "Para"
```

---

# 17. Evoluir a função `converter()`

Substitua a função da Aula 05.1 por:

```python
# Realiza a conversão selecionada pelo usuário.
def converter():

    try:

        # Obtém e converte a entrada para float.
        valor = float(entrada.get())

        # Obtém a grandeza atual.
        grandeza = combo_grandeza.get()

        # Obtém as unidades selecionadas.
        unidade_de = combo_de.get()
        unidade_para = combo_para.get()

        # Temperatura possui uma estratégia específica.
        if grandeza == "Temperatura":

            valor_convertido = converter_temperatura(
                valor,
                unidade_de,
                unidade_para
            )

        # As demais grandezas utilizam fatores.
        else:

            # Obtém o dicionário da grandeza selecionada.
            fatores = grandezas[grandeza]

            # Converte a origem para a unidade de referência.
            valor_referencia = (
                valor * fatores[unidade_de]
            )

            # Converte da referência para o destino.
            valor_convertido = (
                valor_referencia
                / fatores[unidade_para]
            )

        # Apresenta o resultado.
        resultado.configure(
            text=f"{valor_convertido:.6g} {unidade_para}"
        )

    except ValueError:

        resultado.configure(
            text="Digite um valor numérico válido."
        )
```

---

# 18. Por que utilizar `:.6g`?

Na Aula 05 utilizamos:

```python
:.2f
```

Isso é adequado para muitos resultados, mas agora teremos valores muito diferentes.

Por exemplo:

```text
1 m² = 1 000 000 mm²
```

e:

```text
1 mL = 0,000001 m³
```

Nesta etapa utilizaremos:

```python
:.6g
```

para apresentar até seis algarismos significativos de forma mais compacta.

Mais adiante, o EngConvert poderá oferecer configuração de precisão.

---

# 19. Manter `inverter_unidades()`

A função continua válida:

```python
# Inverte as unidades de origem e destino.
def inverter_unidades():

    unidade_de = combo_de.get()
    unidade_para = combo_para.get()

    combo_de.set(unidade_para)
    combo_para.set(unidade_de)
```

Observe que ela não precisa saber se estamos convertendo:

```text
Pressão
Comprimento
Área
Volume
Temperatura
```

Ela apenas troca as duas seleções.

---

# 20. Evoluir a interface

Agora criaremos um novo seletor:

```text
Grandeza
```

A interface deverá seguir:

```text
Grandeza
    ↓
De ↔ Para
    ↓
Entrada
    ↓
Converter
    ↓
Saída
```

---

# 21. Atualizar o subtítulo

Utilize:

```python
subtitulo = ctk.CTkLabel(
    container,
    text="Conversor de Unidades de Engenharia"
)
```

Agora o programa não é mais apenas um conversor de pressão.

---

# 22. Criar o rótulo `Grandeza`

Antes dos seletores de unidade, adicione:

```python
# Cria o rótulo do seletor de grandeza.
label_grandeza = ctk.CTkLabel(
    container,
    text="Grandeza"
)

label_grandeza.pack(pady=(10, 5))
```

---

# 23. Criar `combo_grandeza`

Adicione:

```python
# Cria o seletor de grandeza.
combo_grandeza = ctk.CTkComboBox(
    container,
    values=lista_grandezas,
    width=300,
    command=atualizar_unidades
)

combo_grandeza.pack(pady=(0, 15))
```

A novidade está em:

```python
command=atualizar_unidades
```

Quando o usuário escolher uma grandeza, o CustomTkinter chamará a função.

---

# 24. Definir a grandeza inicial

Depois de:

```python
combo_grandeza.pack(...)
```

adicione:

```python
combo_grandeza.set("Pressão")
```

O EngConvert abrirá inicialmente na categoria já conhecida pelos alunos.

---

# 25. Posicionar as unidades antes da entrada

Nesta versão, organizaremos visualmente:

```text
Grandeza

De        ↔        Para

Entrada

Converter

Saída
```

Isso deixa clara a sequência:

```text
o que converter?
        ↓
entre quais unidades?
        ↓
qual valor?
```

---

# 26. Criar o `frame_unidades`

Utilize:

```python
frame_unidades = ctk.CTkFrame(
    container,
    fg_color="transparent"
)

frame_unidades.pack(pady=10)
```

Dentro dele permanecerão:

```text
frame_de
botao_inverter
frame_para
```

---

# 27. Criar o seletor `De`

```python
frame_de = ctk.CTkFrame(
    frame_unidades,
    fg_color="transparent"
)

frame_de.pack(
    side="left",
    padx=10
)

label_de = ctk.CTkLabel(
    frame_de,
    text="De"
)

label_de.pack(pady=(0, 5))

combo_de = ctk.CTkComboBox(
    frame_de,
    values=list(fatores_pressao.keys()),
    width=180
)

combo_de.pack()
combo_de.set("bar")
```

---

# 28. Manter o botão `↔`

```python
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
```

---

# 29. Criar o seletor `Para`

```python
frame_para = ctk.CTkFrame(
    frame_unidades,
    fg_color="transparent"
)

frame_para.pack(
    side="left",
    padx=10
)

label_para = ctk.CTkLabel(
    frame_para,
    text="Para"
)

label_para.pack(pady=(0, 5))

combo_para = ctk.CTkComboBox(
    frame_para,
    values=list(fatores_pressao.keys()),
    width=180
)

combo_para.pack()
combo_para.set("kPa")
```

---

# 30. Criar o rótulo `Entrada`

Antes do campo de entrada:

```python
label_entrada = ctk.CTkLabel(
    container,
    text="Entrada"
)

label_entrada.pack(pady=(15, 5))
```

---

# 31. Atualizar o `CTkEntry`

Utilize:

```python
entrada = ctk.CTkEntry(
    container,
    width=300,
    placeholder_text="Digite o valor"
)

entrada.pack(pady=(0, 10))
```

Agora a unidade não precisa aparecer no campo.

Ela já está identificada em:

```text
De
```

---

# 32. Manter o botão `Converter`

```python
botao_converter = ctk.CTkButton(
    container,
    text="Converter",
    command=converter
)

botao_converter.pack(pady=15)
```

---

# 33. Criar o rótulo `Saída`

Adicione:

```python
label_saida = ctk.CTkLabel(
    container,
    text="Saída"
)

label_saida.pack(pady=(10, 5))
```

E mantenha o resultado:

```python
resultado = ctk.CTkLabel(
    container,
    text="Resultado",
    font=("Arial", 20, "bold")
)

resultado.pack(pady=(0, 20))
```

---

# 34. Fluxo visual esperado

A aplicação deverá apresentar aproximadamente:

```text
┌──────────────────────────────────────────────┐
│                  EngConvert                  │
│                                              │
│      Conversor de Unidades de Engenharia     │
│                                              │
│                  Grandeza                    │
│              [ Pressão ▼ ]                   │
│                                              │
│          De       ↔        Para              │
│       [ bar ▼ ]         [ kPa ▼ ]            │
│                                              │
│                  Entrada                     │
│              [           ]                   │
│                                              │
│               [ Converter ]                  │
│                                              │
│                   Saída                      │
│                 Resultado                    │
│                                              │
└──────────────────────────────────────────────┘
```

---

# 35. Código completo da Sprint 05

Substitua o conteúdo de `main.py` pela versão completa abaixo:

```python
# Importa a biblioteca CustomTkinter.
import customtkinter as ctk


# ---------------------------------------------------------
# DADOS
# ---------------------------------------------------------

# Fatores de pressão em relação ao pascal.
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


# Fatores de comprimento em relação ao metro.
fatores_comprimento = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1_000,
    "in": 0.0254,
    "ft": 0.3048
}


# Fatores de área em relação ao metro quadrado.
fatores_area = {
    "mm²": 0.000001,
    "cm²": 0.0001,
    "m²": 1,
    "in²": 0.00064516,
    "ft²": 0.09290304
}


# Fatores de volume em relação ao metro cúbico.
fatores_volume = {
    "mL": 0.000001,
    "cm³": 0.000001,
    "L": 0.001,
    "m³": 1,
    "in³": 0.000016387064,
    "ft³": 0.028316846592,
    "gal (US)": 0.003785411784,
    "gal (UK)": 0.00454609
}


# Organiza as grandezas com conversão multiplicativa.
grandezas = {
    "Pressão": fatores_pressao,
    "Comprimento": fatores_comprimento,
    "Área": fatores_area,
    "Volume": fatores_volume
}


# Unidades disponíveis para temperatura.
unidades_temperatura = [
    "°C",
    "°F",
    "K",
    "°R"
]


# Lista apresentada no seletor de grandeza.
lista_grandezas = [
    "Pressão",
    "Comprimento",
    "Área",
    "Volume",
    "Temperatura"
]


# ---------------------------------------------------------
# FUNÇÕES
# ---------------------------------------------------------

# Converte temperaturas utilizando kelvin como referência.
def converter_temperatura(valor, unidade_de, unidade_para):

    # Converte a origem para kelvin.
    if unidade_de == "°C":
        valor_k = valor + 273.15

    elif unidade_de == "°F":
        valor_k = (valor - 32) * 5 / 9 + 273.15

    elif unidade_de == "K":
        valor_k = valor

    elif unidade_de == "°R":
        valor_k = valor * 5 / 9

    # Converte de kelvin para o destino.
    if unidade_para == "°C":
        return valor_k - 273.15

    elif unidade_para == "°F":
        return (valor_k - 273.15) * 9 / 5 + 32

    elif unidade_para == "K":
        return valor_k

    elif unidade_para == "°R":
        return valor_k * 9 / 5


# Retorna as unidades da grandeza selecionada.
def obter_unidades(grandeza):

    if grandeza == "Temperatura":
        return unidades_temperatura

    return list(grandezas[grandeza].keys())


# Atualiza os ComboBox quando a grandeza muda.
def atualizar_unidades(grandeza_selecionada):

    unidades = obter_unidades(grandeza_selecionada)

    combo_de.configure(values=unidades)
    combo_para.configure(values=unidades)

    combo_de.set(unidades[0])
    combo_para.set(unidades[1])

    resultado.configure(text="Resultado")


# Realiza a conversão.
def converter():

    try:

        valor = float(entrada.get())

        grandeza = combo_grandeza.get()

        unidade_de = combo_de.get()
        unidade_para = combo_para.get()

        # Temperatura possui conversão específica.
        if grandeza == "Temperatura":

            valor_convertido = converter_temperatura(
                valor,
                unidade_de,
                unidade_para
            )

        # As demais grandezas utilizam fatores.
        else:

            fatores = grandezas[grandeza]

            valor_referencia = (
                valor * fatores[unidade_de]
            )

            valor_convertido = (
                valor_referencia
                / fatores[unidade_para]
            )

        resultado.configure(
            text=f"{valor_convertido:.6g} {unidade_para}"
        )

    except ValueError:

        resultado.configure(
            text="Digite um valor numérico válido."
        )


# Inverte as unidades.
def inverter_unidades():

    unidade_de = combo_de.get()
    unidade_para = combo_para.get()

    combo_de.set(unidade_para)
    combo_para.set(unidade_de)


# ---------------------------------------------------------
# CONFIGURAÇÃO DA INTERFACE
# ---------------------------------------------------------

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


# Cria a janela principal.
app = ctk.CTk()

app.title("EngConvert")
app.geometry("700x650")


# Cria o frame principal.
container = ctk.CTkFrame(app)

container.pack(
    padx=30,
    pady=30,
    fill="both",
    expand=True
)


# Título.
titulo = ctk.CTkLabel(
    container,
    text="EngConvert",
    font=("Arial", 28, "bold")
)

titulo.pack(pady=(25, 5))


# Subtítulo.
subtitulo = ctk.CTkLabel(
    container,
    text="Conversor de Unidades de Engenharia"
)

subtitulo.pack(pady=(0, 15))


# ---------------------------------------------------------
# SELETOR DE GRANDEZA
# ---------------------------------------------------------

label_grandeza = ctk.CTkLabel(
    container,
    text="Grandeza"
)

label_grandeza.pack(pady=(10, 5))


combo_grandeza = ctk.CTkComboBox(
    container,
    values=lista_grandezas,
    width=300,
    command=atualizar_unidades
)

combo_grandeza.pack(pady=(0, 15))

combo_grandeza.set("Pressão")


# ---------------------------------------------------------
# SELETORES DE UNIDADE
# ---------------------------------------------------------

frame_unidades = ctk.CTkFrame(
    container,
    fg_color="transparent"
)

frame_unidades.pack(pady=10)


# Unidade de origem.
frame_de = ctk.CTkFrame(
    frame_unidades,
    fg_color="transparent"
)

frame_de.pack(
    side="left",
    padx=10
)


label_de = ctk.CTkLabel(
    frame_de,
    text="De"
)

label_de.pack(pady=(0, 5))


combo_de = ctk.CTkComboBox(
    frame_de,
    values=list(fatores_pressao.keys()),
    width=180
)

combo_de.pack()
combo_de.set("bar")


# Botão de inversão.
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


# Unidade de destino.
frame_para = ctk.CTkFrame(
    frame_unidades,
    fg_color="transparent"
)

frame_para.pack(
    side="left",
    padx=10
)


label_para = ctk.CTkLabel(
    frame_para,
    text="Para"
)

label_para.pack(pady=(0, 5))


combo_para = ctk.CTkComboBox(
    frame_para,
    values=list(fatores_pressao.keys()),
    width=180
)

combo_para.pack()
combo_para.set("kPa")


# ---------------------------------------------------------
# ENTRADA
# ---------------------------------------------------------

label_entrada = ctk.CTkLabel(
    container,
    text="Entrada"
)

label_entrada.pack(pady=(15, 5))


entrada = ctk.CTkEntry(
    container,
    width=300,
    placeholder_text="Digite o valor"
)

entrada.pack(pady=(0, 10))


# ---------------------------------------------------------
# BOTÃO CONVERTER
# ---------------------------------------------------------

botao_converter = ctk.CTkButton(
    container,
    text="Converter",
    command=converter
)

botao_converter.pack(pady=15)


# ---------------------------------------------------------
# SAÍDA
# ---------------------------------------------------------

label_saida = ctk.CTkLabel(
    container,
    text="Saída"
)

label_saida.pack(pady=(10, 5))


resultado = ctk.CTkLabel(
    container,
    text="Resultado",
    font=("Arial", 20, "bold")
)

resultado.pack(pady=(0, 20))


# Inicia o loop principal de eventos.
app.mainloop()
```

---

# 36. Executar o programa

No terminal:

```powershell
python main.py
```

Confirme que aparece:

```text
EngConvert

Conversor de Unidades de Engenharia

Grandeza
[ Pressão ▼ ]

De              Para
[ bar ▼ ] ↔ [ kPa ▼ ]

Entrada
[             ]

[ Converter ]

Saída
Resultado
```

---

# 37. Testar a atualização da grandeza

Sem digitar nenhum valor, altere:

```text
Pressão
```

para:

```text
Comprimento
```

Os seletores deverão mudar automaticamente para unidades de comprimento.

Depois selecione:

```text
Área
```

Depois:

```text
Volume
```

Depois:

```text
Temperatura
```

Confirme que as unidades mudam em cada caso.

---

# 38. Teste — Pressão

Selecione:

```text
Grandeza: Pressão
De:       bar
Para:     kPa
Entrada:  1
```

Resultado esperado:

```text
100 kPa
```

---

# 39. Teste — Comprimento

Selecione:

```text
Grandeza: Comprimento
De:       m
Para:     mm
Entrada:  1
```

Resultado esperado:

```text
1000 mm
```

---

# 40. Teste — Área

Selecione:

```text
Grandeza: Área
De:       m²
Para:     mm²
Entrada:  1
```

Resultado esperado:

```text
1e+06 mm²
```

> 📌 Com `:.6g`, números grandes podem ser apresentados em notação científica. A configuração de apresentação será refinada posteriormente.

---

# 41. Teste — Volume

Selecione:

```text
Grandeza: Volume
De:       L
Para:     mL
Entrada:  1
```

Resultado esperado:

```text
1000 mL
```

---

# 42. Teste — galão americano

Selecione:

```text
Grandeza: Volume
De:       gal (US)
Para:     L
Entrada:  1
```

Resultado aproximado:

```text
3.78541 L
```

---

# 43. Teste — galão imperial

Selecione:

```text
Grandeza: Volume
De:       gal (UK)
Para:     L
Entrada:  1
```

Resultado esperado:

```text
4.54609 L
```

Isso confirma novamente:

```text
gal (US) ≠ gal (UK)
```

---

# 44. Teste — litro para galão US

Selecione:

```text
Grandeza: Volume
De:       L
Para:     gal (US)
Entrada:  1
```

Resultado aproximado:

```text
0.264172 gal (US)
```

---

# 45. Teste — Celsius para Fahrenheit

Selecione:

```text
Grandeza: Temperatura
De:       °C
Para:     °F
Entrada:  0
```

Resultado esperado:

```text
32 °F
```

---

# 46. Teste — Celsius para kelvin

Selecione:

```text
Grandeza: Temperatura
De:       °C
Para:     K
Entrada:  0
```

Resultado esperado:

```text
273.15 K
```

Observe:

```text
K
```

e não:

```text
°K
```

---

# 47. Teste — Fahrenheit para Rankine

Selecione:

```text
Grandeza: Temperatura
De:       °F
Para:     °R
Entrada:  32
```

Resultado esperado:

```text
491.67 °R
```

---

# 48. Teste — kelvin para Rankine

Selecione:

```text
Grandeza: Temperatura
De:       K
Para:     °R
Entrada:  0
```

Resultado esperado:

```text
0 °R
```

Temos:

```text
0 K = 0 °R
```

---

# 49. Teste — inversão

Selecione:

```text
Grandeza: Volume
De:       L
Para:     gal (US)
```

Clique:

```text
↔
```

O resultado deverá ser:

```text
De:       gal (US)
Para:     L
```

A mesma função de inversão continua funcionando em todas as categorias.

---

# 50. Teste — entrada inválida

Digite:

```text
abc
```

Clique:

```text
Converter
```

Resultado esperado:

```text
Digite um valor numérico válido.
```

---

# 51. O que mudou no algoritmo?

Na Aula 05:

```text
Pressão
   ↓
origem → Pa → destino
```

Agora:

```text
Grandeza selecionada
        ↓
        ├── Pressão
        ├── Comprimento
        ├── Área
        └── Volume
               ↓
          usar fatores
```

ou:

```text
Grandeza selecionada
        ↓
Temperatura
        ↓
converter_temperatura()
        ↓
origem → K → destino
```

---

# 52. Dados, lógica e interface

O `main.py` já começa a apresentar três regiões conceituais:

```text
DADOS
  ↓
fatores
grandezas
listas

LÓGICA
  ↓
converter_temperatura()
obter_unidades()
atualizar_unidades()
converter()
inverter_unidades()

INTERFACE
  ↓
CTk
frames
labels
ComboBox
Entry
Button
```

Ainda está tudo no mesmo arquivo.

Isso é proposital nesta etapa.

Primeiro compreendemos o funcionamento completo.

Depois surgirá naturalmente a necessidade de modularizar.

---

# 53. Atualizar a Sprint 05

Abra:

```text
docs/sprints/sprint-05-engconvert-multicategorias.md
```

Depois de concluir os testes, altere as tarefas para:

```markdown
- [x] manter os fatores de pressão;
- [x] criar os fatores de comprimento;
- [x] criar os fatores de área;
- [x] criar os fatores de volume;
- [x] organizar as grandezas multiplicativas;
- [x] criar as unidades de temperatura;
- [x] criar a função de conversão de temperatura;
- [x] criar o seletor de grandeza;
- [x] atualizar as unidades quando a grandeza mudar;
- [x] atualizar o conversor para múltiplas grandezas;
- [x] manter a inversão de unidades;
- [x] adaptar Entrada e Saída;
- [x] testar Pressão;
- [x] testar Comprimento;
- [x] testar Área;
- [x] testar Volume;
- [x] testar gal (US);
- [x] testar gal (UK);
- [x] testar °C;
- [x] testar °F;
- [x] testar K;
- [x] testar °R;
- [x] testar entrada inválida.
```

E:

```markdown
## Resultado

O EngConvert passou a trabalhar com Pressão, Comprimento, Área, Volume e Temperatura.

As unidades são atualizadas de acordo com a grandeza selecionada. Pressão, Comprimento, Área e Volume utilizam fatores multiplicativos, enquanto Temperatura utiliza uma função específica com kelvin como referência.

## Status

**CONCLUÍDA**
```

---

# 54. Atualizar o Roadmap

Abra:

```text
docs/roadmap.md
```

Altere:

```markdown
- [ ] **Etapa 6 — Novas grandezas**
```

para:

```markdown
- [x] **Etapa 6 — Novas grandezas**
```

O Roadmap ficará:

```markdown
- [x] **Etapa 1 — Ambiente e estrutura**
- [x] **Etapa 2 — Primeira interface gráfica**
- [x] **Etapa 3 — Widgets e eventos**
- [x] **Etapa 4 — Primeiro conversor**
- [x] **Etapa 5 — Conversor de pressão**
- [x] **Etapa 6 — Novas grandezas**
- [ ] **Etapa 7 — Modularização**
- [ ] **Etapa 8 — Testes**
- [ ] **Etapa 9 — Interface completa**
- [ ] **Etapa 10 — Distribuição**
```

---

# 55. Estado da Sprint

```text
SPRINT 05 — ENGCONVERT MULTICATEGORIAS

STATUS:

CONCLUÍDA
```

e:

```text
ETAPA 6 — NOVAS GRANDEZAS

STATUS:

CONCLUÍDA
```

---

# 56. O que o EngConvert já faz?

Agora temos:

```text
EngConvert
   │
   ├── Pressão
   │
   ├── Comprimento
   │
   ├── Área
   │
   ├── Volume
   │      ├── gal (US)
   │      └── gal (UK)
   │
   └── Temperatura
          ├── °C
          ├── °F
          ├── K
          └── °R
```

Além disso:

```text
seleciona grandeza
      ↓
atualiza unidades
      ↓
seleciona origem
      ↓
seleciona destino
      ↓
recebe entrada
      ↓
converte
      ↓
apresenta saída
```

---

# 57. Conceitos praticados

Nesta Sprint utilizamos:

```text
dicionários
dicionários aninhados
listas
funções
parâmetros
return
if
elif
else
try
except
ValueError
float()
.get()
.set()
.configure()
CTkComboBox
command
eventos
f-string
```

E introduzimos uma ideia importante:

```text
diferentes problemas
podem exigir
diferentes estratégias
```

---

# 58. Checklist final

Confirme:

```text
[ ] Pressão aparece no seletor de grandeza
[ ] Comprimento aparece no seletor
[ ] Área aparece no seletor
[ ] Volume aparece no seletor
[ ] Temperatura aparece no seletor

[ ] as unidades mudam com a grandeza

[ ] Pressão converte corretamente
[ ] Comprimento converte corretamente
[ ] Área converte corretamente
[ ] Volume converte corretamente

[ ] gal (US) está disponível
[ ] gal (UK) está disponível

[ ] °C está disponível
[ ] °F está disponível
[ ] K está disponível
[ ] °R está disponível

[ ] 1 bar → 100 kPa
[ ] 1 m → 1000 mm
[ ] 1 m² → 1e+06 mm²
[ ] 1 L → 1000 mL
[ ] 1 gal (US) → aproximadamente 3.78541 L
[ ] 1 gal (UK) → 4.54609 L
[ ] 0 °C → 32 °F
[ ] 0 °C → 273.15 K
[ ] 32 °F → 491.67 °R
[ ] 0 K → 0 °R

[ ] o botão ↔ funciona
[ ] entrada inválida é tratada

[ ] Sprint 05 está CONCLUÍDA
[ ] Etapa 6 está CONCLUÍDA
```

---

# 59. 📌 Resumo da Aula 06.1

Implementamos:

```text
PRESSÃO
COMPRIMENTO
ÁREA
VOLUME
TEMPERATURA
        ↓
ENGCONVERT MULTICATEGORIAS
```

A estrutura passou a considerar:

```text
GRANDEZA
    ↓
UNIDADES
    ↓
ESTRATÉGIA
    ↓
CONVERSÃO
```

Para:

```text
Pressão
Comprimento
Área
Volume
```

utilizamos:

```text
origem
   ↓
unidade de referência
   ↓
destino
```

Para:

```text
Temperatura
```

utilizamos:

```text
origem
   ↓
kelvin
   ↓
destino
```

---

# 60. 🔜 Próxima etapa

Com a Etapa 6 concluída, o Roadmap aponta para:

```text
Etapa 7 — Modularização
```

Agora existe uma razão concreta para essa evolução.

Nosso `main.py` possui:

```text
dados
+
regras de conversão
+
funções
+
interface
```

À medida que o EngConvert cresce, manter tudo em um único arquivo começa a dificultar:

```text
leitura
manutenção
testes
reutilização
expansão
```

A próxima etapa irá tratar dessa necessidade.

---

# 🧭 Visão do percurso

```text
Aula 05
Conversor de Pressão
   ↓
Etapa 5 — CONCLUÍDA
   ↓
Aula 06.0
Novas Grandezas
   ↓
Aula 06.1
Implementação da Sprint 05
   ↓
Pressão
Comprimento
Área
Volume
Temperatura
   ↓
Sprint 05 — CONCLUÍDA
   ↓
Etapa 6 — CONCLUÍDA
   ↓
Etapa 7
Modularização
```

> 🎯 **Ideia final:** o EngConvert deixou de ser um conversor de uma única grandeza e passou a reconhecer diferentes categorias, atualizar suas unidades dinamicamente e aplicar a estratégia de conversão adequada a cada tipo de problema.
