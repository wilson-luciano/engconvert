# Aula 10.0 — Interface Completa do EngConvert

## Planejamento da interface, preferências, abas e unidades personalizadas

**Disciplina:** Programação para Engenharia Mecânica  
**Projeto didático:** EngConvert — Conversor de Unidades de Engenharia  
**Etapa 10:** Interface Completa  
**Continuidade:** Aula 10.1 — Roteiro Prático

---

## 1. Objetivos de aprendizagem

Ao concluir a aula, o estudante deverá conseguir:

1. Distinguir **interface gráfica**, **experiência do usuário (UX)** e **regras de negócio**.
2. Interpretar as funções **General**, **Tabs**, **Custom** e **About** do Convert 4.10 como requisitos de referência, sem copiar seu código.
3. Justificar o uso de `CTkTabview`, `CTkScrollableFrame`, `CTkToplevel`, `CTkOptionMenu` e `CTkSwitch` conforme a finalidade.
4. Projetar a ampliação do EngConvert sem comprometer as cinco grandezas existentes.
5. Definir regras de precisão, notação científica e temperatura física válida.
6. Explicar como cadastrar e validar unidades personalizadas e salvá-las em JSON.
7. Diferenciar preferências, dados cadastrados e regras matemáticas.
8. Organizar o desenvolvimento em Sprints com critérios de aceitação e testes de regressão.

> **Projeto:** EngConvert — Conversor de Unidades de Engenharia  
> **Etapa:** 10 — Interface Completa  
> **Pré-requisito:** Aulas 09.0 e 09.1 (testes com `pytest`)  
> **Status:** Material conceitual e de planejamento; **não é o roteiro de implementação**.  
> **Continuidade:** Aula 10.1 — implementação incremental e Git/GitHub.

---

## 2. Onde estamos no Roadmap?

```text
01–06  Construção do conversor e das cinco grandezas
   ↓
07     Git e GitHub
   ↓
08     Modularização
   ↓
09     Testes automatizados
   ↓
10     Interface completa e recursos avançados  ← AGORA
   ↓
11     Distribuição do aplicativo
```

O software já possui uma base funcional. A prioridade agora é **melhorar sua utilização e permitir crescimento controlado**, não reescrever cálculos que já funcionam.

---

## 3. A questão orientadora

> Como transformar um conversor didático de cinco grandezas em uma aplicação configurável e extensível, sem perder a clareza, a confiabilidade dos cálculos e a facilidade de manutenção?

A resposta exige **planejamento de requisitos**, **separação de responsabilidades**, **validação de dados** e **testes de regressão**.

---

## 4. O ponto de partida: arquivos efetivos da Aula 08.1

```text
engconvert/
├── main.py                  # inicialização
├── pyproject.toml           # configuração do projeto
├── src/
│   └── engconvert/
│       ├── __init__.py
│       ├── dados.py         # unidades e fatores
│       ├── conversoes.py    # regras matemáticas
│       └── interface.py     # interface CustomTkinter
└── tests/
    └── test_conversoes.py   # testes da Aula 09.1
```

**Não** vamos alterar as aulas congeladas. A Aula 10.1 trabalhará sobre uma **nova branch**, preservando os arquivos como ponto de partida. Os nomes acima são os existentes na etapa anterior; os novos módulos abaixo são **propostas**, não arquivos já implementados.

---

## 5. Referência funcional: Convert 4.10

As imagens apresentadas do Convert 4.10 mostram uma janela com categorias de grandezas e as janelas **Options → General**, **Options → Tabs**, **Options → Custom** e **About**.

**General:** precisão, notação científica e aviso para temperaturas incompatíveis com zero absoluto.  
**Tabs:** exibição e ordenação de categorias.  
**Custom:** inclusão de unidades e fatores definidos pelo usuário.  
**About:** versão, autoria e créditos.

Vamos estudar essas **funcionalidades**, não reproduzir a aparência antiga nem assumir acesso ao código-fonte do programa original. O EngConvert terá identidade própria.

---

## 6. Interface gráfica (GUI) versus experiência do usuário (UX)

**GUI — Graphical User Interface (Interface Gráfica do Usuário):** elementos visíveis e interativos, como botões, caixas de texto e abas.

**UX — User Experience (Experiência do Usuário):** facilidade para realizar tarefas, compreender resultados, corrigir erros e confiar no aplicativo.

```text
GUI: "onde está o botão?"
UX:  "o usuário consegue converter corretamente e sem confusão?"
```

Uma interface bonita, mas que mistura galão americano e imperial sem identificação, produz uma experiência inadequada para engenharia.

---

## 7. Requisitos funcionais e não funcionais

**Funcionais:** ações que o software deve executar: converter, inverter unidades, selecionar grandezas, salvar preferências e cadastrar uma unidade personalizada.

**Não funcionais:** propriedades de qualidade: legibilidade, desempenho, manutenção, robustez, compatibilidade com Windows, acessibilidade e confiabilidade numérica.

| Tipo          | Exemplo                  | Como verificar                    |
| ------------- | ------------------------ | --------------------------------- |
| Funcional     | ocultar uma categoria    | categoria desaparece da navegação |
| Funcional     | salvar precisão          | valor persiste após reiniciar     |
| Não funcional | mensagens compreensíveis | teste de uso e revisão textual    |
| Não funcional | não quebrar conversões   | `pytest` e testes manuais         |

---

## 8. Separação entre núcleo de cálculo e interface

```text
USUÁRIO
   ↓
INTERFACE  ← eventos, campos, abas e mensagens
   ↓
SERVIÇOS/REGRAS  ← validação, conversão, configuração
   ↓
DADOS  ← unidades, fatores, preferências
```

A interface **não** deve recriar as fórmulas matemáticas. Ela solicita a conversão à camada responsável. Isso permite testar o cálculo sem abrir janelas.

---

## 9. O que é uma aba (tab)?

Uma **aba** agrupa conteúdo por assunto dentro da mesma janela. O componente `CTkTabview` do CustomTkinter permite criar páginas selecionáveis.

```text
[ Pressão ] [ Comprimento ] [ Área ] [ Volume ] [ Temperatura ]
┌───────────────────────────────────────────────────────┐
│ Conteúdo da categoria selecionada                     │
└───────────────────────────────────────────────────────┘
```

O uso de abas pode ser confortável para poucas categorias; com dezenas de categorias, uma única faixa de abas pode ficar sobrecarregada. **Não existe obrigação de colocar todas as grandezas em abas.**

---

## 10. Tabs: três decisões distintas

É importante não confundir:

1. **Navegação:** como o usuário escolhe a grandeza (abas, lista, pesquisa).
2. **Visibilidade:** quais grandezas aparecem.
3. **Ordem:** em que sequência aparecem.

O painel **Options → Tabs** do Convert é referência para **visibilidade e ordem**. No EngConvert, podemos combinar abas para favoritas e uma lista/pesquisa para o catálogo completo.

---

## 11. CTkTabview, CTkScrollableFrame e CTkComboBox

| Componente           | Finalidade                 | Uso provável                    |
| -------------------- | -------------------------- | ------------------------------- |
| `CTkTabview`         | alternar páginas           | categorias ou preferências      |
| `CTkScrollableFrame` | conteúdo longo com rolagem | lista de categorias disponíveis |
| `CTkComboBox`        | escolher entre opções      | unidade de origem/destino       |
| `CTkEntry`           | digitar texto              | valor, nome de unidade          |
| `CTkButton`          | executar ação              | converter, salvar, restaurar    |
| `CTkSwitch`          | ativar/desativar           | notação científica, avisos      |
| `CTkToplevel`        | janela secundária          | preferências, sobre             |

Esses nomes são **componentes da biblioteca CustomTkinter**, não novas bibliotecas independentes.

---

## 12. Uma proposta de navegação para o EngConvert

```text
┌──────────────────────────────────────────────────────────┐
│ EngConvert                       ⚙ Preferências  Sobre  │
├──────────────────────────────────────────────────────────┤
│ [Favoritas] [Todas as grandezas]                         │
│ Grandeza: [Pressão                         ▼]            │
│ De:       [bar          ▼]  ↔  Para: [kPa       ▼]       │
│ Valor:    [1                ]                            │
│                     [ Converter ]                        │
│ Resultado: 100 kPa                                       │
└──────────────────────────────────────────────────────────┘
```

**Esboço conceitual:** a implementação visual definitiva será definida e validada na Aula 10.1. O exemplo mantém os recursos que já existem e adiciona pontos de entrada para preferências e ajuda.

---

## 13. Visibilidade não é exclusão de dados

Quando o usuário desmarca “Área” na lista de abas, **a grandeza não deve ser apagada** do catálogo nem perder seus fatores.

```text
CATÁLOGO DE GRANDEZAS ── permanece completo
         ↓
PREFERÊNCIAS DO USUÁRIO ── escolhem o que mostrar
         ↓
INTERFACE ── apresenta somente o selecionado
```

Essa distinção evita perda de informação e simplifica restaurar o padrão.

---

## 14. Reordenar categorias

Uma opção é disponibilizar botões **Subir** e **Descer**. Internamente, a preferência pode ser uma lista ordenada:

```python
ordem_categorias = [
    "Pressão", "Temperatura", "Comprimento", "Área", "Volume"
]
```

O sistema precisa impedir duplicatas e lidar com categorias adicionadas em versões futuras. O botão **Restaurar padrão** deve recuperar uma ordem conhecida.

---

## 15. Preferências gerais: General

O painel General reúne configurações de **apresentação** e **avisos**:

- quantidade de algarismos na saída;
- notação científica;
- mensagens sobre temperatura abaixo do zero absoluto;
- eventualmente modo claro/escuro.

É essencial distinguir **precisão de exibição** de **precisão interna do cálculo**.

---

## 16. Precisão numérica: cálculo versus exibição

O EngConvert anterior exibe resultados com formatação semelhante a:

```python
f"{resultado:.6g}"
```

O formato `.6g` significa **seis algarismos significativos**, e não seis casas decimais. Exemplo:

```python
valor = 123.456789
print(f"{valor:.6g}")  # 123.457
print(f"{valor:.6f}")  # 123.456789
```

No projeto, o número de algarismos significativos exibidos poderá ser configurável. **Não arredonde o resultado interno antes de realizar outras operações.**

---

## 17. Algarismos significativos versus casas decimais

| Número    | `.3f` (três casas) | `.3g` (três algarismos significativos) |
| --------- | -----------------: | -------------------------------------: |
| 12.34567  |             12.346 |                                   12.3 |
| 0.0123456 |              0.012 |                                 0.0123 |
| 12345.6   |          12345.600 |                               1.23e+04 |

O formato `g` pode optar automaticamente por notação exponencial conforme a magnitude. A opção “usar notação científica” exige especificar **quando** usá-la e **qual formato** mostrar.

---

## 18. Notação científica

Em engenharia, valores muito pequenos e muito grandes são comuns:

```text
0,000001 m³ = 1 × 10⁻⁶ m³
1000000 Pa  = 1 × 10⁶ Pa
```

Python permite:

```python
valor = 0.000001
print(f"{valor:.3e}")  # 1.000e-06
```

A opção poderá oferecer `Automática`, `Científica` e `Decimal`, desde que o comportamento de cada modo seja explicado. A escolha modifica a **representação**, não a conversão matemática.

---

## 19. Zero absoluto: um limite físico

A escala kelvin não admite temperaturas termodinâmicas negativas no domínio usual do EngConvert.

```text
0 K = −273,15 °C = −459,67 °F = 0 °R
```

**Atenção:** Rankine (`°R`) é escala absoluta; não confundir com Réaumur. Ao converter uma entrada abaixo do zero absoluto, o software deve aplicar uma política explícita: **bloquear a conversão** ou **avisar claramente**. Para a etapa de interface, recomendamos validar o domínio físico e explicar o motivo do erro.

A configuração “mostrar aviso” **não deve ser interpretada como autorização para aceitar resultados fisicamente inválidos**.

---

## 20. Validação da entrada numérica

A entrada `CTkEntry` devolve texto. Antes de converter, o aplicativo precisa tratar:

```text
"12.5"    → número válido
"abc"     → entrada inválida
""        → campo vazio
"1e6"     → notação científica válida
"nan"     → requer rejeição explícita
"inf"     → requer rejeição explícita
```

`float("nan")` e `float("inf")` não geram `ValueError`; portanto, uma verificação de finitude (`math.isfinite`) é necessária quando a aplicação não aceita esses valores. Separar **erro de entrada** de **erro de conversão** melhora as mensagens.

---

## 21. Preferências persistentes

**Persistência** significa manter dados após encerrar e reabrir o aplicativo.

```text
usuário muda precisão
        ↓
preferências salvas em arquivo
        ↓
fecha o aplicativo
        ↓
abre novamente
        ↓
precisão restaurada
```

As preferências devem ficar fora dos módulos que definem as fórmulas. A implementação poderá utilizar JSON.

---

## 22. O que é JSON?

**JSON — JavaScript Object Notation** é um formato textual de troca/armazenamento de dados, amplamente utilizado também por programas Python.

```json
{
  "precisao": 7,
  "modo_numerico": "automatico",
  "aviso_zero_absoluto": true,
  "categorias_visiveis": [
    "Pressão",
    "Comprimento",
    "Área",
    "Volume",
    "Temperatura"
  ]
}
```

JSON não executa código Python. Valores lógicos são escritos `true` e `false` (minúsculos), diferentemente de `True` e `False` em Python.

---

## 23. Não salvar preferências dentro do código-fonte

Evite editar `dados.py` ou `interface.py` para memorizar escolhas do usuário.

```text
CÓDIGO DO PROGRAMA  ≠  PREFERÊNCIAS DO USUÁRIO
```

Para um aplicativo Windows distribuído, é preferível uma pasta de dados do usuário, com caminho apropriado, em vez de escrever ao lado do executável, que pode estar em local sem permissão de escrita. A Aula 10.1 decidirá a implementação concreta.

---

## 24. O que significa Custom?

No Convert 4.10, a seção Custom permite definir unidades e fatores. No EngConvert, propomos **cadastro de unidades personalizadas**, associado a uma grandeza existente, com regras de validação.

Exemplo: cadastrar uma unidade de vazão **somente depois de existir a grandeza Vazão volumétrica**; não devemos misturar unidades de grandezas físicas diferentes.

---

## 25. Uma grandeza não é uma unidade

```text
GRANDEZA: Pressão
UNIDADES: Pa, kPa, bar, psi, ...

GRANDEZA: Volume
UNIDADES: m³, L, gal (US), gal (UK), ...
```

Um usuário não deve cadastrar `psi` como unidade de comprimento nem `L/min` como unidade de volume: `L/min` é unidade de **vazão volumétrica**. Essa verificação é essencial para coerência dimensional.

---

## 26. Como funciona um fator de conversão

Para grandezas multiplicativas, cada unidade pode possuir um fator relativo a uma unidade de referência:

```text
1 bar = 100000 Pa
1 kPa = 1000 Pa
```

Fórmula:

$
V*{\mathrm{destino}} = V*{\mathrm{origem}}\,\frac{F*{\mathrm{origem}}}{F*{\mathrm{destino}}}
$

Exemplo:

$
1\,\mathrm{bar}\times\frac{100000\,\mathrm{Pa/bar}}{1000\,\mathrm{Pa/kPa}}=100\,\mathrm{kPa}
$

**Regra de cadastro:** o fator é a quantidade da **unidade de referência** correspondente a **uma unidade cadastrada**. Essa definição deve aparecer no formulário para evitar inversões.

---

## 27. Exemplo de unidade personalizada coerente

Suponha que o EngConvert permita incluir `yd` (jarda) na grandeza **Comprimento**.

```text
Grandeza: Comprimento
Unidade: yd
Referência: m
Fator: 0.9144
```

Portanto:

```text
1 yd = 0,9144 m
```

Essa unidade pode participar das mesmas regras multiplicativas usadas por metro, pé e polegada, desde que o cadastro seja validado.

---

## 28. Por que temperatura é diferente?

A relação entre Celsius e Fahrenheit envolve **deslocamento**, além de escala:

$
T*{^\circ\mathrm{F}}=\frac{9}{5}T*{^\circ\mathrm{C}}+32
$

Logo, não basta cadastrar um único fator multiplicativo para qualquer nova escala de temperatura. **Primeira versão do Custom:** aceitar apenas unidades multiplicativas em grandezas compatíveis. Fórmulas especiais são uma evolução futura, com projeto e validação próprios.

---

## 29. Validações indispensáveis no Custom

Antes de aceitar uma nova unidade, o sistema deve verificar:

1. Nome/símbolo não vazio.
2. Grandeza existente e compatível.
3. Símbolo sem duplicidade na grandeza (ou tratamento explícito de colisões).
4. Fator numérico **finito e maior que zero**.
5. Unidade de referência identificada e convenção do fator explicada.
6. Impedir alteração indevida das unidades-padrão.
7. Mensagem clara em caso de erro.
8. Possibilidade de desfazer/excluir uma unidade personalizada sem apagar as unidades originais.

**Exemplo inválido:** fator `0` causaria divisão por zero quando usado como destino.

---

## 30. Edição, exclusão e identidade de unidades

Uma unidade personalizada não deve ser identificada **apenas pela posição na lista**. Se o usuário mudar a ordem, isso não pode alterar seu significado.

Devemos distinguir:

```text
unidades originais → fornecidas pelo EngConvert
unidades customizadas → cadastradas pelo usuário
```

Ao editar ou excluir, o programa deve verificar se a operação atinge apenas o cadastro do usuário e não modifica silenciosamente a base padrão.

---

## 31. Como salvar unidades personalizadas

Exemplo conceitual de arquivo JSON:

```json
{
  "versao_esquema": 1,
  "unidades_personalizadas": [
    {
      "grandeza": "Comprimento",
      "simbolo": "yd",
      "referencia": "m",
      "fator": 0.9144
    }
  ]
}
```

O campo `versao_esquema` ajuda a evoluir o formato. **Ler JSON não significa confiar nele:** os dados devem ser validados novamente quando carregados.

---

## 32. O que fazer com JSON ausente ou corrompido?

Uma aplicação robusta precisa prever:

```text
arquivo não existe → iniciar com valores padrão
arquivo válido → carregar preferências/cadastros
arquivo inválido → avisar, preservar evidência e usar padrão seguro
```

Não sobrescreva silenciosamente um arquivo corrompido antes de permitir diagnóstico ou cópia de segurança. Na implementação, a gravação deve minimizar o risco de perda por interrupção.

---

## 33. About: identidade, versão e créditos

Uma janela **Sobre** pode conter:

```text
EngConvert
Conversor de Unidades de Engenharia
Versão do aplicativo
Tecnologias: Python e CustomTkinter
Autoria / instituição / licença (conforme definição do projeto)
Links para documentação e repositório
```

Não confunda versão do software com número da aula ou da Sprint. Créditos de bibliotecas e referências devem respeitar suas licenças e termos aplicáveis.

---

## 34. Menu e arquitetura de janelas

Proposta:

```text
EngConvert
├── Converter
├── Preferências
│   ├── Geral
│   ├── Categorias (Tabs)
│   └── Unidades personalizadas (Custom)
└── Ajuda
    └── Sobre
```

Uma janela de preferências pode utilizar `CTkToplevel` com um `CTkTabview` interno. A aplicação principal deve continuar acessível e coerente, evitando múltiplas janelas duplicadas de configuração.

---

## 35. Estado da interface: o que é?

**Estado** são os valores que determinam o que o usuário vê naquele momento:

```text
grandeza selecionada
unidade de origem
unidade de destino
valor digitado
resultado exibido
preferências atuais
```

Quando a grandeza muda, as unidades de origem e destino precisam ser atualizadas sem deixar uma seleção incompatível. Isso é uma **transição de estado**.

---

## 36. Eventos e atualização da interface

Exemplo de sequência:

```text
usuário seleciona "Volume"
        ↓
evento de alteração
        ↓
consultar unidades de Volume
        ↓
atualizar ComboBoxes
        ↓
definir seleção inicial válida
        ↓
limpar/atualizar resultado anterior
```

O evento **não** deve redefinir os fatores de conversão. Ele deve consultar os dados e coordenar os componentes visuais.

---

## 37. Tratamento de erros: informar sem assustar

Compare:

```text
ERRO!
```

com:

```text
Digite um número válido no campo Valor.
```

E, para cadastro:

```text
Não foi possível cadastrar "yd": já existe uma unidade
com esse símbolo na grandeza Comprimento.
```

Mensagens devem identificar o problema e orientar a correção, sem exibir rastreamentos técnicos de exceção para o usuário final.

---

## 38. Acessibilidade e legibilidade

Planeje:

- contraste suficiente em modo claro e escuro;
- fontes legíveis e dimensões que não cortem texto;
- ordem lógica de navegação por teclado;
- rótulos visíveis, não depender apenas de `placeholder`;
- unidades explícitas no resultado;
- mensagens que não dependam apenas de cor;
- áreas clicáveis adequadas.

Interface moderna não significa apenas trocar cores: significa **reduzir erros de uso**.

---

## 39. Responsividade da janela

O aplicativo deve ser testado em tamanhos de janela distintos e em escalas de exibição comuns no Windows.

`pack`, `grid` e frames permitem organizar layouts, mas devem ser usados conscientemente. **Não misture `pack` e `grid` no mesmo contêiner pai**; é possível utilizar gerenciadores diferentes em contêineres diferentes.

---

## 40. Escopo: novas grandezas entram agora?

O Convert original apresenta muitas grandezas além das cinco já existentes. Podemos ampliar o EngConvert, mas **não é aconselhável adicionar dezenas de categorias de uma vez**.

Critério sugerido:

1. manter e validar as cinco atuais;
2. implementar navegação e preferências;
3. selecionar novas grandezas prioritárias de engenharia (por exemplo, velocidade, força, energia, potência e vazão);
4. para cada grandeza, documentar unidade de referência, fatores, restrições e testes;
5. só depois expandir o catálogo.

Essas novas grandezas são **propostas para planejamento**, não recursos já implementados.

---

## 41. Rastreabilidade: requisito → código → teste

| Requisito             | Possível local de implementação    | Teste necessário                 |
| --------------------- | ---------------------------------- | -------------------------------- |
| precisão configurável | formatação + preferências          | valores pequenos e grandes       |
| ocultar categorias    | navegação + preferências           | ocultar sem excluir dados        |
| cadastro Custom       | serviço de unidades + persistência | fator válido/inválido, duplicata |
| zero absoluto         | validação física                   | entradas abaixo de 0 K           |
| janela Sobre          | interface                          | exibição correta de metadados    |

Os nomes dos novos arquivos serão definidos na Aula 10.1 conforme a necessidade, sem transformar esta tabela em arquitetura obrigatória.

---

## 42. Proposta de módulos adicionais

A estrutura **existente** da Aula 08.1 continua sendo a base. Se a complexidade justificar, poderemos criar:

```text
src/engconvert/
├── dados.py             # existente
├── conversoes.py        # existente
├── interface.py         # existente
├── preferencias.py      # PROPOSTO
├── persistencia.py      # PROPOSTO
└── unidades_custom.py   # PROPOSTO
```

**Não criar módulos por criar:** cada arquivo novo precisa representar uma responsabilidade real. Para a primeira versão, parte dessas funções pode ser reunida de maneira simples e coerente.

---

## 43. Estratégia incremental: uma mudança por vez

```text
branch de desenvolvimento
      ↓
implementar um recurso pequeno
      ↓
executar testes existentes
      ↓
adicionar testes do novo recurso
      ↓
validar GUI manualmente
      ↓
commit
      ↓
próximo recurso
```

Não devemos desenvolver General, Tabs e Custom simultaneamente antes de executar os testes. A **regressão** deve ser verificada a cada incremento.

---

## 44. Planejamento de Sprints da Etapa 10

| Sprint proposta | Foco               | Entrega verificável                               |
| --------------- | ------------------ | ------------------------------------------------- |
| 09              | Navegação e Tabs   | seleção, visibilidade e ordenação de categorias   |
| 10              | General            | precisão, formato numérico, avisos e persistência |
| 11              | Custom             | cadastro multiplicativo validado e salvo em JSON  |
| 12              | About e acabamento | créditos, documentação, revisão de usabilidade    |

**Numeração proposta:** as Sprints 09–12 poderão ser ajustadas quando construirmos os roteiros práticos. A Aula 10.1 não precisa necessariamente executar todas em uma única sessão; ela poderá introduzir a implementação e orientar a continuidade.

---

## 45. Critérios de aceitação para Tabs

Um recurso está pronto quando podemos demonstrar:

- [ ] categoria oculta não aparece na navegação;
- [ ] categoria oculta continua cadastrada;
- [ ] reordenar não duplica nem perde categorias;
- [ ] restaurar padrão recupera a ordem inicial;
- [ ] trocar categoria atualiza corretamente as unidades;
- [ ] os testes anteriores continuam passando.

---

## 46. Critérios de aceitação para General

- [ ] precisão selecionada altera somente a apresentação;
- [ ] notação científica funciona conforme a política documentada;
- [ ] configuração é restaurada após reiniciar;
- [ ] entradas não finitas são rejeitadas;
- [ ] temperatura abaixo do zero absoluto recebe tratamento explícito;
- [ ] valores e conversões já existentes continuam corretos.

---

## 47. Critérios de aceitação para Custom

- [ ] unidade cadastrada pertence a uma grandeza compatível;
- [ ] fator é finito e positivo;
- [ ] duplicatas são tratadas;
- [ ] unidades originais são protegidas;
- [ ] nova unidade pode ser usada em conversões;
- [ ] cadastro persiste após reiniciar;
- [ ] arquivo JSON inválido não derruba o aplicativo;
- [ ] testes verificam inclusão, edição, exclusão e conversão.

---

## 48. Critérios de aceitação para About

- [ ] exibe nome do aplicativo e versão;
- [ ] identifica corretamente autoria e créditos;
- [ ] links, quando incluídos, apontam para destinos válidos;
- [ ] janela abre e fecha sem interromper a conversão;
- [ ] conteúdo não é cortado na resolução testada.

---

## 49. Por que precisamos dos testes da Etapa 9?

As funções de conversão foram separadas da interface na Etapa 8 e passaram a receber testes automatizados na Etapa 9.

Isso permite modificar a interface sem revalidar cada fórmula apenas manualmente. **Entretanto, testes matemáticos não substituem testes de GUI**: botões, menus, visibilidade e persistência exigem verificações adicionais.

---

## 50. Testes unitários, integração e GUI

```text
UNITÁRIO
  → fator e cálculo de conversão

INTEGRAÇÃO
  → cadastro personalizado + leitura JSON + conversão

GUI / SISTEMA
  → usuário altera preferências e observa o resultado
```

Cada nível responde a perguntas diferentes. Um `pytest` aprovado para `converter()` não prova que o botão “Salvar preferências” funciona.

---

## 51. Testes de fronteira para engenharia

Exemplos relevantes:

| Recurso      | Caso de fronteira                                                   |
| ------------ | ------------------------------------------------------------------- |
| Pressão      | valor zero e valores negativos quando aplicáveis ao tipo de pressão |
| Temperatura  | exatamente 0 K e valores inferiores                                 |
| Fator Custom | zero, negativo, `nan`, `inf`                                        |
| Precisão     | mínimo/máximo configurado                                           |
| Categorias   | nenhuma visível, uma visível, todas visíveis                        |
| JSON         | arquivo ausente, vazio, malformado                                  |

**Importante:** pressão negativa pode ter significado em certos contextos (por exemplo, pressão manométrica); não imponha proibições físicas sem definir o tipo de grandeza e a convenção adotada.

---

## 52. Segurança: não executar fórmulas digitadas livremente

Na primeira versão do Custom, o usuário informará **fatores numéricos**, não expressões Python arbitrárias.

Evite:

```python
eval(texto_digitado)
```

Executar texto fornecido pelo usuário como código pode permitir comportamentos perigosos. Uma futura funcionalidade de fórmulas exigiria linguagem restrita, análise/validação e projeto próprio.

---

## 53. Versionamento e rastreabilidade no Git

Na implementação prática:

```bash
git status
git switch -c feature-interface-completa
```

São exemplos do fluxo esperado. O nome final da branch poderá refletir uma Sprint menor, como `feature-tabs`, para facilitar revisão.

```text
planejar → implementar → testar → commit → revisar → integrar
```

A Aula 10.0 apresenta o planejamento; a Aula 10.1 trará a sequência operacional completa de comandos, arquivos e testes.

---

## 54. Definition of Done: o que significa pronto?

**Definition of Done (DoD)** é um conjunto de condições para considerar uma tarefa concluída.

Para este projeto:

```text
[ ] requisito atendido
[ ] cálculo preservado
[ ] testes novos e antigos aprovados
[ ] mensagens de erro verificadas
[ ] GUI conferida manualmente
[ ] documentação atualizada
[ ] alterações registradas no Git
```

Uma janela “bonita” sem validação e testes ainda não está pronta.

---

## 55. O que ficará fora do escopo inicial

Para evitar complexidade excessiva, não planejamos nesta primeira entrega:

- mecanismo genérico de fórmulas arbitrárias;
- banco de dados remoto e autenticação de usuários;
- sincronização em nuvem;
- dezenas de novas grandezas simultaneamente;
- transformação forçada em MVC/MVVM;
- empacotamento final em `.exe` (Etapa 11).

Essa delimitação ajuda a concluir uma versão estável antes de crescer.

---

## 56. Exercício 1 — requisitos

Redija três requisitos funcionais e dois não funcionais para o painel **General**. Para cada requisito, escreva um critério de aceitação observável.

**Exemplo:** “Ao escolher precisão 4, o aplicativo apresenta quatro algarismos significativos na saída, mantendo o valor numérico interno.”

---

## 57. Exercício 2 — consistência dimensional

Analise os cadastros propostos:

1. `yd` na grandeza Comprimento, fator `0.9144` em relação ao metro.
2. `L/min` na grandeza Volume, fator `0.001` em relação ao metro cúbico.
3. `psi` na grandeza Pressão, fator `6894.757` em relação ao pascal.
4. `m` na grandeza Pressão, fator `1` em relação ao pascal.

Identifique os válidos, os inválidos e justifique dimensionalmente.

---

## 58. Exercício 3 — desenho de interface

Faça um esboço da tela de **Preferências** com três páginas:

```text
Geral | Categorias | Personalizadas
```

Indique onde o usuário altera precisão, reorganiza categorias, adiciona unidade, salva e cancela.

---

## 59. Exercício 4 — testes

Elabore cinco casos de teste para Custom, incluindo:

- um cadastro válido;
- símbolo duplicado;
- fator zero;
- fator não finito;
- arquivo de cadastro malformado.

Para cada caso, registre **entrada**, **resultado esperado** e **mensagem exibida**, quando aplicável.

---

## 60. Discussão: Custom e Tabs valem a pena?

**Sim**, desde que sejam implementados com objetivos claros:

**Tabs** melhora a navegação e a personalização de um catálogo crescente.  
**Custom** amplia a utilidade técnica, permitindo unidades específicas de equipamentos e processos.

Mas há riscos:

```text
mais opções
   ↓
mais estados e validações
   ↓
mais casos de teste
   ↓
mais responsabilidade de manutenção
```

Por isso, o crescimento será incremental.

---

## 61. Síntese da arquitetura proposta

```text
                    EngConvert
                        │
             ┌──────────┴──────────┐
             │                     │
          INTERFACE           PREFERÊNCIAS
             │                     │
        ┌────┴────┐           PERSISTÊNCIA
        │         │                │
   NAVEGAÇÃO   CONVERTER          JSON
                  │
               REGRAS
                  │
           DADOS + UNIDADES
                  │
         UNIDADES CUSTOMIZADAS
```

Diagrama **conceitual**, não indicação de que todos os blocos devem virar arquivos separados.

---

## 62. Resumo final da Aula 10.0

Nesta aula compreendemos:

1. A diferença entre interface e experiência do usuário.
2. O papel de **General**, **Tabs**, **Custom** e **About**.
3. A diferença entre precisão numérica e formatação de saída.
4. O significado físico do zero absoluto.
5. O conceito de persistência com JSON.
6. A necessidade de validar unidades personalizadas e dimensões físicas.
7. O planejamento de Sprints e critérios de aceitação.
8. A importância dos testes já criados na Etapa 9.

> **Ideia-chave:** uma interface completa não é a que oferece o maior número de botões, mas a que permite executar operações corretas, compreensíveis, verificáveis e extensíveis.

---

## 63. Próxima aula: 10.1 — roteiro prático

Na Aula 10.1, partiremos dos **arquivos efetivos** da Aula 09.1 e do código modularizado da Aula 08.1, sem modificar os materiais congelados.

O roteiro prático deverá apresentar:

- a branch e os commits da implementação;
- os arquivos `.py` completos após cada etapa relevante;
- a construção dos componentes CustomTkinter;
- as decisões de persistência em JSON;
- os testes automatizados e manuais;
- a documentação e a atualização do Roadmap.

**Atenção:** a execução integral de General, Tabs, Custom e About poderá ser distribuída por mais de uma Sprint. A 10.1 não deve sacrificar a didática tentando implementar tudo de uma vez.

---

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
