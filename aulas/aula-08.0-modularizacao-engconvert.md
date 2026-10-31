# Aula 08.0 — Modularização do EngConvert

## Do `main.py` Monolítico para uma Arquitetura Organizada em Módulos

> **Projeto-guia:** EngConvert — Engineering Unit Converter  
> **Etapa do Roadmap:** Etapa 8 — Modularização  
> **Pré-requisito:** Aulas 07.0 e 07.1 concluídas.  
> **Objetivo:** compreender por que e como dividir um programa Python em módulos e pacotes, preparando o EngConvert para crescer com organização, testes e manutenção.

---

# 🎯 Objetivos da aula

Ao final desta aula, o aluno deverá ser capaz de:

- compreender o conceito de **modularização**;
- identificar responsabilidades diferentes dentro de um programa;
- reconhecer os problemas de um arquivo `main.py` excessivamente grande;
- compreender **separação de responsabilidades**;
- distinguir **arquivo**, **módulo**, **pacote** e **aplicação**;
- compreender o funcionamento de `import`;
- utilizar `from ... import ...` conscientemente;
- compreender `__name__` e `if __name__ == "__main__":`;
- compreender o papel de `__init__.py`;
- reconhecer importações absolutas e relativas;
- organizar dados, regras de conversão e interface gráfica em módulos diferentes;
- compreender por que a modularização facilita testes;
- utilizar Git antes de uma alteração estrutural;
- planejar a nova arquitetura do EngConvert sem alterar seu comportamento externo.

---

# 1. Onde estamos no projeto?

O EngConvert já percorreu várias etapas:

```text
Ambiente
   ↓
GUI
   ↓
Widgets e eventos
   ↓
Primeiro conversor
   ↓
Conversor de pressão
   ↓
Múltiplas grandezas
   ↓
Git e GitHub
```

Agora possuímos:

```text
PROGRAMA FUNCIONAL
        +
CONTROLE DE VERSÃO
        +
REPOSITÓRIO REMOTO
```

Isso nos permite realizar uma mudança estrutural importante com mais segurança.

---

# 2. O próximo problema não é uma nova conversão

Até aqui, muitas evoluções significaram adicionar funcionalidades.

Agora o problema é diferente.

O programa funciona, mas seu código tende a concentrar responsabilidades em um único arquivo:

```text
main.py
   │
   ├── dados das unidades
   ├── fatores de conversão
   ├── funções matemáticas
   ├── tratamento de temperatura
   ├── eventos
   ├── widgets
   ├── layout
   └── inicialização da aplicação
```

Isso funciona em programas pequenos.

À medida que o projeto cresce, porém:

```text
mais funcionalidades
        ↓
mais código
        ↓
mais responsabilidades
        ↓
mais dificuldade de manutenção
```

---

# 3. A pergunta central desta etapa

Precisamos responder:

```text
COMO ORGANIZAR
UM PROGRAMA QUE CRESCE?
```

Uma das respostas fundamentais em desenvolvimento de software é:

```text
MODULARIZAÇÃO
```

---

# 4. O que é modularização?

Modularização é o processo de dividir um programa em partes menores, organizadas e com responsabilidades bem definidas.

Em vez de:

```text
main.py
   │
   └── tudo
```

podemos evoluir para:

```text
main.py
   │
   └── inicia a aplicação

engconvert/
   │
   ├── dados
   ├── conversões
   └── interface
```

A ideia não é simplesmente criar mais arquivos.

A ideia é:

```text
SEPARAR RESPONSABILIDADES
```

---

# 5. Uma analogia com Engenharia Mecânica

Uma máquina complexa raramente é tratada como uma única peça indivisível.

Podemos encontrar:

```text
MÁQUINA
  │
  ├── estrutura
  ├── acionamento
  ├── transmissão
  ├── sistema de controle
  ├── lubrificação
  └── proteção
```

Cada subsistema possui uma função.

O conjunto forma a máquina.

Em software:

```text
APLICAÇÃO
  │
  ├── dados
  ├── regras
  ├── interface
  └── inicialização
```

> 📌 **Ideia-chave:** modularizar um software é semelhante a organizar um sistema de engenharia em subsistemas com funções bem definidas.

---

# 6. Modularizar não significa alterar o resultado

Um ponto importante:

```text
ANTES DA MODULARIZAÇÃO
EngConvert funciona
```

Depois:

```text
DEPOIS DA MODULARIZAÇÃO
EngConvert deve continuar funcionando
```

A mudança principal ocorre:

```text
POR DENTRO
```

e não necessariamente:

```text
PARA O USUÁRIO
```

---

# 7. Refatoração

Essa mudança está relacionada ao conceito de:

```text
REFACTORING
```

ou:

```text
REFACTORING
      ↓
REFATORAÇÃO
```

Refatorar significa reorganizar ou melhorar a estrutura interna do código sem alterar intencionalmente seu comportamento externo.

Exemplo:

```text
ANTES

main.py
  500 linhas
```

```text
DEPOIS

main.py
conversoes.py
dados.py
interface.py
```

Se o programa realiza as mesmas conversões corretamente, houve uma mudança estrutural, não uma nova funcionalidade.

---

# 8. Por que refatorar agora?

Porque já temos três condições importantes:

```text
1. programa funcional
2. complexidade crescente
3. Git e GitHub configurados
```

Isso cria um momento didaticamente adequado:

```text
VERSÃO FUNCIONAL
       ↓
COMMIT
       ↓
BRANCH
       ↓
REFATORAÇÃO
       ↓
TESTES MANUAIS
       ↓
COMMIT
       ↓
MERGE
```

---

# 9. Separação de responsabilidades

Um princípio importante é:

```text
cada parte do programa
deve possuir uma responsabilidade clara
```

No EngConvert podemos identificar pelo menos:

```text
DADOS
   ↓
quais grandezas e unidades existem?

REGRAS
   ↓
como os valores são convertidos?

INTERFACE
   ↓
como o usuário interage?

ENTRADA DA APLICAÇÃO
   ↓
como o programa é iniciado?
```

---

# 10. O problema do `main.py` monolítico

Um arquivo muito grande pode apresentar:

```text
muitas variáveis
muitas funções
muitos widgets
muitos eventos
muitas regras
```

Isso dificulta responder perguntas simples:

```text
Onde está a conversão de temperatura?

Onde estão os fatores de volume?

Onde é criado o ComboBox?

Onde a aplicação é iniciada?

O que posso testar sem abrir a GUI?
```

A modularização ajuda a tornar essas respostas mais claras.

---

# 11. Coesão

Um conceito relacionado é:

```text
COESÃO
```

Um módulo possui boa coesão quando seus elementos estão fortemente relacionados ao propósito daquele módulo.

Por exemplo:

```text
conversoes.py
   │
   ├── converter_por_fator()
   ├── converter_temperatura()
   └── converter()
```

Essas funções possuem relação direta:

```text
CONVERSÃO DE UNIDADES
```

---

# 12. Acoplamento

Outro conceito importante é:

```text
ACOPLAMENTO
```

Acoplamento representa o grau de dependência entre partes do sistema.

Se tudo depende diretamente de tudo:

```text
A ↔ B ↔ C ↔ D
↕   ↕   ↕   ↕
E ↔ F ↔ G ↔ H
```

qualquer mudança pode produzir efeitos difíceis de prever.

Queremos dependências mais claras:

```text
interface
    ↓
conversoes
    ↓
dados
```

Não significa eliminar todas as dependências.

Significa:

```text
TORNÁ-LAS CONTROLADAS E COMPREENSÍVEIS
```

---

# 13. Alta coesão e baixo acoplamento

Uma orientação clássica de projeto é buscar:

```text
ALTA COESÃO
      +
BAIXO ACOPLAMENTO
```

De forma didática:

```text
cada módulo
faz bem uma função
        +
depende do mínimo necessário
dos outros módulos
```

Não trataremos isso como uma regra matemática.

É uma orientação de organização.

---

# 14. Arquivo Python

Considere:

```text
conversoes.py
```

Esse é um arquivo Python.

Dentro dele podemos ter:

```python
def converter():
    pass
```

Um arquivo `.py` pode ser executado diretamente ou utilizado por outros arquivos.

---

# 15. O que é um módulo?

Em Python, um arquivo `.py` que pode ser importado é normalmente tratado como um:

```text
MÓDULO
```

Exemplo:

```text
conversoes.py
```

pode ser importado por:

```python
import conversoes
```

Então:

```text
arquivo .py
     ↓
pode atuar como
     ↓
módulo Python
```

---

# 16. O que é um pacote?

Um **pacote** organiza módulos relacionados em uma estrutura de diretórios importável.

Exemplo:

```text
engconvert/
│
├── __init__.py
├── dados.py
├── conversoes.py
└── interface.py
```

Aqui:

```text
engconvert
```

é o pacote.

E:

```text
dados.py
conversoes.py
interface.py
```

são módulos do pacote.

---

# 17. Estrutura que utilizaremos

A evolução planejada será:

```text
engconvert/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   └── engconvert/
│       ├── __init__.py
│       ├── dados.py
│       ├── conversoes.py
│       └── interface.py
│
├── docs/
├── aulas/
├── tests/
└── .venv/
```

A pasta:

```text
src/
```

passará a concentrar o código-fonte organizado da aplicação.

---

# 18. Por que utilizar `src/`?

A estrutura:

```text
src/
   └── engconvert/
```

separa claramente:

```text
CÓDIGO-FONTE DA APLICAÇÃO
```

de:

```text
documentação
aulas
testes
arquivos de configuração
ambiente virtual
```

Visualmente:

```text
PROJETO
│
├── src/       ← código
├── tests/     ← testes
├── docs/      ← documentação
└── aulas/     ← material didático
```

---

# 19. Por que não fizemos isso na Aula 01?

Porque naquele momento teríamos criado uma estrutura que o aluno ainda não precisava compreender.

Começamos com:

```text
main.py
```

porque era suficiente.

Agora o problema surgiu naturalmente:

```text
main.py cresceu
       ↓
responsabilidades aumentaram
       ↓
precisamos organizar
       ↓
src/engconvert/
```

> 🎯 **Ideia pedagógica:** a arquitetura aparece como resposta a uma necessidade real do projeto.

---

# 20. `__init__.py`

Dentro do pacote teremos:

```text
__init__.py
```

Estrutura:

```text
src/
└── engconvert/
    ├── __init__.py
    ├── dados.py
    ├── conversoes.py
    └── interface.py
```

Historicamente, `__init__.py` identifica diretórios tratados como pacotes regulares.

Mesmo que Python moderno também suporte **namespace packages** sem esse arquivo em determinados cenários, utilizaremos `__init__.py` porque torna a intenção explícita e é apropriado para nossa estrutura didática.

No EngConvert, o arquivo poderá conter somente a docstring `"""Pacote principal do EngConvert."""`, sem lógica de conversão.

---

# 21. O que acontece quando usamos `import`?

Considere:

```python
import math
```

Estamos dizendo ao Python:

```text
localize o módulo
      ↓
carregue-o
      ↓
disponibilize o nome math
```

Depois:

```python
math.sqrt(25)
```

No nosso projeto poderemos ter:

```python
from engconvert.conversoes import converter
```

---

# 22. `import modulo`

Primeira forma:

```python
import math
```

Uso:

```python
resultado = math.sqrt(25)
```

Vantagem:

```text
fica explícito
de onde veio sqrt
```

---

# 23. `from modulo import nome`

Outra forma:

```python
from math import sqrt
```

Uso:

```python
resultado = sqrt(25)
```

No EngConvert:

```python
from engconvert.conversoes import converter
```

e depois:

```python
resultado = converter(...)
```

---

# 24. Como ler `from ... import ...` corretamente?

Considere novamente:

```python
from math import sqrt
```

É comum, no início, tentar ler esse comando como:

```text
"importe a classe sqrt
da biblioteca math"
```

Essa leitura possui uma ideia correta:

```text
estamos trazendo sqrt
a partir de math
```

Mas existem dois problemas de terminologia:

```text
sqrt
```

não é uma classe. Nesse caso, `sqrt` é uma:

```text
FUNÇÃO
```

E:

```text
math
```

é, mais precisamente, um:

```text
MÓDULO
```

que faz parte da:

```text
BIBLIOTECA PADRÃO DO PYTHON
```

Portanto, para esse exemplo, uma leitura precisa é:

> **“Do módulo `math`, importe a função `sqrt`.”**

---

# 25. Uma leitura universal para `from ... import ...`

Existe uma forma geral e segura de interpretar essa sintaxe.

Considere:

```python
from X import Y
```

Podemos ler:

> **“De `X`, importe o nome `Y`.”**

Essa é uma leitura universal porque primeiro identifica o **nome importado**, sem classificá-lo incorretamente como função ou classe.

Depois verificamos o que `X` e `Y` representam naquele contexto.

De forma geral:

```text
X pode ser
    ↓
módulo
ou
pacote
```

E o nome `Y` pode representar diferentes objetos, como:

```text
função
classe
constante
variável
módulo / submódulo
pacote / subpacote
ou outro objeto disponibilizado por X
```

> 📌 **Ideia-chave:** depois de `import`, não devemos chamar automaticamente o nome importado de função ou de classe. Primeiro identificamos o **nome**; depois classificamos o objeto quando sabemos o que ele representa.

---

# 26. Leitura universal × leitura específica

Considere:

```python
from math import sqrt
```

A leitura universal é:

> **“De `math`, importe o nome `sqrt`.”**

Agora identificamos os elementos:

```text
math
  ↓
módulo

sqrt
  ↓
função
```

Então podemos utilizar uma leitura mais específica:

> **“Do módulo `math`, importe a função `sqrt`.”**

Compare com:

```python
from tkinter import Button
```

Nesse caso:

```text
tkinter
   ↓
módulo

Button
   ↓
classe
```

Logo:

> **“Do módulo `tkinter`, importe a classe `Button`.”**

Outro exemplo:

```python
from math import pi
```

Nesse caso, `pi` é um nome disponibilizado pelo módulo `math` e associado ao valor da constante matemática π.

Portanto, podemos dizer:

> **“Do módulo `math`, importe `pi`.”**

---

# 27. Módulo × pacote × biblioteca

Neste ponto, é importante distinguir:

```text
MÓDULO
PACOTE
BIBLIOTECA
```

Eles estão relacionados, mas não significam exatamente a mesma coisa.

---

# 28. Módulo

Didaticamente, podemos pensar:

> **Módulo é uma unidade de código Python que pode ser importada.**

Frequentemente, um módulo corresponde a um arquivo:

```text
arquivo.py
```

Por exemplo:

```text
conversoes.py
```

pode conter:

```python
def converter_pressao(valor):
    ...
```

Outro módulo poderá utilizar:

```python
import conversoes
```

ou:

```python
from conversoes import converter_pressao
```

Nesse exemplo:

```text
conversoes
      ↓
módulo

converter_pressao
      ↓
função
```

---

# 29. Pacote

Um pacote permite organizar módulos e, quando necessário, outros subpacotes relacionados.

Podemos pensar inicialmente:

```text
PACOTE
  │
  ├── módulo
  ├── módulo
  └── subpacote
```

No EngConvert utilizaremos um pacote para reunir os módulos responsáveis pelas diferentes partes da aplicação.

O exemplo concreto da estrutura do EngConvert será apresentado uma única vez no item **33 — Aplicando ao EngConvert**.

---

# 30. Biblioteca

O termo:

```text
BIBLIOTECA
```

é mais amplo.

Podemos pensar em uma biblioteca como:

> **uma coleção organizada de código reutilizável criada para disponibilizar determinadas funcionalidades.**

Uma biblioteca pode reunir:

```text
módulos
pacotes
funções
classes
dados
e outros recursos
```

Diferentemente de **módulo** e **pacote**, “biblioteca” é um termo mais geral do desenvolvimento de software e não representa uma única unidade estrutural específica da linguagem Python.

---

# 31. Relação conceitual

Uma representação didática útil é:

```text
BIBLIOTECA
    │
    ├── PACOTES
    │      │
    │      ├── MÓDULOS
    │      │      │
    │      │      ├── funções
    │      │      ├── classes
    │      │      └── outros nomes/objetos
    │      │
    │      └── subpacotes
    │
    └── outros recursos
```

Esse diagrama apresenta uma **visão conceitual geral**.

Ele ajuda a perceber que uma biblioteca pode reunir estruturas menores e reutilizáveis, como pacotes e módulos, e que os módulos podem disponibilizar funções, classes e outros objetos.

> 📌 **Atenção:** essa hierarquia é uma **representação didática** para compreender a relação entre os conceitos. “Biblioteca” é um termo mais amplo e não exige que toda biblioteca Python possua exatamente essa estrutura.

---

# 32. A Biblioteca Padrão do Python

O Python acompanha uma grande coleção de módulos e pacotes conhecida como:

```text
Python Standard Library
```

ou:

```text
Biblioteca Padrão do Python
```

Entre seus recursos encontramos, por exemplo:

```text
math
random
statistics
pathlib
datetime
...
```

Nesse contexto:

```text
math
   ↓
módulo da Biblioteca Padrão do Python
```

e:

```text
sqrt
   ↓
função disponibilizada pelo módulo math
```

Portanto:

```python
from math import sqrt
```

pode ser lido especificamente como:

> **“Do módulo `math`, importe a função `sqrt`.”**

---

# 33. Aplicando ao EngConvert

Agora aplicamos os conceitos ao nosso projeto.

A estrutura planejada é:

```text
src/
└── engconvert/             ← pacote
    │
    ├── __init__.py
    ├── dados.py            ← módulo
    ├── conversoes.py       ← módulo
    └── interface.py        ← módulo
```

Portanto:

```text
engconvert
     ↓
pacote
```

e:

```text
dados.py
conversoes.py
interface.py
     ↓
módulos do pacote
```

Se escrevermos:

```python
from engconvert.conversoes import converter
```

a leitura universal será:

> **“De `engconvert.conversoes`, importe o nome `converter`.”**

Depois identificamos:

```text
engconvert
     ↓
pacote

conversoes
     ↓
módulo

converter
     ↓
função
```

Assim, conhecendo a estrutura, podemos utilizar a leitura específica:

> **“Do módulo `engconvert.conversoes`, importe a função `converter`.”**

---

# 34. Regra didática para leitura de importações

Ao encontrar:

```python
from X import Y
```

utilize primeiro a leitura universal:

> **“De `X`, importe o nome `Y`.”**

Depois pergunte:

```text
O que é X?
     ↓
módulo ou pacote?

O que é Y?
     ↓
função?
classe?
constante?
variável?
módulo / submódulo?
pacote / subpacote?
outro objeto?
```

Exemplo:

```python
from math import sqrt
```

```text
math
   ↓
módulo

sqrt
   ↓
função
```

Então:

> **“Do módulo `math`, importe a função `sqrt`.”**

Essa sequência evita associações incorretas como:

```text
tudo depois de import
é uma função
```

ou:

```text
tudo depois de import
é uma classe
```

E estabelece um padrão de leitura que continuará válido quando o EngConvert passar a utilizar seus próprios módulos e pacotes.

---

# 35. Evitar `import *`

Python permite:

```python
from modulo import *
```

Mas evitaremos essa forma.

Por quê?

Porque ela torna menos claro:

```text
quais nomes foram importados
de onde vieram
se existem conflitos
```

Prefira importações explícitas.

---

# 36. Módulo `dados.py`

Esse módulo poderá armazenar informações como:

```text
grandezas
unidades
fatores de conversão
```

Conceitualmente, o dicionário já existente no `main.py` associa cada grandeza aos fatores correspondentes:

```python
grandezas = {
    "Pressão": fatores_pressao,
    "Comprimento": fatores_comprimento,
    "Área": fatores_area,
    "Volume": fatores_volume
}
```

As definições completas dos fatores serão copiadas na Aula 08.1; não se trata de um novo dicionário a ser criado.

O objetivo de `dados.py` é responder:

```text
QUAIS DADOS
DE CONVERSÃO EXISTEM?
```

---

# 37. Convenções de nomes: minúsculas e constantes

Em Python, nomes em maiúsculas (por exemplo, `PI` ou `GRAVIDADE`) são utilizados, por convenção, para valores que não se pretende modificar durante a execução. Essa convenção não torna automaticamente um objeto imutável.

No **EngConvert**, entretanto, o dicionário real já se chama `grandezas`, em minúsculas, assim como `fatores_pressao`, `fatores_comprimento`, `fatores_area` e `fatores_volume`.

**Preservaremos esses nomes na refatoração.** A modularização altera a organização do código, não exige renomear variáveis nem modificar os valores das unidades.

---

# 38. Módulo `conversoes.py`

Esse módulo ficará responsável pelas regras matemáticas.

Por exemplo:

```python
def converter_por_fator(...):
    ...
```

```python
def converter_temperatura(...):
    ...
```

```python
def converter(...):
    ...
```

Sua pergunta principal é:

```text
COMO CONVERTER?
```

---

# 39. O módulo de conversões não precisa conhecer widgets

Uma regra importante para nossa arquitetura:

```text
conversoes.py
```

não deveria precisar saber o que é:

```text
CTkButton
CTkEntry
CTkComboBox
CTkLabel
```

Ele recebe dados:

```text
valor
grandeza
unidade de origem
unidade de destino
```

e devolve:

```text
resultado
```

---

# 40. Função pura — primeira aproximação

Considere:

```python
def converter_por_fator(valor, fator_origem, fator_destino):
    return valor * fator_origem / fator_destino
```

Essa função:

```text
recebe valores
      ↓
calcula
      ↓
retorna resultado
```

Ela não precisa:

```text
abrir janela
ler Entry
alterar Label
mostrar mensagem
```

Funções assim são particularmente fáceis de testar.

---

# 41. Interface e regra de negócio

Compare:

```text
INTERFACE
   ↓
ler texto digitado
selecionar unidades
mostrar resultado
```

com:

```text
REGRA DE NEGÓCIO
   ↓
calcular a conversão
```

Queremos evitar:

```text
GUI + cálculo
misturados em toda parte
```

---

# 42. Módulo `interface.py`

Esse módulo concentrará:

```text
janela
frames
labels
entries
comboboxes
buttons
eventos da interface
layout
```

Sua pergunta é:

```text
COMO O USUÁRIO
INTERAGE COM O PROGRAMA?
```

---

# 43. Dependência desejada

Queremos algo próximo de:

```text
interface.py
     │
     │ usa
     ▼
conversoes.py
     │
     │ usa
     ▼
dados.py
```

Enquanto:

```text
dados.py
```

não precisa conhecer a interface.

---

# 44. `main.py`

Depois da modularização, o `main.py` deverá ficar muito menor.

Sua responsabilidade será aproximadamente:

```text
INICIAR A APLICAÇÃO
```

Conceitualmente:

```python
from engconvert.interface import iniciar_aplicacao

iniciar_aplicacao()
```

Em vez de conter toda a implementação.

---

# 45. Ponto de entrada

Chamamos de:

```text
ENTRY POINT
```

ou:

```text
PONTO DE ENTRADA
```

o local pelo qual iniciamos a aplicação.

No nosso projeto:

```text
main.py
```

continuará funcionando como ponto de entrada didático.

Assim o aluno poderá continuar executando:

```bash
python main.py
```

---

# 46. `__name__`

Python define automaticamente uma variável especial:

```python
__name__
```

Ela ajuda a identificar como um módulo está sendo utilizado.

Quando um arquivo é executado diretamente:

```text
__name__ == "__main__"
```

Quando ele é importado, `__name__` assume o nome correspondente ao módulo.

---

# 47. `if __name__ == "__main__":`

Uma estrutura muito comum é:

```python
if __name__ == "__main__":
    iniciar_aplicacao()
```

Podemos ler:

```text
SE este arquivo
está sendo executado diretamente
        ↓
inicie a aplicação
```

---

# 48. Por que isso é útil?

Sem essa proteção, um código de inicialização pode executar simplesmente porque o arquivo foi importado.

Queremos separar:

```text
DEFINIR
funções/classes
```

de:

```text
EXECUTAR
a aplicação
```

Assim:

```python
def main():
    iniciar_aplicacao()


if __name__ == "__main__":
    main()
```

torna o ponto de entrada explícito.

---

# 49. Antes e depois

Antes:

```text
main.py
│
├── dados
├── funções
├── widgets
├── eventos
├── layout
└── mainloop
```

Depois:

```text
main.py
   ↓
inicia

src/engconvert/
│
├── dados.py
│      ↓
│    dados
│
├── conversoes.py
│      ↓
│    regras
│
└── interface.py
       ↓
     GUI
```

---

# 50. Fluxo de uma conversão depois da modularização

Imagine que o usuário digite:

```text
1 bar
```

e escolha:

```text
kPa
```

Fluxo:

```text
interface.py
      ↓
obtém:
1, Pressão, bar, kPa
      ↓
conversoes.py
      ↓
consulta dados necessários
      ↓
calcula
      ↓
retorna 100
      ↓
interface.py
      ↓
mostra:
100 kPa
```

---

# 51. O usuário percebe a modularização?

Idealmente:

```text
NÃO
```

A interface pode permanecer visualmente igual.

As mesmas conversões devem continuar funcionando.

Isso é uma característica importante da refatoração.

---

# 52. Importações absolutas

Dentro de uma estrutura de pacote, podemos utilizar importações explícitas a partir do pacote.

Exemplo:

```python
from engconvert.dados import grandezas
```

Isso é uma importação absoluta em relação ao pacote disponível no ambiente.

Ela deixa claro:

```text
de qual pacote
o objeto está vindo
```

---

# 53. Importações relativas

Dentro do próprio pacote também podemos encontrar:

```python
from .dados import grandezas
```

O ponto:

```text
.
```

indica:

```text
pacote atual
```

Assim:

```python
from .dados import grandezas
```

pode ser lido como:

```text
importe grandezas
do módulo dados
deste pacote
```

---

# 54. Qual utilizaremos?

Para iniciantes, priorizaremos uma organização consistente e importações fáceis de rastrear.

Na implementação prática definiremos um padrão para o projeto e o manteremos.

O mais importante é evitar uma mistura desnecessária de estilos.

---

# 55. Caminho de importação

Ao utilizar:

```python
from engconvert.conversoes import converter
```

o Python precisa conseguir localizar:

```text
engconvert
```

Isso nos leva a um assunto importante:

```text
COMO O PYTHON ENCONTRA MÓDULOS?
```

---

# 56. `sys.path` — conceito inicial

Python mantém uma lista de locais onde procura módulos.

Essa lista pode ser observada com:

```python
import sys

print(sys.path)
```

Não manipularemos `sys.path` manualmente como solução principal.

A ideia é apenas compreender que:

```text
import
  ↓
precisa localizar
o módulo/pacote
```

---

# 57. Por que não usar "gambiarras" de caminho?

É possível encontrar códigos como:

```python
import sys
sys.path.append("alguma/pasta")
```

Isso pode resolver situações específicas, mas não será nossa estratégia normal de arquitetura.

Queremos uma estrutura previsível.

> 📌 **Ideia-chave:** organizar corretamente o projeto é melhor do que espalhar correções manuais de caminho pelo código.

---

# 58. A estrutura `src` e a execução

Ao adotar:

```text
src/engconvert/
```

precisamos garantir que o pacote seja importável de forma consistente.

Na Aula 08.1 faremos isso cuidadosamente, sem simplesmente mover arquivos e esperar que tudo continue funcionando.

Essa é uma das razões para a modularização ser uma etapa própria.

---

# 59. Não mover tudo de uma vez

Uma estratégia perigosa seria:

```text
selecionar centenas de linhas
       ↓
recortar
       ↓
colar em vários arquivos
       ↓
executar
       ↓
descobrir dezenas de erros
```

Prefira:

```text
PASSOS PEQUENOS
       ↓
executar
       ↓
verificar
       ↓
commit
       ↓
próximo passo
```

---

# 60. Estratégia incremental

Podemos modularizar nesta ordem:

```text
1. criar estrutura
       ↓
2. mover dados
       ↓
3. testar
       ↓
4. mover conversões
       ↓
5. testar
       ↓
6. mover interface
       ↓
7. testar
       ↓
8. simplificar main.py
       ↓
9. testar tudo
```

---

# 61. Git entra diretamente nesta etapa

Agora Git deixa de ser apenas conteúdo da aula anterior.

Antes da refatoração:

```bash
git status
```

Depois:

```bash
git log --oneline
```

Confirme que existe uma versão funcional registrada.

---

# 62. Branch para modularização

Esta etapa é uma ótima oportunidade para utilizar uma branch real:

```bash
git switch -c feature-modularizacao
```

Agora:

```text
main
  │
  └── feature-modularizacao
```

A reorganização pode acontecer nessa nova linha de desenvolvimento.

---

# 63. Por que usar branch aqui?

Porque estamos prestes a realizar:

```text
MUDANÇA ESTRUTURAL IMPORTANTE
```

Se algo der errado:

```text
main
```

continua representando a versão anterior validada.

Isso transforma o conceito de branch em uma ferramenta necessária, e não apenas teórica.

---

# 64. Commits menores

Evite um único commit:

```text
refactor: muda tudo
```

Prefira etapas compreensíveis:

```text
refactor: cria estrutura do pacote

refactor: move dados de conversão

refactor: separa regras de conversão

refactor: separa interface gráfica

refactor: simplifica ponto de entrada
```

Isso produz um histórico mais útil.

---

# 65. Modularização e testes

Na próxima etapa do Roadmap teremos:

```text
Etapa 9 — Testes
```

A modularização prepara esse caminho.

Por exemplo, testar:

```python
converter_temperatura(0, "°C", "K")
```

é muito mais simples quando a função está isolada de:

```text
janela
botões
labels
mainloop
```

---

# 66. Dependência da interface

Queremos evitar funções de conversão assim:

```python
def converter():
    texto = entrada.get()
    unidade = combo.get()
    ...
    label.configure(...)
```

porque a função fica diretamente ligada à GUI.

Preferimos separar:

```python
def converter(valor, grandeza, unidade_de, unidade_para):
    ...
    return resultado
```

e deixar a interface fazer:

```text
ler
   ↓
chamar função
   ↓
receber resultado
   ↓
exibir
```

---

# 67. Entrada e saída das funções

Uma boa função de domínio deve deixar claro:

```text
ENTRADAS
   ↓
valor
grandeza
unidade origem
unidade destino

PROCESSAMENTO
   ↓
conversão

SAÍDA
   ↓
resultado
```

Isso facilita:

```text
leitura
reutilização
teste
manutenção
```

---

# 68. Tratamento de erros: onde fica?

Nem todo erro deve ser tratado no mesmo lugar.

Exemplo:

```text
texto inválido digitado pelo usuário
```

é fortemente relacionado à interação.

Já:

```text
unidade inexistente
```

pode ser detectada pela lógica de conversão.

Precisamos decidir conscientemente:

```text
quem detecta?
quem gera o erro?
quem apresenta a mensagem?
```

---

# 69. Exceções atravessando camadas

Uma possibilidade:

```text
conversoes.py
      ↓
detecta problema
      ↓
raise ValueError(...)
      ↓
interface.py
      ↓
except ValueError
      ↓
mostra mensagem ao usuário
```

Isso mantém:

```text
regra
```

separada de:

```text
apresentação do erro
```

---

# 70. Exemplo conceitual

Em `conversoes.py`:

```python
def converter(valor, grandeza, unidade_de, unidade_para):
    if grandeza not in grandezas:
        raise ValueError("Grandeza inválida.")

    ...
```

Na interface:

```python
try:
    resultado = converter(...)
except ValueError as erro:
    # apresentar o erro ao usuário
    ...
```

Assim cada módulo mantém sua responsabilidade.

---

# 71. Dados não são interface

O dicionário:

```python
grandezas
```

não precisa estar misturado ao código que cria:

```text
CTkComboBox
```

A interface apenas utiliza esses dados.

Isso permite, futuramente, usar as mesmas regras em outra interface.

---

# 72. E se no futuro existir outra interface?

Imagine:

```text
EngConvert Desktop
```

e futuramente:

```text
EngConvert Web
```

Se as regras estiverem isoladas:

```text
conversoes.py
```

elas poderão ser reutilizadas com mais facilidade.

A interface muda.

A matemática pode permanecer.

---

# 73. Arquitetura em camadas — primeira visão

Sem aprofundar padrões arquiteturais, podemos enxergar:

```text
┌────────────────────────────┐
│         INTERFACE          │
│        interface.py        │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│      REGRAS / LÓGICA       │
│       conversoes.py        │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│           DADOS            │
│          dados.py          │
└────────────────────────────┘
```

E:

```text
main.py
```

inicia o sistema.

---

# 74. Isso é MVC?

Ao observarmos a organização proposta para o EngConvert:

```text
interface.py
      ↓
conversoes.py
      ↓
dados.py
```

poderia surgir uma pergunta:

> **Essa separação significa que estamos utilizando o padrão MVC?**

Não necessariamente.

Separar um programa em módulos com responsabilidades diferentes é um **princípio geral de organização de software**.

Já padrões como MVC, MVP e MVVM propõem formas mais específicas de organizar as responsabilidades e a comunicação entre as partes de uma aplicação.

---

## MVC — Model, View, Controller

MVC significa:

```text
Model
View
Controller
```

ou:

```text
Modelo
Visão
Controlador
```

De forma simplificada:

```text
MODEL
   ↓
dados e regras da aplicação

VIEW
   ↓
interface apresentada ao usuário

CONTROLLER
   ↓
recebe/interpreta ações
e coordena Model e View
```

Uma representação didática seria:

```text
USUÁRIO
   ↓
 VIEW
   ↓
CONTROLLER
   ↓
 MODEL
```

Por exemplo, em um conversor de unidades:

```text
usuário clica em Converter
          ↓
       VIEW
          ↓
     CONTROLLER
          ↓
        MODEL
          ↓
realiza a conversão
          ↓
resultado retorna para a interface
```

---

## Então o EngConvert é MVC?

Neste momento:

```text
NÃO ESTAMOS IMPLEMENTANDO
FORMALMENTE O PADRÃO MVC
```

Nossa preocupação é mais fundamental:

```text
SEPARAR RESPONSABILIDADES
```

Estamos organizando:

```text
dados.py
      ↓
dados das unidades

conversoes.py
      ↓
regras de conversão

interface.py
      ↓
interface e interação

main.py
      ↓
inicialização
```

Existem semelhanças conceituais com arquiteturas como MVC, mas não criaremos artificialmente:

```text
Model
View
Controller
```

apenas para dizer que o projeto utiliza MVC.

> 📌 **Ideia-chave:** todo MVC envolve separação de responsabilidades, mas nem toda separação de responsabilidades significa que estamos utilizando MVC.

---

## Existem outros padrões?

Sim. Ao longo da evolução do desenvolvimento de software surgiram diferentes maneiras de organizar aplicações.

Alguns exemplos são:

| Padrão/arquitetura         | Ideia central                                                          |
| -------------------------- | ---------------------------------------------------------------------- |
| **MVC**                    | separa Modelo, Visão e Controlador                                     |
| **MVP**                    | utiliza um Presenter para intermediar a interface e a lógica           |
| **MVVM**                   | utiliza um ViewModel entre a interface e os dados/lógica               |
| **Clean Architecture**     | procura separar regras de negócio das tecnologias externas             |
| **Hexagonal Architecture** | procura isolar o núcleo da aplicação de interfaces e sistemas externos |

Não precisamos estudar esses padrões profundamente neste momento.

Eles aparecem aqui para mostrar que:

```text
organização de software
        ↓
pode evoluir
        ↓
para diferentes
padrões arquiteturais
```

No EngConvert, começaremos pelo princípio mais importante para o estágio atual:

```text
SEPARAÇÃO DE RESPONSABILIDADES
            ↓
dados
            ↓
regras de conversão
            ↓
interface
            ↓
inicialização
```

Somente devemos adotar uma arquitetura mais complexa quando ela resolver uma necessidade real do projeto.

---

# 75. Não criar arquitetura por vaidade

Mais arquivos não significam automaticamente código melhor.

Um projeto pode sofrer de:

```text
OVERENGINEERING
```

quando recebe complexidade arquitetural maior do que a necessidade real.

Queremos:

```text
organização suficiente
para o tamanho e objetivo
do EngConvert
```

---

# 76. Nem monolito gigante, nem fragmentação excessiva

Dois extremos:

```text
EXTREMO 1

main.py
5000 linhas
```

```text
EXTREMO 2

80 arquivos
com 3 linhas cada
```

Nosso objetivo está entre eles:

```text
módulos com
responsabilidades claras
```

---

# 77. Nomes dos módulos

Prefira nomes que indiquem função:

```text
dados.py
conversoes.py
interface.py
```

Evite nomes vagos:

```text
coisas.py
utils2.py
novo.py
funcoes_finais.py
arquivo.py
```

O nome do módulo deve ajudar a localizar responsabilidades.

---

# 78. O risco de `utils.py`

Um arquivo chamado:

```text
utils.py
```

pode parecer conveniente.

Mas frequentemente vira:

```text
utils.py
   │
   ├── função de conversão
   ├── função de arquivo
   ├── função de interface
   ├── validação
   ├── formatação
   └── qualquer outra coisa
```

Para nosso primeiro projeto modular, preferiremos nomes específicos.

---

# 79. Dependência circular

Um problema que pode surgir é:

```text
A importa B
e
B importa A
```

Exemplo:

```text
interface.py
      ↓ importa
conversoes.py
      ↓ importa
interface.py
```

Isso pode gerar:

```text
IMPORTAÇÃO CIRCULAR
```

Nossa arquitetura deve evitar esse ciclo.

---

# 80. Fluxo de dependências

Preferimos:

```text
main
  ↓
interface
  ↓
conversoes
  ↓
dados
```

e não:

```text
main ↔ interface ↔ conversoes ↔ dados ↔ main
```

A direção clara facilita compreender o sistema.

---

# 81. `main.py` não deve voltar a crescer

Depois da modularização, evite usar `main.py` novamente como destino de toda nova funcionalidade.

Ele deve permanecer próximo de:

```text
IMPORTAR
   ↓
INICIAR
```

Enquanto as funcionalidades pertencem aos módulos apropriados.

---

# 82. Documentação da arquitetura

Na pasta:

```text
docs/
```

podemos criar:

```text
arquitetura.md
```

Ela poderá registrar:

```text
estrutura de pastas
responsabilidade de cada módulo
fluxo de dependências
decisões arquiteturais
```

Isso ajuda o aluno a compreender que documentação não se limita ao README.

---

# 83. Diagrama inicial da arquitetura

Podemos registrar:

```text
main.py
   │
   ▼
interface.py
   │
   ▼
conversoes.py
   │
   ▼
dados.py
```

Responsabilidades:

```text
main.py
→ inicialização

interface.py
→ interação e apresentação

conversoes.py
→ regras de conversão

dados.py
→ unidades e fatores
```

---

# 84. Teste de regressão manual

Antes de modularizar, registre resultados conhecidos:

```text
1 bar → 100 kPa
1 m → 1000 mm
1 m² → 1 000 000 mm²
1 L → 1000 mL
1 gal (US) → 3,785411784 L
1 gal (UK) → 4,54609 L
0 °C → 32 °F
0 °C → 273,15 K
32 °F → 491,67 °R
0 K → 0 °R
```

Depois da modularização, repita os mesmos testes.

---

# 85. O que é regressão?

Uma **regressão** ocorre quando uma funcionalidade que funcionava deixa de funcionar após uma alteração.

Exemplo:

```text
ANTES
1 bar → 100 kPa ✓

refatoração
      ↓

DEPOIS
1 bar → 10 kPa ✗
```

Mesmo sem adicionar nova funcionalidade, podemos introduzir erros.

---

# 86. Por isso os testes vêm depois

A Etapa 9 formalizará:

```text
TESTES AUTOMATIZADOS
```

Mas nesta etapa já começaremos a pensar como testadores:

```text
antes
   ↓
resultado conhecido

mudança
   ↓

depois
   ↓
mesmo resultado
```

---

# 87. Modularização e responsabilidade do aluno

Durante a Aula 08.1, não queremos apenas:

```text
copiar novos arquivos
```

Queremos que o aluno consiga responder:

```text
Por que esta função está aqui?

Por que este dicionário foi movido?

Quem importa quem?

Qual arquivo inicia a aplicação?

Onde devo procurar um erro de conversão?

Onde devo procurar um erro visual?
```

---

# 88. Como decidir onde colocar um código?

Pergunte:

```text
ESTE CÓDIGO DEFINE DADOS?
        ↓
dados.py

ESTE CÓDIGO CALCULA CONVERSÕES?
        ↓
conversoes.py

ESTE CÓDIGO CRIA OU CONTROLA GUI?
        ↓
interface.py

ESTE CÓDIGO APENAS INICIA?
        ↓
main.py
```

Essa regra não resolve todos os projetos do mundo.

Mas é adequada ao EngConvert nesta etapa.

---

# 89. O que não faremos ainda?

Não precisamos introduzir agora:

```text
banco de dados
API
framework web
injeção de dependência
microserviços
ORM
Docker
arquiteturas empresariais complexas
```

Nada disso resolve o problema atual do EngConvert.

---

# 90. O que faremos na prática?

Na Aula 08.1:

```text
1. conferir Git
2. criar branch
3. criar src/engconvert
4. criar __init__.py
5. criar dados.py
6. mover dados
7. testar
8. criar conversoes.py
9. mover lógica
10. testar
11. criar interface.py
12. mover GUI
13. simplificar main.py
14. testar novamente
15. documentar arquitetura
16. criar commits
17. integrar a branch
18. enviar ao GitHub
```

---

# 91. Sprint prevista

A implementação será organizada como:

```text
SPRINT 07 — MODULARIZAÇÃO DO ENGCONVERT
```

Objetivos:

```text
[ ] preservar versão funcional
[ ] criar branch de modularização
[ ] criar estrutura src/engconvert
[ ] criar __init__.py
[ ] separar dados
[ ] separar regras de conversão
[ ] separar interface
[ ] simplificar main.py
[ ] verificar importações
[ ] executar testes manuais
[ ] documentar arquitetura
[ ] criar commits incrementais
[ ] integrar alterações
[ ] atualizar GitHub
```

---

# 92. Critério de sucesso

A Sprint estará correta se:

```text
ORGANIZAÇÃO INTERNA
       ↓
melhorou
```

enquanto:

```text
COMPORTAMENTO DO PROGRAMA
       ↓
permaneceu correto
```

Ou seja:

```text
MESMAS CONVERSÕES
+
MESMA INTERAÇÃO ESSENCIAL
+
CÓDIGO MAIS ORGANIZADO
```

---

# 93. Antes da Sprint

O estado esperado é:

```text
main
  │
  └── versão funcional
      publicada no GitHub
```

Então:

```bash
git status
```

deve indicar um estado limpo antes de iniciarmos a branch.

---

# 94. Durante a Sprint

A branch será:

```text
feature-modularizacao
```

Fluxo:

```text
main
  │
  ●
   \
    ●──●──●──●
    feature-modularizacao
```

Cada ponto poderá representar um commit coerente.

---

# 95. Depois da Sprint

Após validar:

```text
feature-modularizacao
        ↓
merge
        ↓
main
        ↓
push
        ↓
GitHub
```

Assim utilizaremos Git em uma situação real.

---

# 96. Relação com a próxima etapa

Depois da modularização:

```text
conversoes.py
```

terá funções que poderão ser chamadas diretamente por testes.

Então:

```text
Etapa 8 — Modularização
        ↓
Etapa 9 — Testes
```

deixa de ser apenas uma sequência arbitrária.

Uma etapa prepara a outra.

---

# 97. Visão de evolução

```text
ANTES

main.py
   ↓
tudo junto
```

```text
DEPOIS

main.py
   ↓
interface
   ↓
conversões
   ↓
dados
```

```text
PRÓXIMO

tests/
   ↓
testar conversões
automaticamente
```

---

# 98. Checklist conceitual

Antes da Aula 08.1, confirme se você consegue explicar:

```text
[ ] o que é modularização
[ ] o que é refatoração
[ ] o que é separação de responsabilidades
[ ] diferença entre arquivo, módulo e pacote
[ ] para que serve import
[ ] para que serve __init__.py
[ ] o que significa __name__
[ ] para que serve if __name__ == "__main__"
[ ] responsabilidade de dados.py
[ ] responsabilidade de conversoes.py
[ ] responsabilidade de interface.py
[ ] responsabilidade de main.py
[ ] por que modularização facilita testes
[ ] por que usar uma branch nesta etapa
```

---

# 99. Vocabulário essencial

| Termo            | Significado didático                                             |
| ---------------- | ---------------------------------------------------------------- |
| Modularização    | Divisão do programa em partes organizadas                        |
| Módulo           | Arquivo Python importável                                        |
| Pacote           | Organização de módulos relacionados                              |
| Refatoração      | Melhoria interna sem intenção de mudar o comportamento externo   |
| Responsabilidade | Função principal de uma parte do sistema                         |
| Coesão           | Relação entre elementos de um mesmo módulo                       |
| Acoplamento      | Dependência entre partes do sistema                              |
| Import           | Mecanismo para utilizar código de outro módulo                   |
| Entry point      | Ponto de entrada da aplicação                                    |
| Regressão        | Funcionalidade existente que deixa de funcionar após uma mudança |
| Branch           | Linha de desenvolvimento separada                                |
| Merge            | Integração das alterações de uma branch                          |

---

# 100. Mapa mental da etapa

```text
PROGRAMA CRESCE
      ↓
main.py concentra responsabilidades
      ↓
surge dificuldade de manutenção
      ↓
MODULARIZAÇÃO
      ↓
separar responsabilidades
      ↓
dados
regras
interface
entrada
      ↓
código mais testável
      ↓
Etapa 9 — Testes
```

---

# 101. Resumo da aula

Nesta aula compreendemos que modularização não significa simplesmente:

```text
CRIAR MAIS ARQUIVOS
```

Significa:

```text
ORGANIZAR RESPONSABILIDADES
```

A arquitetura planejada é:

```text
main.py
   │
   ▼
src/engconvert/
│
├── __init__.py
├── interface.py
├── conversoes.py
└── dados.py
```

Com responsabilidades:

```text
main.py
→ iniciar

interface.py
→ interagir

conversoes.py
→ calcular

dados.py
→ fornecer dados
```

---

# 102. Ideia-chave

```text
Um programa bem organizado
não é aquele que possui
o maior número de arquivos.

É aquele em que sabemos
onde cada responsabilidade
deve estar.
```

E:

```text
MODULARIZAÇÃO
      ↓
não muda o objetivo
do EngConvert

muda a forma
como seu código
é organizado
```

---

# 103. Próxima aula

## Aula 08.1 — Roteiro Prático

### Modularizando o EngConvert

Na próxima aula faremos:

```text
Git
 ↓
branch
 ↓
src/engconvert
 ↓
dados.py
 ↓
conversoes.py
 ↓
interface.py
 ↓
main.py simplificado
 ↓
testes manuais
 ↓
commits
 ↓
merge
 ↓
GitHub
```

---

# 🧭 Visão do percurso

```text
Aula 07.1
GitHub
   ↓
versão funcional protegida
   ↓
Aula 08.0
Modularização
   ↓
Aula 08.1
Sprint 07
   ↓
Etapa 8 — CONCLUÍDA
   ↓
Aula 09.0
Testes
```

> 🎯 **Ideia final:** até agora aprendemos a construir o EngConvert. A partir desta etapa começamos a aprender algo igualmente importante: **como organizar um software para que ele continue compreensível à medida que cresce**.

---

# APÊNDICE — Fundamentos complementares para a Aula 08.1

> **Orientação de estudo:** os conceitos básicos de módulos, importações, separação de responsabilidades, Git, testes e arquitetura já foram apresentados nas 103 seções anteriores. Este apêndice aprofunda apenas pontos necessários para compreender a implementação. **Não é um roteiro de comandos para executar agora.** O código integral e a sequência de trabalho estão na Aula 08.1.

## A. Por que a temperatura exige uma regra própria?

Pressão, comprimento, área e volume utilizam fatores em relação a uma unidade de referência. Uma conversão multiplicativa pode ser expressa como:

```python
def converter_por_fator(valor, fator_origem, fator_destino):
    return valor * fator_origem / fator_destino
```

Já a temperatura pode exigir um deslocamento de escala, além de multiplicação. Por exemplo:

```text
°C → °F : multiplicar por 9/5 e somar 32
°C → K  : somar 273,15
```

Por isso, `dados.py` armazena a lista `unidades_temperatura`, enquanto `conversoes.py` implementará a matemática específica. A lista de unidades não substitui as fórmulas.

## B. Função geral de conversão e interface gráfica

A função geral `converter(valor, grandeza, unidade_de, unidade_para)` decidirá entre a regra de temperatura e a regra multiplicativa. A interface, por sua vez, deverá coletar os dados digitados, chamar a função e apresentar o resultado.

```text
CTkEntry / CTkComboBox
          ↓
      interface.py
          ↓
      converter(...)
          ↓
      conversoes.py
          ↓
        dados.py
```

O nome `ao_converter` pode identificar o evento do botão, enquanto `converter` identifica a função matemática. Assim, evita-se misturar a ação de clicar com o cálculo de unidades.

## C. Escopo dos widgets e funções de evento

Ao reunir a construção da interface dentro de `iniciar_aplicacao()`, é preciso garantir que os eventos continuem acessando os widgets necessários. Uma solução simples é definir as funções de evento no escopo adequado, com acesso às referências utilizadas.

**Não é necessário introduzir uma classe `EngConvertApp` apenas para modularizar os arquivos.** Orientação a objetos poderá ser estudada separadamente, quando houver necessidade real.

## D. O papel de `pyproject.toml`

O arquivo `pyproject.toml` declara informações de configuração, construção e empacotamento de um projeto Python. Na estrutura adotada pelo EngConvert, ele ajuda a informar que os módulos importáveis estão dentro de `src/`.

Um exemplo de configuração é:

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "engconvert"
version = "0.1.0"
requires-python = ">=3.12"

[tool.setuptools.packages.find]
where = ["src"]
```

A versão mínima de Python declarada é uma escolha do projeto, não uma exigência universal do empacotamento.

## E. Instalação editável e importações

Na raiz do projeto, com o ambiente virtual ativo, a instalação em modo editável é realizada com:

```powershell
python -m pip install -e .
```

Nesse modo, o ambiente passa a reconhecer o pacote `engconvert`, enquanto os arquivos-fonte permanecem em `src/`. Alterações normais no código Python são refletidas sem reinstalar o pacote a cada edição; alterações em metadados ou dependências podem exigir nova instalação.

Dentro do pacote, uma importação relativa adequada é:

```python
from .dados import grandezas
```

Já no ponto de entrada `main.py`, localizado na raiz do projeto, pode-se utilizar:

```python
from engconvert.interface import iniciar_aplicacao
```

Evite resolver problemas de importação com alterações improvisadas de `sys.path`. Antes, confira a estrutura de pastas, o ambiente ativo e a instalação editável.

## F. Revisão e integração segura com Git

Durante a modularização, os commits devem representar **etapas funcionais significativas**, não cada pequena linha alterada. O Git permite preparar apenas os arquivos relacionados à etapa:

```powershell
git add src/engconvert/conversoes.py src/engconvert/interface.py main.py pyproject.toml
git --no-pager diff --cached --name-status
```

Esse exemplo é ilustrativo: antes de criar o commit, confira a lista real de arquivos preparados. **Evite `git add .` quando houver modificações locais de outras aulas ou documentos.**

O comando abaixo permite comparar a branch de trabalho com a base da `main`:

```powershell
git --no-pager diff main...feature-modularizacao
```

A integração por `merge` só deve ocorrer depois da validação funcional e da conferência do estado do repositório. Caso apareçam conflitos, analise cada arquivo e preserve o trabalho existente; não utilize comandos destrutivos para forçar a integração.

## G. Preparação para testes automatizados e integração contínua

Uma regra de conversão independente de widgets pode ser chamada diretamente:

```python
resultado = converter(1, "Pressão", "bar", "kPa")
```

O resultado esperado é `100`. Na próxima etapa, essa verificação poderá ser automatizada com `pytest`, usando testes que comparem resultados reais com valores esperados.

```text
funções independentes da GUI
            ↓
      testes com pytest
            ↓
   detecção de regressões
            ↓
   futura integração contínua
```

A configuração de CI, como GitHub Actions, não faz parte desta Sprint. O ganho imediato é tornar as funções matemáticas mais fáceis de verificar e manter.

---

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
