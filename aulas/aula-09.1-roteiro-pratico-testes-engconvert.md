# Aula 09.1 — Roteiro Prático: Testes Automatizados do EngConvert

**Disciplina:** Programação para Engenharia Mecânica  
**Projeto:** EngConvert — Conversor de Unidades de Engenharia  
**Etapa 9:** Testes de Software  
**Sprint 08:** Testes automatizados com pytest  
**Situação:** EM REVISÃO — v1  
**Base:** arquivos **efetivos** da Aula 08.1  

---

> **Orientação:** executar os comandos no terminal integrado do VSCode, dentro de `C:\Projetos\engconvert`, com `.venv` ativo. O projeto entregue na Aula 08.1 é a fonte dos módulos; nesta aula não substituímos as funções originais por exemplos inventados.

---
## 1. Objetivo da Sprint 08

Criar testes automatizados com `pytest` para **os arquivos efetivos da Aula 08.1**. Não reescrever `conversoes.py`, `dados.py`, `interface.py` nem `main.py`. A alteração nesta etapa será a inclusão de testes e documentação, preservando a aplicação funcional.

---

## 2. Ponto de partida e estrutura real

Partimos do projeto modularizado da Aula 08.1:

```text
engconvert/
├── main.py
├── pyproject.toml
├── src/engconvert/
│   ├── __init__.py
│   ├── dados.py
│   ├── conversoes.py
│   └── interface.py
└── tests/                 ← acrescentaremos nesta aula
    └── test_conversoes.py
```

O arquivo `conversoes.py` contém exatamente `converter_temperatura(valor, unidade_de, unidade_para)`, `obter_unidades(grandeza)` e `converter(valor, grandeza, unidade_de, unidade_para)`. O arquivo `dados.py` contém `grandezas` e `unidades_temperatura`.

---

## 3. Planejar os testes antes de programar

Vamos verificar pressão, comprimento, área, volume, temperatura, unidades disponíveis e conversões de identidade. O teste automatizado compara **resultado obtido** com **resultado esperado**, inclusive com tolerância para números de ponto flutuante. A função `converter()` devolve um número; não formata a saída da GUI.

---

## 4. Abrir o projeto no VSCode

No PowerShell:

```powershell
cd C:\Projetos\engconvert
code .
```

Confirme que está na pasta que contém `pyproject.toml`.

---

## 5. Ativar o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
python --version
```

Selecione o interpretador `.venv` no VSCode. Não execute os testes em um Python diferente daquele que utiliza para o projeto.

---

## 6. Confirmar a versão funcional

```powershell
python main.py
```

Faça uma conversão de referência, por exemplo `1 bar → 100 kPa`. Feche a GUI antes de iniciar os testes. Isso distingue um problema preexistente de uma falha introduzida na Sprint.

---

## 7. Verificar o Git

```bash
git status
git branch
```

A `main` deve conter a Etapa 8 concluída. Caso existam alterações não registradas, avalie-as antes de prosseguir.

---

## 8. Criar a branch de testes

```bash
git switch main
git pull
git switch -c feature-testes-pytest
```

Esta branch separa a implementação dos testes da versão já validada na `main`.

---

## 9. Registrar a Sprint 08

Crie `docs/sprints/sprint-08-testes.md` com objetivo, tarefas e critérios de conclusão. Exemplo:

```markdown
# Sprint 08 — Testes automatizados

## Objetivo
Validar as conversões do EngConvert com pytest.

## Tarefas
- [ ] Instalar pytest
- [ ] Criar tests/test_conversoes.py
- [ ] Executar casos parametrizados
- [ ] Verificar todas as cinco grandezas
- [ ] Testar unidades e identidades
- [ ] Registrar evidências
- [ ] Fazer commits e merge

## Status
Em andamento
```

---

## 10. Instalar o pytest

```powershell
python -m pip install pytest
python -m pytest --version
```

`python -m pytest` utiliza o mesmo interpretador do ambiente virtual. `pytest` é uma dependência **de desenvolvimento**, não necessária para que o usuário final converta unidades.

---

## 11. Confirmar a instalação editável do EngConvert

Se o projeto ainda não estiver instalado no `.venv`:

```powershell
python -m pip install -e .
```

O ponto final (`.`) representa a pasta atual. A instalação editável é importante porque os módulos estão dentro de `src/engconvert`. Não usar `sys.path.append("src")` como atalho.

---

## 12. Criar a pasta e o arquivo de testes

No explorador do VSCode, crie `tests/` na raiz e depois `tests/test_conversoes.py`.

O nome `test_*.py` segue a convenção de descoberta do pytest. A pasta de testes não deve ficar dentro de `src/engconvert`.

---

## 13. Importações usadas pelos testes

```python
import pytest
from engconvert.conversoes import converter, converter_temperatura, obter_unidades
from engconvert.dados import grandezas, unidades_temperatura
```

**Leia:** do módulo `conversoes` do pacote `engconvert`, importe os nomes indicados. O módulo de testes não importa `interface.py`, portanto não precisa abrir janelas.

---

## 14. Primeiro teste: bar para kPa

```python
def test_bar_para_kpa():
    resultado = converter(1, "Pressão", "bar", "kPa")
    assert resultado == pytest.approx(100)
```

A função de teste não recebe parâmetros neste exemplo. `assert` exige que a comparação seja verdadeira. `pytest.approx` admite pequenas diferenças numéricas.

---

## 15. Executar o primeiro teste

```powershell
python -m pytest -v
```

`-v` significa **verbose**, exibindo cada caso com mais detalhes. `PASSED` indica aprovação e `FAILED` indica falha. A primeira execução pode mostrar apenas um teste, se você ainda não copiou os demais.

---

## 16. Por que usar parametrização?

Ao invés de criar uma função quase idêntica para cada par de unidades, `@pytest.mark.parametrize` fornece diferentes entradas e saídas esperadas para a mesma função de teste. Assim, cada linha da tabela vira um caso independente no relatório.

---

## 17. Código completo de `tests/test_conversoes.py`

Copie integralmente o código a seguir. Ele usa **os nomes reais e os fatores da Aula 08.1**, sem mudar o código de produção.

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

## 18. Compreender os casos de pressão

O código testa `1 bar → 100 kPa` e `1 atm → 101325 Pa`. O resultado deriva dos fatores reais de `dados.py`, cuja unidade de referência é o pascal. Não altere os fatores para fazer um teste passar; confira primeiro qual resultado é fisicamente esperado.

---

## 19. Compreender os casos de comprimento

`1 m → 1000 mm` e `12 in → 1 ft` testam duas relações independentes. A primeira usa unidades SI; a segunda compara unidades imperiais. Os fatores são os já registrados no EngConvert.

---

## 20. Compreender os casos de área

`1 m² → 10000 cm²` mostra que a relação de área envolve unidades ao quadrado. `1 ft² → 0.09290304 m²` utiliza o fator já presente em `dados.py`.

---

## 21. Compreender os casos de volume

`1 L → 1000 mL`, `1 gal (US) → 3.785411784 L` e `1 gal (UK) → 4.54609 L` distinguem explicitamente os dois tipos de galão. Os valores são calculados com os fatores cadastrados, sem arredondamento prematuro.

---

## 22. Compreender os casos de temperatura

A função real converte primeiro para kelvin e depois para a escala de destino. Os testes verificam °C, °F, K e °R (Rankine). Por exemplo, `491.67 °R → 32 °F` e `540 °R → 300 K`. Aqui não basta aplicar um único fator às escalas com deslocamento.

---

## 23. Teste de identidade

Uma conversão de uma unidade para ela mesma deve preservar o valor, respeitada a tolerância numérica. A parametrização percorre as quatro grandezas multiplicativas, enquanto um teste específico cobre temperatura.

---

## 24. Testar `obter_unidades()`

Os testes confirmam que `obter_unidades("Pressão")` retorna as chaves do dicionário `grandezas["Pressão"]` e que `obter_unidades("Temperatura")` retorna a lista `unidades_temperatura`. Isso verifica o comportamento efetivo do código existente.

---

## 25. Tolerância absoluta e relativa

```python
assert resultado == pytest.approx(esperado, rel=1e-9, abs=1e-9)
```

`rel` é a tolerância proporcional ao valor esperado e `abs` é a tolerância absoluta. A tolerância absoluta é especialmente importante perto de zero. Esses valores são escolhas didáticas, não especificações metrológicas universais.

---

## 26. Executar a suíte completa

```powershell
python -m pytest tests/test_conversoes.py -v
```

A versão entregue possui **22 casos parametrizados ou independentes**: 14 conversões conhecidas, 4 identidades multiplicativas e 4 verificações adicionais. O resultado esperado, em um ambiente corretamente configurado, é todos passarem.

---

## 27. Executar todos os testes do projeto

```powershell
python -m pytest -q
```

`-q` significa **quiet**: exibe uma saída mais concisa. Esse comando será útil quando acrescentarmos outros arquivos de teste.

---

## 28. Investigar um teste que falhou

Leia o relatório: nome do teste, entrada, resultado obtido, resultado esperado e traceback. Se a falha for de importação, confirme o `.venv` e a instalação editável. Se for de valor, confira primeiro as unidades, fatores e a expectativa. **Não modifique a regra de conversão apenas para satisfazer uma expectativa errada.**

---

## 29. Experimento controlado de falha

Em uma branch de exercício ou antes de commitar, altere **temporariamente** a expectativa de `1 bar → 100 kPa` para `101` e execute `python -m pytest -v`. Observe `FAILED`. Restaure imediatamente `100` e execute novamente. **Não comite a expectativa incorreta.**

---

## 30. Limitações dos testes atuais

Estes testes validam as funções matemáticas e as listas de unidades. **Não** verificam automaticamente o layout, os botões, a abertura da janela, o aviso visual de entrada inválida ou a distribuição como executável. Esses aspectos exigem testes adicionais. Também não pressupomos que o código atual rejeite unidades inválidas com uma mensagem amigável: ele pode lançar `KeyError` ou retornar `None` em caminhos não previstos.

---

## 31. Teste de regressão

Repita a suíte sempre que mudar uma conversão, acrescentar uma unidade ou reorganizar os módulos. Um teste de regressão ajuda a identificar quando algo que funcionava deixou de funcionar após uma alteração.

---

## 32. Registrar o resultado no Git

```bash
git status
git diff
git add tests/test_conversoes.py docs/sprints/sprint-08-testes.md
git commit -m "test: adiciona testes de conversao com pytest"
```

Se o documento da Sprint ainda não existir, crie-o antes do `git add`. Não inclua `.venv/` nem `__pycache__/`.

---

## 33. Atualizar `.gitignore` quando necessário

Confirme que o `.gitignore` ignora, ao menos:

```gitignore
.venv/
__pycache__/
.pytest_cache/
*.pyc
```

Se precisou alterá-lo, inclua essa mudança em um commit. Não apague os arquivos de código do projeto.

---

## 34. Conferir a branch e integrar

Depois que todos os testes passarem:

```bash
git status
git switch main
git pull
git merge feature-testes-pytest
python -m pytest -q
git push
```

O teste **após o merge** confirma o estado final da `main`. Resolva conflitos se houver; não presuma que o merge foi automático.

---

## 35. Atualizar Sprint e Roadmap

Após validação, marque a Sprint 08 como concluída em `docs/sprints/sprint-08-testes.md` e a Etapa 9 no Roadmap. Registre o comando executado e a quantidade de testes aprovados. Faça commit e push dessa documentação. Se a suíte falhou, não marque a Sprint como concluída.

---

## 36. Checklist de conclusão

- [ ] Código de produção da Aula 08.1 preservado
- [ ] `.venv` ativo e `pytest` instalado
- [ ] `python -m pip install -e .` executado quando necessário
- [ ] `tests/test_conversoes.py` criado
- [ ] Pressão, comprimento, área, volume e temperatura testados
- [ ] Galões US e UK testados
- [ ] `obter_unidades` e identidade testados
- [ ] Suíte completa aprovada
- [ ] Git commit, merge e push realizados
- [ ] Sprint e Roadmap atualizados

---

## 37. Resumo e próxima etapa

Nesta Sprint aprendemos a escrever testes reproduzíveis, parametrizar casos, comparar números reais com tolerância, interpretar `PASSED`/`FAILED` e proteger a evolução do EngConvert com Git. A próxima etapa do Roadmap poderá ampliar a interface (abas, preferências e unidades personalizadas), usando a suíte criada como rede de segurança.

**Ideia-chave:** testar é transformar um resultado esperado em uma verificação repetível e documentada.

---

<sub>© 2026 Wilson Luciano · Programação para Engenharia Mecânica · EngConvert · Aula 09.1 · Em revisão v1</sub>
