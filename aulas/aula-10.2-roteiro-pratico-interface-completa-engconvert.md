# Aula 10.2 — Roteiro Prático: Finalização da Interface do EngConvert

**Disciplina:** Programação para Engenharia Mecânica  
**Projeto:** EngConvert — Conversor de Unidades de Engenharia  
**Etapa:** 10 — Interface Completa  
**Sprints:** 10 (General + JSON), 11 (Custom), 12 (About + integração)  
**Pré-requisitos:** Aulas 08.1, 09.1, 10.0 e 10.1

> Esta aula complementa a Aula 10.1 sem alterar seu material congelado. Não é ainda a aula de geração do `.exe`: o empacotamento e o GitHub Releases ficam para a Aula 11. O roteiro apresenta os módulos completos e uma única versão final de `interface.py`, evitando substituições repetidas; os commits documentam as três Sprints separadamente.

---

## 1. Objetivos de aprendizagem

Ao concluir, o aluno deverá ser capaz de configurar tema, idioma (português/inglês), cores dos botões, algarismos significativos, notação científica e aviso de zero absoluto; salvar preferências, favoritos, ordem, visibilidade e altura do painel em JSON; cadastrar e validar unidades personalizadas; **preservar integralmente a interface aprovada na Aula 10.1**; testar a aplicação e registrar as três Sprints no Git.

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
# Execute git pull apenas se houver remoto e upstream configurados.
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

- **Tema:** Sistema, Claro ou Escuro (valores internos JSON: `System`, `Light`, `Dark`).
- **Idioma:** português (`pt`) ou inglês (`en`), com tradução dos elementos da interface.
- **Cor dos botões:** Azul, Transparente, Cinza claro, Verde, Laranja, Vermelho ou Roxo; com contraste em caixas de seleção, menus, abas e painel de resultados.
- **Precisão:** 1 a 12 **algarismos significativos** na exibição, sem alterar o cálculo interno.
- **Notação científica:** exibir, por exemplo, `1.000000e+03` conforme a precisão selecionada.
- **Zero absoluto:** quando habilitado, alertar se uma entrada de temperatura estiver abaixo de 0 K.
- **Ordem, visibilidade e favoritos:** salvar as preferências já trabalhadas na Sprint 09.
- **Geometria:** salvar a altura do painel de categorias. A janela principal inicia em dimensão compacta padronizada, sem restaurar largura e altura antigas do JSON.

Os arquivos JSON serão gravados em uma pasta do usuário: `%APPDATA%\EngConvert` no Windows, ou `~/.config/EngConvert` quando `APPDATA` não existir. **Não** gravamos dentro de `src/`, nem na pasta do futuro executável. O programa cria os arquivos ao salvar preferências; não é necessário copiá-los para o GitHub.

### 5.1. Criar o módulo de configurações

No VSCode, abra `src/engconvert/configuracoes.py` (ou crie-o se ainda não existir). Copie integralmente o código de referência abaixo. **Nesta revisão, o módulo já inclui as preferências de idioma e cores; os testes complementares estão na Seção 5.3.2.**

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
    return {'versao_esquema': 1, 'tema': 'System', 'idioma': 'pt', 'cor_botoes': 'Azul', 'precisao': 6,
            'cientifica': False, 'avisar_zero_absoluto': True,
            'ordem': ['Pressão', 'Comprimento', 'Área', 'Volume', 'Temperatura'],
            'visiveis': ['Pressão', 'Comprimento', 'Área', 'Volume', 'Temperatura'],
            'favoritas': ['Pressão', 'Temperatura'], 'altura_categorias': 125,
            'largura_janela': None, 'altura_janela': None}


def validar(dados):
    """Normaliza o JSON recebido sem confiar em tipos ou valores externos."""
    resultado = padrao()
    if not isinstance(dados, dict):
        return resultado
    if dados.get('idioma') in ('pt', 'en'):
        resultado['idioma'] = dados['idioma']
    if dados.get('cor_botoes') in ('Azul', 'Transparente', 'Cinza claro', 'Verde', 'Laranja', 'Vermelho', 'Roxo'):
        resultado['cor_botoes'] = dados['cor_botoes']
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
    favoritas = dados.get('favoritas')
    if isinstance(favoritas, list) and all(isinstance(x, str) for x in favoritas):
        resultado['favoritas'] = [x for x in resultado['ordem']
                                if x in favoritas and x in resultado['visiveis']]
    altura = dados.get('altura_categorias')
    if type(altura) is int and 100 <= altura <= 320:
        resultado['altura_categorias'] = altura
    for chave in ('largura_janela', 'altura_janela'):
        valor = dados.get(chave)
        if type(valor) is int and 420 <= valor <= 3000:
            resultado[chave] = valor
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

### 5.3.1. Testes adicionais de favoritos e geometria

Acrescente ao final de `tests/test_configuracoes.py`:

```python
def test_favoritos_e_geometria_persistem(tmp_path):
    arquivo = tmp_path / "configuracoes.json"
    dados = cfg.padrao()
    dados.update(favoritas=["Volume", "Pressão"], altura_categorias=180,
                 largura_janela=750, altura_janela=600)
    cfg.salvar(dados, arquivo)
    restaurado = cfg.carregar(arquivo)
    assert set(restaurado["favoritas"]) == {"Volume", "Pressão"}
    assert restaurado["altura_categorias"] == 180
    assert restaurado["largura_janela"] == 750
    assert restaurado["altura_janela"] == 600


def test_geometria_invalida_retorna_ao_padrao():
    dados = cfg.validar({"altura_categorias": -10, "largura_janela": "muito",
                        "altura_janela": 99999, "favoritas": ["Inexistente"]})
    assert dados["altura_categorias"] == 125
    assert dados["largura_janela"] is None
    assert dados["altura_janela"] is None
    assert dados["favoritas"] == []
```

**Total esperado para `test_configuracoes.py`: seis testes**, após acrescentar os dois novos.

Execute:

```powershell
python -m pytest tests/test_configuracoes.py -q
```

**Resultado esperado:** seis testes aprovados, incluindo os dois testes adicionais de favoritos e geometria. Os testes utilizam `tmp_path` para não modificar as preferências reais do aluno.

### 5.3.2. Testar as novas preferências de idioma e cores

Como `configuracoes.py` foi ampliado durante a integração, acrescente ao final de `tests/test_configuracoes.py` estes testes complementares:

```python
def test_idioma_e_cor_persistem(tmp_path):
    arquivo = tmp_path / "configuracoes.json"
    dados = cfg.padrao()
    dados.update(idioma="en", cor_botoes="Transparente")
    cfg.salvar(dados, arquivo)
    restaurado = cfg.carregar(arquivo)
    assert restaurado["idioma"] == "en"
    assert restaurado["cor_botoes"] == "Transparente"

def test_idioma_e_cor_invalidos_voltam_ao_padrao():
    dados = cfg.validar({"idioma": "xx", "cor_botoes": "Inexistente"})
    assert dados["idioma"] == "pt"
    assert dados["cor_botoes"] == "Azul"
```

**Nota de sequência:** os seis testes anteriores correspondem à entrega parcial da Sprint 10. Estes dois testes adicionais são executados após a atualização de `configuracoes.py` na Parte III; o total esperado passa a **oito testes de configurações** (e, mantendo os 22 testes anteriores e dez personalizados, **40 testes no projeto**). Registre o resultado real.

### 5.4. Registrar a entrega da Sprint 10

Nesta etapa registraremos **somente o módulo `configuracoes.py`, seus testes e o documento de acompanhamento**. A janela General será integrada à `interface.py` na Parte III; portanto, a Sprint 10 ainda **não estará concluída**.

#### 5.4.1. Criar o documento da Sprint

Como a pasta `docs\sprints` já existe desde a Sprint 09, **não é necessário criá-la novamente**. Se `docs/sprints/sprint-10-general.md` **ainda não existir**, crie-o:

```powershell
New-Item -ItemType File -Path docs\sprints\sprint-10-general.md
code docs\sprints\sprint-10-general.md
```

Se já existir, **não o recrie nem apague seu conteúdo**: abra-o diretamente com `code docs\sprints\sprint-10-general.md`.

#### 5.4.2. Conteúdo completo de `docs/sprints/sprint-10-general.md`

Copie o modelo abaixo. As caixas ficam inicialmente desmarcadas; marque-as apenas após verificar cada atividade. Preencha os resultados reais, sem presumir que os testes passaram.

```markdown
# Sprint 10 — General e persistência JSON

**Projeto:** EngConvert — Conversor de Unidades de Engenharia  
**Etapa:** 10 — Interface Completa  
**Sprint:** 10 — General e persistência JSON  
**Branch:** `feature-interface-final`  
**Status:** Em andamento

## 1. Objetivo

Implementar preferências gerais do EngConvert e sua persistência em JSON, mantendo as funcionalidades da Sprint 09 e os cálculos de conversão existentes.

## 2. Funcionalidades previstas

- Seleção de tema: Sistema, Claro e Escuro.
- Precisão de exibição de 1 a 12 algarismos significativos.
- Opção de notação científica.
- Aviso para temperatura abaixo do zero absoluto, quando habilitado.
- Persistência de tema, favoritos, ordem, visibilidade e dimensões da interface.
- Gravação das preferências em pasta do usuário, fora do código-fonte.
- Recuperação de valores padrão para configurações ausentes ou inválidas.

## 3. Checklist de desenvolvimento

### Preparação

- [ ] Confirmar a branch `feature-interface-final`.
- [ ] Executar os testes existentes antes das modificações.
- [ ] Verificar a interface da Sprint 09.

### Módulo de configurações

- [ ] Criar `src/engconvert/configuracoes.py`.
- [ ] Implementar valores padrão e validação das preferências.
- [ ] Implementar leitura e gravação de JSON.
- [ ] Criar `tests/test_configuracoes.py`.
- [ ] Executar e registrar o resultado dos testes de configurações.
- [ ] Registrar em commit o módulo, os testes e este documento.

### Integração da interface — Parte III da Aula 10.2

- [ ] Integrar a janela General à `interface.py`.
- [ ] Verificar alteração e restauração do tema.
- [ ] Verificar precisão e notação científica.
- [ ] Verificar o aviso de zero absoluto.
- [ ] Verificar persistência de favoritos, ordem e visibilidade.
- [ ] Verificar persistência de dimensões e altura ajustável.
- [ ] Fechar e reabrir o aplicativo para confirmar a persistência.
- [ ] Verificar que as funcionalidades da Sprint 09 foram preservadas.

## 4. Critérios de aceitação

A Sprint 10 estará funcionalmente concluída quando as preferências forem validadas, gravadas e restauradas após reiniciar o EngConvert; a janela General funcionar; os testes automatizados pertinentes passarem; e a interface da Sprint 09 continuar operante.

## 5. Resultados e evidências

**Testes automatizados:** Pendente de execução/registro.  
**Testes manuais:** Pendentes da integração na Parte III.  
**Commit do módulo de persistência:** Pendente.  
**Pendências ou observações:** Preencher após as verificações.

## 6. Situação da Sprint

**Status:** Em andamento. A implementação da janela General e a validação integrada ocorrerão na Parte III da Aula 10.2.
```

#### 5.4.3. Executar os testes e conferir o Git

```powershell
python -m pytest tests/test_configuracoes.py -q
git status
git diff --check
```

Registre no documento o resultado observado. Se os testes falharem, corrija os problemas antes do commit.

#### 5.4.4. Registrar a entrega parcial

Depois de salvar o documento e confirmar os testes:

```powershell
git add src/engconvert/configuracoes.py tests/test_configuracoes.py docs/sprints/sprint-10-general.md
git diff --cached --check
git diff --cached --stat
git commit -m "feat: adiciona persistencia e validacao de preferencias"
git status
```

**Importante:** este commit documenta a **entrega parcial** da Sprint 10. Não marque a janela General como concluída nem altere o status da Sprint para "Concluída" antes de implementar e validar a interface na Parte III.

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
    if isinstance(fator, bool):
        raise ValueError('O fator deve ser numérico, não booleano.')
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

$
\text{valor}_{\text{destino}}=\text{valor}_{\text{origem}}\times\frac{\text{fator}_{\text{origem}}}{\text{fator}_{\text{destino}}}\
$

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

**Resultado esperado:** dez testes aprovados no conjunto apresentado. Incluem fatores zero, negativos, `nan`, `inf`, duplicatas, temperatura, persistência, exclusão e JSON inválido.

### 7.3. Registrar a entrega parcial da Sprint 11

Nesta etapa, registraremos o módulo de unidades personalizadas e seus testes. A janela **Custom** será integrada somente na Parte III; portanto, a Sprint 11 permanecerá **Em andamento**.

#### 7.3.1. Criar e abrir o documento da Sprint 11

No PowerShell, na raiz do projeto, a pasta `docs\sprints` já existe. Crie apenas o arquivo, se necessário:

```powershell
if (-not (Test-Path docs\sprints\sprint-11-custom.md)) {
    New-Item -ItemType File -Path docs\sprints\sprint-11-custom.md
}
code docs\sprints\sprint-11-custom.md
```

Se o documento já existir, os comandos **não apagam seu conteúdo**.

#### 7.3.2. Conteúdo completo de `docs/sprints/sprint-11-custom.md`

Copie o conteúdo abaixo. Marque cada caixa somente após verificar a atividade:

```markdown
# Sprint 11 — Unidades personalizadas (Custom)

**Projeto:** EngConvert — Conversor de Unidades de Engenharia

**Etapa:** 10 — Interface Completa

**Branch:** `feature-interface-final`

**Status:** Em andamento

## 1. Objetivo

Implementar cadastro, validação, exclusão, conversão e persistência em JSON de unidades multiplicativas personalizadas, preservando as unidades originais.

## 2. Escopo

- Grandezas permitidas: Pressão, Comprimento, Área e Volume.
- Fatores positivos, finitos e relativos a Pa, m, m² e m³.
- Proibição de nomes vazios, nomes duplicados e escalas de Temperatura.
- Arquivo de dados na pasta do usuário, fora do repositório.

## 3. Checklist

### Módulo e testes — Parte II

- [ ] Criar `src/engconvert/personalizadas.py`.
- [ ] Validar nomes e fatores de conversão.
- [ ] Impedir duplicatas e cadastro de Temperatura.
- [ ] Implementar adição, exclusão e persistência JSON.
- [ ] Criar `tests/test_personalizadas.py`.
- [ ] Executar os dez testes previstos e registrar o resultado real.
- [ ] Registrar o commit parcial do módulo, testes e documentação.

### Interface — Parte III

- [ ] Integrar a janela Custom à `interface.py`.
- [ ] Cadastrar uma unidade e utilizá-la em uma conversão.
- [ ] Confirmar persistência após fechar e reabrir o EngConvert.
- [ ] Excluir uma unidade personalizada sem afetar o catálogo original.
- [ ] Verificar mensagens para fatores inválidos e nomes duplicados.

## 4. Critérios de aceitação

A Sprint 11 será concluída quando o módulo e os testes funcionarem, a janela Custom permitir cadastro e exclusão, as unidades participarem corretamente das conversões e os dados persistirem após reiniciar o aplicativo.

## 5. Resultados e evidências

**Testes automatizados:** Pendente de registro.

**Testes manuais da interface:** Pendentes da Parte III.

**Commit parcial:** Pendente.

**Observações:** Preencher com os resultados efetivamente observados.

## 6. Situação

**Status:** Em andamento até a integração e validação manual da janela Custom.
```

#### 7.3.3. Executar os testes e conferir alterações

```powershell
python -m pytest tests/test_personalizadas.py -q
git status
git diff --check
```

Se os testes falharem, corrija-os antes do commit. Registre o resultado observado no documento.

#### 7.3.4. Registrar o commit parcial

```powershell
git add src/engconvert/personalizadas.py tests/test_personalizadas.py docs/sprints/sprint-11-custom.md
git diff --cached --check
git diff --cached --stat
git commit -m "feat: adiciona unidades personalizadas validadas"
git status
```

**Importante:** não marque a janela Custom como concluída antes de sua implementação e validação na Parte III.

---

**Atenção à sequência didática:** os commits das Sprints 10 e 11 registram primeiro os módulos e testes; os recursos visuais são integrados na Sprint 12. Por isso, não marque as interfaces General e Custom como concluídas nos commits intermediários. O aluno deverá registrar os testes de cada etapa e validar a GUI após a integração.

# PARTE III — SPRINT 12: ABOUT E INTERFACE INTEGRADA

## 8. Atualizar a interface sem perder a Sprint 09

A nova `interface.py` preserva a interface aprovada na Aula 10.1: cabeçalho compacto da janela Categorias, grade de botões, favoritos, fontes ampliadas, campo centralizado, resultado destacado, conversão com Enter, inversão, divisor arrastável e janela compacta. Acrescenta Configurações gerais, Unidades personalizadas, Sobre o EngConvert, idioma português/inglês, paleta de cores e persistência JSON. O tema passa a ser configurado nas Configurações gerais, não no início da janela.

**Procedimento:** abra `src/engconvert/interface.py` e substitua seu conteúdo pelo arquivo completo abaixo. Faça isso **somente após** confirmar que os testes dos módulos novos passaram. O Git permite recuperar a versão anterior.

**Observação didática:** apresentamos uma única versão final da interface para não exigir três substituições do mesmo arquivo. A separação entre Sprints é preservada nos módulos, testes, documentação e commits; a validação completa das três interfaces ocorrerá após esta integração.

**Arquivo:** `src/engconvert/interface.py`

```python

"""Interface integrada do EngConvert — Sprints 09 a 12."""
import tkinter as tk
import math
from tkinter import messagebox
import customtkinter as ctk
from .dados import lista_grandezas
from . import configuracoes as cfg
from . import personalizadas as pers

VERSAO = "0.1.0"

# Identificadores estáveis em JSON; somente os textos visíveis são traduzidos.
TEMAS = {"Sistema": "System", "Claro": "Light", "Escuro": "Dark"}
CORES = {
    "Azul": ("#3B8ED0", "#1F6AA5"),
    "Transparente": "transparent",
    "Cinza claro": ("#D1D5DB", "#6B7280"),
    "Verde": ("#409B78", "#287659"),
    "Laranja": ("#E69A42", "#B96B24"),
    "Vermelho": ("#CE6464", "#A34343"),
    "Roxo": ("#9474CB", "#7252A7"),
}
TRADUCOES = {
    "Arquivo": "File", "Opções": "Options", "Ajuda": "Help",
    "Copiar resultado": "Copy result", "Sair": "Exit", "Inverter unidades": "Swap units",
    "Categorias...": "Categories...", "Configurações gerais...": "General settings...",
    "Unidades personalizadas...": "Custom units...", "Sobre o EngConvert...": "About EngConvert...",
    "Configurações gerais": "General settings", "Unidades personalizadas": "Custom units",
    "Sobre o EngConvert": "About EngConvert", "Tema": "Theme",
    "Algarismos significativos (1 a 12)": "Significant digits (1 to 12)",
    "Notação científica": "Scientific notation", "Avisar sobre zero absoluto": "Warn about absolute zero",
    "Salvar": "Save", "Cancelar": "Cancel", "Fechar": "Close",
    "Grandeza": "Quantity", "Digite o valor": "Enter value", "Converter": "Convert",
    "RESULTADO DA CONVERSÃO": "CONVERSION RESULT", "Favoritas": "Favorites",
    "Todas as grandezas": "All quantities", "Nenhuma favorita visível.": "No visible favorites.",
    "arraste para ajustar a altura": "drag to adjust height",
    "Preferências — Categorias": "Preferences — Categories", "↑↓  Categoria": "↑↓  Category",
    "★ Favorito": "★ Favorite", "👁 Mostrar": "👁 Show", "Subir": "Up", "Descer": "Down",
    "Restaurar": "Restore", "Mantenha pelo menos uma categoria visível.": "Keep at least one category visible.",
    "Grandeza (exceto Temperatura)": "Quantity (except Temperature)",
    "Nome da unidade": "Unit name", "Fator em relação à referência SI": "Factor relative to SI reference",
    "Referências: Pa, m, m² e m³": "References: Pa, m, m² and m³",
    "Nenhuma unidade cadastrada": "No registered units", "Adicionar unidade": "Add unit",
    "Excluir unidade selecionada": "Delete selected unit", "Unidades personalizadas atualizadas.": "Custom units updated.",
    "Licença MIT": "MIT License", "Autor: Wilson Luciano": "Author: Wilson Luciano",
    "Projeto didático — Programação para Engenharia Mecânica": "Teaching project — Mechanical Engineering Programming",
    "Pressão": "Pressure", "Temperatura": "Temperature", "Comprimento": "Length",
    "Área": "Area", "Volume": "Volume", "Versão": "Version",
    "Sistema": "System", "Claro": "Light", "Escuro": "Dark",
    "Azul": "Blue", "Transparente": "Transparent", "Cinza claro": "Light gray",
    "Verde": "Green", "Laranja": "Orange", "Vermelho": "Red", "Roxo": "Purple",
    "Idioma": "Language", "Cor dos botões": "Button color",
}


def formatar_numero(valor, preferencias):
    p = preferencias["precisao"]
    return f"{valor:.{p}e}" if preferencias["cientifica"] else f"{valor:.{p}g}"


def iniciar_aplicacao():
    """Monta a janela e associa eventos aos controles."""
    preferencias = cfg.carregar()
    unidades_custom = pers.carregar()
    preferencias.setdefault("idioma", "pt")
    preferencias.setdefault("cor_botoes", "Azul")
    idioma = preferencias["idioma"] if preferencias["idioma"] in ("pt", "en") else "pt"
    def t(texto):
        return TRADUCOES.get(texto, texto) if idioma == "en" else texto
    def cat_exibida(nome):
        return t(nome)
    def cat_original(nome):
        return next((chave for chave in lista_grandezas if t(chave) == nome), nome)
    def estilo_botao():
        cor = preferencias.get("cor_botoes", "Azul")
        if cor not in CORES:
            cor = "Azul"
        # CTkButton requer a string literal "transparent" para retirar o preenchimento.
        # Uma tupla de cores transparentes pode não atualizar o desenho corretamente.
        fundo = "transparent" if cor == "Transparente" else CORES[cor]
        return dict(fg_color=fundo, hover_color=("#B9C5D0", "#4B5563") if cor == "Transparente" else
                                ("#B7C3D0", "#586675") if cor == "Cinza claro" else
                                CORES[cor][1],
                    border_width=1 if cor == "Transparente" else 0,
                    border_color=("#5B6570", "#AEB7C2"),
                    text_color=("#202020", "#F5F5F5") if cor == "Transparente" else
                               ("#202020", "#FFFFFF") if cor == "Cinza claro" else ("#FFFFFF", "#FFFFFF"))
    # Controles de seleção também seguem a paleta, não apenas CTkButton.
    controles_coloridos = []
    linhas_selecionadas = []

    def paleta_selecao():
        nome = preferencias.get("cor_botoes", "Azul")
        if nome not in CORES:
            nome = "Azul"
        if nome == "Transparente":
            # Para caixas de seleção e menus, usar fundo neutro e contorno.
            return ("#E5E7EB", "#374151"), ("#D1D5DB", "#4B5563"), ("#5B6570", "#AEB7C2")
        base = CORES[nome]
        return base, (base[1], base[1]), base

    def colorir_controle(widget, tipo):
        principal, hover, contorno = paleta_selecao()
        if tipo == "opcao":
            widget.configure(fg_color=principal, button_color=principal,
                             button_hover_color=hover,
                             text_color=("#202020", "#FFFFFF") if preferencias.get("cor_botoes") == "Transparente" else
                                        ("#202020", "#FFFFFF") if preferencias.get("cor_botoes") == "Cinza claro" else
                                        ("#FFFFFF", "#FFFFFF"))
        elif tipo == "checkbox":
            if preferencias.get("cor_botoes") == "Transparente":
                # O fundo da caixa marcada precisa contrastar com o simbolo ✓.
                # Aplicado a General e aos campos Favorito/Mostrar em Categorias.
                widget.configure(
                    fg_color=("#4B5563", "#D1D5DB"),
                    hover_color=("#374151", "#B8C0CA"),
                    border_color=("#5B6570", "#AEB7C2"),
                    checkmark_color=("#FFFFFF", "#202020"),
                )
            else:
                widget.configure(
                    fg_color=principal, hover_color=hover,
                    border_color=contorno,
                    checkmark_color=("#202020", "#FFFFFF") if preferencias.get("cor_botoes") == "Cinza claro" else "#FFFFFF",
                )
        elif tipo == "radio":
            if preferencias.get("cor_botoes") == "Transparente":
                widget.configure(
                    fg_color=("#4B5563", "#D1D5DB"),
                    hover_color=("#374151", "#B8C0CA"),
                    border_color=("#5B6570", "#AEB7C2"),
                )
            else:
                widget.configure(fg_color=principal, hover_color=hover,
                                 border_color=contorno)
        elif tipo == "abas":
            # Ambas as abas precisam manter o texto legível, inclusive a inativa.
            # O CTkTabview usa internamente um CTkSegmentedButton.
            if preferencias.get("cor_botoes") == "Transparente":
                widget._segmented_button.configure(
                    fg_color=("#D9DDE2", "#40464F"),
                    selected_color=("#C4CBD3", "#58616D"),
                    unselected_color=("#E5E7EB", "#343A40"),
                    selected_hover_color=("#BFC5CD", "#596575"),
                    unselected_hover_color=("#E5E7EB", "#374151"),
                    text_color=("#202020", "#FFFFFF"),
                )
            else:
                widget._segmented_button.configure(
                    selected_color=principal,
                    unselected_color=("#D1D5DB", "#4B5563"),
                    selected_hover_color=hover,
                    unselected_hover_color=("#BFC5CD", "#596575"),
                    text_color=("#202020", "#FFFFFF") if preferencias.get("cor_botoes") == "Cinza claro" else ("#FFFFFF", "#FFFFFF"),
                )

    def registrar_controle(widget, tipo):
        controles_coloridos.append((widget, tipo))
        colorir_controle(widget, tipo)
        return widget

    def cor_linha_selecionada():
        nome = preferencias.get("cor_botoes", "Azul")
        if nome == "Transparente":
            return ("#E5E7EB", "#374151")
        if nome == "Cinza claro":
            return ("#E5E7EB", "#4B5563")
        return CORES.get(nome, CORES["Azul"])

    def estilo_resultado():
        nome = preferencias.get("cor_botoes", "Azul")
        if nome == "Transparente":
            return (("#ECEFF1", "#343A40"), ("#364152", "#E5E7EB"),
                    ("#202020", "#FFFFFF"))
        if nome == "Cinza claro":
            return (("#E5E7EB", "#4B5563"), ("#374151", "#F9FAFB"),
                    ("#202020", "#FFFFFF"))
        base = CORES.get(nome, CORES["Azul"])
        return (base, ("#FFFFFF", "#FFFFFF"), ("#FFFFFF", "#FFFFFF"))

    def atualizar_estilo_resultado():
        fundo, titulo_cor, valor_cor = estilo_resultado()
        painel_resultado.configure(fg_color=fundo)
        rotulo_resultado.configure(text_color=titulo_cor)
        resultado.configure(text_color=valor_cor)

    def atualizar_paleta_completa():
        for controle in botoes:
            if controle.winfo_exists():
                controle.configure(**estilo_botao())
        for controle, tipo in controles_coloridos:
            if controle.winfo_exists():
                colorir_controle(controle, tipo)
        for linha in linhas_selecionadas:
            if linha.winfo_exists():
                linha.configure(fg_color=cor_linha_selecionada())
        atualizar_estilo_resultado()

    botoes = []
    def botao(pai, **kwargs):
        kwargs.setdefault("text", "")
        kwargs["text"] = t(kwargs["text"])
        widget = ctk.CTkButton(pai, **kwargs)
        botoes.append(widget)
        widget.configure(**{k:v for k,v in estilo_botao().items() if v is not None})
        return widget
    ctk.set_appearance_mode(preferencias["tema"])
    ctk.set_default_color_theme("blue")
    reiniciar = {"necessario": False}
    app = ctk.CTk()
    app.title(f"EngConvert — v{VERSAO}")
    # Dimensão inicial padronizada da janela principal.
    # Não restaura dimensões antigas do JSON: uma janela maximizada ou
    # ampliada anteriormente não deve ocupar a tela na próxima abertura.
    largura_tela = app.winfo_screenwidth()
    altura_tela = app.winfo_screenheight()
    largura_inicial = min(790, max(420, largura_tela - 60))
    altura_inicial = min(620, max(420, altura_tela - 140))
    pos_x = max(0, (largura_tela - largura_inicial) // 2)
    pos_y = 20
    app.geometry(f"{largura_inicial}x{altura_inicial}+{pos_x}+{pos_y}")
    app.minsize(min(580, largura_inicial), min(520, altura_inicial))

    # Estado restaurado do JSON, com validação em configuracoes.py.
    ordem = list(preferencias["ordem"])
    visiveis = list(preferencias["visiveis"])
    favoritas = list(preferencias["favoritas"])
    colunas_grade = 3

    def persistir():
        preferencias.update(ordem=list(ordem), visiveis=list(visiveis),
                           favoritas=list(favoritas),
                           altura_categorias=int(painel_navegacao.winfo_height()))
        try:
            cfg.salvar(preferencias)
            return True
        except OSError as erro:
            messagebox.showerror("EngConvert", f"Falha ao salvar preferências: {erro}", parent=app)
            return False

    def categorias_disponiveis():
        return [nome for nome in ordem if nome in visiveis]

    def atualizar_unidades(_=None):
        unidades = pers.unidades_disponiveis(cat_original(combo_grandeza.get()), unidades_custom)
        combo_de.configure(values=unidades)
        combo_para.configure(values=unidades)
        combo_de.set(unidades[0])
        combo_para.set(unidades[1] if len(unidades) > 1 else unidades[0])
        resultado.configure(text=t("—"), text_color=("#1769aa", "#8ac7ff"))

    def selecionar_grandeza(nome):
        if nome not in categorias_disponiveis():
            return
        combo_grandeza.set(cat_exibida(nome))
        atualizar_unidades()

    def atualizar_navegacao():
        disponiveis = categorias_disponiveis()
        if not disponiveis:
            # Uma categoria deve permanecer visível para evitar estado vazio.
            visiveis.append(ordem[0])
            disponiveis = categorias_disponiveis()
        combo_grandeza.configure(values=[cat_exibida(n) for n in disponiveis])
        if cat_original(combo_grandeza.get()) not in disponiveis:
            combo_grandeza.set(cat_exibida(disponiveis[0]))
            atualizar_unidades()
        for quadro in (quadro_favoritas, quadro_todas):
            for widget in quadro.winfo_children():
                widget.destroy()

        def montar_grade(quadro, nomes):
            for coluna in range(colunas_grade):
                quadro.grid_columnconfigure(coluna, weight=1, uniform="categorias")
            for indice, nome in enumerate(nomes):
                linha, coluna = divmod(indice, colunas_grade)
                botao(
                    quadro, text=cat_exibida(nome), height=34,
                    command=lambda n=nome: selecionar_grandeza(n)
                ).grid(row=linha, column=coluna, padx=5, pady=5, sticky="ew")

        fav = [nome for nome in disponiveis if nome in favoritas]
        if not fav:
            ctk.CTkLabel(quadro_favoritas, text=t("Nenhuma favorita visível.")).grid(
                row=0, column=0, padx=10, pady=15
            )
        else:
            montar_grade(quadro_favoritas, fav)
        montar_grade(quadro_todas, disponiveis)

    def abrir_categorias():
        janela = ctk.CTkToplevel(app)
        janela.title(t("Preferências — Categorias"))
        janela.geometry("470x520")
        janela.transient(app)
        # Cópias: cancelar fecha sem alterar o estado ativo.
        ordem_temp = list(ordem)
        visiveis_temp = list(visiveis)
        favoritas_temp = list(favoritas)
        selecionada = ctk.StringVar(value=ordem_temp[0])
        # Cabeçalho autoexplicativo: ordenação, favoritos e visibilidade.
        # Dispensa os dois cartões de instruções e libera espaço vertical.
        titulos = ctk.CTkFrame(janela, fg_color="transparent")
        titulos.pack(fill="x", padx=22, pady=(12, 0))
        titulos.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(
            titulos, text=t("↑↓  Categoria"), anchor="w",
            font=ctk.CTkFont(size=13, weight="bold")
        ).grid(row=0, column=0, sticky="w", padx=(4, 0))
        ctk.CTkLabel(
            titulos, text=t("★ Favorito"), width=90,
            font=ctk.CTkFont(size=12, weight="bold")
        ).grid(row=0, column=1, padx=0)
        ctk.CTkLabel(
            titulos, text=t("👁 Mostrar"), width=82,
            font=ctk.CTkFont(size=12, weight="bold")
        ).grid(row=0, column=2, padx=(0, 6))
        lista = ctk.CTkScrollableFrame(janela, height=300)
        lista.pack(fill="both", expand=True, padx=18, pady=(5, 12))

        def desenhar():
            for widget in lista.winfo_children():
                widget.destroy()
            for nome in ordem_temp:
                linha = ctk.CTkFrame(lista, fg_color=("transparent"))
                linha.pack(fill="x", pady=2)
                linha.grid_columnconfigure(0, weight=1)

                def destacar(n=nome):
                    selecionada.set(n)
                    desenhar()

                registrar_controle(ctk.CTkRadioButton(
                    linha, text=cat_exibida(nome), variable=selecionada, value=nome,
                    command=destacar, width=150
                ), "radio").grid(row=0, column=0, sticky="w", padx=(4, 2), pady=4)
                if selecionada.get() == nome:
                    linha.configure(fg_color=cor_linha_selecionada())
                    linhas_selecionadas.append(linha)

                mostrar_var = ctk.BooleanVar(value=nome in visiveis_temp)
                favorito_var = ctk.BooleanVar(value=nome in favoritas_temp)

                def alterar_mostrar(n=nome, v=mostrar_var):
                    if v.get():
                        if n not in visiveis_temp:
                            visiveis_temp.append(n)
                    else:
                        if n in visiveis_temp:
                            visiveis_temp.remove(n)
                        if n in favoritas_temp:
                            favoritas_temp.remove(n)
                        desenhar()

                def alterar_favorito(n=nome, v=favorito_var):
                    if v.get() and n in visiveis_temp:
                        if n not in favoritas_temp:
                            favoritas_temp.append(n)
                    elif n in favoritas_temp:
                        favoritas_temp.remove(n)

                registrar_controle(ctk.CTkCheckBox(
                    linha, text=t(""), variable=favorito_var, width=28,
                    state="normal" if nome in visiveis_temp else "disabled",
                    command=alterar_favorito
                ), "checkbox").grid(row=0, column=1, padx=(4, 34), sticky="e")
                registrar_controle(ctk.CTkCheckBox(
                    linha, text=t(""), variable=mostrar_var, width=28,
                    command=alterar_mostrar
                ), "checkbox").grid(row=0, column=2, padx=(0, 20), sticky="e")

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
            favoritas_temp[:] = ["Pressão", "Temperatura"]
            selecionada.set(ordem_temp[0])
            desenhar()

        def salvar():
            if not visiveis_temp:
                aviso.configure(text=t("Mantenha pelo menos uma categoria visível."))
                return
            ordem[:] = ordem_temp
            visiveis[:] = visiveis_temp
            favoritas[:] = [n for n in favoritas_temp if n in visiveis_temp]
            atualizar_navegacao()
            if persistir():
                janela.destroy()

        desenhar()
        comandos = ctk.CTkFrame(janela)
        comandos.pack(padx=15, pady=4)
        botao(comandos, text=t("Subir"), width=75, command=lambda: mover(-1)).pack(side="left", padx=3)
        botao(comandos, text=t("Descer"), width=75, command=lambda: mover(1)).pack(side="left", padx=3)
        botao(comandos, text=t("Restaurar"), width=90, command=restaurar).pack(side="left", padx=3)
        aviso = ctk.CTkLabel(janela, text=t(""))
        aviso.pack()
        rodape = ctk.CTkFrame(janela, fg_color="transparent")
        rodape.pack(pady=8)
        botao(rodape, text=t("Salvar"), command=salvar).pack(side="left", padx=5)
        botao(rodape, text=t("Cancelar"), command=janela.destroy).pack(side="left", padx=5)
        janela.grab_set()

    def inverter_unidades():
        de, para = combo_de.get(), combo_para.get()
        combo_de.set(para)
        combo_para.set(de)
        # O resultado anterior pertence à direção de conversão antiga.
        resultado.configure(text=t("—"), text_color=("#1769aa", "#8ac7ff"))

    def ao_converter():
        try:
            valor = float(entrada.get().strip().replace(",", "."))
            if not math.isfinite(valor):
                raise ValueError("Informe um número finito.")
            categoria = cat_original(combo_grandeza.get())
            convertido = pers.converter(valor, categoria, combo_de.get(), combo_para.get(), unidades_custom)
            if categoria == "Temperatura" and preferencias["avisar_zero_absoluto"]:
                kelvin = pers.converter(valor, "Temperatura", combo_de.get(), "K", unidades_custom)
                if kelvin < -1e-9:
                    resultado.configure(text=t("Temperature below absolute zero." if idioma == "en" else "Temperatura abaixo do zero absoluto."),
                                        text_color=("#b42318", "#ff9c94"))
                    return
            if not math.isfinite(convertido):
                raise ValueError("Resultado não finito.")
            resultado.configure(text=f"{formatar_numero(convertido, preferencias)} {combo_para.get()}",
                                text_color=("#1769aa", "#8ac7ff"))
        except (ValueError, KeyError, ZeroDivisionError):
            resultado.configure(text=t("Check the value and selected units." if idioma == "en" else "Verifique o valor e as unidades selecionadas."),
                                text_color=("#b42318", "#ff9c94"))


    def abrir_general():
        janela = ctk.CTkToplevel(app)
        janela.title(t("Configurações gerais"))
        janela.geometry("440x580")
        janela.transient(app)
        janela.resizable(False, False)
        ctk.CTkLabel(janela, text="Idioma / Language").pack(pady=(14, 3))
        idiomas = {"Português": "pt", "English": "en"}
        idioma_menu = registrar_controle(ctk.CTkOptionMenu(janela, values=list(idiomas)), "opcao")
        idioma_menu.set("English" if idioma == "en" else "Português")
        idioma_menu.pack()
        ctk.CTkLabel(janela, text=t("Tema")).pack(pady=(12, 3))
        nomes_temas = list(TEMAS)
        tema = registrar_controle(ctk.CTkOptionMenu(janela, values=[t(n) for n in nomes_temas]), "opcao")
        tema.set(t(next((n for n,v in TEMAS.items() if v == preferencias["tema"]), "Sistema")))
        tema.pack()
        ctk.CTkLabel(janela, text=t("Cor dos botões")).pack(pady=(12, 3))
        cor = registrar_controle(ctk.CTkOptionMenu(janela, values=[t(n) for n in CORES]), "opcao")
        cor.set(t(preferencias.get("cor_botoes", "Azul")))
        cor.pack()
        ctk.CTkLabel(janela, text=t("Algarismos significativos (1 a 12)")).pack(pady=(12, 3))
        precisao = ctk.CTkEntry(janela, width=150)
        precisao.insert(0, str(preferencias["precisao"]))
        precisao.pack()
        cientifica = ctk.BooleanVar(value=preferencias["cientifica"])
        zero = ctk.BooleanVar(value=preferencias["avisar_zero_absoluto"])
        registrar_controle(ctk.CTkCheckBox(janela, text=t("Notação científica"), variable=cientifica), "checkbox").pack(pady=12)
        registrar_controle(ctk.CTkCheckBox(janela, text=t("Avisar sobre zero absoluto"), variable=zero), "checkbox").pack(pady=8)
        aviso = ctk.CTkLabel(janela, text="")
        aviso.pack()

        def salvar():
            try:
                n = int(precisao.get())
                if not 1 <= n <= 12:
                    raise ValueError
            except ValueError:
                aviso.configure(text="Enter an integer from 1 to 12." if idioma == "en" else "Informe um inteiro entre 1 e 12.")
                return
            anterior = preferencias.copy()
            tema_interno = TEMAS[next(n for n in nomes_temas if t(n) == tema.get())]
            cor_interna = next(n for n in CORES if t(n) == cor.get())
            preferencias.update(tema=tema_interno, precisao=n, cientifica=cientifica.get(),
                                avisar_zero_absoluto=zero.get(), idioma=idiomas[idioma_menu.get()],
                                cor_botoes=cor_interna)
            if persistir():
                ctk.set_appearance_mode(preferencias["tema"])
                atualizar_paleta_completa()
                janela.destroy()
                if preferencias["idioma"] != idioma:
                    # Reinicia apenas a GUI para atualizar menus, rótulos e categorias.
                    reiniciar["necessario"] = True
                    app.after(50, app.destroy)
            else:
                preferencias.clear()
                preferencias.update(anterior)

        botao(janela, text="Salvar", command=salvar).pack(pady=8)
        botao(janela, text="Cancelar", command=janela.destroy).pack(pady=3)
        janela.grab_set()

    def abrir_custom():
        nonlocal unidades_custom
        janela = ctk.CTkToplevel(app)
        janela.title(t("Unidades personalizadas"))
        janela.geometry("500x540")
        janela.transient(app)
        ctk.CTkLabel(janela, text=t("Grandeza (exceto Temperatura)")).pack(pady=(12, 3))
        categoria = registrar_controle(ctk.CTkOptionMenu(janela, values=[cat_exibida(n) for n in pers.grandezas]), "opcao")
        categoria.pack()
        ctk.CTkLabel(janela, text=t("Nome da unidade")).pack(pady=(10, 3))
        nome = ctk.CTkEntry(janela, width=260, placeholder_text=t("Ex.: duplo_metro"))
        nome.pack()
        ctk.CTkLabel(janela, text=t("Fator em relação à referência SI")).pack(pady=(10, 3))
        fator = ctk.CTkEntry(janela, width=260, placeholder_text=t("Ex.: 2"))
        fator.pack()
        ctk.CTkLabel(janela, text=t("Referências: Pa, m, m² e m³"), wraplength=430).pack(pady=6)
        lista = registrar_controle(ctk.CTkOptionMenu(janela, values=["Nenhuma unidade cadastrada"]), "opcao")
        lista.pack(pady=5)
        aviso = ctk.CTkLabel(janela, text=t(""), wraplength=450)
        aviso.pack(pady=5)

        def atualizar_lista(_=None):
            nomes = list(unidades_custom.get(cat_original(categoria.get()), {}))
            opcoes = nomes or ["Nenhuma unidade cadastrada"]
            lista.configure(values=opcoes)
            lista.set(opcoes[0])

        def gravar(novas):
            nonlocal unidades_custom
            try:
                pers.salvar(novas)
            except (OSError, ValueError) as erro:
                aviso.configure(text=f"Falha ao salvar: {erro}")
                return
            unidades_custom = novas
            atualizar_lista()
            atualizar_unidades()
            aviso.configure(text=t("Unidades personalizadas atualizadas."))

        def adicionar():
            try:
                novas = pers.adicionar(unidades_custom, cat_original(categoria.get()), nome.get(), fator.get())
            except (ValueError, TypeError) as erro:
                aviso.configure(text=str(erro))
                return
            gravar(novas)

        def excluir():
            try:
                novas = pers.excluir(unidades_custom, cat_original(categoria.get()), lista.get())
            except ValueError as erro:
                aviso.configure(text=str(erro))
                return
            gravar(novas)

        categoria.configure(command=atualizar_lista)
        atualizar_lista()
        botao(janela, text=t("Adicionar unidade"), command=adicionar).pack(pady=6)
        botao(janela, text=t("Excluir unidade selecionada"), command=excluir).pack(pady=5)
        botao(janela, text=t("Fechar"), command=janela.destroy).pack(pady=5)
        janela.grab_set()

    def abrir_about():
        janela = ctk.CTkToplevel(app)
        janela.title(t("Sobre o EngConvert"))
        janela.geometry("440x300")
        janela.transient(app)
        ctk.CTkLabel(janela, text=t("EngConvert"), font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(22, 8))
        ctk.CTkLabel(janela, text=f"{t('Versão')} {VERSAO} | Python + CustomTkinter").pack(pady=5)
        ctk.CTkLabel(janela, text=t("Autor: Wilson Luciano")).pack(pady=5)
        ctk.CTkLabel(janela, text=t("Projeto didático — Programação para Engenharia Mecânica")).pack(pady=5)
        ctk.CTkLabel(janela, text=t("Licença MIT")).pack(pady=5)
        botao(janela, text=t("Fechar"), command=janela.destroy).pack(pady=14)
        janela.grab_set()

    cabecalho = ctk.CTkFrame(app)
    cabecalho.pack(fill="x", padx=22, pady=(10, 7))
    ctk.CTkLabel(cabecalho, text=t("EngConvert"), font=("Arial", 26, "bold")).pack(
        side="left", padx=15, pady=10
    )
    # Barra de menus nativa: mantém a tela principal dedicada à conversão.
    # O tema é configurado exclusivamente em Opções > Configurações gerais.
    def copiar_resultado():
        texto = resultado.cget("text")
        if not texto or texto == "—" or texto.startswith(("Verifique", "Temperatura abaixo")):
            messagebox.showinfo("EngConvert", "Perform a valid conversion before copying." if idioma == "en" else "Faça uma conversão válida antes de copiar.", parent=app)
            return
        app.clipboard_clear()
        app.clipboard_append(texto)
        app.update_idletasks()

    barra_menus = tk.Menu(app)
    menu_arquivo = tk.Menu(barra_menus, tearoff=False)
    menu_arquivo.add_command(label=t("Copiar resultado"), command=copiar_resultado)
    menu_arquivo.add_separator()
    menu_arquivo.add_command(label=t("Sair"), command=lambda: ao_fechar())
    barra_menus.add_cascade(label=t("Arquivo"), menu=menu_arquivo)

    menu_opcoes = tk.Menu(barra_menus, tearoff=False)
    menu_opcoes.add_command(label=t("Inverter unidades"), command=inverter_unidades)
    menu_opcoes.add_command(label=t("Categorias..."), command=abrir_categorias)
    menu_opcoes.add_separator()
    menu_opcoes.add_command(label=t("Configurações gerais..."), command=abrir_general)
    menu_opcoes.add_command(label=t("Unidades personalizadas..."), command=abrir_custom)
    barra_menus.add_cascade(label=t("Opções"), menu=menu_opcoes)

    menu_ajuda = tk.Menu(barra_menus, tearoff=False)
    menu_ajuda.add_command(label=t("Sobre o EngConvert..."), command=abrir_about)
    barra_menus.add_cascade(label=t("Ajuda"), menu=menu_ajuda)
    app.configure(menu=barra_menus)

    # Altura da navegação restaurada das preferências.
    ALTURA_INICIAL = preferencias["altura_categorias"]
    ALTURA_MINIMA = 100
    ALTURA_MAXIMA = 320
    ALTURA_MINIMA_CONVERSOR = 350

    painel_navegacao = ctk.CTkFrame(app, height=min(ALTURA_INICIAL, max(100, altura_inicial - 470)))
    painel_navegacao.pack(fill="x", padx=22, pady=(2, 0))
    painel_navegacao.pack_propagate(False)

    abas = registrar_controle(ctk.CTkTabview(painel_navegacao), "abas")
    abas.pack(fill="both", expand=True, padx=12, pady=(7, 5))
    aba_favoritas = abas.add(t("Favoritas"))
    aba_todas = abas.add(t("Todas as grandezas"))
    quadro_favoritas = ctk.CTkScrollableFrame(aba_favoritas)
    quadro_favoritas.pack(fill="both", expand=True, padx=4, pady=4)
    quadro_todas = ctk.CTkScrollableFrame(aba_todas)
    quadro_todas.pack(fill="both", expand=True, padx=4, pady=4)

    # O divisor fica imediatamente abaixo do painel de categorias.
    # Arrastar para cima libera espaço para o resultado da conversão.
    divisor = ctk.CTkFrame(app, height=18, fg_color="transparent")
    divisor.pack(fill="x", padx=22, pady=(0, 1))
    divisor.pack_propagate(False)
    pega = ctk.CTkLabel(
        divisor, text=t("━━  arraste para ajustar a altura  ━━"),
        height=16, font=ctk.CTkFont(size=11),
        text_color=("#687988", "#aab8c5")
    )
    pega.pack(fill="both", expand=True)

    corpo = ctk.CTkFrame(app)
    corpo.pack(fill="both", expand=True, padx=22, pady=(0, 6))

    arraste = {"inicio_y": 0, "altura_inicial": ALTURA_INICIAL}

    def limite_altura():
        # Calcula o espaço efetivamente disponível após a montagem da janela.
        # Nunca permite que o divisor esconda o formulário e o resultado.
        altura_total = app.winfo_height()
        outros = (cabecalho.winfo_height() + divisor.winfo_height() + 36)
        limite = altura_total - outros - ALTURA_MINIMA_CONVERSOR
        return max(ALTURA_MINIMA, min(ALTURA_MAXIMA, limite))

    def iniciar_arraste(event):
        arraste["inicio_y"] = event.y_root
        arraste["altura_inicial"] = painel_navegacao.winfo_height()

    def mover_divisor(event):
        nova = arraste["altura_inicial"] + event.y_root - arraste["inicio_y"]
        nova = max(ALTURA_MINIMA, min(limite_altura(), nova))
        painel_navegacao.configure(height=int(nova))

    def ao_redimensionar(event):
        if event.widget is app:
            altura = painel_navegacao.winfo_height()
            limite = limite_altura()
            if altura > limite:
                painel_navegacao.configure(height=limite)

    for controle in (divisor, pega):
        controle.bind("<ButtonRelease-1>", lambda event: persistir())
        controle.bind("<ButtonPress-1>", iniciar_arraste)
        controle.bind("<B1-Motion>", mover_divisor)
    app.bind("<Configure>", ao_redimensionar, add="+")

    ctk.CTkLabel(corpo, text=t("Grandeza"), font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(7, 3))
    combo_grandeza = ctk.CTkComboBox(
        corpo, values=[cat_exibida(n) for n in ordem], width=270, height=40,
        font=ctk.CTkFont(size=20), dropdown_font=ctk.CTkFont(size=17),
        command=atualizar_unidades, state="readonly"
    )
    combo_grandeza.pack()
    combo_grandeza.set(cat_exibida("Pressão"))
    linha = ctk.CTkFrame(corpo, fg_color="transparent")
    linha.pack(pady=6)
    combo_de = ctk.CTkComboBox(
        linha, width=155, height=40, state="readonly",
        font=ctk.CTkFont(size=20), dropdown_font=ctk.CTkFont(size=17)
    )
    combo_de.pack(side="left", padx=8)
    botao(
        linha, text=t("↔"), width=46, height=40,
        font=ctk.CTkFont(size=21), command=inverter_unidades
    ).pack(side="left", padx=4)
    combo_para = ctk.CTkComboBox(
        linha, width=155, height=40, state="readonly",
        font=ctk.CTkFont(size=20), dropdown_font=ctk.CTkFont(size=17)
    )
    combo_para.pack(side="left", padx=8)
    entrada = ctk.CTkEntry(
        corpo, width=240, height=42, placeholder_text=t("Digite o valor"),
        font=ctk.CTkFont(size=21), justify="center"
    )
    entrada.pack(pady=3)
    botao(
        corpo, text=t("Converter"), width=175, height=40,
        font=ctk.CTkFont(size=18), command=ao_converter
    ).pack(pady=5)
    painel_resultado = ctk.CTkFrame(
        corpo, fg_color=("#e3f0fa", "#264b69"), corner_radius=10
    )
    painel_resultado.pack(fill="x", padx=24, pady=(2, 4))
    rotulo_resultado = ctk.CTkLabel(
        painel_resultado, text=t("RESULTADO DA CONVERSÃO"),
        font=ctk.CTkFont(size=11, weight="bold"),
        text_color=("#476a86", "#c4d8ec")
    )
    rotulo_resultado.pack(pady=(5, 0))
    resultado = ctk.CTkLabel(
        painel_resultado, text=t("—"), font=ctk.CTkFont(size=24, weight="bold"),
        wraplength=520, text_color=("#1769aa", "#8ac7ff")
    )
    resultado.pack(pady=(0, 5))
    atualizar_estilo_resultado()
    atualizar_unidades()
    atualizar_navegacao()

    # Permite digitar o valor imediatamente ao abrir a aplicação.
    entrada.focus_set()
    # Enter e o botão Converter chamam a mesma função.
    app.bind("<Return>", lambda event: ao_converter())

    # Após o gerenciador de janelas aplicar DPI e decorações, verifica a
    # geometria efetiva. Se necessário, reduz e reposiciona a janela.
    def ajustar_apos_abrir():
        app.update_idletasks()
        margem_inferior = 100
        limite_inferior = app.winfo_screenheight() - margem_inferior
        topo = app.winfo_rooty()
        altura = app.winfo_height()
        if topo + altura > limite_inferior:
            nova_altura = max(440, limite_inferior - topo - 12)
            if nova_altura < altura:
                app.geometry(f"{app.winfo_width()}x{nova_altura}+{app.winfo_x()}+{app.winfo_y()}")
        # Em monitores menores, libera ainda mais espaço para o resultado.
        if app.winfo_height() < 590:
            painel_navegacao.configure(height=100)

    app.after(150, ajustar_apos_abrir)

    def ao_fechar():
        preferencias["largura_janela"] = app.winfo_width()
        preferencias["altura_janela"] = app.winfo_height()
        persistir()
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", ao_fechar)
    app.mainloop()
    if reiniciar["necessario"]:
        iniciar_aplicacao()
```

### 8.1. Arquivos existentes que não devem ser alterados

Os seguintes arquivos permanecem com o conteúdo aprovado nas Aulas 08.1 e 10.1: `src/engconvert/dados.py`, `src/engconvert/conversoes.py`, `main.py`, `pyproject.toml` e `tests/test_conversoes.py`. **O `pyproject.toml` deve manter o conteúdo completo da Aula 10.1 congelada**, incluindo autor, descrição, licença MIT e URL do repositório. O aluno deve preservá-los. Para consulta e conferência, seus conteúdos completos são reproduzidos no Anexo A, ao final da aula.

## 9. Executar a versão integrada

```powershell
python -m pytest -q
python main.py
```

**Referência didática:** o conjunto anterior previa 22 testes preexistentes, seis testes iniciais de configurações e dez testes de unidades personalizadas (38 no total). Com os dois testes adicionais da Seção 5.3.2, o total esperado passa a 40; registre o resultado real no computador do aluno. No computador do aluno, repita `python -m pytest -q` e registre o resultado real. **Esses testes não substituem a validação visual e manual da GUI no Windows.**

### 9.1. Verificações manuais obrigatórias

1. Abra **Configurações gerais**, selecione **Escuro**, precisão `8` e notação científica; salve. Feche e reabra o aplicativo: as preferências devem permanecer.
2. Volte ao tema **Sistema** ou **Claro**, se desejar. Teste `1 bar → 100 kPa` e confira o formato numérico.
3. Em **Configurações gerais**, mantenha o aviso de zero absoluto ativo. Selecione Temperatura e tente converter `-300 °C` para K: deve surgir um aviso, sem apresentar um resultado físico inválido.
4. Abra **Unidades personalizadas** e cadastre `duplo_metro` em Comprimento com fator `2`. Converta `3 duplo_metro` para `m`: resultado esperado `6 m`.
5. Feche e reabra o aplicativo; a unidade personalizada deve continuar disponível.
6. Tente cadastrar fator `0`, negativo e `nan`: devem ser rejeitados. Tente cadastrar `bar` em Pressão: deve ser rejeitado como duplicata.
7. Exclua `duplo_metro` e confirme que ela deixa de aparecer. As unidades originais permanecem intactas.
8. Em **Categorias**, oculte Área, altere a ordem, marque favoritos e salve. Reinicie: ordem, visibilidade e favoritos devem ser restaurados.
9. Abra **Sobre o EngConvert** e confira versão, autoria, tecnologias e informações de créditos.
10. Confirme que a janela permanece compacta e utilizável na escala de exibição do Windows do laboratório. Arraste o divisor, feche e reabra: a altura do painel deverá ser restaurada dentro do limite disponível. A largura e a altura da janela principal não são restauradas do JSON.
11. Em **Configurações gerais**, alterne **Português** e **English**; confirme tradução dos menus, rótulos e categorias e persistência após reabrir.
12. Teste as sete cores da paleta; em **Transparente**, confira o texto das duas abas, opções de tema/idioma/cor, símbolos ✓ em Notação científica, Zero absoluto, Favorito e Mostrar, e os controles circulares.
13. Verifique se o fundo do painel **Resultado da conversão** acompanha a cor selecionada, mantendo leitura adequada nos temas claro e escuro.

**Limitação conhecida:** os testes automatizados desta aula validam cálculo, JSON e regras de cadastro, **não automatizam cliques de GUI**. A inspeção manual acima é indispensável. O cadastro não inclui edição direta de fator: para alterá-lo, exclua e cadastre novamente.

### 9.2. Criar o documento de acompanhamento da Sprint 12

Após integrar `interface.py` e executar as verificações iniciais, crie o documento da Sprint 12. Seu checklist só deverá ser marcado à medida que cada item for comprovado.

#### 9.2.1. Criar e abrir o arquivo

A pasta `docs\sprints` já existe. Não a recrie; crie apenas o documento se estiver ausente.

```powershell
if (-not (Test-Path docs\sprints\sprint-12-about.md)) {
    New-Item -ItemType File -Path docs\sprints\sprint-12-about.md
}
code docs\sprints\sprint-12-about.md
```

#### 9.2.2. Conteúdo completo de `docs/sprints/sprint-12-about.md`

```markdown
# Sprint 12 — About e integração final

**Projeto:** EngConvert — Conversor de Unidades de Engenharia

**Etapa:** 10 — Interface Completa

**Branch:** `feature-interface-final`

**Status:** Em andamento

## 1. Objetivo

Integrar as funcionalidades General, Custom e About à interface aprovada na Sprint 09, preservando navegação, cálculos e preferências, e validar a aplicação antes da Aula 11.

## 2. Entregas previstas

- Janela Sobre o EngConvert com versão, autoria, tecnologias e licença.
- Seleção de idioma português/inglês e tradução da interface.
- Paleta de sete cores, incluindo Transparente, com contraste de texto e símbolos de seleção.
- Painel de resultado com fundo compatível com a cor escolhida.
- Interface integrada às preferências JSON e unidades personalizadas.
- Preservação das abas, favoritos, ordenação e dimensões da janela.
- Testes automatizados e validação manual no Windows.

## 3. Checklist

### Integração

- [ ] Integrar a versão final de `src/engconvert/interface.py`.
- [ ] Confirmar a janela Sobre o EngConvert e seus créditos.
- [ ] Confirmar idioma, paleta de cores e persistência no JSON.
- [ ] Validar legibilidade de abas, caixas marcadas, menus e resultado na cor Transparente.
- [ ] Confirmar a janela General e a persistência de preferências.
- [ ] Confirmar a janela Custom e a persistência de unidades.
- [ ] Preservar as funcionalidades da Sprint 09.

### Validação

- [ ] Executar `python -m pytest -q` e registrar o resultado real.
- [ ] Executar `python main.py`.
- [ ] Realizar as treze verificações manuais da Seção 9.1.
- [ ] Confirmar que a interface funciona no monitor do laboratório.
- [ ] Atualizar os checklists das Sprints 10 e 11.

### Entrega

- [ ] Revisar a documentação e o roadmap, se necessário.
- [ ] Registrar o commit da integração.
- [ ] Integrar a branch à `main` sem conflitos.
- [ ] Executar novamente os testes após o merge.
- [ ] Enviar a `main` ao GitHub, se o remoto estiver configurado.

## 4. Critérios de aceitação

A Sprint 12 será concluída após a aprovação dos testes automatizados, a validação manual das janelas e conversões, a preservação das funcionalidades anteriores e o registro da integração no Git.

## 5. Resultados e evidências

**Testes automatizados:** Pendente de registro.

**Testes manuais:** Pendente de registro.

**Commit da integração:** Pendente.

**Merge e push:** Pendentes.

**Problemas encontrados:** Preencher após os testes.

## 6. Decisão para a Aula 11

**Situação:** Aguardando validação final. O empacotamento em `.exe` só será abordado na Aula 11.
```

#### 9.2.3. Conferir o documento

```powershell
git status
git diff --check
```

O documento será incluído no commit de integração indicado na Seção 11, juntamente com `interface.py` e a atualização dos documentos das Sprints 10 e 11. **Não registre conclusão antecipada**.

---

## 10. JSON: onde ficam os dados?

No PowerShell, consulte o caminho padrão do Windows:

```powershell
explorer $env:APPDATA\EngConvert
```

Se ainda não existir, salve uma preferência no aplicativo e tente novamente. Esperam-se os arquivos `configuracoes.json` e `unidades_personalizadas.json` após utilizar os recursos correspondentes. Não inclua dados pessoais nem esses arquivos de preferências nos commits do projeto.

## 11. Git — concluir e integrar

Depois dos testes e das verificações manuais, atualize os documentos das Sprints e registre a integração. **Inclua `configuracoes.py`**, que recebeu idioma e cores. Não adicione automaticamente o arquivo da aula em avaliação que aparece como *untracked* no `git status`:

```powershell
git status
git diff
git add src/engconvert/interface.py src/engconvert/configuracoes.py docs/sprints/sprint-12-about.md
# Inclua os documentos das Sprints 10 e 11 somente se tiverem novas alterações:
# git add docs/sprints/sprint-10-general.md docs/sprints/sprint-11-custom.md
git diff --cached --check
git diff --cached --stat
python -m pytest -q
# Faça o commit apenas após aprovação dos testes e da validação manual:
git commit -m "feat: integra interface configuracoes e personalizacao visual"
git status
```

Antes do merge, confira que não há alterações pendentes nos arquivos do projeto e que os testes e a interface foram validados. Arquivos didáticos ainda não adicionados ao Git podem aparecer como *untracked*; não os inclua automaticamente no commit funcional.

```powershell
git status
git switch main
# Execute git pull apenas se houver remoto e upstream configurados e for necessário atualizar a main.
git merge feature-interface-final
python -m pytest -q
python main.py
```

Se o Git mostrar `Fast-forward`, a `main` avançou para os commits da branch de desenvolvimento sem conflito. No registro de execução desta aula, **38 testes foram aprovados** (`38 passed in 0.23s`); em outro computador ou após novas alterações, registre o resultado realmente obtido. A execução de `python main.py` exige também a conferência visual da interface.

### 11.1. Conferir e publicar a integração no GitHub

Após fechar a interface e confirmar que os testes passaram, execute na branch `main`:

```powershell
git status
git log -1 --oneline
git push origin main
git status
```

- `git status`: verifica a branch atual e identifica alterações locais pendentes; arquivos *untracked* não impedem necessariamente o envio dos commits.
- `git log -1 --oneline`: mostra o commit mais recente incorporado à `main`.
- `git push origin main`: envia os commits locais da `main` ao repositório remoto `origin`. Requer conexão, permissão de escrita e remoto configurado.
- `git status` final: verifica o estado local após o envio; confirme também a mensagem de sucesso do `git push`.

**Não confunda merge local com publicação remota:** o `Fast-forward` e os testes aprovados confirmam a integração local, mas somente a saída bem-sucedida do `git push origin main` confirma o envio ao GitHub. Se houver rejeição do push, não force o envio; examine a mensagem antes de prosseguir.

**Conferência manual:** abra o EngConvert com `python main.py` e verifique idioma português/inglês, temas, paleta de cores (inclusive Transparente), contraste de caixas de seleção e botões de opção, abas, conversões e recuperação das preferências após reiniciar.

O executável **não será enviado nesta aula**: será criado e publicado na Aula 11 via GitHub Releases. A explicação e criação didática do arquivo `LICENSE` (MIT) ficam reservadas às Aulas **11.0 e 11.1**; não é necessário alterar a Aula 10.1 congelada.

---

## 12. Consultar e atualizar os documentos das três Sprints

Os documentos agora são criados **no momento em que cada Sprint é trabalhada**, sem obrigar o aluno a procurar modelos em outra seção:

- **Sprint 10:** Seção 5.4.2 — `docs/sprints/sprint-10-general.md`.
- **Sprint 11:** Seção 7.3.2 — `docs/sprints/sprint-11-custom.md`.
- **Sprint 12:** Seção 9.2.2 — `docs/sprints/sprint-12-about.md`.

Nesta etapa, **não recrie nem substitua** os arquivos. Apenas atualize os checklists, os resultados dos testes e as evidências após as validações correspondentes. A integração final e o registro no Git estão descritos na Seção 11.

## 13. Checklist de conclusão da Etapa 10

- [ ] Configurações gerais salva e restaura preferências, idioma e cor dos botões.
- [ ] Os textos e símbolos de seleção continuam legíveis na opção Transparente.
- [ ] O painel de resultado acompanha a cor selecionada.
- [ ] Custom cadastra, utiliza, exclui e persiste unidades válidas.
- [ ] About apresenta versão, autoria e créditos.
- [ ] Tabs preserva ordenação, visibilidade e favoritos após reiniciar.
- [ ] A altura das categorias é restaurada e a janela inicia compacta, respeitando a área útil do monitor.
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
description = "Conversor de unidades de engenharia desenvolvido com Python e CustomTkinter"
requires-python = ">=3.12"
authors = [
    { name = "Wilson Luciano" }
]
license = "MIT"
dependencies = [
    "customtkinter"
]

[project.urls]
Repository = "https://github.com/wilson-luciano/engconvert"

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


