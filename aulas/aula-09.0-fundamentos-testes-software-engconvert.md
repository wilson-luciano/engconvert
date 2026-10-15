# Aula 09.0 — Fundamentos de Testes de Software com Python

**Disciplina:** Programação para Engenharia Mecânica  
**Projeto:** EngConvert — Conversor de Unidades de Engenharia  
**Etapa 9:** Testes de Software  
**Situação:** EM REVISÃO — v1  
**Continuidade:** Aulas 08.0 e 08.1 — Modularização

---

## 1. Objetivos de aprendizagem

Ao concluir esta aula, o estudante deverá conseguir:

1. Explicar por que testar software é uma atividade de engenharia, não apenas de programação.
2. Distinguir teste manual, automatizado, unitário, de integração, de sistema e de regressão.
3. Diferenciar resultado esperado de resultado obtido.
4. Empregar `assert` e compreender o significado de `AssertionError`.
5. Identificar o papel do `pytest` e a convenção de descoberta de testes.
6. Selecionar casos de teste para conversões de engenharia, inclusive casos-limite.
7. Comparar resultados numéricos considerando a representação de ponto flutuante.
8. Compreender `pytest.approx`, tolerância absoluta e relativa.
9. Reconhecer a diferença entre cobertura de código e qualidade dos testes.
10. Preparar a passagem para a Aula 09.1, sem alterar os arquivos congelados da Etapa 8.

---

## 2. A pergunta que orienta a etapa

> Como demonstrar, de maneira repetível, que o EngConvert continua produzindo os resultados corretos após uma modificação?

Na Aula 08.1, a aplicação foi reorganizada em módulos. A refatoração preservou a proposta matemática do programa, mas reorganizou onde o código é executado.

```text
main.py
   ↓
interface.py
   ↓
conversoes.py
   ↓
dados.py
```

Essa estrutura facilita testar a **regra de conversão** sem abrir a interface gráfica.

**Ideia-chave:** um programa abrir sem apresentar erro não prova que seus cálculos estão corretos.

---

## 3. O que é um teste de software?

É uma verificação planejada do comportamento de um sistema em condições especificadas. Um teste executa uma operação, observa o resultado e compara esse resultado com um critério previamente definido.

```text
ENTRADA
   ↓
EXECUÇÃO
   ↓
RESULTADO OBTIDO
   ↓
COMPARAÇÃO COM O RESULTADO ESPERADO
   ↓
APROVADO / REPROVADO
```

Em engenharia mecânica, essa lógica lembra a verificação de um instrumento de medição contra um padrão de referência. A analogia ajuda a compreender o processo, mas não significa que testes de software substituam calibração metrológica ou validação física.

---

## 4. Por que isso importa em engenharia?

Um erro de conversão pode propagar-se para dimensionamentos, cálculos de pressão, especificação de componentes ou interpretação de dados. O EngConvert é didático, mas sua matemática representa operações comuns em atividades técnicas.

Exemplo:

```text
1 bar = 100 kPa
```

Se o programa retornar `10 kPa`, a interface pode continuar funcionando normalmente, mas o resultado está incorreto.

Por isso distinguimos **funcionamento visual** e **correção do comportamento**.

---

## 5. Resultado esperado × resultado obtido

| Elemento              | Exemplo                               |
| --------------------- | ------------------------------------- |
| Entrada               | 1 bar                                 |
| Unidade de destino    | kPa                                   |
| Resultado esperado    | 100 kPa                               |
| Resultado obtido      | Valor retornado pelo EngConvert       |
| Critério de aprovação | Concordância segundo a regra definida |

Um teste confiável precisa conhecer o resultado esperado por uma fonte independente do código que está sendo testado. Copiar a mesma fórmula defeituosa para o teste pode fazer o erro passar despercebido.

---

## 6. Teste manual

É realizado por uma pessoa, que interage com o software e confere o resultado.

No EngConvert:

1. Abrir a interface.
2. Selecionar Pressão.
3. Informar `1`.
4. Selecionar `bar` e `kPa`.
5. Clicar em **Converter**.
6. Conferir o valor `100 kPa`.

**Vantagens:** ajuda a avaliar interface, mensagens, usabilidade e comportamento visual.  
**Limitações:** demanda repetição humana, pode ser demorado e pode omitir casos importantes.

---

## 7. Teste automatizado

É executado por código e compara automaticamente o resultado com um critério.

Exemplo conceitual:

```python
resultado = 100_000 / 1_000
assert resultado == 100
```

O comando `assert` verifica uma condição. Se for verdadeira, a execução prossegue; se for falsa, Python produz uma exceção `AssertionError`.

**Atenção:** `assert` é adequado para testes e verificações internas, não para substituir validação de entradas de usuários. Python pode desabilitar asserts quando executado em modo otimizado (`-O`).

---

## 8. Lendo um `assert`

```python
assert resultado == esperado
```

Leitura didática:

> Verifique se `resultado` é igual a `esperado`; se não for, sinalize falha.

Exemplo que passa:

```python
assert 2 + 3 == 5
```

Exemplo que falha:

```python
assert 2 + 3 == 6
```

Em testes com `pytest`, as mensagens de falha costumam apresentar informações úteis sobre os valores comparados.

---

## 9. O que é `pytest`?

`pytest` é uma ferramenta externa do ecossistema Python para criar e executar testes. **Não integra a biblioteca padrão** e precisa ser instalada no ambiente do projeto.

Na Aula 09.1 usaremos:

```powershell
python -m pip install pytest
```

Para executar:

```powershell
python -m pytest
```

O prefixo `python -m` ajuda a usar o pacote associado ao interpretador Python ativo, preferencialmente o do `.venv`.

---

## 10. Organização de testes

Uma organização didática para a próxima Sprint é:

```text
engconvert/
├── main.py
├── pyproject.toml
├── src/
│   └── engconvert/
│       ├── __init__.py
│       ├── dados.py
│       ├── conversoes.py
│       └── interface.py
└── tests/
    ├── test_conversoes.py
    └── test_dados.py
```

O diretório `tests/` guarda o código que verifica o comportamento do programa. Os testes **não substituem** os módulos de produção.

---

## 11. Convenções de nomes

Por padrão, o `pytest` descobre arquivos como:

```text
test_conversoes.py
```

E funções como:

```python
def test_bar_para_kpa():
    ...
```

O prefixo `test_` comunica a finalidade da função e permite que o `pytest` a encontre automaticamente. As reticências representam código ainda não escrito, não um teste completo.

---

## 12. Teste unitário

Verifica uma pequena unidade de comportamento — frequentemente uma função — de maneira isolada ou com poucas dependências.

No EngConvert, uma candidata natural é:

```python
converter(valor, grandeza, unidade_de, unidade_para)
```

Exemplo com a assinatura real do projeto modularizado:

```python
from engconvert.conversoes import converter


def test_bar_para_kpa():
    resultado = converter(1, "Pressão", "bar", "kPa")
    assert resultado == 100
```

O teste não precisa abrir a janela do CustomTkinter.

---

## 13. Teste de integração

Verifica se partes diferentes do sistema funcionam corretamente quando usadas juntas.

Exemplo: `conversoes.py` utiliza os fatores definidos em `dados.py`. Um teste que chama `converter()` e utiliza esses dados também verifica, em alguma medida, a integração entre esses módulos.

**Importante:** categorias de teste não são compartimentos completamente separados. Um mesmo teste pode verificar uma função e sua integração com dados de outro módulo.

---

## 14. Teste de sistema

Verifica a aplicação como um todo, considerando seu comportamento completo.

No EngConvert, poderia envolver:

```text
abrir janela
   ↓
selecionar grandeza
   ↓
digitar valor
   ↓
clicar em Converter
   ↓
conferir resultado apresentado
```

Esse tipo de teste é diferente de chamar diretamente uma função matemática. Não precisamos automatizar a interface nesta primeira etapa.

---

## 15. Teste de regressão

**Regressão** é quando uma funcionalidade que funcionava deixa de funcionar após uma alteração.

Exemplo:

```text
ANTES
1 bar → 100 kPa
       ↓
REFATORAÇÃO
       ↓
DEPOIS
1 bar → 10 kPa   ❌
```

Um conjunto de testes automatizados ajuda a detectar regressões repetindo verificações que já foram aprovadas.

---

## 16. Um caso de teste deve ser pequeno e claro

Compare:

```python
def test_tudo():
    ...
```

com:

```python
def test_bar_para_kpa():
    ...


def test_celsius_para_fahrenheit():
    ...
```

Nomes específicos ajudam a identificar rapidamente qual comportamento falhou.

---

## 17. Casos positivos, limites e entradas inválidas

Para cada funcionalidade, pense em:

| Tipo                    | Exemplo            | O que verifica                       |
| ----------------------- | ------------------ | ------------------------------------ |
| Comum                   | 1 bar → kPa        | Conversão cotidiana                  |
| Identidade              | 10 m → m           | Unidade igual na origem e destino    |
| Zero                    | 0 °C → K           | Tratamento do zero da escala Celsius |
| Negativo válido         | -40 °C → °F        | Temperaturas abaixo de zero          |
| Valor muito pequeno     | 0,001 m → mm       | Escala numérica                      |
| Valor muito grande      | 1.000.000 Pa → MPa | Escala numérica                      |
| Entrada inválida na GUI | `abc`              | Tratamento de erro na interface      |

**Atenção:** nem toda entrada negativa é inválida. Em temperatura, valores negativos em °C e °F podem ser perfeitamente válidos.

---

## 18. Casos de teste das cinco grandezas

| Grandeza    | Entrada     | Resultado esperado |
| ----------- | ----------- | ------------------ |
| Pressão     | 1 bar → kPa | 100                |
| Comprimento | 1 m → mm    | 1000               |
| Área        | 1 m² → cm²  | 10000              |
| Volume      | 1 L → mL    | 1000               |
| Temperatura | 0 °C → °F   | 32                 |

Os valores são obtidos a partir das definições de unidade e da implementação prevista para o EngConvert.

---

## 19. Particularidade dos galões

No projeto existem duas unidades distintas:

```text
gal (US) — galão líquido americano
gal (UK) — galão imperial
```

Não são equivalentes. Portanto, um teste que utilize galões deve indicar explicitamente qual dos dois está sendo empregado.

O arquivo `dados.py` do projeto contém os fatores de cada unidade em relação ao metro cúbico.

---

## 20. Particularidade das temperaturas

No EngConvert, a conversão de temperatura passa por kelvin como referência. As escalas disponíveis são:

```text
°C — grau Celsius
°F — grau Fahrenheit
K  — kelvin
°R — grau Rankine
```

Diferentemente das grandezas multiplicativas, as conversões Celsius–Fahrenheit e Celsius–kelvin incluem deslocamentos de escala.

Exemplos importantes:

```text
0 °C = 32 °F
0 °C = 273,15 K
-40 °C = -40 °F
0 K = 0 °R
```

---

## 21. Por que `float` merece atenção?

Python representa números `float` normalmente com ponto flutuante binário de precisão dupla. Muitas frações decimais não possuem representação binária exata.

Por isso, operações aparentemente simples podem produzir pequenas diferenças numéricas.

Exemplo conhecido:

```python
print(0.1 + 0.2)
```

Em geral, será exibido:

```text
0.30000000000000004
```

Isso não significa, por si só, que a fórmula de engenharia está errada.

---

## 22. Comparação exata × comparação aproximada

Comparação exata:

```python
assert resultado == esperado
```

É apropriada quando a igualdade exata é realmente esperada e estável.

Comparação aproximada:

```python
assert resultado == pytest.approx(esperado)
```

É útil para resultados de ponto flutuante que admitem pequenas diferenças de arredondamento.

---

## 23. Como usar `pytest.approx`

```python
import pytest

from engconvert.conversoes import converter


def test_celsius_para_kelvin():
    resultado = converter(0, "Temperatura", "°C", "K")
    assert resultado == pytest.approx(273.15)
```

O `pytest.approx` permite comparar valores numéricos com tolerâncias apropriadas.

---

## 24. Tolerância absoluta e relativa

Em termos gerais, uma comparação numérica aproximada considera a diferença entre resultado e referência.

**Tolerância absoluta:** estabelece uma diferença máxima em unidades do valor comparado.

**Tolerância relativa:** estabelece uma diferença proporcional à magnitude da referência.

Exemplo explícito:

```python
assert resultado == pytest.approx(
    esperado,
    rel=1e-6,
    abs=1e-9
)
```

Leitura:

```text
rel=1e-6 → tolerância relativa de 0,000001
abs=1e-9 → tolerância absoluta de 0,000000001
```

O `pytest.approx` aceita a comparação quando a diferença satisfaz a tolerância absoluta **ou** a relativa. Os valores acima são apenas ilustrativos: tolerâncias técnicas devem ser escolhidas conforme a grandeza, a escala e o objetivo do teste.

---

## 25. A tolerância não pode esconder um erro real

Um teste não deve aprovar uma conversão de `1 bar → 99 kPa` apenas porque escolhemos uma tolerância exageradamente ampla.

O objetivo da tolerância é lidar com pequenas diferenças de representação, **não aceitar resultados fisicamente incorretos**.

---

## 26. Exemplo: `pytest` detectando uma falha

```python
from engconvert.conversoes import converter


def test_bar_para_kpa():
    resultado = converter(1, "Pressão", "bar", "kPa")
    assert resultado == 10  # valor esperado propositalmente errado
```

O teste deve falhar, pois o resultado correto é `100`.

Essa falha é **intencional e didática**: demonstra como um teste informa que o resultado observado não corresponde à expectativa registrada.

Após a demonstração, corrija a expectativa para `100`.

---

## 27. O que significam PASS, FAIL e ERROR?

| Indicação | Significado didático                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| `PASSED`  | O teste executou e satisfez suas verificações                                                  |
| `FAILED`  | Uma verificação falhou ou ocorreu uma falha associada ao teste                                 |
| `ERROR`   | Houve problema na preparação, coleta ou execução que impediu o teste de prosseguir normalmente |

Esses termos ajudam a interpretar a saída do `pytest`. Uma suíte com todos os testes aprovados ainda não prova ausência de todos os defeitos possíveis.

---

## 28. Testes parametrizados

Às vezes queremos testar a mesma função com muitas entradas.

Sem parametrização, repetimos várias funções semelhantes. Com `pytest.mark.parametrize`, podemos organizar os casos em uma tabela.

```python
import pytest

from engconvert.conversoes import converter


@pytest.mark.parametrize(
    "valor, grandeza, origem, destino, esperado",
    [
        (1, "Pressão", "bar", "kPa", 100),
        (1, "Comprimento", "m", "mm", 1000),
        (1, "Área", "m²", "cm²", 10000),
        (1, "Volume", "L", "mL", 1000),
        (0, "Temperatura", "°C", "°F", 32),
    ],
)
def test_conversoes_basicas(valor, grandeza, origem, destino, esperado):
    resultado = converter(valor, grandeza, origem, destino)
    assert resultado == pytest.approx(esperado)
```

Cada linha representa um caso de teste. Na Aula 09.1, construiremos essa estrutura passo a passo.

---

## 29. Como ler `@pytest.mark.parametrize`?

O símbolo `@` introduz um **decorador** em Python. Aqui, o decorador informa ao `pytest` que a mesma função deverá ser executada várias vezes, usando conjuntos diferentes de argumentos.

Não precisamos estudar todos os detalhes de decoradores nesta etapa.

Basta compreender:

```text
UMA FUNÇÃO DE TESTE
        ↓
VÁRIAS LINHAS DE DADOS
        ↓
VÁRIAS EXECUÇÕES
```

---

## 30. Testar a lista de unidades

Além de testar números, podemos testar a função real:

```python
obter_unidades(grandeza)
```

Exemplo:

```python
from engconvert.conversoes import obter_unidades


def test_unidades_de_temperatura():
    unidades = obter_unidades("Temperatura")
    assert unidades == ["°C", "°F", "K", "°R"]
```

Esse teste verifica um comportamento diferente da conversão matemática: a lista de opções oferecida para uma grandeza.

---

## 31. E as entradas inválidas?

É importante distinguir duas responsabilidades:

- A interface (`interface.py`) converte o texto digitado em número e apresenta mensagens amigáveis quando a entrada não é numérica.
- A função matemática (`conversoes.py`) recebe valores já convertidos e realiza o cálculo.

Portanto, testar que `float("abc")` gera `ValueError` não é o mesmo que testar a mensagem visual apresentada pela interface.

Não devemos afirmar que `converter()` valida texto digitado se essa validação pertence à GUI.

---

## 32. Testes de exceções

O `pytest` permite verificar se uma operação gera uma exceção esperada:

```python
import pytest


def test_texto_nao_numerico():
    with pytest.raises(ValueError):
        float("abc")
```

Esse exemplo ensina o mecanismo `pytest.raises`. Ele **não é ainda** um teste da interface do EngConvert.

---

## 33. Casos de entrada não previstos no código atual

O `conversoes.py` modularizado pressupõe que grandezas e unidades informadas existam nos dicionários.

Assim, um nome inexistente pode provocar `KeyError`. Da mesma forma, a função de temperatura atual não possui uma mensagem de erro explícita para uma escala desconhecida.

Isso não deve ser disfarçado na apostila. Primeiro testaremos o **comportamento realmente implementado**; melhorias de validação poderão ser propostas em uma Sprint posterior, com critérios claros.

---

## 34. O que é cobertura de testes?

Cobertura mede quanto do código foi exercitado durante os testes, segundo uma métrica definida — por exemplo, linhas ou ramos de decisão.

Uma cobertura de 100% **não garante** que todos os resultados estejam corretos: o teste pode executar todas as linhas sem verificar adequadamente o que elas produzem.

A pergunta mais importante é:

> Os testes verificam os comportamentos e riscos relevantes?

---

## 35. Testar as decisões do programa

No EngConvert existe uma decisão fundamental:

```python
if grandeza == "Temperatura":
    ...
else:
    ...
```

Um conjunto de testes que cobre somente Pressão deixa sem verificação a regra específica de Temperatura.

Também precisamos exercitar os quatro caminhos de entrada e saída de temperatura, em combinações representativas.

---

## 36. Uma matriz de testes

Uma matriz de testes organiza a cobertura funcional pretendida.

| Módulo          | Comportamento        | Caso recomendado   |
| --------------- | -------------------- | ------------------ |
| `dados.py`      | Fatores de pressão   | bar e kPa          |
| `dados.py`      | Galões distintos     | US e UK            |
| `conversoes.py` | Pressão              | bar → kPa          |
| `conversoes.py` | Comprimento          | m → mm             |
| `conversoes.py` | Área                 | m² → cm²           |
| `conversoes.py` | Volume               | L → mL             |
| `conversoes.py` | Temperatura          | °C → °F            |
| `conversoes.py` | Temperatura absoluta | K → °R             |
| `conversoes.py` | Lista de unidades    | Temperatura        |
| `interface.py`  | Entrada inválida     | texto não numérico |

A última linha exige um teste de interface ou uma estratégia específica para testar a função de interação; não será coberta simplesmente chamando `converter()`.

---

## 37. Testes devem ser independentes

O resultado de um teste não deveria depender de outro teste ter sido executado antes.

Evite modificar dicionários globais do EngConvert durante um teste e deixar a alteração afetar os seguintes.

Uma boa suíte permite executar um teste isoladamente ou o conjunto inteiro, com resultados consistentes.

---

## 38. Testes e Git

Os testes devem ser versionados junto com o código de produção:

```text
src/engconvert/
    ↓
implementação

tests/
    ↓
verificações

Git
    ↓
registra ambos
```

Quando corrigirmos um defeito, idealmente adicionaremos um teste que reproduza o problema, para ajudar a impedir sua reaparição.

---

## 39. CI — Integração Contínua

**CI** significa _Continuous Integration_, em português **Integração Contínua**.

É uma prática de integrar alterações com frequência e verificá-las automaticamente. Uma plataforma como o GitHub Actions pode executar testes após determinados eventos do repositório.

```text
alteração no código
       ↓
push / pull request
       ↓
execução automatizada
       ↓
pytest
       ↓
resultado dos testes
```

**Pull Request** é uma solicitação de integração de alterações, normalmente acompanhada de revisão. Não configuraremos CI nesta Aula 09.0; primeiro aprenderemos a criar testes confiáveis.

---

## 40. O que são TDD e desenvolvimento orientado a testes?

**TDD** significa _Test-Driven Development_, ou **Desenvolvimento Orientado a Testes**.

Em uma forma clássica, o ciclo é:

```text
RED
escrever teste que falha
       ↓
GREEN
implementar o mínimo para passar
       ↓
REFACTOR
melhorar o código mantendo testes aprovados
```

O EngConvert não foi iniciado em TDD. Estamos introduzindo testes após uma etapa de modularização, o que é uma trajetória pedagógica válida. Mais adiante, podemos experimentar TDD ao acrescentar uma nova unidade.

---

## 41. A diferença entre testar e depurar

**Testar** é procurar evidências sobre o comportamento e identificar falhas.

**Depurar** (_debugging_) é investigar a causa de uma falha e corrigir o problema.

```text
TESTE FALHA
    ↓
ANALISAR MENSAGEM
    ↓
LOCALIZAR CAUSA
    ↓
CORRIGIR
    ↓
EXECUTAR TESTE NOVAMENTE
```

---

## 42. Boas práticas para os testes do EngConvert

1. Nomeie testes pelo comportamento verificado.
2. Use valores de referência compreensíveis.
3. Compare números de ponto flutuante com tolerância adequada quando necessário.
4. Não utilize tolerâncias tão amplas que escondam defeitos.
5. Cubra as cinco grandezas e as diferenças entre escalas.
6. Separe testes matemáticos de testes da interface.
7. Não modifique os dados globais sem restaurar o estado.
8. Execute a suíte após mudanças no código.
9. Registre testes e correções no Git.
10. Não confunda testes aprovados com garantia absoluta de ausência de defeitos.

---

## 43. Erros conceituais frequentes

| Afirmação                                                | Avaliação                                                           |
| -------------------------------------------------------- | ------------------------------------------------------------------- |
| “Se abriu, está correto.”                                | Incorreta: pode calcular errado                                     |
| “Teste automatizado elimina todo teste manual.”          | Incorreta: têm finalidades complementares                           |
| “`assert` é uma mensagem para o usuário.”                | Incorreta: é verificação de condição                                |
| “`pytest` já vem com Python.”                            | Incorreta: precisa ser instalado                                    |
| “`0.1 + 0.2` sempre resulta em `0.3` exato em `float`.”  | Incorreta                                                           |
| “100% de cobertura significa software sem defeitos.”     | Incorreta                                                           |
| “Um teste de conversão também prova que a GUI funciona.” | Incorreta                                                           |
| “Um teste que falha pode ser útil.”                      | Correta: pode revelar um problema real ou uma expectativa incorreta |

---

## 44. Exercícios de fixação

**Exercício 1.** Explique, com suas palavras, a diferença entre teste manual e teste automatizado.

**Exercício 2.** Por que `1 bar → 100 kPa` é um bom caso inicial, mas insuficiente para testar todo o EngConvert?

**Exercício 3.** Escreva um teste usando `assert` para verificar que `1 m → 1000 mm`.

**Exercício 4.** Explique por que `-40 °C → -40 °F` é um caso interessante.

**Exercício 5.** Diferencie `pytest.approx` de `==` e dê um exemplo de quando a comparação aproximada é apropriada.

**Exercício 6.** Um teste de conversão retorna `100`, mas a interface mostra `10`. Que partes do sistema deveriam ser investigadas?

**Exercício 7.** Explique por que é importante diferenciar `gal (US)` e `gal (UK)` nos testes.

**Exercício 8.** Defina regressão e dê um exemplo envolvendo a modularização da Aula 08.1.

---

## 45. Resumo da aula

```text
TESTES DE SOFTWARE
        ↓
resultado esperado × obtido
        ↓
manual / automatizado
        ↓
unitário / integração / sistema
        ↓
regressão
        ↓
assert
        ↓
pytest
        ↓
casos parametrizados
        ↓
ponto flutuante + tolerância
        ↓
cobertura e boas práticas
        ↓
EngConvert preparado para a Sprint de testes
```

**Ideia-chave:** testar é transformar expectativas técnicas em verificações repetíveis. No EngConvert, a modularização tornou as regras de conversão acessíveis sem a interface; agora podemos verificar essas regras de forma sistemática.

---

## 46. Próxima aula — 09.1

Na **Aula 09.1 — Roteiro Prático**, faremos, passo a passo:

```text
criar branch da Sprint de testes
        ↓
instalar pytest no .venv
        ↓
criar tests/
        ↓
criar test_conversoes.py
        ↓
testar cinco grandezas
        ↓
testar temperaturas e galões
        ↓
parametrizar casos
        ↓
executar pytest no terminal
        ↓
interpretar PASS / FAIL
        ↓
registrar commits
        ↓
integrar ao GitHub
```

A Aula 09.1 partirá dos arquivos **efetivos** da Aula 08.1, preservando os nomes `converter()`, `converter_temperatura()`, `obter_unidades()`, `grandezas` e `unidades_temperatura`.

---

<sub>© 2026 Wilson Luciano · Programação para Engenharia Mecânica · EngConvert · Aula 09.0 · Versão em revisão 1</sub>
