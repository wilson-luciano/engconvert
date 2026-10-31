# Aula 11.0 — Fundamentos: Empacotamento e Distribuição do EngConvert

**Disciplina:** Programação para Engenharia Mecânica  
**Projeto:** EngConvert — Conversor de Unidades de Engenharia  
**Etapa 11:** Distribuição para Windows e GitHub Releases  
**Pré-requisitos:** Aulas 10.0, 10.1 e 10.2

> **Meta:** distribuir uma versão utilizável do EngConvert, mantendo o código-fonte no GitHub e oferecendo um pacote para Windows na área **Releases**. Esta aula explica os conceitos; a Aula 11.1 contém os comandos de execução.

---

## 1. Objetivos

Ao final, o aluno deverá distinguir código-fonte, ambiente virtual, empacotamento, executável, instalador, repositório, tag e release; explicar por que testar em outra máquina é indispensável; e conhecer o fluxo de publicação sem incluir arquivos temporários no Git.

## 2. O que já está pronto?

Na Etapa 10, o EngConvert passou a incluir abas e navegação (Sprint 09), configurações gerais e JSON (Sprint 10), unidades personalizadas (Sprint 11) e informações do programa (Sprint 12). O projeto mantém o ponto de entrada `main.py`, o pacote em `src/engconvert/`, `pyproject.toml` e testes com `pytest`.

**Importante:** os arquivos JSON são dados do usuário. No Windows, o módulo `configuracoes.py` utiliza `%APPDATA%\EngConvert`, portanto as preferências não devem ser colocadas na pasta do executável nem publicadas no GitHub.

## 3. Quatro conceitos diferentes

| Conceito      | Exemplo                                    | Papel                                                                                  |
| ------------- | ------------------------------------------ | -------------------------------------------------------------------------------------- |
| Código-fonte  | `main.py`, `interface.py`                  | Permite estudar e modificar o aplicativo                                               |
| Pacote Python | `engconvert`, definido em `pyproject.toml` | Organiza a aplicação e suas dependências                                               |
| Executável    | `EngConvert.exe`                           | Inicia o programa no Windows sem exigir que o usuário execute `python main.py`         |
| Instalador    | `.msi` ou assistente `.exe`                | Instala, cria atalhos e pode oferecer desinstalação; **não será produzido nesta aula** |

**Empacotar não é compilar todo o Python para código nativo.** O PyInstaller reúne o interpretador Python, o código e dependências necessárias para executar a aplicação no sistema-alvo.

## 4. Ferramenta: PyInstaller

O **PyInstaller** gera distribuições de aplicações Python. A compilação deve ser realizada no sistema-alvo: para criar um executável Windows, use Windows. O resultado não é automaticamente compatível com macOS ou Linux.

### 4.1. `--onedir` e `--onefile`

| Modo        | Resultado                              | Vantagem                                           | Atenção                                                                              |
| ----------- | -------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `--onedir`  | Pasta com `.exe` e arquivos auxiliares | Mais simples de inspecionar e solucionar problemas | Distribuir **a pasta inteira**, não apenas o `.exe`                                  |
| `--onefile` | Um `.exe`                              | Download simples                                   | Extração temporária na inicialização, possível demora e exigência de testar recursos |

**Escolha didática:** começar com `--onedir`. Só testar `--onefile` depois de validar a distribuição em pasta.

### 4.2. `--windowed` e `--name`

`--windowed` evita abrir uma janela de console adicional para uma interface gráfica; `--name EngConvert` define o nome do executável e da pasta de distribuição. Para investigar erros, gerar temporariamente uma versão **sem** `--windowed` pode facilitar a leitura de mensagens no terminal.

## 5. CustomTkinter: recursos que precisam acompanhar o executável

O CustomTkinter usa arquivos de tema, fontes e outros recursos. Dependendo da versão do PyInstaller e do CustomTkinter, esses recursos podem exigir coleta explícita. Na prática, a Aula 11.1 usará `--collect-all customtkinter`, e o aluno deverá verificar se a interface realmente abre na distribuição gerada. Uma compilação bem-sucedida **não** garante uma aplicação funcional.

## 6. Git não é a mesma coisa que GitHub Releases

```text
PROJETO LOCAL
  │
  ├── Git: commits e histórico do código
  │       └── git push → repositório GitHub (arquivos-fonte)
  │
  └── PyInstaller → dist/EngConvert/ (arquivos para Windows)
                      │
                      └── compactar ZIP
                              │
                              ▼
                       GitHub Release
                       v0.1.0 + ZIP
```

`git push` envia commits, **não publica automaticamente um executável em Releases**. Uma **tag** identifica uma versão específica do histórico (por exemplo, `v0.1.0`). Uma **Release** apresenta essa versão ao público, com notas e arquivos para download (_assets_).

## 7. Versionamento inicial

Nesta aula adotaremos **`v0.1.0` como exemplo didático**. Antes de publicar, verificar se o repositório já possui essa tag ou versão. Se já existir, escolher outra versão; não substituir uma release publicada sem uma justificativa clara.

## 8. O que entra e o que não entra no Git?

**Versionar:** `main.py`, `src/`, `tests/`, `docs/`, `README.md`, `pyproject.toml`, `.gitignore` e, se adotado, o arquivo de configuração `.spec` do PyInstaller.

**Ignorar:** `.venv/`, `__pycache__/`, `.pytest_cache/`, `build/`, `dist/`, `*.pyc` e configurações pessoais em JSON. O pacote ZIP da Release pode ser gerado localmente e enviado diretamente ao GitHub, sem ser adicionado ao repositório.

## 9. Segurança, limitações e testes

- Gerar o executável **no Windows** e testar em Windows compatível, preferencialmente também em outro computador.
- Conferir se os botões, abas, unidades, JSON, Custom e About funcionam.
- Testar primeiro com `python -m pytest -q`, depois com o `.exe`; testes automatizados de cálculo não substituem a inspeção da GUI.
- Não interpretar alertas de antivírus como prova de malware nem ignorá-los automaticamente; verificar origem, integridade e comportamento do arquivo.
- A ausência de assinatura digital pode causar avisos de reputação do Windows. Não ensinar o usuário a desativar a proteção como procedimento padrão.
- Não afirmar que o `.exe` é universal: arquitetura, versão do Windows e bibliotecas podem influenciar a compatibilidade.

## 10. Critérios para publicar

- [ ] Testes Python aprovados.
- [ ] Aplicação abre pelo executável.
- [ ] Cinco grandezas e suas conversões verificadas.
- [ ] General, Custom, About e persistência JSON verificados.
- [ ] ZIP contém a distribuição completa.
- [ ] `README.md` explica instalação e execução.
- [ ] Código-fonte versionado, tag correta e Release com arquivo anexado.

## 11. Perguntas de fixação

1. Qual a diferença entre um executável e um instalador?
2. Por que enviar somente `EngConvert.exe` é inadequado quando usamos `--onedir`?
3. Qual a diferença entre `git push`, tag e GitHub Release?
4. Por que os arquivos de preferências devem ficar fora do repositório?
5. Por que precisamos testar o executável, mesmo após o sucesso do `pytest`?

## 12. Resumo

A distribuição exige **código estável → testes → empacotamento → validação → ZIP → tag → GitHub Release**. Na Aula 11.1 executaremos cada etapa no Windows e no navegador.

---

<sub>© 2026 <b>Wilson Luciano</b> · Programação para Engenharia Mecânica · EngConvert · Material didático · Versão 1.0</sub>
