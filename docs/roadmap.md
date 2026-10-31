# Roadmap — EngConvert

## Visão do projeto

O **EngConvert (Engineering Unit Converter)** é um projeto didático da disciplina **Programação para Engenharia Mecânica**. Será desenvolvido de forma incremental, permitindo que o aluno compreenda cada evolução antes de adicionar novas camadas de complexidade.

O projeto parte de uma interface gráfica simples em Python e CustomTkinter e avança para um conversor de unidades organizado em módulos, com testes automatizados, interface completa e distribuição para Windows.

## Planejamento das Sprints

| Sprint | Objetivo principal | Referência didática |
| --- | --- | --- |
| 00 | Preparação do VSCode, Python, ambiente virtual, pip e estrutura inicial | Aulas 00 e 01 |
| 01–06 | Fundamentos de GUI, widgets e eventos, primeiros conversores, categorias, novas grandezas, Git e GitHub | Aulas 02 a 07; consultar os roteiros de cada etapa |
| **07** | **Modularização do EngConvert**, separando dados, conversões e interface | Aulas 08.0 e 08.1 |
| **08** | **Testes automatizados** das regras de conversão com `pytest` | Aulas 09.0 e 09.1 |
| **09** | **Navegação por abas**, visibilidade e ordenação das categorias | Aula 10.1 |
| **10** | Aba **General**, preferências e persistência em JSON | Aula 10.2 |
| **11** | Aba **Custom**, unidades personalizadas e validações | Aula 10.2 |
| **12** | Aba **About**, integração e verificações finais da interface | Aula 10.2 |
| A definir | Empacotamento com PyInstaller, executável Windows e publicação no GitHub Releases | Aulas 11.0 e 11.1 |

> **Nota de organização:** os números das **aulas** e das **Sprints** não são equivalentes. Por exemplo, a Aula 08 corresponde à Sprint 07; a Aula 10 abrange as Sprints 09 a 12. As Sprints iniciais devem ser consultadas nos respectivos roteiros, evitando atribuir uma correspondência artificial entre cada aula e cada Sprint.

## Etapas didáticas

| Etapa | Conteúdo | Situação da documentação |
| --- | --- | --- |
| 1–7 | Ambiente, interface inicial, widgets, conversores, novas grandezas e Git/GitHub | Aulas disponibilizadas no repositório |
| **8** | **Modularização e arquitetura** | Aulas 08.0 e 08.1 publicadas |
| **9** | **Fundamentos e testes com `pytest`** | Aulas 09.0 e 09.1 publicadas |
| **10** | **Interface completa, abas e personalização** | Aulas 10.0, 10.1 e 10.2 publicadas |
| **11** | **Empacotamento e distribuição** | Aulas 11.0 e 11.1 publicadas |

**Importante:** a publicação de uma aula ou roteiro não significa, por si só, que todas as funcionalidades descritas foram implementadas, testadas ou entregues. O progresso técnico deve ser acompanhado pelos commits, testes e registros de cada Sprint.

## Arquitetura prevista

A partir da modularização, o projeto utiliza uma estrutura semelhante a:

```text
engconvert/
├── main.py
├── pyproject.toml
├── requirements.txt
├── src/
│   └── engconvert/
│       ├── __init__.py
│       ├── dados.py
│       ├── conversoes.py
│       └── interface.py
├── tests/
├── aulas/
└── docs/
    └── sprints/
```

Os arquivos e pastas poderão evoluir conforme as Sprints seguintes, sem alterar retroativamente os materiais didáticos já congelados.

## Evolução planejada das grandezas

### Mecânica

Comprimento, área, volume, massa, tempo, velocidade, aceleração, força, torque, pressão, energia e potência.

### Fluidos

Vazão volumétrica, vazão mássica, densidade, viscosidade dinâmica e viscosidade cinemática.

### Térmica

Temperatura, calor específico, condutividade térmica e coeficiente de transferência de calor.

A inclusão dessas grandezas é um **planejamento de evolução**, não uma declaração de que todas já estão disponíveis no aplicativo.

## Critérios de conclusão de uma Sprint

Uma Sprint pode ser considerada concluída quando seu objetivo foi implementado, o comportamento esperado foi verificado, a documentação correspondente foi atualizada e as alterações foram registradas no Git. Quando aplicável, os testes automatizados devem ser executados antes da integração à branch `main`.

## Princípio didático

> Primeiro fazemos funcionar. Depois entendemos por que organizar, testar e melhorar.

A arquitetura profissional aparecerá como resposta a problemas reais do crescimento do projeto, e não como complexidade antecipada.

---

<sub>© 2026 **Wilson Luciano** · Programação para Engenharia Mecânica · EngConvert · Material didático · Versão 1.0</sub>
