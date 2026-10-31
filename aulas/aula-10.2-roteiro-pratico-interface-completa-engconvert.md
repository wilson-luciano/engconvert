# Aula 10.2 — Roteiro Prático: Finalização da Interface do EngConvert

**Disciplina:** Programação para Engenharia Mecânica  
**Projeto:** EngConvert — Conversor de Unidades de Engenharia  
**Etapa:** 10 — Interface Completa  
**Sprints:** 10 (General + JSON), 11 (Custom), 12 (About + integração)  
**Pré-requisitos:** Aulas 08.1, 09.1, 10.0 e 10.1

> Esta aula complementa a Aula 10.1 sem alterar seu material congelado. Não é ainda a aula de geração do `.exe`: o empacotamento e o GitHub Releases ficam para a Aula 11. O roteiro apresenta os módulos completos e uma única versão final de `interface.py`, evitando substituições repetidas; os commits documentam as três Sprints separadamente.

---

## 1. Objetivos de aprendizagem

Ao concluir, o aluno deverá ser capaz de configurar tema, algarismos significativos, notação científica e aviso de zero absoluto; salvar preferências e unidades personalizadas em JSON; validar fatores de conversão; preservar as abas da Sprint 09; testar a aplicação e registrar três entregas no Git.

## 2. Escopo e sequência de trabalho

| Sprint       | Implementação                            | Entrega verificável                           |
| ------------ | ---------------------------------------- | --------------------------------------------- |
| 10 — General | `configuracoes.py`, opções gerais, JSON  | Preferências persistem após fechar e reabrir  |
| 11 — Custom  | `personalizadas.py`, cadastro e exclusão | Unidade cadastrada participa das conversões   |
| 12 — About   | créditos, versão, integração e testes    | Interface integrada, documentação e validação |

**Importante:** `General`, `Custom` e `About` são nomes das funcionalidades de referência da Aula 10.0, não bibliotecas Python. Não copiaremos código de outros aplicativos.

## 3. Preparação no Windows e VSCode

No PowerShell, na raiz do projeto:

```powershell
cd C:\Projetos\engconvert
code .
.\.venv\Scripts\Activate.ps1
python -m pip show engconvert
python -m pytest -q
python main.py
```

Se o pacote não estiver instalado no ambiente ativo, ou estiver associado a outra pasta, execute `python -m pip install -e .` na raiz e verifique novamente. Feche a interface após conferir as abas da Aula 10.1.

Antes de mudar de branch, execute:

```powershell
git status
git branch --show-current
```

Não descarte alterações locais. Se a árvore de trabalho estiver limpa, volte à `main`, atualize-a **somente se houver remoto configurado** e crie a branch da aula:

```powershell
git switch main
git pull
git switch -c feature-interface-final
```

Se não houver remoto/acompanhamento configurado, **omita `git pull`**. Se `feature-interface-final` já existir, use `git switch feature-interface-final` em vez de `-c`. Não continue se aparecerem conflitos ou mudanças locais incompatíveis.

## 4. Organização de arquivos

```text
engconvert/
├── main.py                          # existente; sem alteração
├── pyproject.toml                   # existente; sem alteração
├── docs/
│   └── sprints/
│       ├── sprint-09-tabs.md        # Aula 10.1
│       ├── sprint-10-general.md     # novo
│       ├── sprint-11-custom.md      # novo
│       └── sprint-12-about.md       # novo
├── src/
│   └── engconvert/
│       ├── __init__.py
│       ├── dados.py                 # original preservado
│       ├── conversoes.py            # original preservado
│       ├── configuracoes.py         # novo
│       ├── personalizadas.py        # novo
│       └── interface.py             # substituir pela versão integrada
└── tests/
    ├── test_conversoes.py           # testes anteriores
    ├── test_configuracoes.py        # novo
    └── test_personalizadas.py       # novo
```

**Por que dois módulos novos?** `configuracoes.py` trata das preferências gerais; `personalizadas.py` valida, persiste e aplica fatores. `interface.py` cuida de janelas e eventos. Os cálculos originais continuam separados.

---

# PARTE I — SPRINT 10: GENERAL E PERSISTÊNCIA EM JSON

## 5. Entender as preferências

- **Tema:** `System`, `Light` ou `Dark`.
- **Precisão:** 1 a 12 **algarismos significativos** na exibição, sem alterar o cálculo interno.
- **Notação científica:** exibir, por exemplo, `1.000000e+03` conforme a precisão selecionada.
- **Zero absoluto:** quando habilitado, alertar se uma entrada de temperatura estiver abaixo de 0 K.
- **Ordem e visibilidade:** salvar as preferências já trabalhadas na Sprint 09.

O JSON será gravado em uma pasta do usuário: `%APPDATA%\EngConvert` no Windows, ou `~/.config/EngConvert` quando `APPDATA` não existir. **Não** gravamos dentro de `src/`, nem na pasta do futuro executável. O programa cria os arquivos ao salvar preferências; não é necessário copiá-los para o GitHub.

### 5.1. Criar o módulo de configurações

No VSCode, clique com o botão direito em `src/engconvert`, escolha **New File** e crie `configuracoes.py`. Copie integralmente o código:

**Arquivo:** `src/engconvert/configuracoes.py`

```python
"""Preferências persistentes do EngConvert, sem dependência da GUI."""
import json
import os
from pathlib import Path


def pasta_usuario():
    """Pasta gravável por usuário, inclusive quando houver um .exe."""
    base = os.environ.get('APPDATA')
    return (Path(base) if base else Path.home() / '.config') / 'EngConvert'


def caminho_configuracoes():
    return pasta_usuario() / 'configuracoes.json'


def padrao():
    return {'versao_esquema': 1, 'tema': 'System', 'precisao': 6,
            'cientifica': False, 'avisar_zero_absoluto': True,
            'ordem': ['Pressão', 'Comprimento', 'Área', 'Volume', 'Temperatura'],
            'visiveis': ['Pressão', 'Comprimento', 'Área', 'Volume', 'Temperatura']}


def validar(dados):
    """Normaliza o JSON recebido sem confiar em tipos ou valores externos."""
    resultado = padrao()
    if not isinstance(dados, dict):
        return resultado
    if dados.get('tema') in ('System', 'Light', 'Dark'):
        resultado['tema'] = dados['tema']
    if type(dados.get('precisao')) is int and 1 <= dados['precisao'] <= 12:
        resultado['precisao'] = dados['precisao']
    for chave in ('cientifica', 'avisar_zero_absoluto'):
        if type(dados.get(chave)) is bool:
            resultado[chave] = dados[chave]
    originais = padrao()['ordem']
    ordem = dados.get('ordem')
    if isinstance(ordem, list) and len(ordem) == len(originais) and set(map(str, ordem)) == set(originais) and all(isinstance(x, str) for x in ordem):
        resultado['ordem'] = ordem.copy()
    visiveis = dados.get('visiveis')
    if isinstance(visiveis, list) and visiveis and all(isinstance(x, str) for x in visiveis):
        filtradas = [x for x in resultado['ordem'] if x in visiveis]
        if filtradas:
            resultado['visiveis'] = filtradas
    return resultado


def carregar(caminho=None):
    destino = Path(caminho) if caminho is not None else caminho_configuracoes()
    try:
        return validar(json.loads(destino.read_text(encoding='utf-8')))
    except (OSError, UnicodeError, ValueError, TypeError):
        return padrao()


def salvar(dados, caminho=None):
    destino = Path(caminho) if caminho is not None else caminho_configuracoes()
    destino.parent.mkdir(parents=True, exist_ok=True)
    temporario = destino.with_suffix('.tmp')
    temporario.write_text(json.dumps(validar(dados), ensure_ascii=False, indent=2), encoding='utf-8')
    temporario.replace(destino)
```

### 5.2. Como funciona esse módulo?

- `padrao()` cria valores iniciais seguros.
- `validar()` impede que tipos incorretos e valores fora dos limites sejam usados.
- `carregar()` recupera o JSON e retorna padrões se ele estiver ausente ou inválido.
- `salvar()` grava primeiro um arquivo temporário e depois o substitui, reduzindo o risco de um arquivo parcialmente escrito.
- `pasta_usuario()` mantém preferências fora do repositório.

**Atenção:** quando o arquivo JSON está corrompido, esta versão retorna valores padrão; não faz recuperação automática dos dados antigos. Se houver falha de permissão durante a gravação, a GUI deverá informar o erro.

### 5.3. Testar General sem abrir a interface

Crie `tests/test_configuracoes.py`:

**Arquivo:** `tests/test_configuracoes.py`

```python
import json
from engconvert import configuracoes as cfg


def test_padrao_sem_arquivo(tmp_path):
    assert cfg.carregar(tmp_path / 'ausente.json') == cfg.padrao()


def test_salvar_e_reabrir(tmp_path):
    arquivo = tmp_path / 'preferencias.json'
    preferencias = cfg.padrao()
    preferencias.update(tema='Dark', precisao=8, cientifica=True)
    cfg.salvar(preferencias, arquivo)
    assert cfg.carregar(arquivo)['tema'] == 'Dark'
    assert cfg.carregar(arquivo)['precisao'] == 8


def test_json_corrompido(tmp_path):
    arquivo = tmp_path / 'preferencias.json'
    arquivo.write_text('{invalido', encoding='utf-8')
    assert cfg.carregar(arquivo) == cfg.padrao()


def test_valores_invalidos_sao_normalizados():
    resultado = cfg.validar({'precisao': 0, 'tema': 'Azul', 'visiveis': []})
    assert resultado['precisao'] == 6
    assert resultado['tema'] == 'System'
    assert len(resultado['visiveis']) == 5
```

Execute:

```powershell
python -m pytest tests/test_configuracoes.py -q
```

**Resultado esperado:** quatro testes aprovados. Os testes utilizam `tmp_path` para não modificar as preferências reais do aluno.

### 5.4. Registrar a entrega da Sprint 10

O arquivo `interface.py` integrado será colocado na Parte III, mas já podemos registrar os módulos e testes de persistência, sem declarar a interface General concluída:

```powershell
git add src/engconvert/configuracoes.py tests/test_configuracoes.py docs/sprints/sprint-10-general.md
git commit -m "feat: adiciona persistencia e validacao de preferencias"
```

Crie o documento da Sprint antes desse commit (modelo na Seção 12). O checklist da interface só poderá ser marcado após sua implementação e teste manual.

---

# PARTE II — SPRINT 11: CUSTOM

## 6. O que será permitido cadastrar?

Nesta primeira versão, **somente unidades multiplicativas** de Pressão, Comprimento, Área e Volume. Não cadastraremos escalas de Temperatura por um único fator: elas podem exigir deslocamento de origem e tratamento físico específico.

O fator deve relacionar a nova unidade à unidade de referência: **Pa, m, m² ou m³**. Exemplo: uma unidade de comprimento fictícia `duplo_metro` com fator `2` representa `1 duplo_metro = 2 m`.

**Validações obrigatórias:** nome não vazio, até 30 caracteres, sem duplicação no catálogo original ou no personalizado, fator numérico finito e estritamente positivo. Não executaremos expressões Python digitadas pelo usuário.

## 7. Criar o módulo `personalizadas.py`

Copie o conteúdo integral:

**Arquivo:** `src/engconvert/personalizadas.py`

```python
"""Unidades multiplicativas personalizadas, isoladas da interface."""
import json
import math
from pathlib import Path
from .configuracoes import pasta_usuario
from .dados import grandezas


def caminho_unidades():
    return pasta_usuario() / 'unidades_personalizadas.json'


def validar_unidade(categoria, nome, fator, existentes=None):
    if categoria not in grandezas:
        raise ValueError('Escolha uma grandeza multiplicativa válida; temperatura não é aceita.')
    if not isinstance(nome, str) or not nome.strip() or len(nome.strip()) > 30:
        raise ValueError('O nome deve ter de 1 a 30 caracteres.')
    nome = nome.strip()
    if nome.casefold() in {u.casefold() for u in grandezas[categoria]}:
        raise ValueError('Essa unidade já existe no catálogo original.')
    if existentes and nome.casefold() in {u.casefold() for u in existentes.get(categoria, {})}:
        raise ValueError('Essa unidade personalizada já existe.')
    try:
        numero = float(fator)
    except (TypeError, ValueError, OverflowError):
        raise ValueError('Informe um fator numérico válido.') from None
    if not math.isfinite(numero) or numero <= 0:
        raise ValueError('O fator deve ser positivo e finito.')
    return nome, numero


def adicionar(unidades, categoria, nome, fator):
    nome, numero = validar_unidade(categoria, nome, fator, unidades)
    novo = {cat: valores.copy() for cat, valores in unidades.items()}
    novo.setdefault(categoria, {})[nome] = numero
    return novo


def excluir(unidades, categoria, nome):
    novo = {cat: valores.copy() for cat, valores in unidades.items()}
    if nome not in novo.get(categoria, {}):
        raise ValueError('Unidade personalizada não encontrada.')
    del novo[categoria][nome]
    return novo


def carregar(caminho=None):
    destino = Path(caminho) if caminho is not None else caminho_unidades()
    try:
        bruto = json.loads(destino.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, ValueError, TypeError):
        return {}
    if not isinstance(bruto, dict) or bruto.get('versao_esquema') != 1 or not isinstance(bruto.get('unidades'), dict):
        return {}
    resultado = {}
    for categoria, itens in bruto['unidades'].items():
        if not isinstance(itens, dict):
            continue
        for nome, fator in itens.items():
            try:
                resultado = adicionar(resultado, categoria, nome, fator)
            except (ValueError, TypeError):
                continue
    return resultado


def salvar(unidades, caminho=None):
    destino = Path(caminho) if caminho is not None else caminho_unidades()
    # Revalidar antes de persistir dados.
    validas = {}
    for categoria, itens in unidades.items():
        for nome, fator in itens.items():
            validas = adicionar(validas, categoria, nome, fator)
    destino.parent.mkdir(parents=True, exist_ok=True)
    temporario = destino.with_suffix('.tmp')
    temporario.write_text(json.dumps({'versao_esquema': 1, 'unidades': validas}, ensure_ascii=False, indent=2), encoding='utf-8')
    temporario.replace(destino)


def unidades_disponiveis(categoria, personalizadas):
    if categoria == 'Temperatura':
        from .dados import unidades_temperatura
        return list(unidades_temperatura)
    return list(grandezas[categoria]) + list(personalizadas.get(categoria, {}))


def converter(valor, categoria, origem, destino, personalizadas):
    from .conversoes import converter as converter_original
    if categoria == 'Temperatura':
        return converter_original(valor, categoria, origem, destino)
    fatores = dict(grandezas[categoria])
    fatores.update(personalizadas.get(categoria, {}))
    return valor * fatores[origem] / fatores[destino]
```

### 7.1. Como funciona a conversão?

O módulo combina temporariamente os fatores originais de `dados.py` com os fatores personalizados da categoria. A conversão é:

\[ valor*{destino} = valor*{origem} \times \frac{fator*{origem}}{fator*{destino}} \]

**Exemplo:** `3 duplo_metro` × `2 m/duplo_metro` = `6 m`.

Os dicionários originais de `dados.py` não são modificados. A exclusão é permitida apenas para unidades personalizadas. O JSON contém `versao_esquema` e o dicionário `unidades`, e é validado novamente na leitura.

### 7.2. Criar testes das unidades personalizadas

**Arquivo:** `tests/test_personalizadas.py`

```python
import pytest
from engconvert import personalizadas as p


def test_adicionar_e_converter():
    unidades = p.adicionar({}, 'Comprimento', 'minha_unidade', 2)
    assert p.converter(3, 'Comprimento', 'minha_unidade', 'm', unidades) == pytest.approx(6)


@pytest.mark.parametrize('fator', ['0', '-2', 'nan', 'inf', 'texto'])
def test_fator_invalido(fator):
    with pytest.raises(ValueError):
        p.adicionar({}, 'Pressão', 'unidade_teste', fator)


def test_duplicata_e_temperatura():
    with pytest.raises(ValueError):
        p.adicionar({}, 'Pressão', 'bar', 2)
    with pytest.raises(ValueError):
        p.adicionar({}, 'Temperatura', 'nova_escala', 2)


def test_excluir_sem_afetar_original():
    unidades = p.adicionar({}, 'Área', 'quadra', 100)
    novas = p.excluir(unidades, 'Área', 'quadra')
    assert 'quadra' in unidades['Área']
    assert 'quadra' not in novas['Área']


def test_salvar_e_reabrir(tmp_path):
    arquivo = tmp_path / 'custom.json'
    unidades = p.adicionar({}, 'Volume', 'tanque', 3)
    p.salvar(unidades, arquivo)
    assert p.carregar(arquivo) == unidades


def test_json_invalido(tmp_path):
    arquivo = tmp_path / 'custom.json'
    arquivo.write_text('{erro', encoding='utf-8')
    assert p.carregar(arquivo) == {}
```

Execute:

```powershell
python -m pytest tests/test_personalizadas.py -q
```

**Resultado esperado:** dez testes aprovados. Incluem fatores zero, negativos, `nan`, `inf`, duplicatas, temperatura, persistência, exclusão e JSON inválido.

### 7.3. Registrar a entrega da Sprint 11

Após criar `docs/sprints/sprint-11-custom.md` (modelo na Seção 12):

```powershell
git add src/engconvert/personalizadas.py tests/test_personalizadas.py docs/sprints/sprint-11-custom.md
git commit -m "feat: adiciona unidades personalizadas validadas"
```

Este commit documenta o núcleo funcional. A janela Custom será integrada na Parte III.

---

# PARTE III — SPRINT 12: ABOUT E INTERFACE INTEGRADA

## 8. Atualizar a interface sem perder a Sprint 09

A nova `interface.py` mantém **Favoritas**, **Todas as grandezas**, a janela de ordenação/visibilidade e a conversão. Acrescenta botões `General`, `Custom` e `About`, persistência das preferências e leitura de unidades personalizadas.

**Procedimento:** abra `src/engconvert/interface.py` e substitua seu conteúdo pelo arquivo completo abaixo. Faça isso **somente após** confirmar que os testes dos módulos novos passaram. O Git permite recuperar a versão anterior.

**Observação didática:** apresentamos uma única versão final da interface para não exigir três substituições do mesmo arquivo. A separação entre Sprints é preservada nos módulos, testes, documentação e commits; a validação completa das três interfaces ocorrerá após esta integração.

**Arquivo:** `src/engconvert/interface.py`

```python
"""Interface do EngConvert — Sprints 09 a 12."""
import math
import customtkinter as ctk
from .dados import lista_grandezas
from . import configuracoes as cfg
from . import personalizadas as pers

VERSAO = '0.1.0'


def formatar_numero(valor, preferencias):
    precisao = preferencias['precisao']
    return f'{valor:.{precisao}e}' if preferencias['cientifica'] else f'{valor:.{precisao}g}'


def iniciar_aplicacao():
    preferencias = cfg.carregar()
    unidades_custom = pers.carregar()
    ctk.set_appearance_mode(preferencias['tema'])
    ctk.set_default_color_theme('blue')
    app = ctk.CTk()
    app.title(f'EngConvert — v{VERSAO}')
    app.geometry('800x680')
    app.minsize(680, 590)
    ordem = list(preferencias['ordem'])
    visiveis = list(preferencias['visiveis'])
    favoritas = ['Pressão', 'Temperatura']

    def disponiveis():
        return [nome for nome in ordem if nome in visiveis]

    def persistir():
        preferencias['ordem'] = list(ordem)
        preferencias['visiveis'] = list(visiveis)
        try:
            cfg.salvar(preferencias)
            return True
        except OSError as erro:
            mostrar_erro(f'Não foi possível salvar as preferências: {erro}')
            return False

    def mostrar_erro(mensagem):
        resultado.configure(text=mensagem)

    def atualizar_unidades(_=None):
        categoria = combo_grandeza.get()
        unidades = pers.unidades_disponiveis(categoria, unidades_custom)
        combo_de.configure(values=unidades)
        combo_para.configure(values=unidades)
        combo_de.set(unidades[0])
        combo_para.set(unidades[1] if len(unidades) > 1 else unidades[0])
        resultado.configure(text='Resultado')

    def selecionar_grandeza(nome):
        if nome in disponiveis():
            combo_grandeza.set(nome)
            atualizar_unidades()

    def atualizar_navegacao():
        opcoes = disponiveis()
        combo_grandeza.configure(values=opcoes)
        if combo_grandeza.get() not in opcoes:
            combo_grandeza.set(opcoes[0])
        atualizar_unidades()
        for frame in (aba_favoritas, aba_todas):
            for widget in frame.winfo_children():
                widget.destroy()
        fav = [nome for nome in opcoes if nome in favoritas]
        if not fav:
            ctk.CTkLabel(aba_favoritas, text='Nenhuma favorita visível.').pack(pady=10)
        for nome in fav:
            ctk.CTkButton(aba_favoritas, text=nome, command=lambda n=nome: selecionar_grandeza(n)).pack(fill='x', padx=20, pady=3)
        for nome in opcoes:
            ctk.CTkButton(aba_todas, text=nome, command=lambda n=nome: selecionar_grandeza(n)).pack(fill='x', padx=20, pady=3)

    def janela_categorias():
        janela = ctk.CTkToplevel(app)
        janela.title('Tabs — Categorias')
        janela.geometry('490x540')
        janela.transient(app)
        ordem_temp = list(ordem)
        visiveis_temp = list(visiveis)
        selecionada = ctk.StringVar(value=ordem_temp[0])
        lista = ctk.CTkScrollableFrame(janela, height=300)
        lista.pack(fill='both', expand=True, padx=16, pady=12)

        def desenhar():
            for widget in lista.winfo_children():
                widget.destroy()
            for nome in ordem_temp:
                linha = ctk.CTkFrame(lista, fg_color='transparent')
                linha.pack(fill='x', pady=3)
                ctk.CTkRadioButton(linha, text=nome, variable=selecionada, value=nome).pack(side='left')
                marcada = ctk.BooleanVar(value=nome in visiveis_temp)
                def alternar(n=nome, v=marcada):
                    if v.get() and n not in visiveis_temp:
                        visiveis_temp.append(n)
                    elif not v.get() and n in visiveis_temp:
                        visiveis_temp.remove(n)
                ctk.CTkCheckBox(linha, text='Mostrar', variable=marcada, command=alternar).pack(side='right')

        def mover(delta):
            indice = ordem_temp.index(selecionada.get())
            novo = indice + delta
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
                aviso.configure(text='Mantenha pelo menos uma categoria visível.')
                return
            ordem[:] = ordem_temp
            visiveis[:] = visiveis_temp
            atualizar_navegacao()
            if persistir():
                janela.destroy()

        desenhar()
        botoes = ctk.CTkFrame(janela)
        botoes.pack(pady=4)
        for nome, acao in [('Subir', lambda: mover(-1)), ('Descer', lambda: mover(1)), ('Restaurar', restaurar)]:
            ctk.CTkButton(botoes, text=nome, width=100, command=acao).pack(side='left', padx=3)
        aviso = ctk.CTkLabel(janela, text='')
        aviso.pack()
        rodape = ctk.CTkFrame(janela, fg_color='transparent')
        rodape.pack(pady=8)
        ctk.CTkButton(rodape, text='Salvar', command=salvar).pack(side='left', padx=5)
        ctk.CTkButton(rodape, text='Cancelar', command=janela.destroy).pack(side='left', padx=5)
        janela.grab_set()

    def janela_general():
        janela = ctk.CTkToplevel(app)
        janela.title('General — Configurações')
        janela.geometry('410x360')
        janela.transient(app)
        ctk.CTkLabel(janela, text='Aparência').pack(pady=(18, 4))
        tema = ctk.CTkOptionMenu(janela, values=['System', 'Light', 'Dark'])
        tema.set(preferencias['tema'])
        tema.pack()
        ctk.CTkLabel(janela, text='Algarismos significativos (1 a 12)').pack(pady=(12, 4))
        precisao = ctk.CTkEntry(janela)
        precisao.insert(0, str(preferencias['precisao']))
        precisao.pack()
        cientifica = ctk.BooleanVar(value=preferencias['cientifica'])
        aviso_zero = ctk.BooleanVar(value=preferencias['avisar_zero_absoluto'])
        ctk.CTkCheckBox(janela, text='Notação científica', variable=cientifica).pack(pady=9)
        ctk.CTkCheckBox(janela, text='Avisar sobre zero absoluto', variable=aviso_zero).pack(pady=5)
        aviso = ctk.CTkLabel(janela, text='')
        aviso.pack()

        def salvar():
            try:
                numero = int(precisao.get())
                if not 1 <= numero <= 12:
                    raise ValueError
            except ValueError:
                aviso.configure(text='Informe um inteiro entre 1 e 12.')
                return
            preferencias.update(tema=tema.get(), precisao=numero, cientifica=cientifica.get(), avisar_zero_absoluto=aviso_zero.get())
            ctk.set_appearance_mode(preferencias['tema'])
            if persistir():
                janela.destroy()
        ctk.CTkButton(janela, text='Salvar', command=salvar).pack(pady=5)
        janela.grab_set()

    def janela_custom():
        nonlocal unidades_custom
        janela = ctk.CTkToplevel(app)
        janela.title('Custom — Unidades personalizadas')
        janela.geometry('480x520')
        janela.transient(app)
        ctk.CTkLabel(janela, text='Grandeza (não inclui Temperatura)').pack(pady=(15, 5))
        categoria = ctk.CTkOptionMenu(janela, values=list(pers.grandezas))
        categoria.pack()
        ctk.CTkLabel(janela, text='Nome da nova unidade').pack(pady=(12, 3))
        nome = ctk.CTkEntry(janela, width=250, placeholder_text='Ex.: minha_unidade')
        nome.pack()
        ctk.CTkLabel(janela, text='Fator em relação à unidade de referência SI').pack(pady=(12, 3))
        fator = ctk.CTkEntry(janela, width=250, placeholder_text='Ex.: 1000')
        fator.pack()
        ctk.CTkLabel(janela, text='Para Pressão, fator em Pa; Comprimento, m; Área, m²; Volume, m³.', wraplength=420).pack(pady=8)
        lista = ctk.CTkOptionMenu(janela, values=['Nenhuma unidade cadastrada'])
        lista.pack(pady=5)
        aviso = ctk.CTkLabel(janela, text='', wraplength=430)
        aviso.pack(pady=5)

        def atualizar_lista(_=None):
            nomes = list(unidades_custom.get(categoria.get(), {}))
            lista.configure(values=nomes or ['Nenhuma unidade cadastrada'])
            lista.set((nomes or ['Nenhuma unidade cadastrada'])[0])

        def gravar(novas):
            nonlocal unidades_custom
            try:
                pers.salvar(novas)
            except (OSError, ValueError) as erro:
                aviso.configure(text=f'Não foi possível salvar: {erro}')
                return
            unidades_custom = novas
            atualizar_lista()
            atualizar_unidades()
            aviso.configure(text='Unidades personalizadas atualizadas.')

        def adicionar():
            try:
                novas = pers.adicionar(unidades_custom, categoria.get(), nome.get(), fator.get())
            except ValueError as erro:
                aviso.configure(text=str(erro))
                return
            gravar(novas)

        def excluir():
            try:
                novas = pers.excluir(unidades_custom, categoria.get(), lista.get())
            except ValueError as erro:
                aviso.configure(text=str(erro))
                return
            gravar(novas)

        categoria.configure(command=atualizar_lista)
        atualizar_lista()
        ctk.CTkButton(janela, text='Adicionar unidade', command=adicionar).pack(pady=7)
        ctk.CTkButton(janela, text='Excluir unidade selecionada', command=excluir).pack(pady=5)
        ctk.CTkButton(janela, text='Fechar', command=janela.destroy).pack(pady=6)
        janela.grab_set()

    def janela_about():
        janela = ctk.CTkToplevel(app)
        janela.title('About — Sobre o EngConvert')
        janela.geometry('440x290')
        janela.transient(app)
        mensagem = (f'EngConvert — Versão {VERSAO}\n\n'
                    'Projeto didático: Programação para Engenharia Mecânica\n'
                    'Autoria do material: Wilson Luciano\n'
                    'Tecnologias: Python, CustomTkinter e pytest\n\n'
                    'Créditos das bibliotecas e condições de uso: consultar\n'
                    'as licenças e o README do repositório.\n'
                    'Esta versão é educacional.')
        ctk.CTkLabel(janela, text=mensagem, justify='center').pack(expand=True, padx=12)
        ctk.CTkButton(janela, text='Fechar', command=janela.destroy).pack(pady=12)
        janela.grab_set()

    def inverter():
        origem, destino = combo_de.get(), combo_para.get()
        combo_de.set(destino)
        combo_para.set(origem)

    def converter_valor():
        try:
            valor = float(entrada.get().replace(',', '.'))
            if not math.isfinite(valor):
                raise ValueError('Informe um número finito.')
            categoria = combo_grandeza.get()
            convertido = pers.converter(valor, categoria, combo_de.get(), combo_para.get(), unidades_custom)
            if not math.isfinite(convertido):
                raise ValueError('Resultado fora do intervalo numérico.')
            if categoria == 'Temperatura' and preferencias['avisar_zero_absoluto']:
                kelvin = pers.converter(valor, categoria, combo_de.get(), 'K', unidades_custom)
                if kelvin < -1e-9:
                    mostrar_erro('Aviso: temperatura abaixo do zero absoluto.')
                    return
            resultado.configure(text=f'{formatar_numero(convertido, preferencias)} {combo_para.get()}')
        except (ValueError, KeyError, OverflowError, ZeroDivisionError) as erro:
            mostrar_erro(f'Confira valor e unidades: {erro}')

    cabecalho = ctk.CTkFrame(app)
    cabecalho.pack(fill='x', padx=20, pady=(14, 8))
    ctk.CTkLabel(cabecalho, text='EngConvert', font=('Arial', 24, 'bold')).pack(side='left', padx=12, pady=8)
    for titulo, acao in [('Tabs', janela_categorias), ('General', janela_general), ('Custom', janela_custom), ('About', janela_about)]:
        ctk.CTkButton(cabecalho, text=titulo, width=85, command=acao).pack(side='left', padx=3)
    abas = ctk.CTkTabview(app, height=190)
    abas.pack(fill='x', padx=20, pady=5)
    aba_favoritas = abas.add('Favoritas')
    aba_todas = abas.add('Todas as grandezas')
    corpo = ctk.CTkFrame(app)
    corpo.pack(fill='both', expand=True, padx=20, pady=10)
    ctk.CTkLabel(corpo, text='Grandeza').pack(pady=(12, 4))
    combo_grandeza = ctk.CTkComboBox(corpo, values=disponiveis(), state='readonly', width=310, command=atualizar_unidades)
    combo_grandeza.pack()
    combo_grandeza.set(disponiveis()[0])
    linha = ctk.CTkFrame(corpo, fg_color='transparent')
    linha.pack(pady=12)
    combo_de = ctk.CTkComboBox(linha, width=180, state='readonly')
    combo_de.pack(side='left', padx=5)
    ctk.CTkButton(linha, text='↔', width=40, command=inverter).pack(side='left', padx=4)
    combo_para = ctk.CTkComboBox(linha, width=180, state='readonly')
    combo_para.pack(side='left', padx=5)
    entrada = ctk.CTkEntry(corpo, width=290, placeholder_text='Valor a converter')
    entrada.pack(pady=5)
    ctk.CTkButton(corpo, text='Converter', command=converter_valor).pack(pady=12)
    resultado = ctk.CTkLabel(corpo, text='Resultado', font=('Arial', 18, 'bold'), wraplength=600)
    resultado.pack(pady=4)
    atualizar_navegacao()
    app.mainloop()
```

### 8.1. Arquivos existentes que não devem ser alterados

Os seguintes arquivos permanecem com o conteúdo aprovado nas Aulas 08.1 e 10.1: `src/engconvert/dados.py`, `src/engconvert/conversoes.py`, `main.py`, `pyproject.toml` e `tests/test_conversoes.py`. O aluno deve preservá-los. Para consulta e conferência, seus conteúdos completos são reproduzidos no Anexo A, ao final da aula.

## 9. Executar a versão integrada

```powershell
python -m pytest -q
python main.py
```

**Referência dos testes automatizados:** no conjunto de arquivos que acompanha esta aula, os 22 testes anteriores e os 14 novos passaram, totalizando **36 testes aprovados**. No computador do aluno, o resultado depende de os arquivos terem sido copiados corretamente e do ambiente estar configurado.

### 9.1. Verificações manuais obrigatórias

1. Abra **General**, selecione `Dark`, precisão `8` e notação científica; salve. Feche e reabra o aplicativo: as preferências devem permanecer.
2. Volte ao tema `System` ou `Light`, se desejar. Teste `1 bar → 100 kPa` e confira o formato numérico.
3. Em **General**, mantenha o aviso de zero absoluto ativo. Selecione Temperatura e tente converter `-300 °C` para K: deve surgir um aviso, sem apresentar um resultado físico inválido.
4. Abra **Custom** e cadastre `duplo_metro` em Comprimento com fator `2`. Converta `3 duplo_metro` para `m`: resultado esperado `6 m`.
5. Feche e reabra o aplicativo; a unidade personalizada deve continuar disponível.
6. Tente cadastrar fator `0`, negativo e `nan`: devem ser rejeitados. Tente cadastrar `bar` em Pressão: deve ser rejeitado como duplicata.
7. Exclua `duplo_metro` e confirme que ela deixa de aparecer. As unidades originais permanecem intactas.
8. Em **Tabs**, oculte Área, altere a ordem das categorias e salve. Reinicie: ordem e visibilidade devem ser restauradas.
9. Abra **About** e confira versão, autoria, tecnologias e informações de créditos.
10. Confirme que a janela permanece utilizável na escala de exibição do Windows do laboratório.

**Limitação conhecida:** os testes automatizados desta aula validam cálculo, JSON e regras de cadastro, **não automatizam cliques de GUI**. A inspeção manual acima é indispensável. O cadastro não inclui edição direta de fator: para alterá-lo, exclua e cadastre novamente.

## 10. JSON: onde ficam os dados?

No PowerShell, consulte o caminho padrão do Windows:

```powershell
explorer $env:APPDATA\EngConvert
```

Se ainda não existir, salve uma preferência no aplicativo e tente novamente. Esperam-se os arquivos `configuracoes.json` e `unidades_personalizadas.json` após utilizar os recursos correspondentes. Não inclua dados pessoais nem esses arquivos de preferências nos commits do projeto.

## 11. Git — concluir e integrar

Depois dos testes e das verificações manuais, atualize os documentos das Sprints e registre a integração:

```powershell
git status
git diff
git add src/engconvert/interface.py docs/sprints/sprint-10-general.md docs/sprints/sprint-11-custom.md docs/sprints/sprint-12-about.md
git commit -m "feat: integra General Custom About e navegacao"
python -m pytest -q
```

Antes do merge, confira que não há alterações pendentes e que os testes e a interface foram validados:

```powershell
git status
git switch main
git pull
git merge feature-interface-final
python -m pytest -q
python main.py
```

**Execute `git pull` somente se a `main` acompanhar um remoto configurado.** Se houver conflitos, interrompa o roteiro, resolva-os e valide novamente. Após a confirmação, envie o código-fonte:

```powershell
git push
```

Se a `main` ainda não acompanhar um remoto, configure-o conscientemente antes de usar `git push`; não execute comandos copiados sem verificar a mensagem do Git. O executável **não será enviado nesta aula**: será criado e publicado na Aula 11 via GitHub Releases.

---

## 12. Documentar as três Sprints

No VSCode, crie `docs/sprints` se necessário. Em cada arquivo, copie o modelo correspondente. As caixas começam **desmarcadas** e só devem ser marcadas após comprovação.

### 12.1. `docs/sprints/sprint-10-general.md`

```markdown
# Sprint 10 — General e persistência JSON

**Status:** Em andamento

## Objetivo

Configurar aparência, precisão, notação científica, aviso de zero absoluto e preferências persistentes.

## Checklist

- [ ] Criar e validar `configuracoes.py`.
- [ ] Executar os testes de configurações.
- [ ] Implementar a janela General.
- [ ] Salvar e restaurar preferências após reiniciar.
- [ ] Confirmar aviso de zero absoluto.
- [ ] Registrar resultado dos testes e commit.

## Resultado

**Testes:** preencher com o resultado observado.  
**Observações:** preencher após a validação.
```

### 12.2. `docs/sprints/sprint-11-custom.md`

```markdown
# Sprint 11 — Unidades personalizadas

**Status:** Em andamento

## Objetivo

Cadastrar, validar, excluir e persistir unidades multiplicativas de engenharia.

## Checklist

- [ ] Criar `personalizadas.py`.
- [ ] Rejeitar fator zero, negativo, não numérico e não finito.
- [ ] Impedir duplicatas e cadastro de temperatura multiplicativa.
- [ ] Executar testes automatizados.
- [ ] Implementar a janela Custom.
- [ ] Confirmar cadastro, conversão, exclusão e persistência.
- [ ] Registrar resultado dos testes e commit.

## Resultado

**Testes:** preencher.  
**Observações:** preencher.
```

### 12.3. `docs/sprints/sprint-12-about.md`

```markdown
# Sprint 12 — About e integração final

**Status:** Em andamento

## Objetivo

Integrar General, Custom, Tabs e About e validar a aplicação antes do empacotamento.

## Checklist

- [ ] Criar a janela About e conferir os créditos.
- [ ] Integrar as funcionalidades na `interface.py`.
- [ ] Preservar as abas e as conversões anteriores.
- [ ] Executar a suíte completa de testes.
- [ ] Realizar os dez testes manuais da Aula 10.2.
- [ ] Atualizar a documentação e o roadmap.
- [ ] Registrar commit, fazer merge e enviar ao GitHub.

## Resultado

**Testes:** preencher.  
**Pendências:** preencher.  
**Decisão de liberação para Aula 11:** preencher após validação.
```

## 13. Checklist de conclusão da Etapa 10

- [ ] General salva e restaura preferências.
- [ ] Custom cadastra, utiliza, exclui e persiste unidades válidas.
- [ ] About apresenta versão, autoria e créditos.
- [ ] Tabs preserva ordenação e visibilidade após reiniciar.
- [ ] Zero absoluto é verificado quando o aviso está habilitado.
- [ ] Todos os testes automatizados passaram no ambiente do aluno.
- [ ] Testes manuais da GUI foram concluídos.
- [ ] Commits, merge, documentação e push foram concluídos.

**Somente após esses itens comprovados** a Etapa 10 poderá ser considerada concluída.

## 14. Exercícios de fixação

1. Qual é a diferença entre algarismos significativos e casas decimais?
2. Por que o programa grava preferências na pasta do usuário, em vez de dentro de `src/`?
3. Por que `nan` e `inf` não são fatores de conversão aceitáveis?
4. Por que uma escala de temperatura não pode ser cadastrada somente com um fator multiplicativo?
5. O que é regressão de software e por que mantivemos os testes anteriores?
6. Qual é a diferença entre publicar código-fonte com `git push` e distribuir um executável em GitHub Releases?

## 15. Resumo da aula

```text
Aula 10.1 — Sprint 09: Tabs e navegação (congelada)
                ↓
Aula 10.2 — Sprint 10: General + JSON
                ↓
             Sprint 11: Custom
                ↓
             Sprint 12: About + integração
                ↓
      Testes + documentação + GitHub
                ↓
Aula 11 — PyInstaller + executável + GitHub Releases
```

**Ideia-chave:** a GUI apresenta opções; os módulos independentes validam, calculam e persistem os dados. A distribuição do `.exe` é uma etapa posterior à validação funcional.

---

# ANEXO A — ARQUIVOS EXISTENTES COMPLETOS (PARA CONFERÊNCIA)

> Estes arquivos foram introduzidos em aulas anteriores. **Não os substitua desnecessariamente**; são reproduzidos para que o aluno possa conferir o conteúdo sem procurar outro material.

**Arquivo:** `src/engconvert/dados.py`

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

**Arquivo:** `src/engconvert/conversoes.py`

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

**Arquivo:** `main.py`

```python
"""Ponto de entrada do EngConvert."""

from engconvert.interface import iniciar_aplicacao


def main():
    iniciar_aplicacao()


if __name__ == "__main__":
    main()
```

**Arquivo:** `pyproject.toml`

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

**Arquivo:** `tests/test_conversoes.py`

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

<sub>© 2026 <b>Wilson Luciano</b> · Programação para Engenharia Mecânica · EngConvert · Material didático · Versão 1.0</sub>
