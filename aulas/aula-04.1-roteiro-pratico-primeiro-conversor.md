# Aula 04.1 — Roteiro Prático

## Implementando a Sprint 03 — Primeiro Conversor

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Correspondência:** roteiro prático da **Aula 04.0 — Primeiro Conversor**.

---

## 🎯 Objetivo

Na Aula 04.0 estudamos como transformar a interface interativa do EngConvert em um conversor capaz de realizar seu primeiro cálculo de engenharia.

Agora iremos implementar, passo a passo, a:

```text
SPRINT 03 — PRIMEIRO CONVERSOR
```

Ao final desta aula, o EngConvert deverá ser capaz de:

```text
receber pressão em bar
        ↓
ler a entrada
        ↓
converter string para float
        ↓
calcular bar → kPa
        ↓
formatar o resultado
        ↓
tratar entrada inválida
        ↓
apresentar o resultado na GUI
```

---

# 🧭 Visão geral do roteiro

```text
abrir o projeto
      ↓
registrar a Sprint 03
      ↓
abrir main.py
      ↓
alterar converter()
      ↓
usar float()
      ↓
implementar bar → kPa
      ↓
formatar com f-string
      ↓
adicionar try/except
      ↓
tratar ValueError
      ↓
atualizar os textos da GUI
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

Neste momento, as três primeiras etapas já foram concluídas:

```markdown
- [x] **Etapa 1 — Ambiente e estrutura**
- [x] **Etapa 2 — Primeira interface gráfica**
- [x] **Etapa 3 — Widgets e eventos**
- [ ] **Etapa 4 — Primeiro conversor**
- [ ] **Etapa 5 — Conversor de pressão**
- [ ] **Etapa 6 — Novas grandezas**
- [ ] **Etapa 7 — Modularização**
- [ ] **Etapa 8 — Testes**
- [ ] **Etapa 9 — Interface completa**
- [ ] **Etapa 10 — Distribuição**
```

Nosso objetivo agora é concluir:

```text
Etapa 4 — Primeiro conversor
```

---

# 3. Criar o arquivo da Sprint 03

Na pasta:

```text
docs/sprints/
```

crie:

```text
sprint-03-primeiro-conversor.md
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
    └── sprint-03-primeiro-conversor.md
```

---

# 4. Registrar o planejamento da Sprint 03

Abra:

```text
docs/sprints/sprint-03-primeiro-conversor.md
```

e utilize:

```markdown
# Sprint 03 — Primeiro Conversor

## Objetivo

Transformar a interface interativa do EngConvert em um primeiro conversor funcional de engenharia, realizando a conversão de pressão de bar para kPa.

## Tarefas

- [ ] converter a entrada para `float`;
- [ ] implementar a conversão `bar → kPa`;
- [ ] formatar o resultado;
- [ ] tratar `ValueError`;
- [ ] atualizar os textos da interface;
- [ ] testar entradas válidas;
- [ ] testar entradas inválidas.

## Critério de conclusão

O usuário deverá ser capaz de informar uma pressão em bar e obter o valor correspondente em kPa.

Entradas que não possam ser convertidas para número deverão gerar uma mensagem de orientação na própria interface.

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

Ao final da Aula 03.1, a função principal de interação estava semelhante a:

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

Até aqui, o programa apenas repete a entrada.

Agora iremos transformá-la em um cálculo real.

---

# 6. Converter a entrada para `float`

Substitua:

```python
valor = entrada.get()
```

por:

```python
# Obtém o conteúdo digitado e converte a string para float.
pressao_bar = float(entrada.get())
```

Agora o fluxo é:

```text
CTkEntry
   ↓
.get()
   ↓
string
   ↓
float()
   ↓
pressao_bar
```

Se o usuário digitar:

```text
2.5
```

teremos conceitualmente:

```text
"2.5"
   ↓
float()
   ↓
2.5
```

---

# 7. Implementar `bar → kPa`

Logo depois de:

```python
pressao_bar = float(entrada.get())
```

adicione:

```python
# Converte a pressão de bar para kPa.
pressao_kpa = pressao_bar * 100
```

Estamos aplicando:

```text
1 bar = 100 kPa
```

Portanto:

```text
pressão [kPa] = pressão [bar] × 100
```

Exemplo:

```text
2.5 bar
   ↓
2.5 × 100
   ↓
250 kPa
```

---

# 8. Apresentar o resultado

Substitua:

```python
resultado.configure(
    text=f"Você digitou: {valor}"
)
```

por:

```python
# Atualiza o texto do resultado com duas casas decimais.
resultado.configure(
    text=f"{pressao_kpa:.2f} kPa"
)
```

Agora:

```text
pressao_kpa
      ↓
   250.0
      ↓
   :.2f
      ↓
  250.00
      ↓
   "kPa"
      ↓
250.00 kPa
```

---

# 9. Conferir a primeira versão da função

Neste momento, a função deverá estar assim:

```python
# Define a função responsável pela conversão.
def converter():

    # Obtém o conteúdo digitado e converte a string para float.
    pressao_bar = float(entrada.get())

    # Converte a pressão de bar para kPa.
    pressao_kpa = pressao_bar * 100

    # Atualiza o texto do resultado com duas casas decimais.
    resultado.configure(
        text=f"{pressao_kpa:.2f} kPa"
    )
```

Essa versão já consegue realizar a conversão.

Mas ainda existe um problema:

```text
entrada não numérica
        ↓
float()
        ↓
ValueError
```

Precisamos tratar essa situação.

---

# 10. Adicionar `try`

Dentro da função `converter()`, coloque as instruções de conversão dentro de:

```python
try:
```

A função começará a ficar assim:

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
```

O bloco significa:

```text
TENTE
   ↓
ler
   ↓
converter
   ↓
calcular
   ↓
mostrar
```

---

# 11. Adicionar `except ValueError`

Depois do bloco `try`, adicione:

```python
# Executa este bloco se a entrada não puder ser convertida para float.
except ValueError:

    # Apresenta uma mensagem de orientação ao usuário.
    resultado.configure(
        text="Digite um valor numérico válido."
    )
```

A função completa passa a ser:

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

Agora existem dois caminhos:

```text
ENTRADA
   ↓
float()
   ↓
   ├── válida
   │     ↓
   │   cálculo
   │     ↓
   │   resultado
   │
   └── inválida
         ↓
     ValueError
         ↓
       except
         ↓
      mensagem
```

---

# 12. Atualizar o campo de entrada

Localize:

```python
entrada = ctk.CTkEntry(
    container,
    placeholder_text="Digite um valor"
)
```

Substitua por:

```python
# Cria o campo para entrada da pressão em bar.
entrada = ctk.CTkEntry(
    container,
    width=260,
    placeholder_text="Pressão em bar"
)
```

Agora a própria interface informa qual dado deve ser fornecido.

---

# 13. Atualizar o título

Localize o `CTkLabel` utilizado como título e deixe-o assim:

```python
# Cria o título principal.
titulo = ctk.CTkLabel(
    container,
    text="EngConvert",
    font=("Arial", 28, "bold")
)
```

Depois:

```python
# Posiciona o título.
titulo.pack(pady=(30, 5))
```

---

# 14. Adicionar o subtítulo

Logo depois do título, adicione:

```python
# Cria um subtítulo indicando a conversão atual.
subtitulo = ctk.CTkLabel(
    container,
    text="Pressão: bar → kPa"
)

# Posiciona o subtítulo.
subtitulo.pack(pady=(0, 25))
```

A hierarquia passa a ser:

```text
app
│
└── container
    │
    ├── titulo
    ├── subtitulo
    ├── entrada
    ├── botao
    └── resultado
```

---

# 15. Ajustar o resultado

Localize:

```python
resultado = ctk.CTkLabel(
    container,
    text="Resultado"
)
```

e utilize:

```python
# Cria o campo de resultado.
resultado = ctk.CTkLabel(
    container,
    text="Resultado",
    font=("Arial", 20, "bold")
)
```

Depois:

```python
# Posiciona o resultado.
resultado.pack(pady=20)
```

---

# 16. Ajustar o botão

O botão poderá permanecer com:

```python
# Cria o botão e associa o clique à função converter.
botao = ctk.CTkButton(
    container,
    text="Converter",
    command=converter
)
```

E:

```python
# Posiciona o botão.
botao.pack(pady=15)
```

A instrução fundamental continua sendo:

```python
command=converter
```

---

# 17. Ajustar o tamanho da janela

Utilize:

```python
# Define as dimensões iniciais.
app.geometry("600x430")
```

---

# 18. Conferir o `main.py` completo

Neste ponto, o arquivo deverá estar assim:

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


# Cria o campo para entrada da pressão em bar.
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

Salve o arquivo.

---

# 19. Executar o EngConvert

No terminal:

```powershell
python main.py
```

A interface deverá apresentar aproximadamente:

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
│            Resultado           │
│                                │
└────────────────────────────────┘
```

---

# 20. Teste 1 — valor inteiro

Digite:

```text
1
```

Clique em:

```text
Converter
```

Resultado esperado:

```text
100.00 kPa
```

Verificação:

```text
1 bar × 100 = 100 kPa
```

---

# 21. Teste 2 — valor decimal

Digite:

```text
2.5
```

Resultado esperado:

```text
250.00 kPa
```

Verificação:

```text
2.5 bar × 100 = 250 kPa
```

> 📌 Neste estágio, utilize **ponto** como separador decimal na entrada.

---

# 22. Teste 3 — valor menor que 1

Digite:

```text
0.75
```

Resultado esperado:

```text
75.00 kPa
```

---

# 23. Teste 4 — entrada não numérica

Digite:

```text
dez
```

Clique em:

```text
Converter
```

Resultado esperado:

```text
Digite um valor numérico válido.
```

O fluxo foi:

```text
"dez"
   ↓
float("dez")
   ↓
ValueError
   ↓
except
   ↓
mensagem na GUI
```

---

# 24. Teste 5 — campo vazio

Apague todo o conteúdo do campo e clique em:

```text
Converter
```

Resultado esperado:

```text
Digite um valor numérico válido.
```

Nesse caso:

```python
float("")
```

também gera `ValueError`.

---

# 25. Teste 6 — valor negativo

Digite:

```text
-1
```

O programa apresentará:

```text
-100.00 kPa
```

Nesta etapa, **não bloquearemos automaticamente valores negativos**.

A validação física depende do significado da pressão e da referência utilizada.

O objetivo deste teste é perceber que:

```text
validação de programação
        ≠
validação física
```

---

# 26. Conferir os testes

Podemos resumir:

```text
ENTRADA      RESULTADO

1            100.00 kPa

2.5          250.00 kPa

0.75         75.00 kPa

dez          mensagem de entrada inválida

[vazio]      mensagem de entrada inválida

-1           -100.00 kPa
```

---

# 27. Atualizar a Sprint 03

Volte para:

```text
docs/sprints/sprint-03-primeiro-conversor.md
```

Agora atualize o documento para:

```markdown
# Sprint 03 — Primeiro Conversor

## Objetivo

Transformar a interface interativa do EngConvert em um primeiro conversor funcional de engenharia, realizando a conversão de pressão de bar para kPa.

## Tarefas

- [x] converter a entrada para `float`;
- [x] implementar a conversão `bar → kPa`;
- [x] formatar o resultado;
- [x] tratar `ValueError`;
- [x] atualizar os textos da interface;
- [x] testar entradas válidas;
- [x] testar entradas inválidas.

## Critério de conclusão

O usuário deverá ser capaz de informar uma pressão em bar e obter o valor correspondente em kPa.

Entradas que não possam ser convertidas para número deverão gerar uma mensagem de orientação na própria interface.

## Resultado

O EngConvert realiza sua primeira conversão de engenharia, transformando valores de pressão em bar para kPa.

A aplicação também trata entradas que não possam ser convertidas para número e apresenta uma mensagem de orientação ao usuário.

## Status

**CONCLUÍDA**
```

Salve o arquivo.

---

# 28. Comparar o planejamento com o resultado

Antes:

```text
SPRINT 03

[ ] float
[ ] bar → kPa
[ ] formatação
[ ] ValueError
[ ] textos da interface
[ ] entradas válidas
[ ] entradas inválidas

STATUS: PLANEJADA
```

Depois:

```text
SPRINT 03

[x] float
[x] bar → kPa
[x] formatação
[x] ValueError
[x] textos da interface
[x] entradas válidas
[x] entradas inválidas

STATUS: CONCLUÍDA
```

Novamente percorremos:

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

# 29. Atualizar o Roadmap

Abra:

```text
docs/roadmap.md
```

Altere:

```markdown
- [ ] **Etapa 4 — Primeiro conversor**
```

para:

```markdown
- [x] **Etapa 4 — Primeiro conversor**
```

O início do Roadmap deverá ficar:

```markdown
- [x] **Etapa 1 — Ambiente e estrutura**
- [x] **Etapa 2 — Primeira interface gráfica**
- [x] **Etapa 3 — Widgets e eventos**
- [x] **Etapa 4 — Primeiro conversor**
- [ ] **Etapa 5 — Conversor de pressão**
```

Salve o arquivo.

---

# 30. Conferir o Roadmap

No Preview:

```text
☑ Etapa 1 — Ambiente e estrutura
☑ Etapa 2 — Primeira interface gráfica
☑ Etapa 3 — Widgets e eventos
☑ Etapa 4 — Primeiro conversor
☐ Etapa 5 — Conversor de pressão
```

Nosso próximo objetivo passa a ser:

```text
Etapa 5 — Conversor de pressão
```

---

# 31. Checklist da Aula 04.1

Confira:

```text
[ ] abri o EngConvert no VSCode

[ ] conferi o Roadmap

[ ] criei sprint-03-primeiro-conversor.md

[ ] registrei a Sprint 03 como PLANEJADA

[ ] abri main.py

[ ] utilizei float()

[ ] implementei bar → kPa

[ ] formatei o resultado com .2f

[ ] adicionei try

[ ] adicionei except ValueError

[ ] atualizei o placeholder da entrada

[ ] adicionei o subtítulo da conversão

[ ] executei python main.py

[ ] testei 1 bar

[ ] testei 2.5 bar

[ ] testei 0.75 bar

[ ] testei uma entrada não numérica

[ ] testei o campo vazio

[ ] observei o comportamento com valor negativo

[ ] atualizei a Sprint 03

[ ] alterei o status para CONCLUÍDA

[ ] atualizei a Etapa 4 no Roadmap
```

---

# 32. Resultado da Aula 04

Antes, o EngConvert apenas repetia o conteúdo:

```text
Entrada: 25
     ↓
Você digitou: 25
```

Agora:

```text
Entrada: 2.5 bar
       ↓
     float()
       ↓
      2.5
       ↓
     × 100
       ↓
   250.0 kPa
       ↓
formatação .2f
       ↓
  250.00 kPa
```

Além disso:

```text
entrada inválida
       ↓
ValueError
       ↓
except
       ↓
mensagem na GUI
```

O EngConvert agora possui seu **primeiro conversor funcional de engenharia**.

---

# 33. 🔜 Preparação para a próxima etapa

O Roadmap indica:

```text
Etapa 5 — Conversor de pressão
```

Atualmente temos apenas:

```text
bar
 ↓
kPa
```

Na próxima evolução, o EngConvert poderá trabalhar com várias unidades de pressão.

Conceitualmente:

```text
valor
  ↓
unidade de origem
  ↓
conversão
  ↓
unidade de destino
  ↓
resultado
```

Isso abrirá espaço para novos componentes e estruturas de dados.

---

# 📌 Resumo do roteiro

```text
Sprint 03 planejada
        ↓
float()
        ↓
bar → kPa
        ↓
f-string + .2f
        ↓
try
        ↓
ValueError
        ↓
except
        ↓
GUI atualizada
        ↓
testes válidos
        ↓
testes inválidos
        ↓
Sprint 03 concluída
        ↓
Roadmap atualizado
        ↓
próxima etapa:
CONVERSOR DE PRESSÃO
```

> 🎯 **Ideia-chave:** nesta aula o EngConvert deixou de apenas responder à interface e passou a interpretar uma entrada, realizar um cálculo real de engenharia, tratar uma entrada inadequada e apresentar o resultado ao usuário.

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
