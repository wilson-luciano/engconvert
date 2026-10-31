# Aula 04.0 — Primeiro Conversor

## Da interface interativa ao primeiro cálculo de engenharia

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Pré-requisito:** Aulas 03.0 e 03.1 concluídas e **Sprint 02 — Widgets e Interação** encerrada.

---

## 🎯 Objetivos

Ao final desta aula, o aluno deverá ser capaz de:

- transformar o conteúdo de um `CTkEntry` em um valor numérico;
- compreender a utilização de `float()`;
- implementar a primeira conversão de engenharia do EngConvert;
- converter pressão de **bar para kPa**;
- compreender por que uma entrada inválida pode interromper o programa;
- compreender o conceito de **exceção**;
- utilizar `try` e `except`;
- compreender `ValueError`;
- revisar o uso de funções;
- revisar `f-string`;
- formatar resultados numéricos;
- atualizar a interface utilizando `.configure()`;
- compreender o fluxo completo **entrada → validação → cálculo → resultado**.

---

# 1. Onde estamos no EngConvert?

Na Aula 03 construímos uma interface capaz de receber um valor e responder ao clique do usuário.

O fluxo atual é:

```text
USUÁRIO
   ↓
digita um valor
   ↓
CTkEntry
   ↓
.get()
   ↓
string
   ↓
CTkButton
   ↓
command
   ↓
converter()
   ↓
.configure()
   ↓
interface atualizada
```

Por exemplo, se o usuário digitar:

```text
25
```

a aplicação apresenta:

```text
Você digitou: 25
```

Isso demonstra que a interface já possui:

```text
ENTRADA
   ↓
EVENTO
   ↓
FUNÇÃO
   ↓
SAÍDA
```

Mas ainda falta uma parte fundamental:

> **realizar um cálculo de engenharia.**

---

# 2. A próxima etapa do Roadmap

Na Aula 03.1 concluímos:

```text
Etapa 3 — Widgets e eventos
```

A próxima etapa planejada é:

```text
Etapa 4 — Primeiro conversor
```

Agora o EngConvert começará a cumprir sua finalidade.

O fluxo evoluirá de:

```text
entrada
   ↓
mostrar o mesmo valor
```

para:

```text
entrada
   ↓
converter para número
   ↓
realizar cálculo
   ↓
formatar resultado
   ↓
mostrar resultado
```

---

# 3. Primeiro problema de engenharia

Começaremos com uma conversão simples de pressão:

```text
bar → kPa
```

Sabemos que:

```text
1 bar = 100 kPa
```

Portanto:

```text
pressão [kPa] = pressão [bar] × 100
```

Podemos representar matematicamente:

\[
p*{kPa} = p*{bar} \times 100
\]

Exemplo:

```text
2 bar
   ↓
2 × 100
   ↓
200 kPa
```

Outro exemplo:

```text
2,5 bar
   ↓
2,5 × 100
   ↓
250 kPa
```

> 📌 No código Python, números decimais são normalmente escritos utilizando **ponto** como separador decimal: `2.5`.

---

# 4. O problema: `.get()` fornece texto

Na aula anterior utilizamos:

```python
valor = entrada.get()
```

O método:

```python
.get()
```

obtém o conteúdo do `CTkEntry`.

Porém, esse conteúdo chega inicialmente ao Python como:

```text
string
```

Se o usuário digitar:

```text
2.5
```

podemos representar o conteúdo obtido como:

```python
"2.5"
```

Observe a diferença:

```python
"2.5"
```

é texto.

Enquanto:

```python
2.5
```

é um número.

Para realizar:

```text
pressão × 100
```

precisamos transformar a entrada em um valor numérico.

---

# 5. Convertendo a entrada com `float()`

Para isso utilizaremos:

```python
float()
```

Exemplo:

```python
pressao_bar = float(entrada.get())
```

Podemos decompor essa instrução:

```text
entrada
   ↓
.get()
   ↓
"2.5"
   ↓
float(...)
   ↓
2.5
   ↓
pressao_bar
```

Assim:

```python
entrada.get()
```

obtém uma `string`.

E:

```python
float(entrada.get())
```

converte essa representação textual para um número de ponto flutuante.

---

# 6. O que é `float`?

Em Python, `float` é um tipo numérico utilizado para representar números com parte decimal.

Exemplos:

```python
1.0
2.5
10.75
100.25
```

Podemos comparar:

```text
"25"    → string
25      → int
25.0    → float
```

No EngConvert, utilizaremos `float()` porque grandezas de engenharia frequentemente possuem valores decimais.

Por exemplo:

```text
1.25 bar
2.75 bar
6.4 bar
```

---

# 7. Realizando a conversão

Depois de obter a pressão em bar:

```python
pressao_bar = float(entrada.get())
```

podemos calcular:

```python
pressao_kpa = pressao_bar * 100
```

O fluxo agora é:

```text
CTkEntry
   ↓
entrada.get()
   ↓
string
   ↓
float()
   ↓
pressao_bar
   ↓
× 100
   ↓
pressao_kpa
```

Exemplo:

```text
entrada.get()
      ↓
    "3.5"
      ↓
    float()
      ↓
     3.5
      ↓
    × 100
      ↓
   350.0
```

---

# 8. Atualizando o resultado

Na Aula 03 aprendemos:

```python
resultado.configure(...)
```

Agora podemos utilizá-lo para apresentar o resultado da conversão:

```python
resultado.configure(
    text=f"{pressao_kpa:.2f} kPa"
)
```

Assim, a função começa a assumir a forma:

```python
# Define a função responsável pela conversão.
def converter():

    # Obtém o valor digitado e converte a string para float.
    pressao_bar = float(entrada.get())

    # Converte a pressão de bar para kPa.
    pressao_kpa = pressao_bar * 100

    # Apresenta o resultado na interface.
    resultado.configure(
        text=f"{pressao_kpa:.2f} kPa"
    )
```

---

# 9. Relembrando a `f-string`

Observe:

```python
f"{pressao_kpa:.2f} kPa"
```

O prefixo:

```python
f
```

indica uma **f-string**.

Ela permite inserir valores dentro de uma string:

```python
f"{pressao_kpa}"
```

No nosso exemplo:

```python
:.2f
```

define a formatação numérica.

Podemos interpretar:

```text
:
↓
início da especificação de formato

.2
↓
duas casas decimais

f
↓
formato de ponto flutuante
```

Exemplo:

```text
pressao_kpa = 250
```

com:

```python
f"{pressao_kpa:.2f} kPa"
```

resulta em:

```text
250.00 kPa
```

---

# 10. Primeiro fluxo completo de cálculo

Agora temos:

```text
USUÁRIO
   ↓
digita 2.5
   ↓
CTkEntry
   ↓
.get()
   ↓
"2.5"
   ↓
float()
   ↓
2.5
   ↓
× 100
   ↓
250.0
   ↓
f-string
   ↓
"250.00 kPa"
   ↓
.configure()
   ↓
GUI
```

Esse é o primeiro fluxo completo de cálculo de engenharia do EngConvert.

---

# 11. Mas existe um problema

Considere que o usuário digite:

```text
dez
```

A função tentará executar:

```python
float("dez")
```

Mas `"dez"` não representa um número válido para `float()`.

O Python encontrará um problema durante a execução.

Esse tipo de situação é chamado de:

```text
exceção
```

---

# 12. O que é uma exceção?

Uma **exceção** é um evento que ocorre durante a execução do programa e interrompe o fluxo normal das instruções quando não é tratado.

No nosso caso:

```text
usuário digita "dez"
        ↓
entrada.get()
        ↓
"dez"
        ↓
float("dez")
        ↓
não é possível converter
        ↓
ValueError
```

Sem tratamento, a operação falha e o Python apresenta uma mensagem de erro no terminal.

Uma interface destinada ao usuário não deve depender de ele sempre fornecer exatamente a entrada esperada.

Precisamos tratar essa situação.

---

# 13. `ValueError`

Quando fazemos:

```python
float("dez")
```

o Python gera:

```text
ValueError
```

O nome pode ser interpretado como:

```text
Value
   ↓
valor

Error
   ↓
erro
```

Nesse contexto, o tipo de valor fornecido não pode ser interpretado pela operação de conversão solicitada.

Outro exemplo:

```python
float("")
```

também gera `ValueError`, pois uma string vazia não pode ser convertida diretamente em um número de ponto flutuante.

---

# 14. Introdução ao `try`

Em Python, **`try` significa literalmente “tentar”**.

Ele é utilizado quando queremos executar um trecho de código que pode gerar uma exceção.

Estrutura:

```python
try:
    # Código que será tentado.
    ...
```

No EngConvert:

```python
try:
    pressao_bar = float(entrada.get())
```

Podemos interpretar:

```text
TENTE
   ↓
obter a entrada
   ↓
converter para float
```

---

# 15. Introdução ao `except`

O `except` define o que deverá acontecer caso determinada exceção ocorra.

Exemplo:

```python
try:
    pressao_bar = float(entrada.get())

except ValueError:
    resultado.configure(
        text="Digite um valor numérico válido."
    )
```

Fluxo:

```text
try
 ↓
tenta converter
 ↓
deu certo?
 │
 ├── SIM → continua
 │
 └── NÃO
       ↓
   ValueError
       ↓
     except
       ↓
mensagem ao usuário
```

---

# 16. Tratando a entrada inválida

Podemos agora proteger toda a operação:

```python
# Define a função responsável pela conversão.
def converter():

    # Tenta executar a conversão.
    try:

        # Obtém o valor digitado e converte para float.
        pressao_bar = float(entrada.get())

        # Converte bar para kPa.
        pressao_kpa = pressao_bar * 100

        # Apresenta o resultado.
        resultado.configure(
            text=f"{pressao_kpa:.2f} kPa"
        )

    # Executa este bloco se ocorrer ValueError.
    except ValueError:

        # Informa ao usuário que a entrada é inválida.
        resultado.configure(
            text="Digite um valor numérico válido."
        )
```

Agora a interface consegue responder tanto a uma entrada válida quanto a uma entrada inadequada.

---

# 17. Dois caminhos possíveis

A função possui agora dois fluxos principais.

## Entrada válida

```text
"2.5"
  ↓
float()
  ↓
2.5
  ↓
× 100
  ↓
250.0
  ↓
250.00 kPa
```

## Entrada inválida

```text
"dez"
  ↓
float()
  ↓
ValueError
  ↓
except
  ↓
Digite um valor numérico válido.
```

Isso torna a aplicação mais robusta.

---

# 18. Função × interface

Observe que estamos começando a distinguir duas responsabilidades:

```text
INTERFACE
   ↓
receber entrada
mostrar resultado

FUNÇÃO
   ↓
obter dado
converter
calcular
tratar erro
```

Nesta fase didática, tudo ainda permanece em `main.py`.

Isso é proposital.

A modularização será introduzida quando a complexidade do EngConvert tornar evidente a necessidade de separar responsabilidades em arquivos e módulos.

---

# 19. Evoluindo os textos da interface

Até agora o campo possuía:

```text
Digite um valor
```

Agora sabemos qual grandeza estamos utilizando.

Podemos tornar a interface mais específica.

No campo de entrada:

```python
entrada = ctk.CTkEntry(
    container,
    placeholder_text="Pressão em bar"
)
```

Também podemos acrescentar um subtítulo:

```python
subtitulo = ctk.CTkLabel(
    container,
    text="Pressão: bar → kPa"
)
```

A interface começa a comunicar claramente sua finalidade.

---

# 20. Estrutura visual esperada

A interface poderá assumir aproximadamente:

```text
┌────────────────────────────────┐
│                                │
│           EngConvert           │
│                                │
│      Pressão: bar → kPa        │
│                                │
│     [ Pressão em bar      ]    │
│                                │
│          [ Converter ]         │
│                                │
│           250.00 kPa           │
│                                │
└────────────────────────────────┘
```

Agora já podemos chamar o EngConvert de um **conversor funcional**, ainda que extremamente simples.

---

# 21. Código completo para estudo

> 📌 O código abaixo reúne os conceitos estudados nesta aula. A implementação passo a passo será organizada na Aula 04.1.

```python
# Importa a biblioteca CustomTkinter.
import customtkinter as ctk


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


# Define o modo de aparência da aplicação.
ctk.set_appearance_mode("system")

# Define o tema inicial.
ctk.set_default_color_theme("blue")


# Cria a janela principal.
app = ctk.CTk()

# Define o título da janela.
app.title("EngConvert")

# Define as dimensões iniciais.
app.geometry("600x430")


# Cria um frame para organizar os componentes.
container = ctk.CTkFrame(app)

# Posiciona o frame dentro da janela.
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


# Cria um subtítulo indicando a conversão atual.
subtitulo = ctk.CTkLabel(
    container,
    text="Pressão: bar → kPa"
)

# Posiciona o subtítulo.
subtitulo.pack(pady=(0, 25))


# Cria o campo de entrada.
entrada = ctk.CTkEntry(
    container,
    width=260,
    placeholder_text="Pressão em bar"
)

# Posiciona o campo.
entrada.pack(pady=10)


# Cria o botão e associa o clique à função converter.
botao = ctk.CTkButton(
    container,
    text="Converter",
    command=converter
)

# Posiciona o botão.
botao.pack(pady=15)


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

# 22. O que mudou em relação à Aula 03?

Na Aula 03:

```python
valor = entrada.get()

resultado.configure(
    text=f"Você digitou: {valor}"
)
```

Agora:

```python
pressao_bar = float(entrada.get())

pressao_kpa = pressao_bar * 100

resultado.configure(
    text=f"{pressao_kpa:.2f} kPa"
)
```

A diferença conceitual é importante:

```text
AULA 03

ENTRADA
   ↓
mostrar o conteúdo


AULA 04

ENTRADA
   ↓
interpretar o dado
   ↓
processar
   ↓
calcular
   ↓
mostrar o resultado
```

---

# 23. Testes que precisaremos realizar

Uma aplicação não deve ser verificada apenas com um único valor.

Precisaremos testar diferentes situações.

## Teste 1 — valor inteiro

```text
Entrada:
1

Resultado esperado:
100.00 kPa
```

## Teste 2 — valor decimal

```text
Entrada:
2.5

Resultado esperado:
250.00 kPa
```

## Teste 3 — outro valor decimal

```text
Entrada:
0.75

Resultado esperado:
75.00 kPa
```

## Teste 4 — texto

```text
Entrada:
dez

Resultado esperado:
Digite um valor numérico válido.
```

## Teste 5 — campo vazio

```text
Entrada:
[vazio]

Resultado esperado:
Digite um valor numérico válido.
```

Esses testes serão executados no roteiro prático.

---

# 24. E valores negativos?

Considere:

```text
-1 bar
```

Matematicamente, nosso código produzirá:

```text
-100.00 kPa
```

Devemos simplesmente impedir valores negativos?

A resposta depende do significado físico da grandeza.

Uma pressão negativa pode ter interpretações diferentes dependendo da referência adotada, por exemplo, quando distinguimos pressão **absoluta** e pressão **manométrica**.

Portanto:

> **uma validação de engenharia não deve considerar apenas a programação; deve considerar também o significado físico da variável.**

Neste momento não bloquearemos automaticamente valores negativos.

Esse exemplo será útil mais adiante quando aprofundarmos as regras de validação.

---

# 25. Preparando a próxima Sprint

Concluímos a Sprint 02 na Aula 03.1.

Agora a próxima etapa do Roadmap é:

```text
Etapa 4 — Primeiro conversor
```

Podemos planejar a próxima Sprint:

```text
SPRINT 03 — PRIMEIRO CONVERSOR

[ ] converter a entrada para float
[ ] implementar bar → kPa
[ ] formatar o resultado
[ ] tratar ValueError
[ ] atualizar os textos da interface
[ ] testar entradas válidas
[ ] testar entradas inválidas

STATUS: PLANEJADA
```

Observe a continuidade:

```text
Sprint 02
Widgets e Interação
      ↓
CONCLUÍDA
      ↓
Sprint 03
Primeiro Conversor
      ↓
PLANEJADA
```

Na Aula 04.1 implementaremos e encerraremos essa Sprint.

---

# 26. 🧪 Desafio de compreensão

Considere:

```python
pressao_bar = float(entrada.get())
pressao_kpa = pressao_bar * 100
```

Responda:

1. O que `entrada.get()` retorna inicialmente?
2. Por que utilizamos `float()`?
3. O que será armazenado em `pressao_bar`?
4. O que representa o número `100`?
5. O que será armazenado em `pressao_kpa`?

Agora considere:

```python
try:
    pressao_bar = float(entrada.get())

except ValueError:
    resultado.configure(
        text="Digite um valor numérico válido."
    )
```

Responda:

1. Qual instrução pode gerar `ValueError`?
2. O que acontece se a entrada for `"2.5"`?
3. O que acontece se a entrada for `"dez"`?
4. Qual é a função do `except`?

---

# 26. 🧠 Fluxo completo do primeiro conversor

```text
USUÁRIO
   ↓
digita a pressão
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
valor válido?
   │
   ├── SIM
   │    ↓
   │  × 100
   │    ↓
   │  kPa
   │    ↓
   │  f-string
   │    ↓
   │  .configure()
   │    ↓
   │  RESULTADO
   │
   └── NÃO
        ↓
    ValueError
        ↓
      except
        ↓
 mensagem ao usuário
```

---

# 26. 📌 Resumo da Aula 04.0

Nesta aula revisamos:

```text
.get()
   ↓
obtém o conteúdo

função
   ↓
organiza o comportamento

f-string
   ↓
formata a saída

.configure()
   ↓
atualiza a interface
```

Introduzimos:

```text
float()
   ↓
converte texto em número

bar → kPa
   ↓
primeiro cálculo de engenharia

try
   ↓
tenta executar

ValueError
   ↓
exceção de valor

except
   ↓
trata a exceção
```

E evoluímos conceitualmente de:

```text
GUI INTERATIVA
```

para:

```text
GUI
 ↓
ENTRADA
 ↓
CONVERSÃO DE TIPO
 ↓
CÁLCULO
 ↓
TRATAMENTO DE ERRO
 ↓
RESULTADO
```

---

# 26. 🔜 Próxima etapa — Aula 04.1

Na Aula 04.1 implementaremos a:

```text
Sprint 03 — Primeiro Conversor
```

O roteiro prático seguirá:

```text
abrir o projeto
      ↓
registrar Sprint 03
      ↓
abrir main.py
      ↓
alterar converter()
      ↓
usar float()
      ↓
implementar bar → kPa
      ↓
formatar resultado
      ↓
adicionar try/except
      ↓
tratar ValueError
      ↓
atualizar interface
      ↓
executar testes
      ↓
atualizar Sprint 03
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
Aula 04.0
Primeiro conversor
   ↓
Aula 04.1
Implementação da Sprint 03
   ↓
próxima evolução
Conversor de pressão
```

> 🎯 **Ideia final:** o EngConvert deixa de apenas responder a eventos da interface e passa a interpretar dados, realizar um cálculo de engenharia, tratar entradas inadequadas e apresentar um resultado ao usuário.

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
