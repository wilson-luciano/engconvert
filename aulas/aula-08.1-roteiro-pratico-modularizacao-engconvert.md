# Aula 08.1 — Roteiro Prático

## Modularizando o EngConvert — execução guiada e objetiva

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Correspondência:** roteiro prático da **Aula 08.0 — Modularização do EngConvert**.  
> **Etapa do Roadmap:** Etapa 8 — Modularização.  
> **Sprint:** Sprint 07 — Modularização do EngConvert.

---

# 🎯 Objetivo

Nesta aula reorganizaremos o EngConvert, separando responsabilidades que até agora estavam concentradas principalmente no `main.py`.

A ideia central será:

```text
ANTES

main.py
   ↓
dados + conversões + interface + inicialização
```

para:

```text
DEPOIS

main.py
   ↓
inicialização

src/
└── engconvert/
    ├── __init__.py
    ├── dados.py
    ├── conversoes.py
    └── interface.py
```

Ao final, o EngConvert deverá:

```text
continuar funcionando
        +
produzir as mesmas conversões
        +
possuir responsabilidades separadas
        +
estar preparado para testes automatizados
```

> 📌 **Importante:** esta é uma **refatoração**. Nosso objetivo principal não é acrescentar uma nova funcionalidade, mas melhorar a organização interna sem alterar intencionalmente o comportamento do programa.

---


> **Nota editorial:** versão enxuta, reorganizada em blocos completos de implementação. A teoria detalhada está na Aula 08.0 ampliada. **Este documento ainda não está congelado.**

# 1. Antes de começar

Confirme:

```text
[ ] Aula 08.0 estudada
[ ] Etapa 7 concluída
[ ] Git funcionando
[ ] repositório do EngConvert no GitHub
[ ] branch main existente
[ ] versão multicategorias funcionando
[ ] .venv configurado
[ ] VSCode aberto no projeto
```

A pasta de trabalho continua:

```text
C:\Projetos\engconvert
```

---


# 2. Abrir o projeto

No PowerShell:

```powershell
cd C:\Projetos\engconvert
```

Depois:

```powershell
code .
```

No terminal integrado:

```powershell
pwd
```

Confirme que estamos no projeto correto.

---


# 3. Ativar o ambiente virtual

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se necessário, no CMD:

```bat
.venv\Scripts\activate.bat
```

Depois:

```powershell
python --version
```

e:

```powershell
python main.py
```

Confirme que a versão atual abre normalmente.

---


# 4. Testar antes de modificar

Antes da refatoração, registre alguns resultados conhecidos.

Exemplos:

```text
1 bar → 100 kPa

1 m → 1000 mm

1 L → 1000 mL

0 °C → 32 °F

0 °C → 273,15 K
```

Esses resultados funcionarão como uma referência.

Nosso raciocínio será:

```text
ANTES
resultado conhecido
       ↓
MODULARIZAÇÃO
       ↓
DEPOIS
mesmo resultado
```

---


# 5. Conferir o estado do Git

Execute:

```bash
git status
```

Queremos iniciar a mudança estrutural com o repositório limpo.

Depois:

```bash
git log --oneline
```

Confirme que a versão funcional anterior está registrada.

> ⚠️ Se existirem alterações importantes ainda não commitadas, não avance mecanicamente. Primeiro compreenda e organize o estado atual.

---


# 6. Atualizar a `main`

Como a Aula 07.1 terminou com o projeto publicado no GitHub, confirme a branch:

```bash
git branch
```

O esperado é:

```text
* main
```

Depois:

```bash
git fetch origin
# Antes de integrar alterações remotas, confira o estado local e a divergência entre branches.
```

Se não houver alterações remotas, o Git informará que o projeto já está atualizado.

---


# 7. Criar a Sprint 07

Na pasta:

```text
docs/sprints/
```

crie o arquivo `sprint-07-modularizacao.md` **sem sobrescrever um arquivo já existente**. No terminal PowerShell do VSCode, a partir da raiz do projeto, execute:

```powershell
cd C:\Projetos\engconvert

# Criar a pasta apenas se ainda não existir
New-Item -ItemType Directory -Path .\docs\sprints -Force | Out-Null

# Criar o arquivo apenas se ainda não existir
if (-not (Test-Path .\docs\sprints\sprint-07-modularizacao.md)) {
    New-Item -ItemType File -Path .\docs\sprints\sprint-07-modularizacao.md | Out-Null
}

# Confirmar a existência
Test-Path .\docs\sprints\sprint-07-modularizacao.md
```

**Resultado esperado:** `True`. Se o arquivo já existir, ele será preservado. No Explorador do VSCode, abra `docs/sprints/sprint-07-modularizacao.md` e insira o conteúdo abaixo **somente se o arquivo estiver vazio**; caso contrário, revise o conteúdo existente.

Conteúdo inicial:

```markdown
# Sprint 07 — Modularização do EngConvert

## Objetivo

Reorganizar o EngConvert em módulos com responsabilidades bem definidas, preservando seu comportamento.

## Tarefas

- [ ] confirmar versão funcional na `main`;
- [ ] criar a branch `feature-modularizacao`;
- [ ] criar `src/engconvert`;
- [ ] criar `__init__.py`;
- [ ] criar `dados.py`;
- [ ] separar os dados de conversão;
- [ ] criar `conversoes.py`;
- [ ] separar as regras de conversão;
- [ ] criar `interface.py`;
- [ ] separar a interface gráfica;
- [ ] simplificar `main.py`;
- [ ] testar as conversões;
- [ ] documentar a arquitetura;
- [ ] criar commits incrementais;
- [ ] integrar a branch à `main`;
- [ ] publicar a nova estrutura no GitHub.

## Status

**PLANEJADA**
```

---


# 8. Criar a branch da modularização

Execute:

```bash
git switch -c feature-modularizacao
```

Depois:

```bash
git branch
```

O esperado:

```text
* feature-modularizacao
  main
```

Agora temos:

```text
main
  │
  └── versão funcional protegida
       \
        feature-modularizacao
```

---


# 10. Criar a nova estrutura

Na raiz do projeto, precisamos da pasta:

```text
src/
```

Dentro dela:

```text
engconvert/
```

E dentro de `engconvert`, dos arquivos:

```text
__init__.py
dados.py
conversoes.py
interface.py
```

> 📌 **Atenção:** nas aulas anteriores já criamos `src/engconvert/` e `__init__.py`. Portanto, **não devemos apagar nem substituir o conteúdo existente**. Os comandos abaixo criam somente os arquivos que ainda não existem.

### 10.1. Criar os novos módulos pelo terminal do VSCode

Abra o **terminal integrado do VSCode** e confirme que está utilizando o **PowerShell**. A pasta `src/engconvert` e o arquivo `__init__.py` já existem desde as aulas anteriores; **não é necessário recriá-los**.

Na raiz do projeto, execute:

```powershell
# Entrar na raiz do projeto
cd C:\Projetos\engconvert

# Criar somente os três módulos novos
New-Item -ItemType File -Path src\engconvert\dados.py
New-Item -ItemType File -Path src\engconvert\conversoes.py
New-Item -ItemType File -Path src\engconvert\interface.py

# Conferir pastas e arquivos
tree src /F
```

**Entendendo os comandos:**

- **`cd`** (*Change Directory*): acessa a pasta principal do EngConvert.
- **`New-Item -ItemType File`**: cria cada novo módulo Python vazio.
- **`tree src /F`**: mostra a estrutura da pasta `src`, incluindo os arquivos.

> **Atenção:** execute os três comandos `New-Item` somente se os arquivos ainda não existirem. Caso já tenha realizado essa etapa, use apenas `tree src /F` para conferir a estrutura. Não substitua nem apague os arquivos existentes.

### 10.2. Conferir o resultado

A estrutura deverá ficar semelhante a:

```text
src/
└── engconvert/             ← pacote
    │
    ├── __init__.py
    ├── dados.py            ← módulo
    ├── conversoes.py       ← módulo
    └── interface.py        ← módulo
```

> 💡 **Importante:** nesta etapa criamos apenas a estrutura. O conteúdo de `dados.py`, `conversoes.py` e `interface.py` será desenvolvido nas próximas seções. O `__init__.py` já existente deve ser preservado.

---


# 11. O `__init__.py`

Verifique se o arquivo abaixo **já existe** no projeto:

```text
src/engconvert/__init__.py
```

No terminal integrado do VSCode (PowerShell), execute:

```powershell
Test-Path src/engconvert/__init__.py
```

Se o resultado for `True`, o arquivo já existe e **não precisa ser recriado**. Abra-o no VSCode e confira seu conteúdo. Nesta etapa, ele pode conter apenas:

```python
"""Pacote principal do EngConvert."""
```

Se o resultado for `False`, confira primeiro se está na raiz correta do projeto. Somente se o arquivo realmente não existir, crie-o:

```powershell
New-Item -ItemType File -Path src/engconvert/__init__.py
```

A presença de `__init__.py` identifica explicitamente `engconvert` como um pacote Python regular. Não coloque lógica de conversão nele: os dados, os cálculos e a interface ficarão em `dados.py`, `conversoes.py` e `interface.py`, respectivamente.

---


# 13. Primeiro commit da Sprint

Prepare os arquivos:

```bash
git add src/engconvert/__init__.py src/engconvert/dados.py src/engconvert/conversoes.py src/engconvert/interface.py
```

Depois:

```bash
git status
```

Crie:

```bash
git commit -m "refactor: cria estrutura modular do EngConvert"
```

Temos agora um ponto intermediário claro.

---


# 14. Identificar os dados no `main.py`

Abra `main.py` no VSCode e localize a seção `# DADOS`. **Nesta etapa, apenas identifique; não exclua o código original.**

O EngConvert desenvolvido nas aulas anteriores possui **sete estruturas** que serão transferidas para `src/engconvert/dados.py`:

| Nome no `main.py` | Responsabilidade |
| --- | --- |
| `fatores_pressao` | Fatores em relação ao pascal |
| `fatores_comprimento` | Fatores em relação ao metro |
| `fatores_area` | Fatores em relação ao metro quadrado |
| `fatores_volume` | Fatores em relação ao metro cúbico |
| `grandezas` | Associa cada grandeza multiplicativa ao seu dicionário de fatores |
| `unidades_temperatura` | Lista as quatro escalas de temperatura |
| `lista_grandezas` | Define as cinco opções do seletor da interface |

**Conferência:** observe que `grandezas` é um dicionário que referencia os quatro dicionários de fatores. Portanto, os fatores devem ser definidos **antes** dele. Temperatura aparece nas listas, mas suas regras de conversão não são fatores multiplicativos.

> 📌 Preserve os nomes e os valores do `main.py`. Não crie uma segunda estrutura chamada `GRANDEZAS`.

---


# 15. Preencher `dados.py` com o código completo

No VSCode, abra o arquivo já criado:

```text
src/engconvert/dados.py
```

Sua responsabilidade será fornecer **dados de conversão**, e não realizar cálculos nem construir a interface gráfica.

**Copie integralmente o código abaixo para `dados.py`:**

```python
"""Unidades e fatores de conversão do EngConvert."""

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
```

> **Observação:** todo o código apresentado acima já estava presente no bloco `DADOS` do arquivo `main.py`, desenvolvido nas aulas anteriores. Nesta etapa, estamos apenas transferindo essas estruturas para `src/engconvert/dados.py`, sem alterar seus nomes, unidades ou fatores de conversão.
>
> Por enquanto, mantenha o bloco original no `main.py`. Sua remoção será realizada posteriormente, após os ajustes das importações e a validação do programa.

### 15.1. Validar a sintaxe e conferir a alteração

Salve o arquivo (`Ctrl + S`) e, no terminal PowerShell, execute:

```powershell
python -m py_compile src/engconvert/dados.py
```

Se não houver mensagem de erro, a sintaxe foi validada. Isso **não** comprova, por si só, a exatidão de todos os fatores de conversão.

Como `dados.py` já foi criado e registrado no primeiro commit, confira o que mudou:

```powershell
git --no-pager diff -- src/engconvert/dados.py
git status --short src/engconvert/dados.py
```

O esperado é que o status indique ` M src/engconvert/dados.py`, se o arquivo foi salvo e ainda não foi preparado para o próximo commit.

> ⚠️ **Não apague ainda o bloco `DADOS` do `main.py`.** Primeiro criaremos os módulos dependentes, ajustaremos as importações e validaremos a execução; só depois retiraremos a duplicação. Nesta etapa, não use `git add .`, pois podem existir modificações locais de outras aulas e documentos.

---


# 18. Importar os dados

Quando a lógica de conversão for separada, poderemos utilizar em:

```text
conversoes.py
```

uma importação como:

```python
from .dados import grandezas
```

Leia:

> **“Do módulo `dados`, deste pacote, importe o nome `grandezas`.”**

Nesse caso:

```text
.
↓
pacote atual
```

---


> **Nesta etapa, NÃO copie a importação para `conversoes.py`: mantenha o arquivo vazio.** O código completo será inserido na próxima fase prática.

# 20. Conferir o Git

Execute:

```bash
git status
```

Depois:

```bash
git --no-pager diff -- src/engconvert/dados.py
```

Observe exatamente o que mudou.

---


# 21. Registrar o módulo de dados

Prepare somente o arquivo `dados.py`, sem incluir modificações de outras aulas ou documentos:

```powershell
git add src/engconvert/dados.py
git --no-pager diff --cached --name-status
```

**Confira:** deve aparecer somente `M src/engconvert/dados.py`. Caso existam outros arquivos preparados, interrompa e revise antes de continuar.

```powershell
git commit -m "refactor: separa dados de conversao do EngConvert"
```

### 21.4. Confirmar o registro

```powershell
git --no-pager log -2 --oneline
```

O commit recém-criado deve aparecer acima de `ba8d68c refactor: cria estrutura modular do EngConvert`.

---

# 22. Implementar o módulo de conversões — código completo

Abra `src/engconvert/conversoes.py`. **Agora sim**, substitua o conteúdo vazio pelo código integral abaixo. Ele importa os dados já definidos em `dados.py`, trata temperatura e realiza as conversões multiplicativas.

```python
"""Regras de conversão independentes da interface gráfica."""

from .dados import grandezas, unidades_temperatura


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


def obter_unidades(grandeza):

    if grandeza == "Temperatura":
        return unidades_temperatura

    return list(grandezas[grandeza].keys())


def converter(valor, grandeza, unidade_de, unidade_para):
    """Converte o valor informado e devolve um número."""
    if grandeza == "Temperatura":
        return converter_temperatura(valor, unidade_de, unidade_para)

    fatores = grandezas[grandeza]
    valor_referencia = valor * fatores[unidade_de]
    return valor_referencia / fatores[unidade_para]
```

Salve (`Ctrl + S`) e verifique a sintaxe:

```powershell
python -m py_compile src/engconvert/conversoes.py
git --no-pager diff --check -- src/engconvert/conversoes.py
```

> O `main.py` ainda permanece intacto. Não tente executar diretamente `conversoes.py`: ele utiliza importação relativa do pacote.

---

# 23. Implementar a interface — código completo

Abra `src/engconvert/interface.py` e copie todo o código abaixo. O módulo usa as funções de `conversoes.py` e mantém os eventos junto aos widgets.

```python
"""Interface gráfica do EngConvert em CustomTkinter."""

import customtkinter as ctk

from .dados import fatores_pressao, lista_grandezas
from .conversoes import converter, obter_unidades


def iniciar_aplicacao():
    """Cria os widgets, registra eventos e inicia a aplicação."""
    # Atualiza as unidades quando a categoria é alterada.
    def atualizar_unidades(grandeza_selecionada):
        unidades = obter_unidades(grandeza_selecionada)
        combo_de.configure(values=unidades)
        combo_para.configure(values=unidades)
        combo_de.set(unidades[0])
        combo_para.set(unidades[1])
        resultado.configure(text="Resultado")

    # Evento do botão Converter: recebe dados, chama o cálculo e mostra a saída.
    def ao_converter():
        try:
            valor = float(entrada.get())
            grandeza = combo_grandeza.get()
            unidade_de = combo_de.get()
            unidade_para = combo_para.get()
            valor_convertido = converter(valor, grandeza, unidade_de, unidade_para)
            resultado.configure(text=f"{valor_convertido:.6g} {unidade_para}")
        except ValueError:
            resultado.configure(text="Digite um valor numérico válido.")

    # Inverte as unidades selecionadas.
    def inverter_unidades():
        unidade_de = combo_de.get()
        unidade_para = combo_para.get()
        combo_de.set(unidade_para)
        combo_para.set(unidade_de)

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
        command=ao_converter
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

    # Mantém a janela aberta e processa os eventos do usuário.
    app.mainloop()
```

Salve e confira:

```powershell
python -m py_compile src/engconvert/interface.py
git --no-pager diff --check -- src/engconvert/interface.py
```

> Ainda não substitua `main.py`: primeiro vamos configurar a instalação do pacote.

---

# 24. Configurar o projeto com `pyproject.toml`

Na raiz `C:\Projetos\engconvert`, crie ou confira o arquivo `pyproject.toml`. No PowerShell:

```powershell
cd C:\Projetos\engconvert
if (-not (Test-Path .\pyproject.toml)) {
    New-Item -ItemType File -Path .\pyproject.toml | Out-Null
}
Test-Path .\pyproject.toml
```

O resultado esperado é `True`. **Se já existir, compare antes de substituir** para não apagar configurações anteriores. Conteúdo previsto para esta Sprint:

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "engconvert"
version = "0.1.0"
description = "Conversor de unidades de engenharia"
requires-python = ">=3.12"
dependencies = ["customtkinter"]

[tool.setuptools.packages.find]
where = ["src"]
```

Com `.venv` ativo, instale o projeto em modo editável:

```powershell
python -m pip install -e .
python -c "from engconvert.conversoes import converter; print(converter(1, 'Pressão', 'bar', 'kPa'))"
```

**O que significa o modo editável?** A opção `-e` (*editable*) faz o Python utilizar diretamente os arquivos do projeto em `src/engconvert`, sem precisar reinstalar o pacote a cada alteração do código-fonte. O ponto `.` indica a pasta atual. Mudanças nas dependências ou na configuração de instalação podem exigir nova instalação.

**Resultado esperado:** `100.0`. Se houver erro, não substitua o `main.py` até corrigir a instalação/importação.

---

# 25. Substituir `main.py` — ponto de entrada

Somente após validar a importação, confirme que a versão anterior do `main.py` está registrada no histórico Git. No projeto utilizado nesta aula, a versão multicategorias está no commit `4f82916`:

```powershell
git --no-pager log -5 --oneline -- main.py
git cat-file -e 4f82916:main.py
git status --short -- main.py
```

**Como interpretar:** o primeiro comando lista commits que alteraram `main.py`; o segundo verifica se o arquivo existe no commit indicado (sem saída e sem erro significa que foi encontrado); o terceiro verifica mudanças locais ainda não registradas. **Se `git status --short -- main.py` não mostrar nada**, o arquivo atual não tem alterações pendentes e a versão anterior está recuperável pelo Git. Se mostrar `M`, examine e preserve essas mudanças antes de substituir o arquivo. O hash `4f82916` é específico do histórico deste projeto: em outros repositórios, utilize o commit correspondente.

Depois dessa conferência, abra `main.py` e substitua integralmente pelo código abaixo:

```python
"""Ponto de entrada do EngConvert."""

from engconvert.interface import iniciar_aplicacao


def main():
    iniciar_aplicacao()


if __name__ == "__main__":
    main()
```

Execute:

```powershell
python main.py
```

A janela deve abrir com as mesmas grandezas, unidades e comportamento da versão anterior.

---

# 26. Teste de regressão manual

Confira os seguintes casos antes de qualquer commit de integração:

| Grandeza | Conversão | Resultado esperado |
|---|---|---|
| Pressão | 1 bar → kPa | 100 kPa |
| Comprimento | 1 m → mm | 1000 mm |
| Área | 1 m² → cm² | 10000 cm² |
| Volume | 1 L → mL | 1000 mL |
| Volume | 1 gal (US) → L | 3,78541 L |
| Volume | 1 gal (UK) → L | 4,54609 L |
| Temperatura | 0 °C → °F | 32 °F |
| Temperatura | 0 °C → K | 273,15 K |

Teste também a inversão das unidades, a mudança de categoria e uma entrada inválida (`abc`). A apresentação numérica utiliza `.6g`. **Se algum teste falhar, corrija antes do commit.**

---

# 27. Registrar a implementação modular completa

Prepare apenas os arquivos da implementação. Não utilize `git add .`:

```powershell
git add src/engconvert/conversoes.py src/engconvert/interface.py main.py pyproject.toml
git --no-pager diff --cached --name-status
git --no-pager diff --cached --check
```

**Atenção:** confirme que a área de preparação contém apenas esses arquivos. Se outros estiverem preparados, revise-os antes do commit.

```powershell
git commit -m "refactor: integra conversoes interface e entrada do EngConvert"
git --no-pager log -4 --oneline
```

---

# 28. Documentação e encerramento da Sprint

Atualize `docs/sprints/sprint-07-modularizacao.md` e a documentação de arquitetura com a estrutura modular implementada, os testes realizados e os resultados obtidos. Antes de editar, verifique o conteúdo existente para evitar sobrescrever informações válidas.

Registre a estrutura final e o resultado dos testes; faça um commit documental separado, preparando somente os arquivos efetivamente revisados.

---

# 29. Revisar e integrar a branch à `main`

Antes do merge, verifique o estado da branch e dos arquivos não relacionados:

```powershell
git branch --show-current
git status
git --no-pager log --oneline --decorate -5
git fetch origin
```

**Não execute `git switch main`, `git pull` ou `git merge` mecanicamente se houver alterações locais não registradas**, pois existem arquivos de outras aulas e documentos que precisam ser preservados. Organize essas pendências primeiro, sem `git reset --hard`, `git restore .` ou `git add .`.

Quando a árvore de trabalho estiver segura e as diferenças remotas forem revisadas, o fluxo de integração será (**execute um comando por vez**):

```powershell
git switch main
git pull --ff-only origin main
git merge --no-ff feature-modularizacao
```

Depois de concluir o merge e verificar o estado do Git, execute e teste a aplicação:

```powershell
python main.py
```

Feche a janela da aplicação antes de publicar:

```powershell
git push origin main
```

### 29.1. Se o Git abrir um editor para confirmar a mensagem do merge

Ao executar `git merge --no-ff feature-modularizacao`, o Git pode abrir um editor para confirmar a mensagem do commit de integração. Nesse caso, pode aparecer:

```text
Merge branch 'feature-modularizacao'

# Please enter a commit message to explain why this merge is necessary...
```

As linhas iniciadas por `#` são comentários; não entram na mensagem. A mensagem sugerida pode ser mantida.

**Se o editor abrir uma aba no VSCode (`MERGE_MSG`):** pressione `Ctrl + S` para salvar e feche a aba. O Git continuará quando o editor for fechado.

**Se o editor for o Vim, dentro do terminal:** pressione `Esc`, digite `:wq` e pressione `Enter`. `:wq` significa *salvar e sair* (*write and quit*). O Vim é um editor de texto que pode ser utilizado pelo Git para mensagens de commits e merges.

Se o terminal exibir `hint: Waiting for your editor to close the file...`, **não execute outro merge**: finalize primeiro o editor aberto. Se estiver em outro editor, use o procedimento de salvar e fechar correspondente.

Para evitar essa etapa em **merges futuros**, informe a mensagem diretamente no comando (não execute novamente se o merge atual já estiver em andamento):

```powershell
git merge --no-ff feature-modularizacao -m "merge: integra modularizacao do EngConvert"
```

### 29.2. Confirmar o merge antes de publicar

Quando o editor fechar e o terminal voltar ao prompt, confira:

```powershell
git status
git --no-pager log -3 --oneline
git branch --show-current
```

Confirme que a branch é `main` e que o merge foi concluído. No acompanhamento desta aula, o resultado foi `d4da3c3 Merge branch 'feature-modularizacao'`, com `HEAD -> main` e `origin/main` no mesmo commit. Isso confirma que a integração **já foi publicada**; não repita o merge ou o push sem uma nova alteração. **Execute os comandos do fluxo de integração um de cada vez**: depois do merge, rode `python main.py`, teste e feche a aplicação antes de executar `git push origin main`. Se houver conflitos, erros ou alterações locais inesperadas, interrompa e revise antes de publicar.

> **Atenção:** arquivos `M` (modificados) e `D` (excluídos) mostrados pelo Git podem ser alterações locais de outras aulas ou documentos. `Untracked files` são arquivos ainda não versionados; `src/engconvert.egg-info/` pode ser gerado pela instalação editável e não precisa entrar no commit. Avisos `LF will be replaced by CRLF` normalmente apenas indicam conversão de finais de linha no Windows. Não utilize `git add .`, `git restore .` ou `git reset --hard` para tentar limpá-los automaticamente.

Se surgir conflito, interrompa a sequência, resolva os arquivos afetados e teste novamente antes de publicar. Não use `git push --force`.

---

# 30. Checklist de conclusão

- [ ] `dados.py`, `conversoes.py` e `interface.py` contêm o código completo.
- [ ] `python -m pip install -e .` executou sem erro.
- [ ] `main.py` apenas inicia a aplicação.
- [ ] Todas as categorias, temperaturas e inversão foram verificadas.
- [ ] Entradas inválidas são tratadas.
- [ ] Commits contêm apenas os arquivos previstos.
- [ ] Documentação e Sprint 07 foram revisadas.
- [ ] Merge e push foram feitos apenas após proteger alterações locais.

**Próxima etapa:** Aula 09 — testes automatizados com `pytest`.

---

© 2026 Wilson Luciano · Programação para Engenharia Mecânica · EngConvert · Material didático · **OFICIAL-CONGELADA — v1**
