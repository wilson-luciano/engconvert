# Aula 05.0 — Conversor de Pressão

## De uma conversão fixa para um conversor com múltiplas unidades

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Pré-requisito:** Aulas 04.0 e 04.1 concluídas e **Sprint 03 — Primeiro Conversor** encerrada.

---

## 🎯 Objetivos

Ao final desta aula, o aluno deverá ser capaz de:

- compreender a evolução de uma conversão fixa para um conversor com múltiplas unidades;
- compreender por que é vantajoso utilizar uma **unidade de referência**;
- utilizar o **pascal (Pa)** como unidade intermediária das conversões de pressão;
- representar fatores de conversão utilizando um **dicionário Python**;
- acessar valores de um dicionário por meio de suas chaves;
- compreender como uma única expressão pode substituir diversas fórmulas de conversão;
- utilizar o widget `CTkComboBox`;
- obter a opção selecionada em um `CTkComboBox` utilizando `.get()`;
- definir uma opção em um `CTkComboBox` utilizando `.set()`;
- criar seletores de unidade **De** e **Para**;
- implementar uma função genérica de conversão de pressão;
- implementar a inversão das unidades por meio de um botão `↔`;
- revisar `float()`, `try`, `except`, `ValueError`, `f-string` e `.configure()`;
- compreender o fluxo completo **entrada → unidade de origem → unidade de referência → unidade de destino → resultado**.

---

# 1. Onde estamos no EngConvert?

Na Aula 04 construímos o primeiro conversor real do projeto.

Ele recebe uma pressão em:

```text
bar
```

e converte para:

```text
kPa
```

O fluxo atual é:

```text
USUÁRIO
   ↓
digita a pressão em bar
   ↓
CTkEntry
   ↓
.get()
   ↓
float()
   ↓
pressao_bar
   ↓
× 100
   ↓
pressao_kpa
   ↓
f-string
   ↓
.configure()
   ↓
RESULTADO
```

Exemplo:

```text
2.5 bar
   ↓
250.00 kPa
```

Esse foi um passo importante porque o EngConvert deixou de apenas reproduzir uma entrada e passou a realizar um **cálculo de engenharia**.

Entretanto, a conversão ainda está fixa:

```text
bar → kPa
```

O usuário ainda não pode escolher as unidades.

---

# 2. A próxima etapa do Roadmap

Na Aula 04.1 concluímos:

```text
Etapa 4 — Primeiro conversor
```

A próxima etapa planejada é:

```text
Etapa 5 — Conversor de pressão
```

Agora queremos evoluir de:

```text
bar → kPa
```

para:

```text
          ┌── Pa
          ├── kPa
          ├── MPa
          ├── bar
PRESSÃO ──┼── mbar
          ├── kgf/cm²
          ├── psi
          ├── atm
          └── m.c.a.
```

O usuário deverá escolher:

```text
      valor
        ↓
 DE qual unidade?
        ↓
PARA qual unidade?
        ↓
    converter
```

---

# 3. O problema de escrever uma fórmula para cada conversão

Poderíamos começar criando diversas condições:

```python
if unidade_de == "bar" and unidade_para == "kPa":
    resultado = valor * 100

elif unidade_de == "bar" and unidade_para == "Pa":
    resultado = valor * 100_000

elif unidade_de == "psi" and unidade_para == "bar":
    ...
```

Isso funcionaria para poucos casos.

Mas nosso conversor terá inicialmente **9 unidades**.

Se considerarmos todas as combinações entre unidade de origem e unidade de destino, teremos:

```text
9 × 9 = 81 combinações
```

Isso inclui também situações como:

```text
bar → bar
Pa → Pa
psi → psi
```

Escrever uma condição específica para cada possibilidade tornaria o programa:

- longo;
- repetitivo;
- difícil de manter;
- difícil de ampliar;
- mais sujeito a erros.

Precisamos de uma estratégia melhor.

> 🎯 **Ideia-chave:** em vez de criar uma fórmula para cada par de unidades, podemos converter todas elas por meio de uma unidade comum de referência.

---

# 4. Escolhendo uma unidade de referência

Para pressão, utilizaremos o:

```text
pascal
```

Símbolo:

```text
Pa
```

O pascal é a unidade de pressão do Sistema Internacional de Unidades.

Podemos representar:

$$
1\;Pa = 1\;N/m^2
$$

No EngConvert, o `Pa` será nossa **unidade de referência**.

A estratégia será:

```text
UNIDADE DE ORIGEM
        ↓
       Pa
        ↓
UNIDADE DE DESTINO
```

Exemplo:

```text
bar
 ↓
Pa
 ↓
psi
```

Outro exemplo:

```text
 m.c.a.
   ↓
  Pa
   ↓
  kPa
```

Não precisamos apresentar o valor intermediário ao usuário.

Ele será utilizado internamente pelo programa.

---

# 5. Unidades de pressão utilizadas nesta etapa

Nesta primeira versão do conversor de pressão utilizaremos:

| Unidade                                  | Símbolo no EngConvert | Equivalência adotada em Pa |
| ---------------------------------------- | --------------------- | -------------------------: |
| pascal                                   | `Pa`                  |                          1 |
| quilopascal                              | `kPa`                 |                      1 000 |
| megapascal                               | `MPa`                 |                  1 000 000 |
| bar                                      | `bar`                 |                    100 000 |
| milibar                                  | `mbar`                |                        100 |
| quilograma-força por centímetro quadrado | `kgf/cm²`             |                   98 066,5 |
| libra-força por polegada quadrada        | `psi`                 |                  6 894,757 |
| atmosfera padrão                         | `atm`                 |                    101 325 |
| metro de coluna d'água                   | `m.c.a.`              |                   9 806,65 |

Esses valores serão os **fatores de conversão para pascal** utilizados pelo programa.

---

# 6. Observação de engenharia sobre `m.c.a.`

A unidade:

```text
m.c.a.
```

significa:

```text
metro de coluna d'água
```

Ela é particularmente importante em aplicações como:

- bombas;
- sistemas hidráulicos;
- instalações industriais;
- sistemas de abastecimento;
- manometria.

A relação física entre pressão e altura de uma coluna de fluido pode ser escrita como:

$$
p = \rho g h
$$

onde:

```text
p  → pressão
ρ  → massa específica do fluido
g  → aceleração da gravidade
h  → altura da coluna de fluido
```

Para o EngConvert adotaremos a equivalência convencional:

$$
1\;m.c.a. = 9\,806{,}65\;Pa
$$

Assim:

$$
10\;m.c.a. = 98\,066{,}5\;Pa
$$

e:

$$
10\;m.c.a. = 1\;\mathrm{kgf/cm^2}
$$

considerando os fatores convencionais adotados nesta aula.

> 📌 Em aplicações de engenharia mais específicas, a pressão associada a uma coluna real de fluido depende das propriedades do fluido e das condições consideradas. Nesta etapa, utilizaremos fatores convencionais fixos para construir o conversor de unidades.

---

# 7. Representando os fatores em Python

Precisamos armazenar uma associação entre:

```text
  unidade
     ↓
fator em Pa
```

Por exemplo:

```text
  bar
   ↓
100 000
```

e:

```text
   psi
    ↓
6 894.757
```

Uma estrutura adequada para isso é o:

```text
dicionário
```

Em Python:

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

Observe a estrutura:

```text
CHAVE        VALOR
  ↓            ↓
"bar"   :   100_000
"psi"   :   6_894.757
```

Cada chave representa uma unidade.

Cada valor representa quantos pascals correspondem a **uma unidade** daquela grandeza.

---

# 8. Por que os números possuem `_`?

Observe:

```python
100_000
1_000_000
98_066.5
```

Em Python, o caractere `_` pode ser utilizado em literais numéricos para melhorar a legibilidade.

Assim:

```python
100_000
```

equivale numericamente a:

```python
100000
```

E:

```python
1_000_000
```

equivale a:

```python
1000000
```

O `_` não altera o valor.

Ele apenas facilita a leitura.

Para engenharia, isso é especialmente útil em números com muitos algarismos.

---

# 9. Consultando o dicionário

Se quisermos obter o fator correspondente a `bar`:

```python
fatores_pressao["bar"]
```

obteremos:

```text
100000
```

Para `psi`:

```python
fatores_pressao["psi"]
```

obteremos aproximadamente:

```text
6894.757
```

Podemos imaginar:

```text
    "bar"
      ↓
procura a chave
      ↓
fatores_pressao
      ↓
   100000
```

Essa característica será fundamental para nossa função de conversão.

---

# 10. Primeira etapa matemática — origem para Pa

Considere que o usuário deseje converter:

```text
2 bar
```

Sabemos que o fator de `bar` é:

```text
100 000
```

Então:

$$
p_{Pa} = p_{origem} \times F_{origem}
$$

No exemplo:

$$
p_{Pa} = 2 \times 100\,000
$$

Logo:

$$
p_{Pa} = 200\,000\;Pa
$$

Em Python:

```python
valor_pa = valor * fatores_pressao[unidade_de]
```

---

# 11. Segunda etapa matemática — Pa para destino

Agora suponha que o destino seja:

```text
kPa
```

O fator de `kPa` é:

```text
1 000
```

Então:

$$
p_{destino} =
\frac{p_{Pa}}{F_{destino}}
$$

No exemplo:

$$
p_{kPa} =
\frac{200\,000}{1\,000}
$$

Logo:

$$
p_{kPa} = 200
$$

Em Python:

```python
valor_convertido = valor_pa / fatores_pressao[unidade_para]
```

---

# 12. A expressão geral da conversão

Podemos juntar as duas etapas.

Primeiro:

$$
p_{Pa} = p_{origem}F_{origem}
$$

Depois:

$$
p_{destino} =
\frac{p_{Pa}}{F_{destino}}
$$

Substituindo:

$$
\boxed{
p_{destino}
=
p_{origem}
\frac{F_{origem}}{F_{destino}}
}
$$

onde:

- $p_{origem}$ → valor da pressão na unidade de origem;
- $F_{origem}$ → fator de conversão da unidade de origem para Pa;
- $F_{destino}$ → fator de conversão da unidade de destino para Pa;
- $p_{destino}$ → valor da pressão na unidade de destino.

Em Python, poderíamos escrever diretamente:

```python
valor_convertido = (
    valor
    * fatores_pressao[unidade_de]
    / fatores_pressao[unidade_para]
)
```

Entretanto, nesta etapa didática utilizaremos duas instruções:

```python
valor_pa = valor * fatores_pressao[unidade_de]

valor_convertido = (
    valor_pa / fatores_pressao[unidade_para]
)
```

Isso torna o raciocínio mais visível:

```text
ORIGEM
   ↓
  Pa
   ↓
DESTINO
```

> 🎯 **Ideia-chave:** o código deve ser compreensível, não apenas curto.

---

# 13. Exemplo completo — `bar → psi`

Considere:

```text
valor = 2
unidade_de = "bar"
unidade_para = "psi"
```

Primeira etapa:

```text
2 bar
  ↓
2 × 100000
  ↓
200000 Pa
```

Segunda etapa:

```text
200000 Pa
    ↓
200000 ÷ 6894.757
    ↓
aproximadamente 29.01 psi
```

O programa utiliza a mesma lógica que utilizaria para:

```text
MPa → bar
mbar → kPa
atm → psi
m.c.a. → bar
kgf/cm² → MPa
```

---

# 14. Um detalhe interessante: converter uma unidade para ela mesma

Considere:

```text
bar → bar
```

A expressão será:

$$
p_{destino}
=
p_{origem}
\frac{100000}{100000}
$$

Como:

$$
\frac{100000}{100000}=1
$$

temos:

$$
p_{destino}=p_{origem}
$$

Portanto:

```text
2.5 bar → 2.5 bar
```

funciona naturalmente.

Não precisamos criar uma condição especial para isso.

---

# 15. O novo widget: `CTkComboBox`

Até agora utilizamos:

```text
CTkFrame
CTkLabel
CTkEntry
CTkButton
```

Agora precisamos permitir que o usuário escolha uma unidade em uma lista.

Utilizaremos:

```python
ctk.CTkComboBox
```

Um `CTkComboBox` apresenta opções que podem ser selecionadas pelo usuário.

Exemplo:

```python
combo_de = ctk.CTkComboBox(
    container,
    values=[
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
)
```

Conceitualmente:

```text
CTkComboBox
     ↓
lista de opções
     ↓
usuário seleciona uma
```

---

# 16. O parâmetro `values`

Observe:

```python
values=[
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

O parâmetro:

```text
values
```

define as opções disponíveis no `CTkComboBox`.

Nesse caso, `values` recebe uma:

```text
lista
```

Podemos visualizar:

```text
values
  │
  ├── Pa
  ├── kPa
  ├── MPa
  ├── bar
  ├── mbar
  ├── kgf/cm²
  ├── psi
  ├── atm
  └── m.c.a.
```

---

# 17. Evitando repetir a lista de unidades

Precisaremos de dois `CTkComboBox`:

```text
DE
```

e:

```text
PARA
```

Em vez de repetir a lista em ambos, podemos obtê-la a partir das chaves do próprio dicionário:

```python
unidades_pressao = list(fatores_pressao.keys())
```

Vamos decompor:

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

O resultado será equivalente a:

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

Agora podemos utilizar:

```python
values=unidades_pressao
```

nos dois seletores.

> 🎯 **Ideia-chave:** o dicionário passa a ser a fonte tanto dos fatores de conversão quanto dos nomes das unidades disponíveis.

---

# 18. Criando o seletor `De`

Primeiro podemos criar um rótulo:

```python
label_de = ctk.CTkLabel(
    container,
    text="De"
)
```

Depois:

```python
combo_de = ctk.CTkComboBox(
    container,
    values=unidades_pressao,
    width=180
)
```

E definir uma seleção inicial:

```python
combo_de.set("bar")
```

Assim, quando o programa abrir:

```text
De
[ bar ▼ ]
```

---

# 19. Criando o seletor `Para`

O mesmo princípio é utilizado para a unidade de destino:

```python
label_para = ctk.CTkLabel(
    container,
    text="Para"
)
```

Depois:

```python
combo_para = ctk.CTkComboBox(
    container,
    values=unidades_pressao,
    width=180
)
```

Podemos iniciar com:

```python
combo_para.set("kPa")
```

A interface começará com:

```text
De          Para
bar    →    kPa
```

Isso preserva a conversão utilizada na Aula 04, mas agora ela poderá ser alterada pelo usuário.

---

# 20. Obtendo a unidade selecionada com `.get()`

Já utilizamos:

```python
entrada.get()
```

para obter o conteúdo de um `CTkEntry`.

Também podemos utilizar `.get()` em um `CTkComboBox`.

Exemplo:

```python
unidade_de = combo_de.get()
```

Se o usuário selecionou:

```text
bar
```

a variável receberá:

```python
"bar"
```

Para a unidade de destino:

```python
unidade_para = combo_para.get()
```

Se estiver selecionado:

```text
psi
```

teremos:

```python
"psi"
```

O fluxo será:

```text
CTkComboBox
     ↓
   .get()
     ↓
  "bar"
```

---

# 21. Evoluindo a função `converter()`

Na Aula 04 tínhamos uma conversão fixa:

```python
pressao_bar = float(entrada.get())

pressao_kpa = pressao_bar * 100
```

Agora precisamos descobrir as unidades escolhidas.

Começamos:

```python
valor = float(entrada.get())

unidade_de = combo_de.get()

unidade_para = combo_para.get()
```

Depois convertemos o valor de origem para Pa:

```python
valor_pa = valor * fatores_pressao[unidade_de]
```

E de Pa para a unidade desejada:

```python
valor_convertido = (
    valor_pa / fatores_pressao[unidade_para]
)
```

---

# 22. A nova função `converter()`

Podemos escrever:

```python
def converter():

    try:

        # Obtém e converte o valor digitado.
        valor = float(entrada.get())

        # Obtém as unidades selecionadas.
        unidade_de = combo_de.get()
        unidade_para = combo_para.get()

        # Converte a unidade de origem para pascal.
        valor_pa = (
            valor * fatores_pressao[unidade_de]
        )

        # Converte de pascal para a unidade de destino.
        valor_convertido = (
            valor_pa / fatores_pressao[unidade_para]
        )

        # Apresenta o resultado.
        resultado.configure(
            text=f"{valor_convertido:.2f} {unidade_para}"
        )

    except ValueError:

        resultado.configure(
            text="Digite um valor numérico válido."
        )
```

Observe que `try`, `except` e `ValueError` continuam sendo utilizados.

Não abandonamos o que foi aprendido.

Estamos **evoluindo o mesmo código**.

---

# 23. O fluxo completo da nova função

Agora teremos:

```text
USUÁRIO
   ↓
digita o valor
   ↓
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
consulta o dicionário
   ↓
fator de origem
   ↓
converte para Pa
   ↓
combo_para.get()
   ↓
unidade_para
   ↓
consulta o dicionário
   ↓
fator de destino
   ↓
converte de Pa
   ↓
valor_convertido
   ↓
f-string
   ↓
.configure()
   ↓
RESULTADO
```

Essa é a primeira conversão **genérica** do EngConvert.

---

# 24. Reaproveitando conhecimentos anteriores

Observe quantos conceitos das aulas anteriores continuam presentes:

```text
CTkEntry
   ↓
.get()

CTkButton
   ↓
command

função
   ↓
converter()

float()
   ↓
texto → número

try / except
   ↓
tratamento de exceções

f-string
   ↓
formatação

.configure()
   ↓
atualização da interface
```

E acrescentamos:

```text
dicionário
   ↓
fatores de conversão

CTkComboBox
   ↓
seleção de unidades

.keys()
   ↓
chaves do dicionário

.set()
   ↓
define a opção selecionada

unidade de referência
   ↓
conversão genérica
```

---

# 25. Invertendo as unidades

Conversores de unidades frequentemente permitem inverter rapidamente:

```text
De ↔ Para
```

Por exemplo:

```text
bar → psi
```

pode se tornar:

```text
psi → bar
```

Para isso criaremos uma segunda função:

```python
def inverter_unidades():

    unidade_de = combo_de.get()
    unidade_para = combo_para.get()

    combo_de.set(unidade_para)
    combo_para.set(unidade_de)
```

---

# 26. Entendendo `inverter_unidades()`

Primeiro guardamos as duas seleções atuais:

```python
unidade_de = combo_de.get()
unidade_para = combo_para.get()
```

Imagine:

```text
unidade_de   = "bar"
unidade_para = "psi"
```

Depois:

```python
combo_de.set(unidade_para)
```

faz:

```text
De = psi
```

E:

```python
combo_para.set(unidade_de)
```

faz:

```text
Para = bar
```

Resultado:

```text
ANTES

bar → psi


DEPOIS

psi → bar
```

---

# 27. `.get()` × `.set()`

Agora podemos comparar dois métodos importantes:

```text
.get()
   ↓
OBTÉM o valor atual
```

e:

```text
.set()
   ↓
DEFINE um novo valor
```

Exemplo:

```python
unidade = combo_de.get()
```

lê a seleção.

Enquanto:

```python
combo_de.set("bar")
```

altera a seleção para `bar`.

Podemos resumir:

```text
.get()  → ler
.set()  → definir
```

---

# 28. Criando o botão de inversão

Podemos criar:

```python
botao_inverter = ctk.CTkButton(
    container,
    text="↔",
    width=50,
    command=inverter_unidades
)
```

Observe:

```python
command=inverter_unidades
```

A lógica é a mesma que já utilizamos em:

```python
command=converter
```

Portanto:

```text
CLIQUE
  ↓
command
  ↓
FUNÇÃO
```

Temos agora dois eventos:

```text
[ Converter ]
      ↓
 converter()


[ ↔ ]
   ↓
inverter_unidades()
```

---

# 29. Organizando `De`, `↔` e `Para`

Até agora utilizamos um `container` principal.

Para organizar os seletores horizontalmente, podemos criar um novo frame dentro dele:

```python
frame_unidades = ctk.CTkFrame(
    container,
    fg_color="transparent"
)
```

Depois:

```python
frame_unidades.pack(pady=15)
```

A estrutura passa a ser:

```text
app
 │
 └── container
      │
      ├── titulo
      ├── subtitulo
      ├── entrada
      │
      ├── frame_unidades
      │     │
      │     ├── grupo_de
      │     ├── botao_inverter
      │     └── grupo_para
      │
      ├── botao_converter
      └── resultado
```

Estamos começando a construir uma interface com **agrupamentos internos**.

---

# 30. Frames para os seletores

Podemos criar um pequeno frame para cada lado.

Para `De`:

```python
frame_de = ctk.CTkFrame(
    frame_unidades,
    fg_color="transparent"
)
```

Para `Para`:

```python
frame_para = ctk.CTkFrame(
    frame_unidades,
    fg_color="transparent"
)
```

Assim, cada grupo pode conter:

```text
De
[ bar ▼ ]
```

e:

```text
Para
[ kPa ▼ ]
```

---

# 31. Por que utilizar `side` no `pack()`?

Para colocar os elementos lado a lado podemos utilizar:

```python
frame_de.pack(
    side="left",
    padx=10
)
```

Depois:

```python
botao_inverter.pack(
    side="left",
    padx=5,
    pady=(25, 0)
)
```

E:

```python
frame_para.pack(
    side="left",
    padx=10
)
```

O parâmetro:

```text
side="left"
```

faz com que os widgets sejam posicionados sequencialmente a partir do lado esquerdo do frame.

Visualmente:

```text
┌──────────────────────────────────────────┐
│  De             ↔             Para       │
│ [bar ▼]                     [kPa ▼]      │
└──────────────────────────────────────────┘
```

> 📌 Continuamos utilizando `pack()`. Ainda não precisamos introduzir outro gerenciador de geometria apenas para construir esta etapa.

---

# 32. Evoluindo o campo de entrada

Na Aula 04 utilizávamos:

```python
placeholder_text="Pressão em bar"
```

Agora a unidade de origem pode mudar.

Portanto, um texto mais adequado é:

```python
placeholder_text="Digite o valor da pressão"
```

Assim, o campo não fica associado permanentemente a `bar`.

---

# 33. Evoluindo o subtítulo

Também não faz mais sentido manter:

```text
Pressão: bar → kPa
```

porque as unidades agora são selecionáveis.

Podemos utilizar:

```python
subtitulo = ctk.CTkLabel(
    container,
    text="Conversor de Pressão"
)
```

A interface começa a representar uma **categoria de conversão**, e não apenas uma operação fixa.

---

# 34. Estrutura visual esperada

A interface poderá assumir aproximadamente:

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
│               250.00 kPa                   │
│                                            │
└────────────────────────────────────────────┘
```

Agora o usuário controla:

```text
valor
unidade de origem
unidade de destino
```

---

# 35. Código completo para estudo

> 📌 O código abaixo reúne os conceitos estudados nesta aula. A implementação passo a passo será realizada na **Aula 05.1**.

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

---

# 36. O que mudou em relação à Aula 04?

Na Aula 04:

```text
ENTRADA
   ↓
  bar
   ↓
 × 100
   ↓
  kPa
```

A conversão estava definida diretamente no código:

```python
pressao_kpa = pressao_bar * 100
```

Agora:

```text
     ENTRADA
        ↓
UNIDADE DE ORIGEM
        ↓
 FATOR DE ORIGEM
        ↓
       Pa
        ↓
 FATOR DE DESTINO
        ↓
UNIDADE DE DESTINO
        ↓
    RESULTADO
```

A conversão passou a ser determinada pelos dados armazenados no dicionário:

```python
fatores_pressao
```

Isso representa uma mudança importante na estrutura do programa.

---

# 37. De fórmula fixa para dados + algoritmo

Na Aula 04 tínhamos:

```text
FÓRMULA FIXA
bar × 100 → kPa
```

Agora temos:

```text
DADOS
  ↓
dicionário de fatores

+

ALGORITMO
  ↓
origem → Pa → destino
```

Essa separação traz uma vantagem importante.

Se quisermos acrescentar uma nova unidade compatível com essa estratégia, a lógica central da conversão não precisa necessariamente ser reescrita.

Podemos ampliar os dados utilizados pelo algoritmo.

> 🎯 **Ideia-chave:** um bom programa procura separar os dados que podem variar da lógica geral que processa esses dados.

---

# 38. Testes que precisaremos realizar

Na Aula 05.1 executaremos diferentes testes.

## Teste 1 — preservar a conversão da Aula 04

```text
Entrada:
2.5

De:
bar

Para:
kPa

Resultado esperado:
250.00 kPa
```

---

## Teste 2 — `bar → Pa`

```text
Entrada:
1

De:
bar

Para:
Pa

Resultado esperado:
100000.00 Pa
```

---

## Teste 3 — `MPa → bar`

```text
Entrada:
1

De:
MPa

Para:
bar

Resultado esperado:
10.00 bar
```

---

## Teste 4 — `kgf/cm² → m.c.a.`

```text
Entrada:
1

De:
kgf/cm²

Para:
m.c.a.

Resultado esperado:
10.00 m.c.a.
```

---

## Teste 5 — `atm → kPa`

```text
Entrada:
1

De:
atm

Para:
kPa

Resultado esperado:
101.33 kPa
```

Com duas casas decimais, `101.325` será apresentado como:

```text
101.33 kPa
```

---

## Teste 6 — mesma unidade

```text
Entrada:
25

De:
psi

Para:
psi

Resultado esperado:
25.00 psi
```

---

## Teste 7 — entrada inválida

```text
Entrada:
dez

Resultado esperado:
Digite um valor numérico válido.
```

---

## Teste 8 — campo vazio

```text
Entrada:
[vazio]

Resultado esperado:
Digite um valor numérico válido.
```

---

## Teste 9 — inversão das unidades

Situação inicial:

```text
De: bar
Para: psi
```

Depois de clicar:

```text
↔
```

deverá resultar em:

```text
De: psi
Para: bar
```

---

# 39. E os valores negativos?

A discussão iniciada na Aula 04 continua válida.

Nosso algoritmo consegue calcular, por exemplo:

```text
-0.5 bar
```

em outras unidades.

Mas a validade física de uma pressão negativa depende da referência e do contexto da grandeza.

Por isso, nesta etapa continuaremos sem bloquear automaticamente números negativos.

Estamos separando dois conceitos:

```text
VALIDAÇÃO COMPUTACIONAL
        ↓
o dado pode ser convertido para número?


VALIDAÇÃO FÍSICA
        ↓
o valor faz sentido para o problema?
```

Essa distinção é importante em programas de engenharia.

---

# 40. Precisão decimal nesta etapa

Continuaremos apresentando:

```python
f"{valor_convertido:.2f} {unidade_para}"
```

Portanto, nesta versão:

```text
:.2f
```

significa que o resultado será mostrado com duas casas decimais.

Exemplo:

```text
101.325
   ↓
101.33
```

Neste momento, a precisão permanecerá fixa.

Mais adiante, o EngConvert poderá evoluir para permitir que o usuário escolha a precisão de apresentação e utilize notação científica quando necessário.

Por enquanto, o objetivo é manter o foco na **lógica do conversor de pressão**.

---

# 41. O que ainda não estamos fazendo?

Mesmo com essa evolução, ainda existem funcionalidades futuras.

Por exemplo:

```text
outras grandezas
      ↓
temperatura
comprimento
área
volume
velocidade
vazão
massa
força
torque
potência
energia
...
```

Também poderão surgir posteriormente:

```text
configurações
      ↓
precisão decimal
notação científica
organização de categorias
unidades personalizadas
```

Essas funcionalidades não são necessárias para compreender a etapa atual.

Nesta aula, o foco permanece em:

```text
PRESSÃO
   ↓
múltiplas unidades
   ↓
conversão genérica
```

---

# 42. Preparando a próxima Sprint

Com a Sprint 03 concluída, podemos planejar:

```text
SPRINT 04 — CONVERSOR DE PRESSÃO

[ ] criar o dicionário de fatores de pressão
[ ] criar a lista de unidades
[ ] criar o ComboBox "De"
[ ] criar o ComboBox "Para"
[ ] obter as unidades selecionadas
[ ] converter a unidade de origem para Pa
[ ] converter de Pa para a unidade de destino
[ ] apresentar o símbolo da unidade no resultado
[ ] criar o botão para inverter unidades
[ ] testar diferentes pares de conversão
[ ] testar entrada inválida
[ ] testar campo vazio

STATUS: PLANEJADA
```

A continuidade do projeto será:

```text
Sprint 03
Primeiro Conversor
      ↓
CONCLUÍDA
      ↓
Sprint 04
Conversor de Pressão
      ↓
PLANEJADA
```

Na Aula 05.1 implementaremos essa Sprint passo a passo.

---

# 43. 🧪 Desafio de compreensão

Considere:

```python
fatores_pressao = {
    "Pa": 1,
    "kPa": 1_000,
    "bar": 100_000
}
```

Responda:

1. O que representa a chave `"bar"`?
2. O que representa o valor `100_000`?
3. O que será retornado por `fatores_pressao["kPa"]`?
4. Por que escolhemos `Pa` como unidade de referência?
5. Qual vantagem existe em utilizar um dicionário?

Agora considere:

```python
valor_pa = valor * fatores_pressao[unidade_de]

valor_convertido = (
    valor_pa / fatores_pressao[unidade_para]
)
```

Responda:

1. O que representa `valor_pa`?
2. Por que multiplicamos pelo fator da unidade de origem?
3. Por que dividimos pelo fator da unidade de destino?
4. O que acontece se `unidade_de` e `unidade_para` forem iguais?
5. Quantas fórmulas específicas precisamos escrever para converter as nove unidades entre si utilizando essa estratégia?

Agora considere:

```python
unidade_de = combo_de.get()
combo_de.set("bar")
```

Responda:

1. Qual é a função de `.get()`?
2. Qual é a função de `.set()`?
3. Qual tipo de informação esperamos obter de `combo_de.get()`?
4. Por que dois `CTkComboBox` são necessários nesta interface?

---

# 44. 🧠 Fluxo completo do Conversor de Pressão

```text
USUÁRIO
   ↓
digita o valor
   ↓
CTkEntry
   ↓
.get()
   ↓
STRING
   ↓
float()
   ↓
NÚMERO
   ↓
   ├──────────────────────────────┐
   │                              │
combo_de.get()              combo_para.get()
   │                              │
   ↓                              ↓
UNIDADE DE ORIGEM           UNIDADE DE DESTINO
   │                              │
   ↓                              ↓
fatores_pressao             fatores_pressao
   │                              │
   ↓                              ↓
FATOR DE ORIGEM             FATOR DE DESTINO
   │                              │
   └───────────┐      ┌───────────┘
               ↓      ↓
          ORIGEM → Pa → DESTINO
                    ↓
             valor_convertido
                    ↓
                 f-string
                    ↓
               .configure()
                    ↓
                 RESULTADO
```

Se a entrada não puder ser convertida:

```text
STRING INVÁLIDA
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

# 45. 📌 Resumo da Aula 05.0

Nesta aula revisamos:

```text
CTkEntry
   ↓
entrada de dados

.get()
   ↓
obtém conteúdo ou seleção

float()
   ↓
texto → número

try / except
   ↓
tratamento de exceções

f-string
   ↓
formatação do resultado

.configure()
   ↓
atualização da GUI
```

Introduzimos:

```text
DICIONÁRIO
   ↓
unidade : fator

  Pa
   ↓
unidade de referência

.keys()
   ↓
obtém as chaves

list()
   ↓
cria a lista de unidades

CTkComboBox
   ↓
seleção de opções

.set()
   ↓
define uma seleção

De / Para
   ↓
origem e destino

   ↔
   ↓
inversão das unidades
```

E evoluímos conceitualmente de:

```text
CONVERSÃO FIXA

bar
 ↓
× 100
 ↓
kPa
```

para:

```text
CONVERSÃO GENÉRICA

UNIDADE DE ORIGEM
        ↓
       Pa
        ↓
UNIDADE DE DESTINO
```

---

# 46. 🔜 Próxima etapa — Aula 05.1

Na Aula 05.1 implementaremos:

```text
Sprint 04 — Conversor de Pressão
```

O roteiro prático seguirá aproximadamente:

```text
abrir o projeto
      ↓
conferir o Roadmap
      ↓
registrar Sprint 04
      ↓
abrir main.py
      ↓
criar fatores_pressao
      ↓
criar unidades_pressao
      ↓
criar ComboBox "De"
      ↓
criar ComboBox "Para"
      ↓
evoluir converter()
      ↓
origem → Pa
      ↓
Pa → destino
      ↓
criar inverter_unidades()
      ↓
criar botão ↔
      ↓
executar testes
      ↓
atualizar Sprint 04
      ↓
CONCLUÍDA
      ↓
atualizar Roadmap
```

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
próxima evolução
Novas grandezas
```

> 🎯 **Ideia final:** o EngConvert deixa de possuir uma única fórmula fixa e passa a utilizar dados estruturados, seleção de unidades e uma estratégia de conversão por unidade de referência. Com isso, o mesmo algoritmo passa a atender diversas combinações de pressão sem a necessidade de escrever uma fórmula específica para cada par de unidades.

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
