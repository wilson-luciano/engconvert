# EngConvert

**Engineering Unit Converter**  
Projeto didático da disciplina **Programação para Engenharia Mecânica**.

## Objetivo

Construir, de forma incremental, um conversor de unidades para engenharia enquanto aprendemos:

- interfaces gráficas (GUI), Tkinter e CustomTkinter;
- programação orientada a eventos e tratamento de entradas;
- VSCode, terminal integrado e ambientes virtuais;
- conversão de unidades de diferentes grandezas físicas;
- organização de código em módulos e pacotes Python;
- Git e GitHub, documentação e trabalho com branches;
- fundamentos de testes, empacotamento e distribuição de aplicações.

O projeto evolui por etapas: cada aula apresenta conceitos e, quando aplicável, um roteiro prático para implementá-los.

## Organização das aulas

Os arquivos das aulas estão na pasta [`aulas/`](aulas/). A numeração `.0` identifica a aula de fundamentos e `.1` o roteiro prático correspondente, quando disponível.

| Aulas | Tema |
| --- | --- |
| 01.0 e 01.1 | VSCode, estrutura do projeto e ambiente de desenvolvimento |
| 02.0 e 02.1 | Fundamentos de GUI, roadmap e Sprints |
| 03.0 e 03.1 | Widgets e eventos |
| 04.0 e 04.1 | Primeiro conversor |
| 05.0 e 05.1 | Conversor de pressão |
| 06.0 e 06.1 | Novas grandezas e conversor multicategorias |
| 07.0 e 07.1 | Git, GitHub e controle de versão |
| 07.2 | README de perfil do GitHub |
| 08.0 e 08.1 | Modularização do EngConvert |
| 09.0 e 09.1 | Fundamentos e prática de testes de software |
| 10.0, 10.1 e 10.2 | Interface completa e roteiros práticos |
| 11.0 e 11.1 | Fundamentos de empacotamento e geração de executável |

> **Nota:** algumas aulas podem estar em preparação ou disponíveis apenas na cópia local do projeto, antes de sua publicação no GitHub.

Consulte também o [`roadmap`](docs/roadmap.md) e a documentação das Sprints em `docs/sprints/`.

## Estrutura do projeto

```text
engconvert/
├── aulas/                 # Material didático
├── docs/                  # Roadmap, Sprints e documentação
├── src/
│   └── engconvert/        # Pacote Python do aplicativo
├── tests/                 # Testes e documentação de testes
├── main.py                # Ponto de entrada do aplicativo
├── pyproject.toml         # Metadados e configuração do pacote
├── requirements.txt       # Dependências básicas
└── README.md
```

## Preparação do ambiente (Windows / PowerShell)

Na pasta raiz do projeto, com **Python 3.12 ou superior** instalado:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

A instalação editável (`-e .`) utiliza o `pyproject.toml`, instala as dependências declaradas — incluindo `customtkinter` — e permite importar o pacote localizado em `src/engconvert/`.

Se o PowerShell bloquear a ativação do ambiente virtual, consulte as orientações da Aula 01 antes de alterar configurações de execução.

## Executar o EngConvert

Com o ambiente virtual ativado, execute:

```powershell
python main.py
```

Para encerrar o ambiente virtual:

```powershell
deactivate
```

## Dependências e desenvolvimento

- **Python:** versão mínima 3.12, conforme `pyproject.toml`.
- **Interface gráfica:** `customtkinter`.
- **Instalação do pacote:** `python -m pip install -e .`.

O arquivo `requirements.txt` também pode ser usado para instalar a dependência básica com `python -m pip install -r requirements.txt`, mas, para trabalhar com a estrutura modular, recomenda-se a instalação editável.

## Git e GitHub

O repositório utiliza a branch principal `main`. Antes de publicar alterações, confira o estado do projeto:

```powershell
git status -sb
git fetch origin
git --no-pager diff --stat origin/main
```

Prepare apenas os arquivos desejados com `git add -- <caminho-do-arquivo>` e revise o conteúdo preparado antes de criar um commit. Consulte as Aulas 07.0 e 07.1 para o procedimento didático completo.

---

<sub>
© 2026 **Wilson Luciano** · Programação para Engenharia Mecânica · EngConvert · Material didático
</sub>
