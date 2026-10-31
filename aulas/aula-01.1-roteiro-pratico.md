# Aula 01.1 — Roteiro Prático

## Da configuração do VSCode à primeira GUI do EngConvert

> **Projeto-guia:** EngConvert — Engineering Unit Converter

---

## 🎯 Objetivo

Este roteiro reúne **somente as novas ações práticas da Aula 01**.

A preparação inicial do projeto, a criação da `.venv`, a instalação do CustomTkinter, a criação dos arquivos e diretórios e o registro inicial das dependências **já foram realizados na Aula 00** e, portanto, **não serão repetidos aqui**.

A **Aula 01** permanece como material completo de estudo e consulta. A **Aula 01.1** funciona como um roteiro direto para acompanhar a implementação prática.

> 🧑‍💻 **Padrão didático adotado:** a partir desta aula, sempre que introduzirmos um trecho novo de programação, procuraremos apresentar comentários com `#` explicando as instruções, os objetos e os parâmetros mais importantes. À medida que os conceitos se tornarem familiares, alguns comentários poderão ser reduzidos para manter o código legível.

---

## 🧭 Fluxo desta atividade

```text
abrir o EngConvert no VSCode
            ↓
confirmar o interpretador Python
            ↓
abrir main.py
            ↓
substituir o teste inicial pela primeira GUI
            ↓
executar o programa
            ↓
verificar a janela
            ↓
testar geometry()
            ↓
testar dark / light / system
            ↓
restaurar a configuração adotada
            ↓
Aula 01 concluída
```

---

# 1. Abrir o projeto no VSCode

Se o projeto ainda não estiver aberto:

```powershell
cd C:\Projetos\engconvert
code .
```

Confirme que a pasta aberta no VSCode é:

```text
C:\Projetos\engconvert
```

---

# 2. Confirmar o interpretador Python no VSCode

Pressione:

```text
Ctrl + Shift + P
```

Digite:

```text
Python: Select Interpreter
```

Selecione:

```text
C:\Projetos\engconvert\.venv\Scripts\python.exe
```

> 💡 A `.venv` já foi criada na Aula 00. Aqui estamos apenas confirmando que o VSCode está utilizando o interpretador correto.

Se desejar verificar também pelo terminal:

```powershell
python -c "import sys; print(sys.executable)"
```

O caminho deverá apontar para:

```text
C:\Projetos\engconvert\.venv\Scripts\python.exe
```

---

# 3. Abrir o `main.py`

No **Explorer** do VSCode, abra:

```text
main.py
```

Na Aula 00 utilizamos um programa simples para verificar se o projeto estava funcionando.

Agora vamos substituir esse teste pela **primeira interface gráfica do EngConvert**.

---

# 4. Criar a primeira GUI do EngConvert

Substitua o conteúdo de `main.py` por:

```python
# Importa a biblioteca CustomTkinter.
# "as ctk" cria o apelido ctk para facilitar seu uso no código.
import customtkinter as ctk


# Define o modo de aparência da aplicação.
# "system" acompanha o modo claro/escuro configurado no sistema operacional.
ctk.set_appearance_mode("system")

# Define o tema de cores padrão utilizado pelos widgets do CustomTkinter.
# Neste projeto começaremos utilizando o tema "blue".
ctk.set_default_color_theme("blue")


# Cria a janela principal da aplicação.
# CTk() é a janela principal fornecida pelo CustomTkinter.
# O objeto criado é armazenado na variável "app".
app = ctk.CTk()

# Define o texto apresentado na barra de título da janela.
app.title("EngConvert")

# Define o tamanho inicial da janela.
# 700 pixels de largura × 450 pixels de altura.
app.geometry("700x450")


# Inicia o loop principal de eventos da interface gráfica.
# A partir daqui, a aplicação permanece ativa aguardando eventos,
# como movimentar/redimensionar a janela ou solicitar seu fechamento.
app.mainloop()
```

Salve com:

```text
Ctrl + S
```

---

# 5. Executar o EngConvert

No terminal integrado:

```powershell
python main.py
```

Também podemos utilizar **Run Python File**, desde que o VSCode esteja utilizando o interpretador correto da `.venv`.

O resultado esperado é a abertura da primeira janela gráfica do **EngConvert**.

---

# 6. Testar as dimensões da janela

Localize:

```python
app.geometry("700x450")
```

Altere temporariamente para:

```python
app.geometry("900x600")
```

Salve e execute novamente:

```powershell
python main.py
```

Observe a alteração no tamanho da janela.

Depois do teste, retorne para:

```python
app.geometry("700x450")
```

---

# 7. Testar os modos de aparência

Localize:

```python
ctk.set_appearance_mode("system")
```

Teste:

```python
ctk.set_appearance_mode("dark")
```

Depois:

```python
ctk.set_appearance_mode("light")
```

Execute o programa após cada alteração e observe o resultado.

Por fim, restaure:

```python
ctk.set_appearance_mode("system")
```

---

# 8. Conferir o código final

Ao concluir os experimentos, o `main.py` deverá estar novamente assim:

```python
# Importa a biblioteca CustomTkinter.
# "as ctk" cria o apelido ctk para facilitar seu uso no código.
import customtkinter as ctk


# Define o modo de aparência da aplicação.
# "system" acompanha o modo claro/escuro configurado no sistema operacional.
ctk.set_appearance_mode("system")

# Define o tema de cores padrão utilizado pelos widgets do CustomTkinter.
# Neste projeto começaremos utilizando o tema "blue".
ctk.set_default_color_theme("blue")


# Cria a janela principal da aplicação.
# CTk() é a janela principal fornecida pelo CustomTkinter.
# O objeto criado é armazenado na variável "app".
app = ctk.CTk()

# Define o texto apresentado na barra de título da janela.
app.title("EngConvert")

# Define o tamanho inicial da janela.
# 700 pixels de largura × 450 pixels de altura.
app.geometry("700x450")


# Inicia o loop principal de eventos da interface gráfica.
# A partir daqui, a aplicação permanece ativa aguardando eventos,
# como movimentar/redimensionar a janela ou solicitar seu fechamento.
app.mainloop()
```

---

# 9. Executar a versão final da Aula 01

Execute:

```powershell
python main.py
```

Podemos representar o resultado:

```text
main.py
   ↓
CustomTkinter
   ↓
CTk()
   ↓
janela EngConvert
   ↓
mainloop()
   ↓
aplicação permanece ativa
```

---

# ✅ Checklist da Aula 01.1

- [ ] projeto `engconvert` aberto no VSCode;
- [ ] VSCode utilizando o Python da `.venv`;
- [ ] `main.py` atualizado;
- [ ] primeira janela do EngConvert executada;
- [ ] `geometry()` testado;
- [ ] modos `dark`, `light` e `system` testados;
- [ ] código final restaurado para `700x450`;
- [ ] modo de aparência final em `"system"`;
- [ ] `python main.py` abre corretamente o EngConvert.

---

## 📌 Resultado desta etapa

```text
EngConvert
│
├── ambiente preparado          ✓
├── .venv configurada           ✓
├── CustomTkinter instalado     ✓
├── VSCode configurado          ✓
└── primeira GUI funcionando    ✓
```

A preparação inicial veio da **Aula 00**.

A fundamentação sobre VSCode, Python, ambientes virtuais, GUI, Tcl/Tk, Tkinter, CustomTkinter e programação orientada a eventos está na **Aula 01**.

Este roteiro registrou apenas os **novos passos práticos necessários para concluir a Aula 01**.

---

## ➡️ Próxima etapa

Na **Aula 02**, continuaremos a evolução do EngConvert a partir desta primeira janela, relacionando o desenvolvimento ao **Roadmap e aos Sprints** e avançando na construção da interface gráfica.

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
