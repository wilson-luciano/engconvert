# Aula 10.1 — Roteiro Prático: Navegação e Tabs do EngConvert

**Disciplina:** Programação para Engenharia Mecânica  
**Projeto:** EngConvert — Conversor de Unidades de Engenharia  
**Etapa 10:** Interface Completa  
**Sprint 09:** Navegação, visibilidade e ordenação de categorias  
**Pré-requisitos:** Aulas 08.1, 09.1 e 10.0

> Esta aula implementa **a primeira Sprint da Etapa 10**. As funcionalidades General, Custom, About e persistência JSON permanecem para as próximas Sprints, conforme o planejamento da Aula 10.0. Não confundir a conclusão desta aula com a conclusão de toda a Etapa 10.

---

## 1. Objetivos de aprendizagem

Ao concluir, o aluno deverá ser capaz de criar uma interface com `CTkTabview`, selecionar grandezas, ocultar e reordenar categorias, restaurar a configuração padrão, manter os cálculos isolados da GUI, executar testes e registrar a evolução com Git.

## 2. Ponto de partida

Utilizaremos **os arquivos efetivos da Sprint 08**, incluindo `dados.py`, `conversoes.py`, `interface.py`, `main.py`, `pyproject.toml` e `tests/test_conversoes.py`.

```text
engconvert/
├── main.py
├── pyproject.toml
├── src/engconvert/
│   ├── __init__.py
│   ├── dados.py
│   ├── conversoes.py
│   └── interface.py
└── tests/test_conversoes.py
```

## 3. Abrir o projeto no VSCode e compreender o ambiente

### 3.1. Por que preparar o ambiente antes de modificar a interface?

Na Aula 08.1, o EngConvert deixou de concentrar todos os recursos no `main.py` e passou a utilizar um **pacote Python** localizado dentro de `src/`:

```text
engconvert/
├── main.py
├── pyproject.toml
├── .venv/
└── src/
    └── engconvert/
        ├── __init__.py
        ├── dados.py
        ├── conversoes.py
        └── interface.py
```

Quando `main.py` executa:

```python
from engconvert.interface import iniciar_aplicacao
```

o Python precisa localizar o pacote `engconvert`. Como ele está em `src/engconvert/`, a instalação editável permite que o ambiente virtual reconheça o pacote sem que precisemos copiar os arquivos ou modificar manualmente `sys.path`.

### 3.2. Abrir a pasta correta

No **PowerShell**, execute:

```powershell
cd C:\Projetos\engconvert
code .
```

- `cd` muda para a pasta do projeto.
- `code .` abre essa pasta no VSCode; o ponto (`.`) significa **diretório atual**.

Abra o terminal integrado do VSCode e ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

O ambiente `.venv` isola as bibliotecas e a instalação do EngConvert das demais instalações de Python do computador. Confira se o terminal indica `(.venv)` e se o interpretador selecionado no VSCode corresponde a `C:\Projetos\engconvert\.venv\Scripts\python.exe`.

### 3.3. Primeiro, verificar se o EngConvert já está instalado

Na Aula 08.1, **orientamos** a instalação editável. Isso não comprova que o comando foi executado no computador do aluno. Antes de instalá-lo novamente, vamos **verificar o ambiente virtual que está ativo**.

No terminal do VSCode, com `(.venv)` ativado, execute:

```powershell
python -m pip show engconvert
```

Se o pacote estiver instalado, a saída será semelhante a:

```text
Name: engconvert
Version: 0.1.0
Location: C:\Projetos\engconvert\.venv\Lib\site-packages
Editable project location: C:\Projetos\engconvert
```

A linha **`Editable project location`** indica a pasta do projeto à qual a instalação editável está associada. Confirme se aponta para **a pasta correta do EngConvert**. A linha `Location` normalmente aponta para a pasta de pacotes do ambiente virtual, **não** para uma cópia integral dos arquivos-fonte.

Se aparecer:

```text
WARNING: Package(s) not found: engconvert
```

isso significa que o `pip` **não encontrou a distribuição instalada no Python atualmente utilizado**. Não significa que os arquivos do projeto desapareceram.

> **Atenção:** um pacote com esse nome pode estar instalado em outro ambiente virtual ou apontar para outra pasta. Por isso, confira tanto o `.venv` ativo quanto o caminho exibido.

### 3.4. O que faz `python -m pip install -e .`?

Se a instalação ainda não existir **nesse ambiente**, ou estiver apontando para um projeto incorreto, execute na raiz `C:\Projetos\engconvert`:

```powershell
python -m pip install -e .
```

| Parte     | Significado            | Função nesta aula                                           |
| --------- | ---------------------- | ----------------------------------------------------------- |
| `python`  | Interpretador ativo    | Usa o Python do `.venv` ativado                             |
| `-m pip`  | Executa o módulo `pip` | Utiliza o instalador associado a esse Python                |
| `install` | Instalar               | Solicita a instalação do projeto                            |
| `-e`      | _Editable_ (editável)  | Associa a instalação aos arquivos-fonte em `src/`           |
| `.`       | Diretório atual        | Indica o projeto cuja configuração está em `pyproject.toml` |

O `pip` lê a configuração do `pyproject.toml`, utiliza o mecanismo de empacotamento e registra o EngConvert no ambiente Python. Assim, as importações encontram o pacote dentro de `src/`, sem precisar copiar manualmente seus módulos para `.venv` ou alterar `sys.path`. Dependências declaradas, como `customtkinter`, também podem ser instaladas ou atualizadas.

### 3.5. Como funciona a instalação editável

O diagrama abaixo pode ser visualizado diretamente na prévia Markdown do VSCode, pois utiliza apenas texto monoespaçado:

```text
┌───────────────────────────────────┐      ┌───────────────────────────────────┐
│ PROJETO: C:\Projetos\engconvert   │      │ AMBIENTE VIRTUAL: .venv           │
│                                   │      │                                   │
│ main.py                           │      │ Python + pip                      │
│ pyproject.toml                    │      │ Registro da instalação editável   │
│ src/engconvert/                   │      │ do pacote engconvert              │
│   ├── __init__.py                 │      │                                   │
│   ├── dados.py                    │      │                                   │
│   ├── conversoes.py               │      │                                   │
│   └── interface.py                │      │                                   │
└──────────────────┬────────────────┘      └──────────────────┬────────────────┘
                   │                                          │
                   └──────── python -m pip install -e . ──────┘
                                                              │
                                                              ▼
                                            O Python do .venv passa a localizar
                                            o pacote no diretório src/engconvert/
                                                              │
                                                              ▼
                                            Editar interface.py ou conversoes.py
                                            não exige reinstalar a cada alteração
```

**Observe:** o código-fonte continua no projeto, enquanto o ambiente virtual mantém os mecanismos necessários para localizá-lo. O comando não gera um `.exe`, não envia arquivos ao GitHub e não transforma automaticamente o programa em uma aplicação distribuível.

### 3.6. Posso executar o comando novamente?

**Sim, normalmente sem problemas.** O `pip` pode reinstalar ou atualizar os registros da instalação editável. Isso **não apaga** o código-fonte nem os commits do Git. Entretanto, a operação pode consultar ou atualizar dependências conforme a configuração do projeto; por isso, não precisamos repeti-la sem necessidade.

Regra prática:

```text
ATIVAR .venv
    │
    ▼
python -m pip show engconvert
    │
    ├── Instalado e apontando para este projeto?
    │       └── SIM → prosseguir, sem reinstalar
    │
    └── Não instalado ou apontando para outro projeto?
            └── executar python -m pip install -e .
                        │
                        ▼
                   verificar novamente
```

### 3.7. Verificar a importação

Após a conferência ou instalação, execute:

```powershell
python -c "import engconvert; print(engconvert.__file__)"
```

O caminho normalmente deve apontar para `C:\Projetos\engconvert\src\engconvert\__init__.py`. Se ocorrer `ModuleNotFoundError`, verifique o interpretador, a ativação do `.venv`, o diretório do projeto e o resultado de `pip show` antes de continuar.

> **Ideia-chave:** na Aula 08.1 aprendemos a **configurar** a instalação editável; nesta aula aprendemos também a **verificar** se ela realmente está disponível no ambiente usado pelo aluno.

## 4. Validar a versão anterior

```powershell
python -m pytest -q
python main.py
```

Confira pelo menos: `1 bar → 100 kPa`, `1 m → 1000 mm`, `0 °C → 32 °F`. Se falhar, corrija **antes** de modificar a interface.

## 5. Criar a branch da Sprint 09 — por que e como?

### 5.1. Qual é o objetivo da branch?

Uma **branch** é uma linha de desenvolvimento que permite trabalhar em novas funcionalidades sem alterar diretamente a versão principal (`main`). Nesta aula, a branch `feature-tabs` será usada para desenvolver as abas e os controles de categorias do EngConvert. **Ela é específica da Sprint 09**, mas a prática de criar branches poderá ser repetida em outras Sprints, com nomes diferentes.

```text
                         criação                         merge
main (versão estável) ──────●──────────────────────────────●──────
                             \                             ↑
                              ●──●──● feature-tabs ────────┘
                                   desenvolver e testar
```

> **Importante:** criar uma branch não cria outra pasta física do projeto. O Git gerencia versões dos arquivos no mesmo repositório. Ao trocar de branch, o conteúdo do diretório de trabalho pode mudar.

### 5.2. Conferir a situação antes de criar a branch

No terminal integrado do VSCode, na raiz do projeto, execute:

```powershell
git status
git branch --show-current
```

`git status` mostra se existem arquivos modificados, novos arquivos ou alterações preparadas para commit. `git branch --show-current` informa em qual branch estamos. O ideal é iniciar a Sprint sem alterações locais pendentes. Se houver alterações, **não as descarte automaticamente**: confira o que foi modificado e decida se precisa concluir um commit ou guardar temporariamente o trabalho, conforme aprendido nas aulas anteriores.

### 5.3. Partir da versão principal

Se o repositório estiver em condições adequadas:

```powershell
git switch main
git pull
```

| Comando           | O que faz                                        | Por que usamos                                    |
| ----------------- | ------------------------------------------------ | ------------------------------------------------- |
| `git switch main` | Seleciona a branch principal                     | Começar da versão de referência do EngConvert     |
| `git pull`        | Busca e integra alterações do remoto configurado | Atualizar a cópia local antes de iniciar a Sprint |

**Atenção:** `git pull` exige um repositório remoto e uma branch com acompanhamento configurado. Se ainda não houver remoto, ou se aparecer uma mensagem de erro, **não execute comandos aleatórios para corrigir**; verifique primeiro `git remote -v` e `git status`. Se o trabalho estiver apenas no computador, é possível criar a branch a partir da `main` local sem executar `git pull`.

### 5.4. Criar a branch de desenvolvimento

```powershell
git switch -c feature-tabs
```

O parâmetro `-c` significa **criar** uma branch e já mudar para ela. O nome `feature-tabs` indica que desenvolveremos uma funcionalidade relacionada às abas (_tabs_).

Confira o resultado:

```powershell
git branch --show-current
git status
```

O primeiro comando deverá mostrar `feature-tabs`. A partir deste ponto, as modificações da Sprint 09 serão registradas nessa branch. Nas Sprints seguintes poderemos utilizar, por exemplo, `feature-general`, `feature-custom` e `feature-about`, conforme o planejamento aprovado.

**Não confunda:** a branch organiza o desenvolvimento; a **Sprint** organiza objetivos, tarefas, testes e critérios de conclusão. Uma Sprint pode ter uma branch própria, mas os conceitos não são sinônimos.

## 6. Planejar a Sprint 09 — criar o documento de acompanhamento

### 6.1. Por que precisamos de um documento da Sprint?

Antes de alterar `interface.py`, precisamos registrar **o que será desenvolvido**, **como verificar o resultado** e **quando considerar o trabalho concluído**. Isso evita implementar funcionalidades sem critérios claros e permite que outra pessoa compreenda o andamento do projeto.

O arquivo `docs/sprints/sprint-09-tabs.md` é um documento Markdown do **projeto EngConvert** — não é um arquivo Python e não será executado pelo interpretador. Seu objetivo é acompanhar a Sprint 09.

### 6.2. Criar as pastas e o arquivo

No explorador de arquivos do VSCode, dentro de `engconvert`, crie a pasta `docs` (se ainda não existir); dentro dela, crie `sprints`. Em seguida, crie o arquivo `sprint-09-tabs.md`.

Alternativamente, no PowerShell, a partir da raiz do projeto:

```powershell
New-Item -ItemType Directory -Force docs\sprints
New-Item -ItemType File -Path docs\sprints\sprint-09-tabs.md -Force
```

**Cuidado:** `-Force` pode atingir um arquivo já existente; se o documento já estiver preenchido, abra-o e preserve seu conteúdo, em vez de recriá-lo. No VSCode, abra `docs/sprints/sprint-09-tabs.md` e copie o conteúdo completo abaixo.

### 6.3. Conteúdo completo de `docs/sprints/sprint-09-tabs.md`

```markdown
# Sprint 09 — Navegação e Tabs do EngConvert

**Projeto:** EngConvert  
**Etapa:** 10 — Interface Completa  
**Sprint:** 09  
**Branch:** `feature-tabs`  
**Status:** Planejada

## 1. Objetivo

Implementar uma interface de navegação com abas, permitindo selecionar, ocultar e reorganizar as cinco categorias de grandezas do EngConvert, preservando as regras matemáticas existentes.

## 2. Funcionalidades previstas

- Criar as abas **Favoritas** e **Todas as grandezas**.
- Permitir selecionar uma grandeza por meio das abas.
- Criar a janela **Categorias**.
- Permitir mostrar ou ocultar categorias.
- Permitir alterar a ordem de apresentação.
- Implementar os comandos **Subir**, **Descer**, **Restaurar**, **Salvar** e **Cancelar**.
- Preservar as conversões existentes.

## 3. Checklist de desenvolvimento

### Preparação

- [ ] Confirmar que o EngConvert funciona antes das alterações.
- [ ] Executar os testes existentes.
- [ ] Criar a branch `feature-tabs`.

### Implementação

- [ ] Adicionar o componente `CTkTabview`.
- [ ] Criar a aba Favoritas.
- [ ] Criar a aba Todas as grandezas.
- [ ] Implementar a seleção de grandezas.
- [ ] Implementar a janela Categorias.
- [ ] Implementar a visibilidade das categorias.
- [ ] Implementar a ordenação das categorias.
- [ ] Implementar Restaurar, Salvar e Cancelar.

### Validação

- [ ] Verificar a navegação pelas abas.
- [ ] Confirmar que ocultar uma categoria não exclui seus dados.
- [ ] Confirmar que Cancelar descarta alterações.
- [ ] Impedir que todas as categorias sejam ocultadas.
- [ ] Executar os testes com `pytest`.
- [ ] Conferir manualmente a interface.

### Git e documentação

- [ ] Atualizar a documentação da Sprint.
- [ ] Registrar as alterações em commit.
- [ ] Integrar a branch à `main`, após validação.
- [ ] Enviar as alterações ao GitHub.

## 4. Critérios de aceitação

A Sprint será considerada concluída quando:

1. As abas estiverem funcionando corretamente.
2. As cinco categorias originais permanecerem disponíveis no catálogo.
3. A visibilidade e a ordenação funcionarem conforme planejado.
4. As conversões matemáticas anteriores continuarem corretas.
5. Os testes automatizados forem aprovados.
6. As alterações estiverem registradas no Git.

## 5. Limitações desta Sprint

As preferências de navegação serão mantidas apenas durante a execução do aplicativo.

O armazenamento permanente em JSON, as configurações numéricas e as unidades personalizadas serão desenvolvidos em Sprints posteriores.

## 6. Resultado final

**Status:** Pendente de validação.

**Testes automatizados:** Ainda não executados nesta Sprint.

**Observações:** Preencher após a implementação e os testes.
```

### 6.4. Como acompanhar o progresso?

No Markdown, `- [ ]` indica uma tarefa pendente; `- [x]` indica uma tarefa concluída. **Não marque uma tarefa apenas porque o código foi digitado**: primeiro execute o recurso, confira o comportamento e, quando aplicável, rode os testes. Ao finalizar a Sprint, atualize o campo **Status**, registre o resultado real dos testes e as observações relevantes.

Esse documento deverá acompanhar o código no Git, conforme os comandos de `git add` e `git commit` apresentados mais adiante nesta aula.

## 7. Separação de responsabilidades

```text
interface.py       → widgets, eventos, seleção e navegação
conversoes.py      → matemática (não modificar nesta Sprint)
dados.py           → catálogo original (não apagar unidades)
```

Ocultar uma categoria **não significa excluí-la** do dicionário de dados.

## 8. Como funcionará a navegação

```text
┌───────────────────────────────────────────────────┐
│ EngConvert                         ⚙ Categorias   │
├───────────────────────────────────────────────────┤
│ [ Favoritas ] [ Todas as grandezas ]              │
│  Botões para escolher uma grandeza                │
├───────────────────────────────────────────────────┤
│ Grandeza: [ Pressão                     ▼ ]       │
│ De: [bar ▼]        ↔       Para: [kPa ▼]          │
│ Valor: [1]                                        │
│               [ Converter ]                       │
│ Resultado: 100 kPa                                │
└───────────────────────────────────────────────────┘
```

**Atenção:** o desenho é conceitual; o posicionamento final depende do tamanho da janela e da escala de exibição do Windows.

## 9. O que é `CTkTabview`?

É um widget do CustomTkinter que agrupa páginas em abas. Nesta Sprint teremos **Favoritas** e **Todas as grandezas**. As grandezas continuam sendo escolhidas no `CTkComboBox`, e as abas oferecem atalhos.

## 10. O que é estado de navegação?

```python
ordem = list(lista_grandezas)
visiveis = list(lista_grandezas)
favoritas = ["Pressão", "Temperatura"]
```

`ordem` define a sequência; `visiveis` define o subconjunto mostrado; `favoritas` define atalhos. São listas independentes. **Ainda não há gravação em JSON:** as alterações duram apenas enquanto a aplicação está aberta.

## 11. Por que utilizar `list(...)`?

`list(lista_grandezas)` cria uma cópia da lista original. Assim, mover elementos em `ordem` não altera a lista-base em `dados.py`.

## 12. Como escolher uma grandeza?

O clique em um botão de aba chama `selecionar_grandeza(nome)`, que atualiza o ComboBox e chama `atualizar_unidades()`. Isso preserva o fluxo já existente da Aula 08.1.

## 13. O papel de `lambda`

```python
command=lambda n=nome: selecionar_grandeza(n)
```

O argumento padrão `n=nome` guarda o nome correspondente a cada botão criado em um laço. Sem esse cuidado, todos os botões poderiam acabar selecionando o último nome da lista.

## 14. Por que criar uma janela secundária?

`CTkToplevel(app)` permite configurar categorias sem substituir a tela de conversão. Nela haverá uma lista com caixas de seleção, controles Subir/Descer, Restaurar, Salvar e Cancelar.

## 15. Cancelar não deve alterar as preferências ativas

Ao abrir a janela criamos **cópias temporárias** das listas. `Cancelar` descarta essas cópias; `Salvar` aplica as escolhas. É uma introdução didática ao conceito de transação de interface.

## 16. Impedir zero categorias visíveis

O usuário não deve conseguir salvar uma navegação sem nenhuma grandeza. A interface apresenta um aviso e mantém a janela aberta para correção.

## 17. Atualizar a interface

Depois de salvar, os botões das abas são reconstruídos com as categorias visíveis, na ordem escolhida. A seleção atual é preservada se ainda for válida; caso contrário, uma grandeza visível é selecionada e as unidades são atualizadas.

## 18. O que não será implementado nesta Sprint

- precisão numérica configurável (`General`);
- salvamento persistente em JSON;
- unidades personalizadas (`Custom`);
- janela completa de créditos (`About`);
- novas grandezas e novas fórmulas.

Esses itens permanecem planejados, não concluídos.

---

# PARTE PRÁTICA — ARQUIVOS COMPLETOS

## 19. Substituir `interface.py`

No VSCode, abra `src/engconvert/interface.py`. Faça uma cópia de segurança por meio do Git (a branch já foi criada) e substitua o conteúdo pelo código completo abaixo. **Não modifique os módulos matemáticos nesta Sprint.**

```python
"""Interface gráfica do EngConvert — Sprint 09: navegação e categorias.

Mantém a matemática no módulo conversoes.py. Preferências persistentes e
cadastro de unidades serão implementados em Sprints posteriores.
"""
import customtkinter as ctk
from .dados import lista_grandezas
from .conversoes import converter, obter_unidades


def iniciar_aplicacao():
    """Monta a janela e associa eventos aos controles."""
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()
    app.title("EngConvert — Sprint 09")
    app.geometry("790x630")
    app.minsize(660, 560)

    # Estado da navegação: somente preferências da sessão atual.
    ordem = list(lista_grandezas)
    visiveis = list(lista_grandezas)
    favoritas = ["Pressão", "Temperatura"]

    def categorias_disponiveis():
        return [nome for nome in ordem if nome in visiveis]

    def atualizar_unidades(_=None):
        unidades = obter_unidades(combo_grandeza.get())
        combo_de.configure(values=unidades)
        combo_para.configure(values=unidades)
        combo_de.set(unidades[0])
        combo_para.set(unidades[1] if len(unidades) > 1 else unidades[0])
        resultado.configure(text="Resultado")

    def selecionar_grandeza(nome):
        if nome not in categorias_disponiveis():
            return
        combo_grandeza.set(nome)
        atualizar_unidades()

    def atualizar_navegacao():
        disponiveis = categorias_disponiveis()
        if not disponiveis:
            # Uma categoria deve permanecer visível para evitar estado vazio.
            visiveis.append(ordem[0])
            disponiveis = categorias_disponiveis()
        combo_grandeza.configure(values=disponiveis)
        if combo_grandeza.get() not in disponiveis:
            combo_grandeza.set(disponiveis[0])
            atualizar_unidades()
        for frame in (aba_favoritas, aba_todas):
            for widget in frame.winfo_children():
                widget.destroy()
        fav = [nome for nome in disponiveis if nome in favoritas]
        if not fav:
            ctk.CTkLabel(aba_favoritas, text="Nenhuma favorita visível.").pack(pady=15)
        for nome in fav:
            ctk.CTkButton(aba_favoritas, text=nome,
                          command=lambda n=nome: selecionar_grandeza(n)).pack(fill="x", padx=20, pady=5)
        for nome in disponiveis:
            ctk.CTkButton(aba_todas, text=nome,
                          command=lambda n=nome: selecionar_grandeza(n)).pack(fill="x", padx=20, pady=4)

    def abrir_categorias():
        janela = ctk.CTkToplevel(app)
        janela.title("Preferências — Categorias")
        janela.geometry("470x520")
        janela.transient(app)
        # Cópias: cancelar fecha sem alterar o estado ativo.
        ordem_temp = list(ordem)
        visiveis_temp = list(visiveis)
        selecionada = ctk.StringVar(value=ordem_temp[0])
        lista = ctk.CTkScrollableFrame(janela, height=300)
        lista.pack(fill="both", expand=True, padx=18, pady=12)

        def desenhar():
            for w in lista.winfo_children():
                w.destroy()
            for nome in ordem_temp:
                linha = ctk.CTkFrame(lista, fg_color="transparent")
                linha.pack(fill="x", pady=3)
                ctk.CTkRadioButton(linha, text=nome, variable=selecionada,
                                   value=nome).pack(side="left", padx=4)
                marcado = ctk.BooleanVar(value=nome in visiveis_temp)
                def alterar(valor, n=nome):
                    if valor and n not in visiveis_temp:
                        visiveis_temp.append(n)
                    elif not valor and n in visiveis_temp:
                        visiveis_temp.remove(n)
                ctk.CTkCheckBox(linha, text="Mostrar", variable=marcado,
                                command=lambda v=marcado, n=nome: alterar(v.get(), n)).pack(side="right")

        def mover(deslocamento):
            nome = selecionada.get()
            indice = ordem_temp.index(nome)
            novo = indice + deslocamento
            if 0 <= novo < len(ordem_temp):
                ordem_temp[indice], ordem_temp[novo] = ordem_temp[novo], ordem_temp[indice]
                desenhar()

        def restaurar():
            ordem_temp[:] = lista_grandezas
            visiveis_temp[:] = lista_grandezas
            selecionada.set(ordem_temp[0])
            desenhar()

        def salvar():
            if not visiveis_temp:
                aviso.configure(text="Mantenha pelo menos uma categoria visível.")
                return
            ordem[:] = ordem_temp
            visiveis[:] = visiveis_temp
            atualizar_navegacao()
            janela.destroy()

        desenhar()
        comandos = ctk.CTkFrame(janela)
        comandos.pack(padx=15, pady=4)
        ctk.CTkButton(comandos, text="Subir", width=75, command=lambda: mover(-1)).pack(side="left", padx=3)
        ctk.CTkButton(comandos, text="Descer", width=75, command=lambda: mover(1)).pack(side="left", padx=3)
        ctk.CTkButton(comandos, text="Restaurar", width=90, command=restaurar).pack(side="left", padx=3)
        aviso = ctk.CTkLabel(janela, text="")
        aviso.pack()
        rodape = ctk.CTkFrame(janela, fg_color="transparent")
        rodape.pack(pady=8)
        ctk.CTkButton(rodape, text="Salvar", command=salvar).pack(side="left", padx=5)
        ctk.CTkButton(rodape, text="Cancelar", command=janela.destroy).pack(side="left", padx=5)
        janela.grab_set()

    def inverter_unidades():
        de, para = combo_de.get(), combo_para.get()
        combo_de.set(para)
        combo_para.set(de)

    def ao_converter():
        try:
            valor = float(entrada.get())
            convertido = converter(valor, combo_grandeza.get(), combo_de.get(), combo_para.get())
            resultado.configure(text=f"{convertido:.6g} {combo_para.get()}")
        except (ValueError, KeyError, ZeroDivisionError):
            resultado.configure(text="Verifique o valor e as unidades selecionadas.")

    cabecalho = ctk.CTkFrame(app)
    cabecalho.pack(fill="x", padx=22, pady=(18, 10))
    ctk.CTkLabel(cabecalho, text="EngConvert", font=("Arial", 26, "bold")).pack(side="left", padx=15, pady=10)
    ctk.CTkButton(cabecalho, text="⚙ Categorias", command=abrir_categorias).pack(side="right", padx=12)

    abas = ctk.CTkTabview(app, height=195)
    abas.pack(fill="x", padx=22, pady=6)
    aba_favoritas = abas.add("Favoritas")
    aba_todas = abas.add("Todas as grandezas")

    corpo = ctk.CTkFrame(app)
    corpo.pack(fill="both", expand=True, padx=22, pady=10)
    ctk.CTkLabel(corpo, text="Grandeza").pack(pady=(15, 4))
    combo_grandeza = ctk.CTkComboBox(corpo, values=ordem, width=330, command=atualizar_unidades, state="readonly")
    combo_grandeza.pack()
    combo_grandeza.set("Pressão")
    linha = ctk.CTkFrame(corpo, fg_color="transparent")
    linha.pack(pady=15)
    combo_de = ctk.CTkComboBox(linha, width=190, state="readonly")
    combo_de.pack(side="left", padx=8)
    ctk.CTkButton(linha, text="↔", width=46, command=inverter_unidades).pack(side="left", padx=4)
    combo_para = ctk.CTkComboBox(linha, width=190, state="readonly")
    combo_para.pack(side="left", padx=8)
    entrada = ctk.CTkEntry(corpo, width=300, placeholder_text="Digite o valor")
    entrada.pack(pady=5)
    ctk.CTkButton(corpo, text="Converter", command=ao_converter).pack(pady=12)
    resultado = ctk.CTkLabel(corpo, text="Resultado", font=("Arial", 19, "bold"))
    resultado.pack(pady=5)
    atualizar_unidades()
    atualizar_navegacao()
    app.mainloop()
```

## 20. Arquivo completo — `dados.py`

O arquivo `dados.py` foi organizado na Aula 08.1 e contém o catálogo das cinco grandezas e seus fatores. **Nesta Sprint não precisamos modificá-lo:** a configuração das abas altera apenas a apresentação das categorias, sem apagar ou modificar unidades e fatores. Seu conteúdo completo é reproduzido abaixo para conferência.

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

## 21. Arquivo completo — `conversoes.py`

O arquivo `conversoes.py` reúne as regras matemáticas separadas da interface na Aula 08.1. **Nesta Sprint não precisamos modificá-lo:** as novas abas mudam a navegação, não as fórmulas. Reproduzimos o código completo para que o aluno confirme que os cálculos continuam independentes da GUI.

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

## 22. Arquivo completo — `main.py`

O arquivo `main.py` foi simplificado na Aula 08.1 para funcionar como **ponto de entrada** da aplicação: ele importa e chama `iniciar_aplicacao()` de `interface.py`. **Nesta Sprint não precisamos modificá-lo**, pois a nova interface continua sendo iniciada pelo mesmo comando `python main.py`. Seu conteúdo é apresentado integralmente para conferência.

```python
"""Ponto de entrada do EngConvert."""

from engconvert.interface import iniciar_aplicacao


def main():
    iniciar_aplicacao()


if __name__ == "__main__":
    main()
```

## 23. Arquivo completo — `pyproject.toml`

O `pyproject.toml` foi introduzido na Aula 08.1 para descrever o projeto, suas dependências e a localização do pacote em `src/`. **Nesta Sprint não precisamos modificá-lo**, porque não alteramos a estrutura do pacote nem suas dependências. Ele é reproduzido para relacionar sua configuração à instalação editável explicada na Seção 3.

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

## 24. Arquivo completo — `tests/test_conversoes.py`

O arquivo `tests/test_conversoes.py` foi criado na Sprint 08 para verificar automaticamente os cálculos do EngConvert. **Nesta Sprint não precisamos modificá-lo**, porque não estamos alterando as fórmulas. Ele é apresentado por completo para conferência e deverá ser executado novamente para detectar regressões.

```python
"""Sprint 08 — testes das funções reais da Aula 08.1."""

import pytest

from engconvert.conversoes import converter, converter_temperatura, obter_unidades
from engconvert.dados import grandezas, unidades_temperatura


@pytest.mark.parametrize(
    "valor, grandeza, origem, destino, esperado",
    [
        (1, "Pressão", "bar", "kPa", 100),
        (1, "Pressão", "atm", "Pa", 101325),
        (1, "Comprimento", "m", "mm", 1000),
        (12, "Comprimento", "in", "ft", 1),
        (1, "Área", "m²", "cm²", 10000),
        (1, "Área", "ft²", "m²", 0.09290304),
        (1, "Volume", "L", "mL", 1000),
        (1, "Volume", "gal (US)", "L", 3.785411784),
        (1, "Volume", "gal (UK)", "L", 4.54609),
        (0, "Temperatura", "°C", "°F", 32),
        (0, "Temperatura", "°C", "K", 273.15),
        (273.15, "Temperatura", "K", "°C", 0),
        (491.67, "Temperatura", "°R", "°F", 32),
        (32, "Temperatura", "°F", "°R", 491.67),
    ],
)
def test_conversoes_conhecidas(valor, grandeza, origem, destino, esperado):
    resultado = converter(valor, grandeza, origem, destino)
    assert resultado == pytest.approx(esperado, rel=1e-9, abs=1e-9)


@pytest.mark.parametrize("grandeza", ["Pressão", "Comprimento", "Área", "Volume"])
def test_conversao_identidade(grandeza):
    unidade = next(iter(grandezas[grandeza]))
    assert converter(123.45, grandeza, unidade, unidade) == pytest.approx(123.45)


def test_temperatura_identidade():
    assert converter_temperatura(25, "°C", "°C") == pytest.approx(25)


def test_obter_unidades_pressao():
    assert obter_unidades("Pressão") == list(grandezas["Pressão"].keys())


def test_obter_unidades_temperatura():
    assert obter_unidades("Temperatura") == unidades_temperatura


def test_temperatura_absoluta_rankine_kelvin():
    assert converter(540, "Temperatura", "°R", "K") == pytest.approx(300)
```

---

## 25. Executar a aplicação

```powershell
python main.py
```

Confirme que aparecem as duas abas e o botão **Categorias**. Escolha Pressão, digite 1 e converta de bar para kPa.

## 26. Exercício guiado — ocultar uma categoria

1. Clique em **Categorias**.
2. Desmarque **Área**.
3. Clique em **Salvar**.
4. Confira que Área não aparece nas abas nem na lista de seleção.
5. Reabra Categorias e marque Área novamente.

**Pergunta:** a categoria foi removida de `dados.py`? Não. Somente a apresentação foi alterada.

## 27. Exercício guiado — alterar a ordem

1. Abra Categorias.
2. Selecione Temperatura no botão de opção.
3. Clique em **Subir** repetidamente.
4. Salve e confira a sequência em Todas as grandezas.
5. Use **Restaurar** e depois **Salvar** para recuperar a ordem original.

## 28. Exercício guiado — cancelar

1. Desmarque Volume.
2. Clique em **Cancelar**.
3. Reabra a janela e confirme que Volume continua marcado.

## 29. Testes de regressão

```powershell
python -m pytest -q
```

Os testes da Aula 09.1 devem continuar passando. Eles validam a matemática, mas **não substituem** a inspeção da GUI.

## 30. Checklist manual da interface

- [ ] A janela abre sem exceções.
- [ ] As abas Favoritas e Todas as grandezas aparecem.
- [ ] Clicar numa grandeza atualiza as unidades.
- [ ] O botão ↔ inverte as unidades.
- [ ] Uma categoria oculta não aparece na navegação.
- [ ] Restaurar recompõe a ordem original.
- [ ] Cancelar descarta alterações.
- [ ] Não é possível salvar todas as categorias ocultas.
- [ ] A conversão 1 bar → 100 kPa continua correta.
- [ ] A interface continua legível na escala do Windows usada no laboratório.

## 31. Registrar as mudanças

```bash
git status
git diff
git add src/engconvert/interface.py docs/sprints/sprint-09-tabs.md
git commit -m "feat: adiciona abas e organizacao de categorias"
```

## 32. Validar e integrar

Depois de executar os testes e conferir a interface:

```bash
git status
git switch main
git pull
git merge feature-tabs
python -m pytest -q
python main.py
git push
```

Se houver conflito, interrompa a sequência e resolva-o antes de continuar. A exclusão opcional da branch local, **após o merge**, é `git branch -d feature-tabs`.

## 33. Atualizar o Roadmap e a Sprint

Marque a **Sprint 09 — Tabs** como concluída apenas quando os critérios de aceitação forem atendidos. **A Etapa 10 permanece em andamento**: General, Custom e About ainda serão desenvolvidos.

## 34. Exercícios de fixação

1. Por que a lista `visiveis` não deve apagar elementos de `grandezas`?
2. Qual a diferença entre `ordem`, `visiveis` e `favoritas`?
3. Por que usamos cópias temporárias na janela de preferências?
4. Qual teste automatizado comprova que o cálculo de pressão foi preservado?
5. Por que a interface exige testes manuais mesmo com `pytest` aprovado?

## 35. Resumo da aula

```text
Sprint 08: testes das conversões
          ↓
Sprint 09: abas + navegação + categorias
          ↓
próximas Sprints: General → Custom → About
          ↓
Etapa 10 completa
```

**Ideia-chave:** a navegação é uma responsabilidade da interface. O catálogo de grandezas e as fórmulas matemáticas devem permanecer independentes da forma como o usuário escolhe uma categoria.

---

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
