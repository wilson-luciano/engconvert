# Aula 11.0 — Fundamentos: Empacotamento e Distribuição do EngConvert

**Disciplina:** Programação para Engenharia Mecânica  
**Projeto:** EngConvert — Conversor de Unidades de Engenharia  
**Etapa 11:** Distribuição para Windows e GitHub Releases  
**Pré-requisitos:** Aulas 10.0, 10.1 e 10.2

> **Meta:** distribuir uma versão utilizável do EngConvert, mantendo o código-fonte no GitHub e oferecendo um pacote para Windows na área **Releases**. Esta aula explica os conceitos; a Aula 11.1 contém os comandos de execução.

---

## 1. Objetivos

Ao final, o aluno deverá distinguir código-fonte, ambiente virtual, empacotamento, executável, instalador, repositório, tag e release; explicar por que testar em outra máquina é indispensável; conhecer o fluxo de publicação sem incluir arquivos temporários no Git; e interpretar direitos autorais, licença MIT e metadados de licenciamento.

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

## 3A. Direitos autorais e licenciamento de software

### 3A.1. Direitos autorais, software livre e código aberto

O **direito autoral** protege o código como obra intelectual. Publicar um repositório no GitHub não significa, por si só, conceder autorização irrestrita para copiar, modificar ou redistribuir o programa. A **licença de software** explicita as condições de uso.

**Software livre** enfatiza liberdades de executar, estudar, modificar e redistribuir; **código aberto** enfatiza a disponibilidade do código e os critérios de licenciamento. Os conceitos têm diferenças históricas e filosóficas, mas a licença MIT é amplamente reconhecida como licença permissiva de software livre e de código aberto.

### 3A.2. Panorama dos principais tipos de licença

As licenças de software podem ser **permissivas**, permitindo ampla reutilização com poucas condições, ou **copyleft**, impondo obrigações de compartilhamento de código em determinadas redistribuições. **Software proprietário** normalmente é disponibilizado sob condições restritivas definidas pelo titular.

| Licença ou modelo           | Tipo                 | Característica principal                                                                            | Atenção na redistribuição                                              |
| --------------------------- | -------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **MIT**                     | Permissiva           | Permite uso, alteração e distribuição, inclusive comercial.                                         | Preservar avisos de copyright e permissão.                             |
| **Apache License 2.0**      | Permissiva           | Inclui concessão expressa de direitos de patente e regras sobre avisos.                             | Observar `NOTICE` quando aplicável e alterações documentadas.          |
| **BSD 2-Clause / 3-Clause** | Permissiva           | Concede liberdades amplas com condições de atribuição.                                              | A BSD 3-Clause inclui restrição ao uso de nomes para endosso.          |
| **GPL v3**                  | Copyleft forte       | Redistribuições de obras cobertas podem exigir fornecimento do código-fonte correspondente sob GPL. | Examinar as condições específicas de distribuição.                     |
| **LGPL v3**                 | Copyleft limitado    | Frequentemente usada em bibliotecas, permitindo certos usos em programas sob outras licenças.       | Cumprir condições sobre a biblioteca e sua substituição/modificação.   |
| **MPL 2.0**                 | Copyleft por arquivo | Permite combinar arquivos sob MPL com arquivos sob outras licenças.                                 | Disponibilizar o código dos arquivos cobertos quando exigido.          |
| **Creative Commons**        | Licenças de conteúdo | Adequadas a textos, imagens e materiais didáticos.                                                  | Não são a escolha recomendada para licenciar código-fonte de software. |
| **Proprietária**            | Modelo contratual    | Uso e redistribuição dependem de autorização do titular.                                            | Consultar os termos específicos; não é uma licença padronizada única.  |

**Por que MIT no EngConvert?** É curta, de fácil compreensão inicial e permite que os alunos estudem, adaptem e redistribuam o programa, mantendo os avisos exigidos. A escolha não elimina as obrigações das licenças das bibliotecas utilizadas.

### 3A.3. O que a licença MIT permite e exige?

| Aspecto                | Interpretação didática                                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Permissões**         | Usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e vender cópias do software.                                    |
| **Condição principal** | Preservar o aviso de direitos autorais e o texto de permissão em todas as cópias ou partes substanciais do software.                 |
| **Limitações**         | O software é fornecido **sem garantias**, e o texto estabelece uma limitação de responsabilidade dos autores, nos termos da licença. |

A MIT **não exige** que toda modificação seja publicada como código aberto. Isso não dispensa o respeito a licenças de dependências, marcas, direitos de terceiros ou outras obrigações legais. A licença não transfere a autoria do código original.

### 3A.4. Estrutura do arquivo `LICENSE`

O arquivo `LICENSE`, localizado na raiz do repositório, contém: (1) identificação da licença; (2) aviso de copyright; (3) permissões concedidas; (4) condição de manutenção dos avisos; e (5) cláusula de ausência de garantias e limitação de responsabilidade.

Para o EngConvert, o cabeçalho será:

```text
MIT License

Copyright (c) 2026 Wilson Luciano
```

Na Aula 11.1, o aluno copiará o **texto integral** da licença MIT fornecido no roteiro, sem traduzir nem resumir o texto jurídico do arquivo.

### 3A.5. `LICENSE` e `pyproject.toml` não são equivalentes

O arquivo `LICENSE` apresenta os termos legais completos. Já `license = "MIT"` dentro da seção `[project]` do `pyproject.toml` declara **metadados de licenciamento** do pacote Python. Essa declaração deve corresponder ao conteúdo do `LICENSE`; sozinha, ela não substitui o arquivo com os termos completos.

```toml
[project]
license = "MIT"
```

Esse exemplo mostra **apenas a linha pertinente**: o aluno deve preservar os demais campos existentes e não criar uma segunda seção `[project]`. A aceitação da sintaxe depende da versão e das ferramentas de empacotamento utilizadas; caso o projeto use um formato de metadados anterior, a adequação deverá ser avaliada antes de alterar o arquivo.

### 3A.6. Licença e distribuição do executável

O PyInstaller reúne o programa e suas dependências, mas **não altera a licença do EngConvert**. Ao distribuir o ZIP, incluiremos uma cópia do `LICENSE` junto da distribuição e verificaremos os avisos de licença das dependências incorporadas. O ZIP e o repositório podem ter conteúdos diferentes, mas ambos devem respeitar as condições aplicáveis.

---

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

**Versionar:** `LICENSE`, `main.py`, `src/`, `tests/`, `docs/`, `README.md`, `LICENSE`, `pyproject.toml`, `.gitignore` e, se adotado, o arquivo de configuração `.spec` do PyInstaller.

**Ignorar:** `.venv/`, `__pycache__/`, `.pytest_cache/`, `build/`, `dist/`, `*.pyc` e configurações pessoais em JSON. O pacote ZIP da Release pode ser gerado localmente e enviado diretamente ao GitHub, sem ser adicionado ao repositório.

## 9. Segurança, limitações e testes

- Gerar o executável **no Windows** e testar em Windows compatível, preferencialmente também em outro computador.
- Conferir se os botões, abas, unidades, JSON, Custom e About funcionam.
- Testar primeiro com `python -m pytest -q`, depois com o `.exe`; testes automatizados de cálculo não substituem a inspeção da GUI.
- Não interpretar alertas de antivírus como prova de malware nem ignorá-los automaticamente; verificar origem, integridade e comportamento do arquivo.
- A ausência de assinatura digital pode causar avisos de reputação do Windows. Não ensinar o usuário a desativar a proteção como procedimento padrão.
- Não afirmar que o `.exe` é universal: arquitetura, versão do Windows e bibliotecas podem influenciar a compatibilidade.

## 9A. Integração segura de branches e publicação: conceitos essenciais

Antes de criar uma **Release**, distinga quatro referências: a **branch de trabalho** (`chore-distribuicao`) guarda o desenvolvimento; a **branch `main`** identifica a versão principal; a **tag `v0.1.0`** identifica um commit específico; a **Release** é a página de publicação associada à tag, onde o ZIP do executável é anexado.

- `git status -sb` mostra a branch e as alterações pendentes; `git log -1 --oneline --decorate` revela as referências apontadas para o último commit.
- `git log --oneline main..chore-distribuicao` mostra os commits da branch de trabalho ainda ausentes da `main`.
- `git fetch origin` atualiza as referências remotas, sem incorporar mudanças ao diretório de trabalho.
- `git stash push -u` guarda temporariamente arquivos modificados **e não rastreados**, permitindo trocar de branch com segurança. Não substitui commit nem backup permanente.
- `git merge --ff-only chore-distribuicao` atualiza a `main` somente quando há possibilidade de avanço direto, sem criar um commit de merge. `Already up to date` também é um resultado válido.
- `git push origin main` publica a branch; `git push origin v0.1.0` publica a tag. Uma tag já publicada pode responder `Everything up-to-date`.
- `git stash pop` restaura o trabalho pendente e, se aplicado com êxito, retira a entrada da lista de stashes. Se houver conflito, interrompa e examine antes de continuar.

**Regra de consistência:** a tag deve apontar para o commit exato do código usado para gerar o executável publicado. Não mova uma tag já divulgada para corrigir alterações posteriores; publique outra versão.

**Atenção à documentação:** arquivos didáticos ainda em revisão não precisam entrar no commit da distribuição. Arquivos `.spec` devem ser versionados apenas se revisados e adotados como configuração reproduzível.

## 10. Critérios para publicar

- [ ] Testes Python aprovados.
- [ ] Aplicação abre pelo executável.
- [ ] Cinco grandezas e suas conversões verificadas.
- [ ] General, Custom, About e persistência JSON verificados.
- [ ] ZIP contém a distribuição completa.
- [ ] `README.md` explica instalação e execução.
- [ ] `LICENSE` MIT está versionado, é compatível com `license = "MIT"` no `pyproject.toml` e acompanha o ZIP; licenças das dependências foram verificadas.
- [ ] Código-fonte versionado, tag correta e Release com arquivo anexado.

## 11. Perguntas de fixação

1. Qual a diferença entre um executável e um instalador?
2. Por que enviar somente `EngConvert.exe` é inadequado quando usamos `--onedir`?
3. Qual a diferença entre `git push`, tag e GitHub Release?
4. Por que os arquivos de preferências devem ficar fora do repositório?
5. Por que precisamos testar o executável, mesmo após o sucesso do `pytest`?
6. Qual a diferença entre licenças permissivas e copyleft?
7. Por que `license = "MIT"` não substitui o arquivo `LICENSE`?

8. O que diferencia `git stash`, commit, branch, tag e Release?
9. Por que `git merge --ff-only` é mais conservador que um merge sem essa opção?

## 12. Resumo

A distribuição exige **código estável → licença → testes → empacotamento → validação → ZIP → tag → GitHub Release**. Na Aula 11.1 executaremos cada etapa no Windows e no navegador.

---

<sub>© 2026 <b>Wilson Luciano</b> · Programação para Engenharia Mecânica · EngConvert · Material didático · Versão 1.0</sub>
