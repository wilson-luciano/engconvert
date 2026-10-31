# Aula 06.0 — Novas Grandezas e EngConvert Multicategorias

## Da conversão de pressão para uma arquitetura com múltiplas grandezas

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Etapa do Roadmap:** Etapa 6 — Novas Grandezas  
> **Pré-requisito:** Aulas 05.0 e 05.1 concluídas — Conversor de Pressão e Sprint 04.

---

# 🎯 Objetivos da aula

Ao final desta aula, o aluno deverá ser capaz de:

- compreender por que o EngConvert precisa evoluir de um conversor de pressão para um conversor **multicategorias**;
- distinguir **grandeza física** de **unidade de medida**;
- compreender a nova sequência de interação: **Grandeza → Unidade de origem → Unidade de destino → Entrada → Saída**;
- compreender como os dados de várias grandezas podem ser organizados em **dicionários aninhados**;
- reconhecer conversões que podem ser realizadas por **fatores multiplicativos**;
- compreender por que área e volume exigem fatores próprios;
- diferenciar **galão US** de **galão UK**;
- compreender por que a **temperatura** não pode ser tratada apenas pela mesma regra multiplicativa;
- preparar conceitualmente a implementação da **Sprint 05 — EngConvert Multicategorias**.

---

# 1. De onde estamos partindo?

Ao final da Aula 05.1, o EngConvert já possui um conversor de pressão funcional.

A interface trabalha com:

```text
valor
  ↓
unidade "De"
  ↓
unidade "Para"
  ↓
Converter
  ↓
resultado
```

E a conversão utiliza o pascal como unidade intermediária:

```text
ORIGEM
   ↓
  Pa
   ↓
DESTINO
```

O programa já trabalha com:

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

Portanto:

```text
ETAPA 5 — CONVERSOR DE PRESSÃO

STATUS:

CONCLUÍDA
```

---

# 2. O próximo problema

O nome do nosso aplicativo é:

```text
EngConvert
```

e não:

```text
PressureConvert
```

Logo, o objetivo final não é converter apenas pressão.

Um conversor de unidades de engenharia deve ser capaz de trabalhar com diferentes **grandezas**.

Exemplos:

```text
Pressão
Comprimento
Área
Volume
Temperatura
Massa
Velocidade
Vazão
Energia
Potência
Torque
...
```

A próxima evolução do projeto é:

```text
CONVERSOR DE PRESSÃO
        ↓
CONVERSOR MULTICATEGORIAS
```

---

# 3. Grandeza física não é unidade

Antes de alterar o programa, precisamos separar dois conceitos.

## Grandeza

É a propriedade que desejamos medir.

Exemplos:

```text
Comprimento
Área
Volume
Pressão
Temperatura
```

## Unidade

É a referência utilizada para expressar numericamente essa grandeza.

Exemplo:

```text
GRANDEZA
Comprimento

UNIDADES
mm
cm
m
km
in
ft
```

Outro exemplo:

```text
GRANDEZA
Pressão

UNIDADES
Pa
kPa
MPa
bar
psi
...
```

Portanto:

```text
GRANDEZA
    ↓
possui
    ↓
UNIDADES
```

---

# 4. A nova organização do EngConvert

Até agora:

```text
EngConvert
   ↓
Pressão
   ↓
unidades de pressão
```

A partir da Etapa 6:

```text
EngConvert
   │
   ├── Pressão
   │      └── unidades de pressão
   │
   ├── Comprimento
   │      └── unidades de comprimento
   │
   ├── Área
   │      └── unidades de área
   │
   ├── Volume
   │      └── unidades de volume
   │
   └── Temperatura
          └── unidades de temperatura
```

Esse é o primeiro passo para transformar o projeto em um verdadeiro conversor de engenharia.

---

# 5. Grandezas da Sprint 05

Nesta etapa não iremos adicionar dezenas de categorias de uma única vez.

A Sprint 05 trabalhará inicialmente com:

```text
Pressão
Comprimento
Área
Volume
Temperatura
```

A estratégia é:

```text
primeiro
fazer poucas categorias funcionarem corretamente

depois
expandir o catálogo
```

Isso evita aumentar a complexidade do programa antes de compreendermos sua nova estrutura.

---

# 6. Pressão permanece no projeto

A categoria:

```text
Pressão
```

não será descartada.

Ela será incorporada à nova estrutura multicategorias.

Continuaremos utilizando:

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

Portanto, o trabalho realizado nas Aulas 05.0 e 05.1 será **reaproveitado**.

Essa é uma característica importante da evolução de software:

```text
não recomeçar
     ↓
reaproveitar
     ↓
adaptar
     ↓
evoluir
```

---

# 7. Comprimento

Para a categoria **Comprimento**, utilizaremos inicialmente:

| Unidade    | Símbolo |
| ---------- | ------- |
| milímetro  | `mm`    |
| centímetro | `cm`    |
| metro      | `m`     |
| quilômetro | `km`    |
| polegada   | `in`    |
| pé         | `ft`    |

Podemos utilizar o metro como unidade de referência:

```text
ORIGEM
   ↓
   m
   ↓
DESTINO
```

Exemplos:

```text
1000 mm = 1 m

100 cm = 1 m

1 km = 1000 m

1 in = 0,0254 m

1 ft = 0,3048 m
```

No código Python, os valores decimais utilizarão ponto:

```python
0.0254
0.3048
```

---

# 8. Fatores de comprimento

Uma possível representação será:

```python
fatores_comprimento = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1_000,
    "in": 0.0254,
    "ft": 0.3048
}
```

Observe a mesma ideia utilizada em pressão:

```text
unidade
   ↓
fator em relação à unidade de referência
```

Para comprimento:

```text
unidade de referência = metro
```

---

# 9. Área

A próxima categoria será:

```text
Área
```

Unidades iniciais:

| Unidade             | Símbolo |
| ------------------- | ------- |
| milímetro quadrado  | `mm²`   |
| centímetro quadrado | `cm²`   |
| metro quadrado      | `m²`    |
| polegada quadrada   | `in²`   |
| pé quadrado         | `ft²`   |

Utilizaremos:

```text
m²
```

como unidade de referência.

---

# 10. Um cuidado importante: área não usa o fator linear

Considere:

```text
1 m = 1000 mm
```

Isso **não** significa:

```text
1 m² = 1000 mm²
```

Como:

$$
1\;\mathrm{m}=1000\;\mathrm{mm}
$$

então:

$$
1\;\mathrm{m^2}
=
(1000\;\mathrm{mm})^2
$$

logo:

$$
1\;\mathrm{m^2}
=
1\,000\,000\;\mathrm{mm^2}
$$

Portanto:

```text
COMPRIMENTO
1 m = 1 000 mm

ÁREA
1 m² = 1 000 000 mm²
```

Esse é um ponto importante para evitar erros em conversões de engenharia.

---

# 11. Fatores de área

Uma possível estrutura será:

```python
fatores_area = {
    "mm²": 0.000001,
    "cm²": 0.0001,
    "m²": 1,
    "in²": 0.00064516,
    "ft²": 0.09290304
}
```

Todos os fatores representam:

```text
quantos m² correspondem a uma unidade
```

---

# 12. Volume

A categoria **Volume** será especialmente interessante porque possui unidades métricas e unidades de outros sistemas.

Utilizaremos inicialmente:

| Unidade           | Símbolo    |
| ----------------- | ---------- |
| mililitro         | `mL`       |
| centímetro cúbico | `cm³`      |
| litro             | `L`        |
| metro cúbico      | `m³`       |
| polegada cúbica   | `in³`      |
| pé cúbico         | `ft³`      |
| galão americano   | `gal (US)` |
| galão imperial    | `gal (UK)` |

A unidade de referência será:

```text
m³
```

---

# 13. Relações importantes de volume

Algumas relações conhecidas são:

```text
1 mL = 1 cm³

1 L = 1000 mL

1 m³ = 1000 L
```

Portanto:

$$
1\;\mathrm{L}
=
0{,}001\;\mathrm{m^3}
$$

e:

$$
1\;\mathrm{mL}
=
0{,}000001\;\mathrm{m^3}
$$

---

# 14. Volume também não utiliza o fator linear

Se:

$$
1\;\mathrm{m}=1000\;\mathrm{mm}
$$

então:

$$
1\;\mathrm{m^3}
=
(1000\;\mathrm{mm})^3
$$

logo:

$$
1\;\mathrm{m^3}
=
1\,000\,000\,000\;\mathrm{mm^3}
$$

Observe a progressão:

```text
COMPRIMENTO

1 m
=
1 000 mm


ÁREA

1 m²
=
1 000 000 mm²


VOLUME

1 m³
=
1 000 000 000 mm³
```

---

# 15. Galão não é uma única unidade

A palavra:

```text
galão
```

pode representar volumes diferentes.

Nesta aula distinguiremos:

```text
gal (US)
```

e:

```text
gal (UK)
```

O **galão líquido americano** corresponde a:

$$
1\;\mathrm{gal\;(US)}
=
3{,}785411784\;\mathrm{L}
$$

O **galão imperial** corresponde a:

$$
1\;\mathrm{gal\;(UK)}
=
4{,}54609\;\mathrm{L}
$$

Portanto:

```text
1 gal (US) ≠ 1 gal (UK)
```

Essa diferença mostra por que o símbolo ou nome da unidade deve identificar claramente qual definição está sendo utilizada.

---

# 16. Fatores de volume

Utilizando `m³` como referência, poderemos representar:

```python
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

Assim, por exemplo:

```text
1 L
   ↓
0,001 m³
   ↓
0,264172... gal (US)
```

---

# 17. Até aqui temos conversões multiplicativas

Pressão, comprimento, área e volume possuem uma característica comum na estrutura que estamos adotando.

Podemos representar a conversão por:

```text
ORIGEM
   ↓
multiplica pelo fator da origem
   ↓
UNIDADE DE REFERÊNCIA
   ↓
divide pelo fator do destino
   ↓
DESTINO
```

Matematicamente:

$$
x_{\mathrm{ref}}
=
x_{\mathrm{origem}}
F_{\mathrm{origem}}
$$

e:

$$
x_{\mathrm{destino}}
=
\frac{x_{\mathrm{ref}}}
{F_{\mathrm{destino}}}
$$

Logo:

$$
\boxed{
x_{\mathrm{destino}}
=
x_{\mathrm{origem}}
\frac{F_{\mathrm{origem}}}
{F_{\mathrm{destino}}}
}
$$

Essa lógica já foi utilizada na pressão.

---

# 18. Mas nem toda conversão funciona dessa maneira

Agora acrescentaremos:

```text
Temperatura
```

Essa categoria introduz uma situação diferente.

Considere:

```text
0 °C = 32 °F
```

Se a conversão dependesse apenas de multiplicação:

```text
0 × qualquer fator = 0
```

Nunca obteríamos:

```text
32
```

Portanto:

> **Temperatura mostra que nem toda conversão pode ser representada apenas por fatores multiplicativos.**

---

# 19. Temperatura

Nesta etapa utilizaremos:

| Unidade         | Símbolo |
| --------------- | ------- |
| grau Celsius    | `°C`    |
| grau Fahrenheit | `°F`    |
| kelvin          | `K`     |
| grau Rankine    | `°R`    |

Observe os símbolos utilizados:

```text
°C
°F
K
°R
```

Em nomes de unidades escritos por extenso, usamos **grau Celsius**, **grau Fahrenheit**, **kelvin** e **grau Rankine**. O símbolo do kelvin é `K`, sem o sinal de grau.

As escalas kelvin e Rankine são escalas absolutas de temperatura.

---

# 20. Celsius e Fahrenheit

A conversão de Celsius para Fahrenheit é:

$$
T_{\mathrm{F}}
=
T_{\mathrm{C}}
\frac{9}{5}
+
32
$$

Exemplo:

$$
T_{\mathrm{C}}=100
$$

Então:

$$
T_{\mathrm{F}}
=
100
\frac{9}{5}
+
32
$$

$$
T_{\mathrm{F}}
=
212
$$

Portanto:

```text
100 °C = 212 °F
```

---

# 21. Fahrenheit e Celsius

A conversão inversa é:

$$
T_{\mathrm{C}}
=
(T_{\mathrm{F}}-32)
\frac{5}{9}
$$

Exemplo:

```text
32 °F = 0 °C
```

---

# 22. Celsius e kelvin

A relação entre Celsius e kelvin é:

$$
T_{\mathrm{K}}
=
T_{\mathrm{C}}
+
273{,}15
$$

Portanto:

```text
0 °C = 273,15 K
```

E:

$$
T_{\mathrm{C}}
=
T_{\mathrm{K}}
-
273{,}15
$$

---

# 23. Rankine

A escala Rankine é uma escala absoluta de temperatura associada ao mesmo tamanho de grau utilizado na escala Fahrenheit.

A relação entre Fahrenheit e Rankine é:

$$
T_{\mathrm{^\circ R}}
=
T_{\mathrm{^\circ F}}
+
459{,}67
$$

Portanto:

```text
32 °F = 491,67 °R
```

A relação entre kelvin e Rankine é:

$$
T_{\mathrm{^\circ R}}
=
T_{\mathrm{K}}
\frac{9}{5}
$$

e, no sentido inverso:

$$
T_{\mathrm{K}}
=
T_{\mathrm{^\circ R}}
\frac{5}{9}
$$

Como kelvin e Rankine são escalas absolutas:

```text
0 K = 0 °R
```

> 📌 **Atenção à notação:** o correto é `K`, e não `°K`. Para Rankine, utiliza-se `°R`.

A inclusão de Rankine é especialmente útil em aplicações de Termodinâmica que utilizam unidades do sistema inglês.

---

# 24. O que mudou?

Nas grandezas anteriores:

```text
valor
 ×
fator
```

era suficiente para chegar à unidade de referência.

Na temperatura aparecem operações como:

```text
+ 32

- 32

+ 273,15

- 273,15
```

Portanto, teremos dois tipos de estratégia:

```text
CONVERSÕES
    │
    ├── MULTIPLICATIVAS
    │      │
    │      ├── Pressão
    │      ├── Comprimento
    │      ├── Área
    │      └── Volume
    │
    └── TRANSFORMAÇÃO ESPECÍFICA
           │
           └── Temperatura
```

---

# 25. Por que isso é importante para programação?

Até agora poderíamos imaginar uma única regra:

```python
valor_convertido = (
    valor
    * fator_origem
    / fator_destino
)
```

Mas agora descobrimos:

```text
essa regra não resolve todos os problemas
```

Isso é muito importante no desenvolvimento de software.

O algoritmo deve representar corretamente o **modelo físico e matemático** do problema.

```text
problema de engenharia
        ↓
modelo matemático
        ↓
algoritmo
        ↓
código
```

Não devemos fazer o caminho inverso e forçar todos os problemas a caberem em um único algoritmo.

---

# 26. Evoluindo os dados do programa

Hoje possuímos:

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

Esse dicionário funciona muito bem enquanto existe apenas:

```text
Pressão
```

Mas agora teremos:

```text
Pressão
Comprimento
Área
Volume
Temperatura
```

Precisamos organizar melhor os dados.

---

# 27. Dicionários aninhados

Uma possibilidade é utilizar um dicionário que contenha outros dicionários.

Conceitualmente:

```python
grandezas = {
    "Pressão": {
        # unidades e fatores
    },

    "Comprimento": {
        # unidades e fatores
    },

    "Área": {
        # unidades e fatores
    },

    "Volume": {
        # unidades e fatores
    }
}
```

Observe a estrutura:

```text
grandezas
   │
   ├── Pressão
   │      └── unidades
   │
   ├── Comprimento
   │      └── unidades
   │
   ├── Área
   │      └── unidades
   │
   └── Volume
          └── unidades
```

Isso é um:

```text
DICIONÁRIO
    ↓
contendo
    ↓
OUTROS DICIONÁRIOS
```

---

# 28. Exemplo com duas grandezas

Um exemplo simplificado:

```python
grandezas = {
    "Pressão": {
        "Pa": 1,
        "kPa": 1_000,
        "bar": 100_000
    },

    "Comprimento": {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1
    }
}
```

Agora podemos acessar:

```python
grandezas["Pressão"]
```

ou:

```python
grandezas["Comprimento"]
```

E também:

```python
grandezas["Pressão"]["bar"]
```

Resultado:

```text
100000
```

---

# 29. Lendo um dicionário aninhado

Considere:

```python
grandezas["Comprimento"]["in"]
```

Podemos interpretar:

```text
grandezas
     ↓
"Comprimento"
     ↓
"in"
     ↓
0.0254
```

Portanto:

```text
grandezas["Comprimento"]["in"]
```

significa:

> acessar o fator da unidade `in` dentro da grandeza `Comprimento`.

Essa estrutura permite que os dados acompanhem o crescimento do programa.

---

# 30. E a temperatura?

A temperatura exige tratamento diferente.

Por isso, não devemos simplesmente inventar fatores e colocá-los no mesmo algoritmo multiplicativo.

Na Sprint 05, a lógica deverá reconhecer:

```text
QUAL É A GRANDEZA?
```

Se for:

```text
Pressão
Comprimento
Área
Volume
```

poderemos utilizar a estratégia multiplicativa.

Se for:

```text
Temperatura
```

utilizaremos uma função específica.

Conceitualmente:

```text
converter()
    │
    ├── grandeza multiplicativa?
    │          ↓
    │     usar fatores
    │
    └── Temperatura?
               ↓
        usar conversão
        de temperatura
```

---

# 31. Uma função específica para temperatura

Ainda não estamos implementando a Sprint, mas conceitualmente poderemos ter:

```python
def converter_temperatura(valor, unidade_de, unidade_para):
    ...
```

E a função principal poderá decidir qual estratégia utilizar.

Isso introduz uma ideia importante:

```text
uma função
     ↓
uma responsabilidade bem definida
```

Mais adiante, essa ideia será importante para a modularização do EngConvert.

---

# 32. A interface também precisa evoluir

A interface atual conhece apenas:

```text
Pressão
```

Por isso temos:

```text
Conversor de Pressão
```

Agora precisamos permitir que o usuário escolha:

```text
Pressão
Comprimento
Área
Volume
Temperatura
```

Surge um novo componente:

```text
SELETOR DE GRANDEZA
```

---

# 33. Nova sequência de interação

A lógica da interface passará a ser:

```text
GRANDEZA
    ↓
UNIDADE DE ORIGEM
    ↓
UNIDADE DE DESTINO
    ↓
ENTRADA
    ↓
CONVERSÃO
    ↓
SAÍDA
```

Exemplo:

```text
Grandeza
Volume

Origem
L

Destino
gal (US)

Entrada
1

Saída
0.264172...
```

---

# 34. Interface conceitual da Etapa 6

A interface poderá evoluir para algo semelhante a:

```text
┌──────────────────────────────────────────────────────┐
│                     EngConvert                       │
│                                                      │
│ Grandeza                                             │
│ [ Volume                                      ▼ ]    │
│                                                      │
│ Unidade de origem          Unidade de destino        │
│ ┌───────────────────┐      ┌───────────────────┐     │
│ │ mL                │      │ mL                │     │
│ │ cm³               │      │ cm³               │     │
│ │ L                 │      │ L                 │     │
│ │ m³                │      │ m³                │     │
│ │ in³               │      │ in³               │     │
│ │ ft³               │      │ ft³               │     │
│ │ gal (US)          │      │ gal (US)          │     │
│ │ gal (UK)          │      │ gal (UK)          │     │
│ └───────────────────┘      └───────────────────┘     │
│                                                      │
│ Entrada                                              │
│ [ 1                                             ]    │
│                                                      │
│ Saída                                                │
│ [ 0.264172                                      ]    │
│                                                      │
│       1 L = 0.264172 gal (US)                        │
└──────────────────────────────────────────────────────┘
```

A apresentação será construída de forma moderna com CustomTkinter.

---

# 35. ComboBox ou lista de unidades?

Até a Aula 05 utilizamos:

```text
CTkComboBox
```

Na nova interface poderemos evoluir a experiência para permitir que as unidades de origem e destino fiquem mais visíveis.

Entretanto, existe um princípio pedagógico importante:

> **A interface deve evoluir sem esconder a lógica que o aluno está aprendendo.**

Por isso, a Sprint 05 poderá implementar a nova estrutura de forma incremental.

Primeiro:

```text
Grandeza → ComboBox
Origem   → seletor
Destino  → seletor
```

Depois, em uma evolução visual posterior, poderemos aproximar ainda mais o comportamento da aplicação com listas permanentes de unidades.

---

# 36. O seletor de grandeza altera as unidades disponíveis

Esse será um dos novos comportamentos mais importantes.

Se o usuário selecionar:

```text
Pressão
```

os seletores deverão apresentar:

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

Se selecionar:

```text
Comprimento
```

deverão apresentar:

```text
mm
cm
m
km
in
ft
```

Se selecionar:

```text
Volume
```

deverão apresentar:

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

Portanto:

```text
GRANDEZA
    ↓
determina
    ↓
UNIDADES DISPONÍVEIS
```

---

# 37. Um novo evento

Até agora estudamos eventos como:

```text
clicar no botão Converter
```

Agora teremos outro tipo de evento:

```text
usuário muda a grandeza
```

Quando isso ocorrer:

```text
selecionar nova grandeza
        ↓
obter as unidades dessa grandeza
        ↓
atualizar seletor "De"
        ↓
atualizar seletor "Para"
        ↓
definir unidades iniciais
```

Esse comportamento será implementado na Aula 06.1.

---

# 38. Exemplo conceitual

Imagine que o aplicativo esteja em:

```text
Grandeza: Pressão

De:   bar
Para: kPa
```

O usuário altera:

```text
Pressão
   ↓
Volume
```

Não podemos continuar exibindo:

```text
bar
kPa
```

porque essas unidades pertencem à pressão.

A interface deverá atualizar automaticamente para algo como:

```text
Grandeza: Volume

De:   L
Para: m³
```

Isso é uma **interface dependente do estado da aplicação**.

---

# 39. Estado da aplicação

O EngConvert passa a possuir informações que determinam seu comportamento atual.

Por exemplo:

```text
grandeza atual = Volume

unidade de origem = L

unidade de destino = gal (US)

valor de entrada = 1
```

Esses dados representam o:

```text
ESTADO ATUAL
```

da aplicação.

Quando o estado muda, a interface e o resultado podem precisar mudar também.

---

# 40. Entrada e saída no EngConvert

A referência clássica apresenta:

```text
Input
Output
```

Na nossa versão utilizaremos:

```text
Entrada
Saída
```

A ideia será:

```text
Entrada
[ valor informado pelo usuário ]

Saída
[ valor convertido ]
```

Isso torna o fluxo visual da aplicação mais claro e organizado.

---

# 41. Converter com botão ou automaticamente?

Existem duas possibilidades.

## Opção A — botão

```text
digitar
   ↓
clicar Converter
   ↓
resultado
```

## Opção B — atualização automática

```text
digitar
   ↓
resultado atualizado
```

Nesta etapa manteremos o botão:

```text
Converter
```

porque ele torna o fluxo de eventos mais explícito para o aluno.

A atualização automática poderá ser estudada posteriormente.

---

# 42. O EngConvert começa a ter arquitetura

Nas primeiras aulas, o programa era pequeno.

Agora começamos a distinguir:

```text
DADOS
   ↓
grandezas
unidades
fatores


LÓGICA
   ↓
conversões
tratamento de temperatura


INTERFACE
   ↓
seletores
entrada
saída
botões
```

Visualmente:

```text
┌─────────────────────────────┐
│            DADOS            │
│ grandezas, unidades, fatores│
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│           LÓGICA            │
│      regras de conversão    │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│         INTERFACE           │
│   interação com o usuário   │
└─────────────────────────────┘
```

Ainda estamos em um único `main.py`, mas a necessidade de organização começa a aparecer naturalmente.

---

# 43. Por que ainda não modularizar?

Poderíamos separar imediatamente:

```text
dados.py
conversoes.py
interface.py
```

Mas, didaticamente, ainda é útil visualizar o programa completo.

Primeiro iremos perceber:

```text
main.py começa a crescer
        ↓
dados aumentam
        ↓
funções aumentam
        ↓
interface aumenta
        ↓
surge a necessidade de separar
```

Então a modularização terá uma justificativa concreta.

---

# 44. Estrutura conceitual dos dados

Para as grandezas multiplicativas, podemos pensar em:

```text
grandezas
   │
   ├── Pressão
   │      ├── Pa
   │      ├── kPa
   │      ├── MPa
   │      └── ...
   │
   ├── Comprimento
   │      ├── mm
   │      ├── cm
   │      ├── m
   │      └── ...
   │
   ├── Área
   │      ├── mm²
   │      ├── cm²
   │      ├── m²
   │      └── ...
   │
   └── Volume
          ├── mL
          ├── cm³
          ├── L
          ├── m³
          ├── gal (US)
          └── gal (UK)
```

A temperatura ficará associada a uma estratégia específica de conversão.

---

# 45. O que será reaproveitado?

Muitos conceitos das aulas anteriores continuam válidos:

```text
CTkFrame
CTkLabel
CTkEntry
CTkButton
CTkComboBox
pack()
command
.get()
.set()
.configure()
float()
try
except
ValueError
dicionários
listas
funções
f-strings
```

A evolução não elimina o que aprendemos.

Ela combina os conceitos em um problema maior.

---

# 46. O que será novo?

Na Sprint 05 teremos principalmente:

```text
múltiplas grandezas

dicionários aninhados

seletor de grandeza

atualização dinâmica das unidades

função chamada quando a grandeza muda

estratégias diferentes de conversão

temperatura

entrada e saída mais claras
na interface do EngConvert
```

---

# 47. Planejamento da Sprint 05

A próxima implementação será:

```text
SPRINT 05 — ENGCONVERT MULTICATEGORIAS
```

Planejamento inicial:

```text
[ ] criar os fatores de comprimento

[ ] criar os fatores de área

[ ] criar os fatores de volume

[ ] manter os fatores de pressão

[ ] organizar grandezas multiplicativas

[ ] criar as unidades de temperatura

[ ] criar a função de conversão de temperatura

[ ] criar o seletor de grandeza

[ ] atualizar as unidades quando a grandeza mudar

[ ] atualizar o conversor para múltiplas grandezas

[ ] manter a inversão de unidades

[ ] adaptar Entrada e Saída

[ ] testar Pressão

[ ] testar Comprimento

[ ] testar Área

[ ] testar Volume

[ ] testar gal (US)

[ ] testar gal (UK)

[ ] testar °C

[ ] testar °F

[ ] testar K

[ ] testar °R

[ ] testar entrada inválida
```

Status:

```text
PLANEJADA
```

---

# 48. Testes que deverão existir

Alguns testes previstos para a implementação:

## Pressão

```text
1 bar → kPa

resultado esperado:
100 kPa
```

## Comprimento

```text
1 m → mm

resultado esperado:
1000 mm
```

## Área

```text
1 m² → mm²

resultado esperado:
1 000 000 mm²
```

## Volume

```text
1 L → mL

resultado esperado:
1000 mL
```

## Galão US

```text
1 gal (US) → L

resultado esperado:
3,785411784 L
```

## Galão UK

```text
1 gal (UK) → L

resultado esperado:
4,54609 L
```

## Temperatura

```text
0 °C → °F

resultado esperado:
32 °F
```

e:

```text
0 °C → K

resultado esperado:
273,15 K
```

Também deveremos verificar Rankine:

```text
32 °F → °R

resultado esperado:
491,67 °R
```

e:

```text
0 K → °R

resultado esperado:
0 °R
```

---

# 49. Comparando as duas etapas

## Etapa 5

```text
PRESSÃO
   ↓
9 unidades
   ↓
um conjunto de fatores
   ↓
uma grandeza
```

## Etapa 6

```text
ENGCONVERT
   │
   ├── Pressão
   ├── Comprimento
   ├── Área
   ├── Volume
   └── Temperatura
          ↓
múltiplas estratégias
```

Essa mudança é maior do que simplesmente adicionar novas unidades.

Estamos modificando o **modelo do aplicativo**.

---

# 50. Um novo nível de abstração

Na Aula 05 pensávamos:

```text
qual unidade de pressão?
```

Agora precisamos pensar:

```text
qual grandeza?
      ↓
quais unidades pertencem a ela?
      ↓
qual regra de conversão ela utiliza?
```

Esse é um nível maior de abstração.

```text
UNIDADE
   ↓
pertence a uma
   ↓
GRANDEZA
   ↓
que utiliza uma
   ↓
ESTRATÉGIA DE CONVERSÃO
```

---

# 51. Fluxo conceitual da Etapa 6

```text
usuário abre o EngConvert
        ↓
seleciona uma grandeza
        ↓
programa identifica
as unidades disponíveis
        ↓
interface atualiza
origem e destino
        ↓
usuário escolhe as unidades
        ↓
informa o valor
        ↓
programa identifica
a estratégia de conversão
        ↓
┌──────────────────────┐
│ multiplicativa?      │
└──────────┬───────────┘
           │
      sim  │
           ↓
      usar fatores
           │
           └──────────────┐
                          ↓
                  apresentar saída

ou:

┌──────────────────────┐
│ temperatura?         │
└──────────┬───────────┘
           │
      sim  │
           ↓
conversão específica
           │
           ↓
   apresentar saída
```

---

# 52. Evolução visual prevista

A evolução da interface pode ser entendida assim:

```text
AULA 04

Entrada
  ↓
bar → kPa
  ↓
Resultado
```

Depois:

```text
AULA 05

Entrada
  ↓
De ↔ Para
  ↓
Resultado
```

Agora:

```text
AULA 06

Grandeza
   ↓
Origem ↔ Destino
   ↓
Entrada
   ↓
Converter
   ↓
Saída
```

Mais adiante, a interface poderá evoluir para listas de unidades permanentemente visíveis, tornando a seleção das unidades ainda mais direta para o usuário.

---

# 53. Por que esta etapa é importante?

Até aqui aprendemos a construir funcionalidades.

Agora começamos a aprender a **organizar crescimento**.

Essa diferença é importante:

```text
PROGRAMA PEQUENO

"como faço funcionar?"
```

e:

```text
PROGRAMA EM CRESCIMENTO

"como faço continuar organizado
enquanto adiciono funcionalidades?"
```

Esse é um dos pontos em que um exercício começa a se transformar em um projeto de software.

---

# 54. 📌 Resumo da Aula 06.0

Nesta aula definimos a evolução:

```text
CONVERSOR DE PRESSÃO
        ↓
ENGCONVERT MULTICATEGORIAS
```

As primeiras categorias serão:

```text
Pressão
Comprimento
Área
Volume
Temperatura
```

Aprendemos que:

```text
Pressão
Comprimento
Área
Volume
        ↓
podem utilizar fatores
multiplicativos
```

Enquanto:

```text
Temperatura
°C, °F, K e °R
        ↓
exige transformação
específica
```

Também introduzimos:

```text
dicionários aninhados

seletor de grandeza

unidades dependentes da grandeza

estado da aplicação

atualização dinâmica da interface
```

E acrescentamos ao Volume:

```text
gal (US)
gal (UK)
```

---

# 55. 🔜 Próxima aula

A próxima aula será:

```text
Aula 06.1 — Roteiro Prático
```

## Implementando a Sprint 05 — EngConvert Multicategorias

Nela iremos:

```text
criar os novos fatores
        ↓
organizar as grandezas
        ↓
implementar temperatura
        ↓
criar o seletor de grandeza
        ↓
atualizar as unidades dinamicamente
        ↓
adaptar converter()
        ↓
adaptar a interface
        ↓
testar todas as categorias
        ↓
concluir a Sprint 05
        ↓
concluir a Etapa 6
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
Aula 05
Conversor de Pressão
   ↓
Sprint 04 — CONCLUÍDA
   ↓
Etapa 5 — CONCLUÍDA
   ↓
Aula 06.0
Novas Grandezas
+
EngConvert Multicategorias
   ↓
Aula 06.1
Sprint 05
   ↓
Etapa 6 — Novas Grandezas
```

> 🎯 **Ideia final:** o objetivo da Etapa 6 não é apenas acrescentar mais unidades. É transformar o EngConvert em um aplicativo capaz de compreender diferentes grandezas, apresentar as unidades correspondentes e selecionar a estratégia matemática adequada para realizar cada conversão.

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
