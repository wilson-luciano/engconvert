# Aula 08.1 — Roteiro Prático

## Modularizando o EngConvert

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
git pull
```

Se não houver alterações remotas, o Git informará que o projeto já está atualizado.

---

# 7. Criar a Sprint 07

Na pasta:

```text
docs/sprints/
```

crie:

```text
sprint-07-modularizacao.md
```

Conteúdo:

````markdown
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
````

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

# 9. Por que criar a branch antes de alterar?

Porque estamos prestes a realizar uma mudança estrutural.

A branch:

```text
feature-modularizacao
```

permite desenvolver essa reorganização separadamente da `main`.

A ideia é:

```text
main
  ↓
versão validada

feature-modularizacao
  ↓
mudança em desenvolvimento
```

---

# 10. Criar a nova estrutura

Na raiz do projeto, crie:

```text
src/
```

Dentro:

```text
engconvert/
```

E dentro de `engconvert`:

```text
__init__.py
dados.py
conversoes.py
interface.py
```

A estrutura ficará:

```text
src/
└── engconvert/             ← pacote
    │
    ├── __init__.py
    ├── dados.py            ← módulo
    ├── conversoes.py       ← módulo
    └── interface.py        ← módulo
```

---

# 11. O `__init__.py`

Crie:

```text
src/engconvert/__init__.py
```

Inicialmente, deixe-o vazio.

Sua presença torna explícita a intenção de utilizar:

```text
engconvert
```

como pacote regular do projeto.

Não precisamos colocar lógica de conversão nele.

---

# 12. Primeira conferência do Git

Execute:

```bash
git status
```

Observe os novos arquivos.

Ainda não movemos a lógica.

Criamos apenas a estrutura.

---

# 13. Primeiro commit da Sprint

Prepare os arquivos:

```bash
git add src
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

Abra:

```text
main.py
```

Localize os dicionários/listas que representam:

```text
grandezas
unidades
fatores de conversão
```

Na versão atual, podem existir estruturas equivalentes a:

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

e estruturas correspondentes às outras grandezas.

> 📌 Os nomes exatos devem seguir o código que você construiu nas aulas anteriores. Não crie uma segunda coleção de dados se ela já existe no projeto.

---

# 15. Criar `dados.py`

Abra:

```text
src/engconvert/dados.py
```

A responsabilidade será:

```text
DADOS DE CONVERSÃO
```

Transfira para esse módulo os dados que descrevem as grandezas e unidades.

Conceitualmente:

```python
# Dados utilizados pelas regras de conversão.

GRANDEZAS = {
    # Estrutura de grandezas/unidades do EngConvert.
}
```

> ⚠️ Não copie cegamente este esqueleto sobre sua estrutura existente. O objetivo é **mover os dados reais do seu EngConvert**, preservando valores e nomenclaturas já utilizados.

---

# 16. Por que usar `GRANDEZAS` em maiúsculas?

Se adotarmos:

```python
GRANDEZAS
```

estamos seguindo a convenção de nomes em maiúsculas para valores tratados como constantes/configurações.

Isso comunica:

```text
estes dados existem
para serem consultados

não para serem alterados
durante uma conversão normal
```

Python não torna automaticamente o dicionário imutável.

É uma convenção.

---

# 17. Não mover temperatura como simples fator

Lembre-se:

```text
Pressão
Comprimento
Área
Volume
```

podem utilizar conversões multiplicativas baseadas em fatores.

Temperatura é diferente.

Por exemplo:

```text
°C → °F
```

não pode ser resolvido apenas com:

```text
valor × fator
```

Portanto, preserve a lógica especial de temperatura.

---

# 18. Importar os dados

Quando a lógica de conversão for separada, poderemos utilizar em:

```text
conversoes.py
```

uma importação como:

```python
from .dados import GRANDEZAS
```

Leia:

> **“Do módulo `dados`, deste pacote, importe o nome `GRANDEZAS`.”**

Nesse caso:

```text
.
↓
pacote atual
```

---

# 19. Testar após mover os dados

Depois de ajustar as referências necessárias, execute:

```powershell
python main.py
```

Teste novamente algumas conversões.

Se algo falhar:

```text
NÃO continue movendo código
```

Primeiro corrija essa etapa.

A estratégia é:

```text
MOVER POUCO
    ↓
TESTAR
    ↓
CONTINUAR
```

---

# 20. Conferir o Git

Execute:

```bash
git status
```

Depois:

```bash
git diff
```

Observe exatamente o que mudou.

---

# 21. Commit dos dados

Quando o programa voltar a funcionar:

```bash
git add .
```

Confira:

```bash
git status
```

Depois:

```bash
git commit -m "refactor: separa dados de conversao"
```

---

# 22. Criar `conversoes.py`

Agora abra:

```text
src/engconvert/conversoes.py
```

Esse módulo terá a responsabilidade:

```text
REGRAS DE CONVERSÃO
```

Ele deverá receber dados e retornar resultados.

Não deverá criar widgets.

---

# 23. Importar os dados em `conversoes.py`

No início do módulo, conforme a estrutura adotada:

```python
from .dados import GRANDEZAS
```

Se os dados de temperatura estiverem separados em outro nome, importe também o que for realmente necessário.

Evite:

```python
from .dados import *
```

Prefira nomes explícitos.

---

# 24. Separar a conversão multiplicativa

Uma função possível é:

```python
def converter_por_fator(valor, fator_origem, fator_destino):
    return valor * fator_origem / fator_destino
```

Observe:

```text
ENTRADA
valor
fator_origem
fator_destino

PROCESSAMENTO
multiplicação/divisão

SAÍDA
resultado
```

Ela não sabe nada sobre:

```text
Entry
ComboBox
Label
Button
```

---

# 25. Separar a conversão de temperatura

Crie/mova a lógica específica de temperatura.

A forma exata deve preservar a implementação construída anteriormente.

Conceitualmente:

```python
def converter_temperatura(valor, unidade_de, unidade_para):
    # converter origem para uma referência
    # converter referência para destino
    # retornar resultado
    ...
```

Não substitua uma lógica funcional por outra apenas porque estamos modularizando.

> 🎯 Refatoração não é o momento de alterar desnecessariamente a matemática que já funciona.

---

# 26. Criar uma função geral

Podemos organizar uma função principal:

```python
def converter(valor, grandeza, unidade_de, unidade_para):
    ...
```

Sua responsabilidade será decidir qual estratégia de conversão utilizar.

Fluxo:

```text
converter(...)
     ↓
grandeza é temperatura?
     │
     ├── SIM → converter_temperatura(...)
     │
     └── NÃO → converter_por_fator(...)
```

---

# 27. Exemplo estrutural

O módulo poderá assumir uma organização semelhante a:

```python
from .dados import GRANDEZAS


def converter_por_fator(valor, fator_origem, fator_destino):
    return valor * fator_origem / fator_destino


def converter_temperatura(valor, unidade_de, unidade_para):
    # preservar a lógica real do projeto
    ...


def converter(valor, grandeza, unidade_de, unidade_para):
    # selecionar a regra adequada
    ...
```

> ⚠️ As reticências (`...`) indicam partes que devem ser preenchidas com a lógica real do EngConvert. Elas não são a implementação final da Sprint.

---

# 28. A interface não deve mais calcular

Depois da separação, a GUI deverá fazer algo conceitualmente parecido com:

```python
resultado = converter(
    valor,
    grandeza,
    unidade_de,
    unidade_para
)
```

E então:

```text
receber resultado
      ↓
formatar
      ↓
mostrar
```

---

# 29. O que queremos evitar

Evite manter espalhado na interface:

```python
if grandeza == "Pressão":
    ...
elif grandeza == "Comprimento":
    ...
elif grandeza == "Temperatura":
    ...
```

se essas decisões pertencem à regra de conversão.

Queremos:

```text
INTERFACE
   ↓
pede conversão

CONVERSOES
   ↓
decide como calcular
```

---

# 30. Testar `conversoes.py` sem GUI

Antes mesmo de pytest, podemos fazer um teste manual temporário no terminal Python.

Abra:

```powershell
python
```

Dependendo de como o pacote estiver disponibilizado no ambiente nesta etapa, a importação deverá seguir a estrutura configurada no projeto.

O objetivo conceitual é conseguir chamar:

```python
converter(...)
```

sem depender de clicar na GUI.

> 📌 Na sequência desta aula ajustaremos a forma de execução do pacote para que as importações sejam consistentes. Não utilize alterações manuais de `sys.path` como solução permanente.

Saia do REPL:

```python
exit()
```

---

# 31. Testar pela aplicação

Execute novamente:

```powershell
python main.py
```

Teste:

```text
Pressão
Comprimento
Área
Volume
Temperatura
```

Use pelo menos um caso de cada categoria.

---

# 32. Commit das regras

Depois de validar:

```bash
git status
git diff
git add .
git commit -m "refactor: separa regras de conversao"
```

---

# 33. Criar `interface.py`

Agora abra:

```text
src/engconvert/interface.py
```

Esse módulo terá a responsabilidade:

```text
INTERFACE GRÁFICA
```

Aqui ficarão elementos relacionados a:

```text
CustomTkinter
janela
frames
labels
entries
comboboxes
buttons
eventos
layout
apresentação do resultado
```

---

# 34. Importações da interface

A interface deverá importar aquilo de que precisa.

Por exemplo:

```python
import customtkinter as ctk

from .conversoes import converter
from .dados import GRANDEZAS
```

Leia:

```text
do módulo conversoes
deste pacote
importe converter
```

e:

```text
do módulo dados
deste pacote
importe GRANDEZAS
```

---

# 35. O evento do botão

A função associada ao botão deverá concentrar a interação.

Fluxo:

```text
usuário clica
      ↓
interface lê Entry
      ↓
interface lê ComboBoxes
      ↓
converte texto para float
      ↓
chama converter(...)
      ↓
recebe resultado
      ↓
formata
      ↓
atualiza Label
```

---

# 36. Exemplo conceitual do evento

A estrutura poderá ser semelhante a:

```python
def ao_converter():
    try:
        valor = float(entrada_valor.get())

        resultado = converter(
            valor,
            categoria.get(),
            unidade_de.get(),
            unidade_para.get()
        )

        resultado_label.configure(
            text=f"{resultado:.6g} {unidade_para.get()}"
        )

    except ValueError as erro:
        resultado_label.configure(
            text=f"Entrada inválida: {erro}"
        )
```

Adapte os nomes:

```text
entrada_valor
categoria
unidade_de
unidade_para
resultado_label
```

aos nomes reais existentes no seu EngConvert.

---

# 37. O que permaneceu na interface?

Observe:

```text
float(...)
try/except
.get()
.configure()
```

continuam ligados à interação com o usuário.

Já a matemática principal:

```text
converter(...)
```

foi separada.

---

# 38. Criar uma função para iniciar a aplicação

Em `interface.py`, podemos encapsular a construção/inicialização da GUI.

Por exemplo:

```python
def iniciar_aplicacao():
    # criar/configurar a aplicação
    # criar widgets
    # executar mainloop
    ...
```

A implementação deve utilizar o código real já construído.

---

# 39. Cuidado com variáveis locais

Ao mover widgets para dentro de:

```python
iniciar_aplicacao()
```

lembre que funções de eventos precisam acessar determinados widgets.

Não mova tudo mecanicamente.

Uma possibilidade didática é manter as funções que utilizam esses widgets no mesmo escopo apropriado, ou organizar a interface de modo que as referências necessárias continuem acessíveis.

> 📌 Nesta etapa, o objetivo é modularização entre arquivos. Não precisamos introduzir uma arquitetura orientada a objetos apenas para resolver o escopo da GUI.

---

# 40. Não transformar tudo em classe agora

Poderíamos criar:

```python
class EngConvertApp:
    ...
```

Mas isso acrescentaria simultaneamente:

```text
modularização
+
arquitetura orientada a objetos
```

Não é necessário neste momento.

Primeiro consolidaremos:

```text
módulos
pacotes
imports
responsabilidades
```

Uma classe de aplicação poderá ser avaliada futuramente se houver necessidade real.

---

# 41. Testar a interface modularizada

Execute:

```powershell
python main.py
```

Se ocorrer:

```text
ModuleNotFoundError
```

não altere `sys.path` aleatoriamente.

Primeiro verifique:

```text
estrutura de pastas
nome do pacote
nome dos módulos
local de execução
importações
```

---

# 42. Simplificar `main.py`

O objetivo é que `main.py` deixe de conter:

```text
dicionários
regras matemáticas
widgets
layout completo
```

e passe a funcionar como:

```text
PONTO DE ENTRADA
```

---

# 43. Estrutura conceitual do novo `main.py`

Queremos algo próximo de:

```python
from engconvert.interface import iniciar_aplicacao


def main():
    iniciar_aplicacao()


if __name__ == "__main__":
    main()
```

Mas há um detalhe importante:

```text
engconvert
```

está dentro de:

```text
src/
```

Precisamos tornar esse pacote importável de forma correta.

---

# 44. Não usar `sys.path.append()` como solução didática principal

Poderíamos encontrar na internet:

```python
import sys
sys.path.append("src")
```

e então:

```python
from engconvert.interface import iniciar_aplicacao
```

Isso pode parecer resolver rapidamente.

Mas não será nossa solução principal.

Queremos que o projeto declare sua estrutura adequadamente.

---

# 45. Tornar o projeto instalável em modo editável

Uma forma profissional e conveniente para a estrutura `src` é instalar o próprio projeto no ambiente virtual em **modo editável**.

Para isso, criaremos um arquivo de configuração:

```text
pyproject.toml
```

na raiz do projeto.

A estrutura passa a incluir:

```text
engconvert/
│
├── pyproject.toml
├── main.py
├── src/
│   └── engconvert/
│       ├── __init__.py
│       ├── dados.py
│       ├── conversoes.py
│       └── interface.py
└── ...
```

---

# 46. O que é `pyproject.toml`?

`pyproject.toml` é um arquivo de configuração padronizado utilizado pelo ecossistema Python para descrever aspectos de construção e empacotamento de projetos.

Não estudaremos empacotamento profundamente agora.

Neste momento ele nos ajudará a declarar:

```text
onde está o pacote
        ↓
src/
```

e permitirá instalar o EngConvert no ambiente virtual em modo editável.

---

# 47. Criar `pyproject.toml`

Na raiz:

```text
C:\Projetos\engconvert
```

crie:

```text
pyproject.toml
```

Uma configuração mínima pode ser:

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "engconvert"
version = "0.1.0"
description = "Conversor de unidades de engenharia"
requires-python = ">=3.12"
dependencies = [
    "customtkinter"
]

[tool.setuptools.packages.find]
where = ["src"]
```

---

# 48. O que essa configuração informa?

Trecho:

```toml
[project]
name = "engconvert"
```

define o nome do projeto.

Trecho:

```toml
requires-python = ">=3.12"
```

declara a versão mínima planejada para esta configuração didática.

E:

```toml
[tool.setuptools.packages.find]
where = ["src"]
```

informa ao `setuptools` que os pacotes devem ser procurados em:

```text
src/
```

---

# 49. Instalar em modo editável

Com `.venv` ativo, execute na raiz:

```powershell
python -m pip install -e .
```

Leia:

```text
python -m pip
      ↓
execute pip com este Python

install
      ↓
instale

-e
      ↓
editable / editável

.
      ↓
projeto da pasta atual
```

---

# 50. O que significa modo editável?

No modo editável:

```text
ambiente virtual
      ↓
reconhece o projeto
      ↓
código continua em src/
```

Quando alteramos os arquivos-fonte, não precisamos reinstalar o pacote após cada pequena modificação.

Isso é muito útil durante o desenvolvimento.

---

# 51. Testar a importação

Depois:

```powershell
python
```

No REPL:

```python
import engconvert
```

Se não houver erro, teste:

```python
from engconvert.conversoes import converter
```

Depois:

```python
exit()
```

Agora o pacote está acessível de maneira consistente no ambiente virtual.

---

# 52. Novo `main.py`

Agora podemos utilizar:

```python
from engconvert.interface import iniciar_aplicacao


def main():
    iniciar_aplicacao()


if __name__ == "__main__":
    main()
```

Observe como o arquivo ficou pequeno.

Sua responsabilidade é clara:

```text
IMPORTAR
    ↓
INICIAR
```

---

# 53. Executar novamente

No terminal:

```powershell
python main.py
```

A aplicação deverá abrir normalmente.

Se não abrir, leia a mensagem de erro.

Não continue até corrigir.

---

# 54. Teste de regressão manual

Repita os casos registrados no início.

Por exemplo:

| Conversão | Resultado esperado |
|---|---:|
| 1 bar → kPa | 100 kPa |
| 1 m → mm | 1000 mm |
| 1 L → mL | 1000 mL |
| 0 °C → °F | 32 °F |
| 0 °C → K | 273,15 K |

Use também casos de:

```text
Área
Volume com galões
Temperatura com °R
```

preservando os fatores e regras definidos nas aulas anteriores.

---

# 55. Testar entrada inválida

Digite algo como:

```text
abc
```

no campo de valor.

O programa não deve encerrar abruptamente.

O tratamento de exceções desenvolvido anteriormente deve continuar funcionando.

---

# 56. Testar troca de unidades

Use o recurso:

```text
De ↔ Para
```

se ele já estiver presente na versão construída.

A modularização não deve quebrar essa interação.

---

# 57. Conferir a estrutura final

Neste ponto, esperamos algo próximo de:

```text
engconvert/
│
├── main.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   └── engconvert/
│       ├── __init__.py
│       ├── dados.py
│       ├── conversoes.py
│       └── interface.py
│
├── docs/
│   ├── roadmap.md
│   └── sprints/
│       └── sprint-07-modularizacao.md
│
├── aulas/
├── tests/
└── .venv/
```

A pasta `.venv/` continua local e ignorada pelo Git.

---

# 58. Criar a documentação da arquitetura

Na pasta:

```text
docs/
```

crie:

```text
arquitetura.md
```

Conteúdo inicial:

````markdown
# Arquitetura do EngConvert

## Estrutura principal

```text
main.py
   │
   ▼
interface.py
   │
   ▼
conversoes.py
   │
   ▼
dados.py
```

## Responsabilidades

### `main.py`

Ponto de entrada da aplicação.

### `interface.py`

Responsável pela interface gráfica e interação com o usuário.

### `conversoes.py`

Responsável pelas regras de conversão.

### `dados.py`

Responsável pelos dados das grandezas, unidades e fatores utilizados nas conversões.

## Objetivo da modularização

Separar responsabilidades, reduzir o acoplamento entre interface e regras de conversão e preparar o projeto para testes automatizados.
````

---

# 59. Conferir dependências

Pergunte:

```text
dados.py
precisa importar interface.py?
```

Resposta esperada:

```text
NÃO
```

E:

```text
conversoes.py
precisa criar CTkButton?
```

Resposta:

```text
NÃO
```

A direção desejada é:

```text
main
  ↓
interface
  ↓
conversoes
  ↓
dados
```

---

# 60. Verificar importação circular

Procure evitar:

```text
interface importa conversoes
        ↑               ↓
        └───────────────┘
```

ou seja:

```text
conversoes.py
```

não deve precisar importar:

```text
interface.py
```

para realizar cálculos.

---

# 61. Conferir o Git novamente

Execute:

```bash
git status
```

Depois:

```bash
git diff
```

Confira especialmente:

```text
main.py
pyproject.toml
src/
docs/
```

---

# 62. Commit da interface e ponto de entrada

Quando a aplicação estiver funcionando:

```bash
git add .
```

Depois:

```bash
git status
```

E:

```bash
git commit -m "refactor: separa interface e ponto de entrada"
```

---

# 63. Commit da documentação, se necessário

Se `arquitetura.md` e a Sprint ainda não tiverem sido incluídos no commit anterior, prepare-os:

```bash
git add docs
```

Depois:

```bash
git commit -m "docs: registra arquitetura modular do EngConvert"
```

Não crie um commit vazio apenas para seguir a apostila.

Se os arquivos já foram incluídos de forma coerente em um commit anterior, prossiga.

---

# 64. Visualizar o histórico da branch

Execute:

```bash
git log --oneline --decorate
```

O histórico poderá conter commits semelhantes a:

```text
refactor: separa interface e ponto de entrada
refactor: separa regras de conversao
refactor: separa dados de conversao
refactor: cria estrutura modular do EngConvert
...
```

Os hashes serão diferentes.

---

# 65. Comparar com `main`

Podemos visualizar as diferenças entre a branch atual e `main`:

```bash
git diff main...feature-modularizacao
```

Isso ajuda a responder:

```text
o que a modularização
mudou no projeto?
```

---

# 66. Último teste antes do merge

Execute:

```powershell
python main.py
```

Teste novamente todas as categorias.

Checklist:

```text
[ ] aplicação abre
[ ] Pressão funciona
[ ] Comprimento funciona
[ ] Área funciona
[ ] Volume funciona
[ ] gal (US) funciona
[ ] gal (UK) funciona
[ ] °C funciona
[ ] °F funciona
[ ] K funciona
[ ] °R funciona
[ ] entrada inválida é tratada
[ ] troca De/Para funciona
```

---

# 67. Conferir se a branch está limpa

Execute:

```bash
git status
```

Queremos:

```text
working tree clean
```

antes de integrar a branch.

---

# 68. Voltar para `main`

Execute:

```bash
git switch main
```

Confirme:

```bash
git branch
```

Agora:

```text
* main
  feature-modularizacao
```

---

# 69. Atualizar `main` antes do merge

Execute:

```bash
git pull
```

Isso reduz a chance de integrar sobre uma `main` local desatualizada.

---

# 70. Fazer o merge

Execute:

```bash
git merge feature-modularizacao
```

Conceitualmente:

```text
feature-modularizacao
        ↓
      merge
        ↓
       main
```

---

# 71. Se não houver conflito

O Git integrará as alterações.

Depois:

```bash
git status
```

e:

```bash
git log --oneline --decorate --graph --all
```

Observe a evolução.

---

# 72. Se houver conflito

Não entre em pânico e não apague arquivos aleatoriamente.

O Git indicará quais arquivos possuem conflito.

O VSCode pode mostrar marcadores ou ferramentas visuais para auxiliar a resolução.

O fluxo geral é:

```text
identificar conflito
       ↓
compreender as duas versões
       ↓
escolher/combinar conteúdo correto
       ↓
salvar
       ↓
git add
       ↓
concluir merge
```

Se um conflito aparecer nesta atividade, trate-o como uma situação real de versionamento.

---

# 73. Testar depois do merge

Mesmo que a branch funcionasse, execute novamente:

```powershell
python main.py
```

A `main` precisa ser validada.

---

# 74. Publicar no GitHub

Depois da validação:

```bash
git push
```

Agora o GitHub receberá a versão modularizada na `main`.

---

# 75. Publicar também a branch é obrigatório?

Não para concluir esta atividade.

A branch local foi utilizada para desenvolver e validar a refatoração.

Em projetos colaborativos, branches frequentemente são publicadas e integradas por meio de Pull Requests.

Esse fluxo será aprofundado quando houver necessidade de colaboração/revisão.

---

# 76. Apagar a branch local?

Depois de confirmar que:

```text
merge concluído
+
main funcionando
+
push concluído
```

podemos remover a branch local:

```bash
git branch -d feature-modularizacao
```

O `-d` solicita uma exclusão segura, normalmente recusando remover uma branch que ainda não foi integrada.

---

# 77. Atualizar a Sprint 07

Abra:

```text
docs/sprints/sprint-07-modularizacao.md
```

Marque as tarefas concluídas:

```markdown
- [x] confirmar versão funcional na `main`;
- [x] criar a branch `feature-modularizacao`;
- [x] criar `src/engconvert`;
- [x] criar `__init__.py`;
- [x] criar `dados.py`;
- [x] separar os dados de conversão;
- [x] criar `conversoes.py`;
- [x] separar as regras de conversão;
- [x] criar `interface.py`;
- [x] separar a interface gráfica;
- [x] simplificar `main.py`;
- [x] testar as conversões;
- [x] documentar a arquitetura;
- [x] criar commits incrementais;
- [x] integrar a branch à `main`;
- [x] publicar a nova estrutura no GitHub.
```

---

# 78. Registrar o resultado

Acrescente:

```markdown
## Resultado

O EngConvert foi reorganizado em módulos com responsabilidades distintas para dados, regras de conversão, interface gráfica e inicialização.

A refatoração foi desenvolvida em uma branch específica, validada e posteriormente integrada à `main`.

## Status

**CONCLUÍDA**
```

---

# 79. Atualizar o Roadmap

Em:

```text
docs/roadmap.md
```

a Etapa 8 passa a ficar concluída:

```markdown
- [x] **Etapa 1 — Ambiente e estrutura**
- [x] **Etapa 2 — Primeira interface gráfica**
- [x] **Etapa 3 — Widgets e eventos**
- [x] **Etapa 4 — Primeiro conversor**
- [x] **Etapa 5 — Conversor de pressão**
- [x] **Etapa 6 — Novas grandezas**
- [x] **Etapa 7 — Git e GitHub**
- [x] **Etapa 8 — Modularização**
- [ ] **Etapa 9 — Testes**
- [ ] **Etapa 10 — Interface completa**
- [ ] **Etapa 11 — Distribuição**
```

---

# 80. Estado da Sprint

```text
SPRINT 07 — MODULARIZAÇÃO DO ENGCONVERT

STATUS:

CONCLUÍDA
```

E:

```text
ETAPA 8 — MODULARIZAÇÃO

STATUS:

CONCLUÍDA
```

---

# 81. Antes × depois

Antes:

```text
main.py
   │
   ├── dados
   ├── conversões
   ├── interface
   └── inicialização
```

Depois:

```text
main.py
   │
   └── inicialização

src/
└── engconvert/
    ├── dados.py
    ├── conversoes.py
    └── interface.py
```

---

# 82. O que ganhamos?

A modularização tornou mais claro:

```text
onde estão os dados
onde estão os cálculos
onde está a GUI
onde a aplicação começa
```

Além disso:

```text
conversoes.py
```

pode ser trabalhado com muito menos dependência da interface gráfica.

Isso será fundamental na próxima etapa.

---

# 83. O que não fizemos?

Não transformamos o EngConvert automaticamente em:

```text
MVC
MVP
MVVM
Clean Architecture
Hexagonal Architecture
```

Também não criamos uma arquitetura orientada a objetos complexa.

Aplicamos o princípio necessário neste estágio:

```text
SEPARAÇÃO DE RESPONSABILIDADES
```

---

# 84. O Git deixou de ser apenas conteúdo teórico

Nesta Sprint utilizamos Git para uma situação real:

```text
main
  ↓
branch
  ↓
refatoração
  ↓
commits incrementais
  ↓
testes
  ↓
merge
  ↓
push
```

Essa é uma evolução importante no fluxo de desenvolvimento.

---

# 85. O que será testado na próxima etapa?

Agora podemos chamar funções de conversão sem depender diretamente de cliques na interface.

Exemplo conceitual:

```python
resultado = converter(
    1,
    "Pressão",
    "bar",
    "kPa"
)
```

Esperamos:

```text
100
```

Na próxima etapa, em vez de verificar isso manualmente, poderemos escrever um teste.

---

# 86. De teste manual para teste automatizado

Hoje:

```text
executar aplicação
      ↓
digitar 1
      ↓
selecionar bar
      ↓
selecionar kPa
      ↓
clicar
      ↓
conferir 100
```

Na próxima etapa:

```text
pytest
   ↓
chamar converter(...)
   ↓
comparar resultado esperado
   ↓
PASS / FAIL
```

---

# 87. Preparação para CI

Na Aula 07.0 conhecemos o conceito de:

```text
CI
↓
Continuous Integration
↓
Integração Contínua
```

Ainda não configuraremos CI nesta Sprint.

Mas agora começamos a construir um requisito importante para isso:

```text
FUNÇÕES TESTÁVEIS
```

Depois teremos:

```text
funções testáveis
       ↓
pytest
       ↓
testes automatizados
       ↓
futuramente
GitHub Actions / CI
```

---

# 88. Checklist final

Confirme:

```text
[ ] main estava funcional antes da mudança
[ ] branch feature-modularizacao criada
[ ] src/engconvert criado
[ ] __init__.py criado
[ ] dados.py criado
[ ] dados separados
[ ] conversoes.py criado
[ ] regras separadas
[ ] interface.py criado
[ ] GUI separada
[ ] main.py simplificado
[ ] pyproject.toml criado
[ ] projeto instalado em modo editável
[ ] import engconvert funciona
[ ] aplicação abre
[ ] conversões continuam corretas
[ ] tratamento de entrada inválida funciona
[ ] arquitetura.md criado
[ ] commits incrementais criados
[ ] merge concluído
[ ] main testada depois do merge
[ ] push concluído
[ ] Sprint 07 concluída
[ ] Etapa 8 concluída
```

---

# 89. 📌 Resumo da Aula 08.1

Executamos uma refatoração estrutural:

```text
main.py monolítico
        ↓
separação de responsabilidades
        ↓
pacote engconvert
        ↓
dados.py
conversoes.py
interface.py
        ↓
main.py simplificado
```

Também utilizamos:

```text
Git
 ↓
branch
 ↓
commits incrementais
 ↓
merge
 ↓
push
```

---

# 90. 🔜 Próxima etapa

A próxima etapa será:

```text
ETAPA 9 — TESTES
```

Começaremos pela pergunta:

```text
Como provar automaticamente
que uma conversão continua correta
depois que o código muda?
```

A resposta nos levará a:

```text
pytest
```

e a conceitos como:

```text
teste unitário
assert
caso de teste
resultado esperado
PASS
FAIL
regressão
parametrização
```

---

# 🧭 Visão do percurso

```text
Aula 07.1
Git e GitHub
      ↓
Aula 08.0
Modularização — conceitos
      ↓
Aula 08.1
Modularização — implementação
      ↓
Sprint 07 — CONCLUÍDA
      ↓
Etapa 8 — CONCLUÍDA
      ↓
Aula 09.0
Testes
      ↓
Aula 09.1
Testes automatizados no EngConvert
```

> 🎯 **Ideia final:** modularizar não significa espalhar o programa em vários arquivos. Significa **organizar responsabilidades** de modo que cada parte do software possa ser compreendida, modificada e testada com mais segurança.


---

# 91. Código completo da Sprint 07 — referência oficial de implementação

> **Esta seção substitui os exemplos com `...` apresentados anteriormente.** Os blocos abaixo são os arquivos completos, derivados do `main.py` fornecido pelo professor. A implementação conserva os fatores, as cinco grandezas, os galões, as quatro escalas de temperatura, os widgets e a formatação `.6g`. O nome da função de evento passa a ser `ao_converter`, enquanto `converter` passa a designar a regra matemática independente da GUI.

## 91.1. Onde colocar cada arquivo

```text
engconvert/
├── main.py
├── pyproject.toml
├── .gitignore
└── src/
    └── engconvert/
        ├── __init__.py
        ├── dados.py
        ├── conversoes.py
        └── interface.py
```

**Importante:** não mantenha simultaneamente os dados e os eventos antigos no `main.py`. Substitua-o pelo novo ponto de entrada **somente depois** de criar os módulos e instalar o projeto em modo editável.

## 91 — Arquivo `main.py`

```python
"""Ponto de entrada do EngConvert."""

from engconvert.interface import iniciar_aplicacao


def main():
    iniciar_aplicacao()


if __name__ == "__main__":
    main()
```

## 91 — Arquivo `src/engconvert/__init__.py`

```python
"""Pacote principal do EngConvert."""
```

## 91 — Arquivo `src/engconvert/dados.py`

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

## 91 — Arquivo `src/engconvert/conversoes.py`

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

## 91 — Arquivo `src/engconvert/interface.py`

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

## 91 — Arquivo `pyproject.toml`

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

## 92. Preparar o ambiente e executar

Na raiz `C:\Projetos\engconvert`, com o ambiente virtual ativo:

```powershell
python -m pip install -e .
python main.py
```

A instalação editável permite importar `engconvert` a partir da pasta `src/` sem modificar manualmente `sys.path`. O `pyproject.toml` declara essa estrutura.

## 93. Verificações manuais após a modularização

| Grandeza | Origem → destino | Resultado esperado |
|---|---|---|
| Pressão | 1 bar → kPa | 100 kPa |
| Comprimento | 1 m → mm | 1000 mm |
| Área | 1 m² → cm² | 10000 cm² |
| Volume | 1 L → mL | 1000 mL |
| Volume | 1 gal (US) → L | 3,78541 L com `.6g` |
| Volume | 1 gal (UK) → L | 4,54609 L |
| Temperatura | 0 °C → °F | 32 °F |
| Temperatura | 0 °C → K | 273,15 K |
| Temperatura | 491,67 °R → °F | aproximadamente 32 °F |

Teste também a troca `De ↔ Para`, a seleção de categorias e a entrada `abc`. Os resultados numéricos acima se referem às regras matemáticas; a apresentação depende da formatação `.6g`.

## 94. Diferenças intencionais em relação ao `main.py` anterior

- `dados.py` recebe **exatamente os fatores e nomes de unidades** da versão anterior.
- `conversoes.py` contém `converter_temperatura`, `obter_unidades` e a nova função matemática `converter(valor, grandeza, unidade_de, unidade_para)`.
- `interface.py` recebe a construção da janela e os eventos, agora definidos dentro de `iniciar_aplicacao()` para manter acesso aos widgets sem variáveis globais entre módulos.
- O antigo evento `converter()` recebe o nome `ao_converter()`, evitando confusão com a função matemática.
- `main.py` passa a conter somente a inicialização.
- `pyproject.toml` permite a instalação editável do pacote na estrutura `src`.

> **Critério de conclusão:** a aplicação precisa abrir, realizar todas as conversões anteriores e tratar entradas inválidas. Só depois faça o merge e o push.
