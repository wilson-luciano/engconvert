# Aula 11.1 — Roteiro Prático: Gerar o EngConvert.exe e Publicar no GitHub

**Disciplina:** Programação para Engenharia Mecânica  
**Projeto:** EngConvert — Conversor de Unidades de Engenharia  
**Etapa 11:** Empacotamento e distribuição  
**Pré-requisitos:** Aula 10.2 e Aula 11.0

> **Objetivo:** gerar uma distribuição Windows do EngConvert com PyInstaller, validá-la, criar um ZIP e publicá-la como arquivo de uma **GitHub Release**. Esta aula **não cria um instalador** e não modifica as funcionalidades concluídas na Etapa 10.

---

## 1. Resultado esperado

Ao concluir, o repositório terá o código-fonte e sua documentação, enquanto a página de Releases disponibilizará um arquivo semelhante a `EngConvert-v0.1.0-Windows.zip`. Dentro do ZIP estará a pasta `EngConvert/`, contendo `EngConvert.exe` e as dependências necessárias.

```text
EngConvert-v0.1.0-Windows.zip
└── EngConvert/
    ├── EngConvert.exe
    └── _internal/              ← arquivos auxiliares (estrutura pode variar)
```

**Atenção:** a estrutura real depende da versão do PyInstaller. Não remover arquivos auxiliares para deixar o ZIP menor.

## 2. Conferir o projeto e o ambiente

Abra **PowerShell** no Windows e execute, linha a linha:

```powershell
cd C:\Projetos\engconvert
code .
.\.venv\Scripts\Activate.ps1
python --version
python -m pip show engconvert
python -m pip show customtkinter
python -m pytest -q
python main.py
```

Se o pacote EngConvert não estiver instalado corretamente no `.venv`, execute `python -m pip install -e .` na raiz e repita a conferência. Feche a janela após verificar as funções **General, Custom, About, Favoritas e Todas as grandezas**.

> **Critério de parada:** não empacote se a aplicação apresentar erro ou se os testes falharem. Corrija primeiro o código-fonte.

## 3. Preparar o Git antes da distribuição

```powershell
git status
git branch --show-current
git remote -v
```

Confira se as Sprints 10, 11 e 12 foram integradas à `main` e se a árvore de trabalho está limpa. **Não descarte alterações pendentes**. Se houver remoto e branch de acompanhamento configurados, atualize a principal:

```powershell
git switch main
git pull
```

Se não houver remoto configurado, não execute `git pull`; consulte o roteiro de Git das aulas anteriores. Para manter a preparação isolada, crie uma branch:

```powershell
git switch -c chore-distribuicao
```

Se essa branch já existir, escolha outro nome ou verifique o trabalho nela; não force sua recriação.

## 4. Criar ou revisar `.gitignore`

No VSCode, abra `.gitignore` na raiz (crie se necessário). **Preserve as regras já existentes** e acrescente apenas as linhas que estiverem faltando:

```gitignore
# Ambiente virtual e caches
.venv/
__pycache__/
*.py[cod]
.pytest_cache/

# Saídas do PyInstaller
build/
dist/

# Preferências pessoais, se alguma cópia for criada no projeto
configuracoes.json
unidades_personalizadas.json

# Pacotes gerados para download
EngConvert-v*-Windows.zip
```

**Não ignore** `src/`, `tests/`, `docs/`, `main.py` ou `pyproject.toml`. Se `build/` ou `dist/` já tiverem sido versionados anteriormente, `.gitignore` não os retira automaticamente do histórico; peça orientação antes de remover arquivos rastreados.

## 5. Instalar o PyInstaller

No `.venv` ativo:

```powershell
python -m pip install pyinstaller
python -m PyInstaller --version
```

O PyInstaller é uma ferramenta **de desenvolvimento**; não é necessário adicioná-lo às dependências de execução em `[project].dependencies` do `pyproject.toml`. Para permitir reprodução exata, registre a versão instalada na documentação ou em um arquivo de dependências de desenvolvimento, conforme a política do projeto.

## 5.1. Atividade opcional — criar o ícone do EngConvert

O arquivo **`.ico`** (com a letra **c**) define o ícone de um programa no Windows. Não confunda com **`.iso`**, que normalmente representa uma imagem de disco. O ícone **não é obrigatório**: sem ele, o PyInstaller utiliza um ícone padrão.

### 5.1.1. Criar a arte

O aluno pode desenhar no Paint, GIMP, Inkscape, Canva ou outro editor, por exemplo, **duas setas horizontais em sentidos opostos, sem texto**. Recomenda-se partir de uma imagem quadrada com pelo menos **256 × 256 pixels**, traços simples e contraste suficiente para leitura em tamanhos pequenos. Salve uma cópia como `assets/engconvert.png`.

Como exemplo opcional para a aula, há um modelo de ícone com duas setas. Cada aluno pode usar o modelo ou criar sua própria identidade visual. **Não é necessário incluir o nome EngConvert dentro do desenho**, pois o Windows já apresenta o nome do programa ao lado do ícone.

### 5.1.2. Preparar a pasta `assets`

No PowerShell, a partir da raiz do projeto:

```powershell
New-Item -ItemType Directory -Path .\assets -Force
```

Salve o PNG em `C:\Projetos\engconvert\assets\engconvert.png`. Para converter o PNG em ICO sem depender de sites externos, use a biblioteca Pillow **somente no ambiente de desenvolvimento**:

```powershell
python -m pip install pillow
```

Crie o arquivo `criar_icone.py` **temporariamente na raiz do projeto**, com este código completo:

```python
"""Converte a imagem PNG opcional em ícone multirresolução do Windows."""
from pathlib import Path
from PIL import Image

pasta = Path(__file__).resolve().parent / "assets"
origem = pasta / "engconvert.png"
destino = pasta / "engconvert.ico"

if not origem.is_file():
    raise FileNotFoundError(f"Imagem não encontrada: {origem}")

with Image.open(origem) as imagem:
    imagem = imagem.convert("RGBA")
    if imagem.width != imagem.height:
        raise ValueError("O PNG deve ser quadrado. Ajuste-o no editor antes de converter.")
    imagem = imagem.resize((256, 256), Image.Resampling.LANCZOS)
    imagem.save(destino, format="ICO", sizes=[
        (16, 16), (24, 24), (32, 32), (48, 48),
        (64, 64), (128, 128), (256, 256),
    ])

print(f"Ícone criado: {destino}")
```

Execute:

```powershell
python .\criar_icone.py
Get-Item .\assets\engconvert.ico
```

Se optar por manter `criar_icone.py` no repositório como material didático, documente sua função. Caso contrário, ele poderá ser excluído **após** a criação do ícone. O `engconvert.png` e o `engconvert.ico` são recursos do projeto e podem ser versionados no Git.

**Observação:** `--icon` altera o ícone associado ao **arquivo executável** no Windows. O ícone da **barra de título da janela CustomTkinter** é uma configuração diferente, que pode exigir `app.iconbitmap(...)` e inclusão do ICO como dado empacotado. Essa configuração adicional não é necessária para concluir a Aula 11.1 e não deve ser confundida com o resultado de `--icon`.

## 6. Gerar o executável no modo `--onedir`

A partir de `C:\Projetos\engconvert`:

```powershell
python -m PyInstaller --noconfirm --clean --onedir --windowed --name EngConvert --collect-all customtkinter main.py
```

| Parâmetro                     | Finalidade                                                                  |
| ----------------------------- | --------------------------------------------------------------------------- |
| `--noconfirm`                 | Permite substituir saídas de compilação existentes sem perguntas adicionais |
| `--clean`                     | Limpa caches de construção do PyInstaller                                   |
| `--onedir`                    | Cria uma pasta com o executável e seus arquivos de suporte                  |
| `--windowed`                  | Evita abrir console extra na aplicação gráfica                              |
| `--name EngConvert`           | Define o nome da distribuição e do `.exe`                                   |
| `--collect-all customtkinter` | Coleta dados e recursos da biblioteca CustomTkinter                         |
| `main.py`                     | Usa o ponto de entrada já empregado nas aulas anteriores                    |

**Se o aluno criou `assets\engconvert.ico`**, substitua o comando acima pela versão com ícone:

```powershell
python -m PyInstaller --noconfirm --clean --onedir --windowed --icon=assets\engconvert.ico --name EngConvert --collect-all customtkinter main.py
```

| Opção adicional                | Função                                              |
| ------------------------------ | --------------------------------------------------- |
| `--icon=assets\engconvert.ico` | Associa o ícone personalizado ao executável Windows |

Não utilize `--icon` apontando para um arquivo inexistente. Os recursos `--add-data "imgs;imgs"` e `--add-data "audio;audio"` do exemplo Flappy Bird **não são necessários** para o EngConvert atual, pois não possui essas pastas. `--add-data` só deve ser acrescentado quando houver arquivos de dados externos que precisem acompanhar a aplicação; o comando `--collect-all customtkinter` já cuida dos recursos dessa biblioteca.

### 6.1. Entendendo cada parâmetro do PyInstaller

Antes de continuar, **leia o comando da esquerda para a direita**. Cada opção modifica a maneira como o PyInstaller constrói e distribui o programa. A tabela reúne os parâmetros do nosso EngConvert e os do exemplo didático do Flappy Bird:

| Parâmetro                      | O que significa                                                                                          | Quando usar no EngConvert                                                                                            |
| ------------------------------ | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `--onedir`                     | Gera uma **pasta** com `EngConvert.exe` e os arquivos necessários à execução.                            | **Primeira opção da aula**; facilita conferir dependências e diagnosticar problemas.                                 |
| `--onefile`                    | Gera **um único arquivo** `.exe`; ao executar, os componentes empacotados são extraídos temporariamente. | Experimento opcional depois que o `--onedir` estiver funcionando.                                                    |
| `--windowed`                   | Impede a abertura de uma janela de console junto à interface gráfica no Windows.                         | Aplicativo CustomTkinter pronto para uso.                                                                            |
| `--console`                    | Mantém o console visível para mensagens e erros.                                                         | Diagnóstico, quando o executável fecha ou não abre. Não combinar com `--windowed`.                                   |
| `--icon=assets\engconvert.ico` | Incorpora um ícone ao **arquivo executável** do Windows.                                                 | Opcional, se o aluno criou ou copiou um arquivo `.ico` válido.                                                       |
| `--name EngConvert`            | Define o nome-base da distribuição, do `.exe`, do diretório de compilação e do arquivo `.spec`.          | Identificar o aplicativo de forma consistente.                                                                       |
| `--collect-all customtkinter`  | Solicita a coleta de dados, submódulos e binários relacionados ao CustomTkinter.                         | Evitar a ausência de recursos necessários à interface.                                                               |
| `--add-data "assets;assets"`   | Copia a pasta local `assets` para uma pasta `assets` dentro dos dados empacotados.                       | **Somente** se o programa precisar abrir esses arquivos em tempo de execução; não é necessário apenas para `--icon`. |
| `--clean`                      | Remove caches e arquivos temporários do PyInstaller antes da compilação.                                 | Recompilar com menos interferência de cache antigo.                                                                  |
| `--noconfirm`                  | Evita perguntas de confirmação ao substituir saídas de compilação.                                       | Repetir a geração após correções.                                                                                    |
| `main.py`                      | Arquivo Python de entrada, que inicia a aplicação.                                                       | É o ponto de entrada do EngConvert, não um parâmetro com `--`.                                                       |

**Exemplo para entender `--add-data`:** no Flappy Bird, `--add-data "imgs;imgs"` inclui imagens e `--add-data "audio;audio"` inclui sons. O trecho antes do `;` é a origem; o trecho depois é o destino relativo no pacote. No Windows, o separador `;` é o usado nos exemplos; a sintaxe e o tratamento de recursos devem ser verificados conforme a versão do PyInstaller. **O EngConvert não precisa incluir `imgs` ou `audio`, pois essas pastas não fazem parte de seu projeto.**

**Atenção:** incluir arquivos com `--add-data` não faz o programa encontrá-los automaticamente. O código precisa usar caminhos adequados ao ambiente empacotado. Por exemplo, um arquivo JSON de **preferências modificáveis** não deve ser gravado dentro do pacote ou ao lado de um executável instalado em uma pasta protegida; deve ficar em um diretório gravável do usuário, como AppData. Antes da publicação, teste o salvamento e a restauração dessas preferências no executável.

**Diferença essencial:** `--icon` define a imagem do `.exe`; `--add-data` disponibiliza arquivos para o aplicativo acessar; `app.iconbitmap(...)`, se implementado na interface, define o ícone da janela. São três operações distintas.

**Não use `--onedir` e `--onefile` juntos:** escolha apenas um modo em cada compilação.

**Não use `--onefile` nesta primeira validação.** O modo `--onedir` torna mais fácil identificar arquivos ausentes e distribuir os recursos do CustomTkinter.

Após a execução, a estrutura deverá ser semelhante a:

```text
engconvert/
├── build/                         ← arquivos temporários
├── dist/
│   └── EngConvert/
│       ├── EngConvert.exe
│       └── _internal/             ← dependências (estrutura pode variar)
├── EngConvert.spec               ← configuração de empacotamento
├── main.py
├── pyproject.toml
└── src/engconvert/
```

O `.spec` pode ser versionado para documentar o empacotamento, após conferência; **não** é obrigatório versionar `build/` e `dist/`.

## 7. Executar o programa empacotado

```powershell
.\dist\EngConvert\EngConvert.exe
```

Confirme manualmente:

- [ ] O programa abre sem exigir o VSCode.
- [ ] As abas **Favoritas** e **Todas as grandezas** aparecem.
- [ ] `1 bar` resulta em `100 kPa`.
- [ ] `1 m` resulta em `1000 mm`.
- [ ] `0 °C` resulta em `32 °F`.
- [ ] **General** permite alterar o tema e a precisão.
- [ ] Ao fechar e reabrir, as preferências continuam salvas.
- [ ] **Custom** permite cadastrar uma unidade válida e utilizá-la em uma conversão.
- [ ] **About** apresenta as informações e créditos.
- [ ] Nenhum arquivo de configuração precisa ser gravado dentro de `dist/`.

**Onde ficam as preferências?** A Aula 10.2 implementou `%APPDATA%\EngConvert`. Para conferir o caminho no PowerShell:

```powershell
Join-Path $env:APPDATA 'EngConvert'
```

Se não houver `APPDATA`, o código da Aula 10.2 prevê uma pasta alternativa no diretório pessoal do usuário. **Não publique os JSON pessoais no GitHub.**

### 7.1. Se o `.exe` não abrir

1. Refaça `python main.py` para distinguir falha do projeto e falha do empacotamento.
2. Confira mensagens de erro do PyInstaller no terminal.
3. Gere **temporariamente** uma versão de diagnóstico, sem `--windowed`, em outro nome:

```powershell
python -m PyInstaller --noconfirm --clean --onedir --console --name EngConvert-Debug --collect-all customtkinter main.py
.\dist\EngConvert-Debug\EngConvert-Debug.exe
```

4. Leia o erro exibido no terminal. Depois de corrigir a causa, refaça a distribuição final `EngConvert` com `--windowed`.

> Não copie DLLs aleatórias da internet nem desative o antivírus como solução padrão.

### 7.2. Limpar saídas de uma compilação anterior (quando necessário)

O PyInstaller normalmente recria os arquivos necessários usando `--noconfirm --clean`. Se houver problemas relacionados a arquivos antigos, feche o EngConvert e, **na raiz correta do projeto**, confira os caminhos antes de excluir:

```powershell
Get-Location
Get-ChildItem .\build, .\dist -ErrorAction SilentlyContinue
```

Depois, se realmente precisar remover **somente os resultados gerados**:

```powershell
if (Test-Path .\build) { Remove-Item .\build -Recurse -Force }
if (Test-Path .\dist)  { Remove-Item .\dist  -Recurse -Force }
```

**Atenção:** não use `rmdir /s /q` no PowerShell: essa sintaxe pertence ao CMD. **Não exclua automaticamente `EngConvert.spec`**. Esse arquivo descreve o empacotamento e pode conter configurações úteis; se precisar regenerá-lo, faça isso conscientemente e preserve o que foi personalizado. A exclusão das pastas acima é irreversível pelo comando e só deve ser feita após confirmar que não contêm arquivos pessoais.

## 8. Testar fora da pasta do projeto

Copie a pasta **inteira** `dist\EngConvert` para outra pasta do Windows ou, preferencialmente, outro computador Windows compatível. Abra `EngConvert.exe` de lá. Esse teste ajuda a detectar dependências acidentais do projeto, do `.venv` ou do VSCode.

**Critério de aceitação:** o programa deve abrir e executar as conversões principais sem o usuário precisar instalar Python ou CustomTkinter. Não confunda esse requisito com compatibilidade garantida com toda versão do Windows.

## 9. Gerar o ZIP para publicação

De volta à raiz do projeto, execute:

```powershell
Compress-Archive -Path .\dist\EngConvert -DestinationPath .\EngConvert-v0.1.0-Windows.zip -Force
```

Confira se o ZIP foi criado:

```powershell
Get-Item .\EngConvert-v0.1.0-Windows.zip
```

Extraia o ZIP em outra pasta e teste novamente o `.exe`. O usuário deverá **extrair todos os arquivos antes de executar**; abrir o executável diretamente de dentro da prévia do ZIP pode causar erros.

## 10. Preparar o `README.md`

No `README.md` do projeto, preserve o conteúdo existente e acrescente uma seção como a seguinte:

```markdown
## Download do EngConvert para Windows

Acesse a seção **Releases** deste repositório e baixe o arquivo
`EngConvert-v0.1.0-Windows.zip` da versão correspondente.

1. Extraia **todo** o conteúdo do ZIP.
2. Abra a pasta `EngConvert` extraída.
3. Execute `EngConvert.exe`.

O programa foi desenvolvido em Python e CustomTkinter. Para utilizar
esta distribuição não é necessário instalar Python separadamente.

As preferências são salvas na pasta de dados do usuário do Windows.

> O executável é destinado ao Windows. Esta versão é distribuída sem
> instalador e pode exibir avisos de reputação do sistema caso não esteja
> assinada digitalmente. Verifique a procedência do download.
```

**Não apague o README anterior.** Atualize também a identificação da versão, se houver um campo específico no documento.

## 11. Registrar a entrega no Git

```powershell
git status
git diff
git add .gitignore README.md
git add assets/engconvert.png assets/engconvert.ico
git add EngConvert.spec
git commit -m "build: prepara distribuicao Windows do EngConvert"
```

Se o aluno **não criou um ícone**, omita a linha `git add assets/engconvert.png assets/engconvert.ico`. Se o arquivo `EngConvert.spec` não tiver sido criado ou não for adotado, **omita** a linha `git add EngConvert.spec`. Se não houver alterações para registrar, o Git informará que nada precisa ser commitado.

Depois dos testes e da revisão, integre a branch:

```powershell
git switch main
git merge chore-distribuicao
python -m pytest -q
git status
```

Se aparecer conflito, **pare e resolva antes de continuar**. Caso o remoto e o acompanhamento já estejam configurados:

```powershell
git push
```

## 12. Criar uma tag de versão

Primeiro, verifique se a tag já existe:

```powershell
git tag --list v0.1.0
```

Se **não** houver resultado e `v0.1.0` for a versão aprovada, crie a tag anotada:

```powershell
git tag -a v0.1.0 -m "EngConvert v0.1.0 - primeira distribuicao Windows"
git push origin v0.1.0
```

`git push origin v0.1.0` pressupõe um remoto chamado `origin`. Confira antes com `git remote -v`. **Não recrie nem sobrescreva uma tag publicada** se ela já existir: escolha uma versão nova após verificar o histórico.

## 13. Publicar no GitHub Releases (navegador)

1. Abra a página do repositório EngConvert no GitHub.
2. Localize **Releases** e selecione **Draft a new release** ou **Create a new release** (a interface pode variar).
3. Em **Choose a tag**, selecione `v0.1.0`, criada na seção anterior.
4. Informe o título `EngConvert v0.1.0 — Windows`.
5. Preencha as notas de lançamento com os recursos realmente testados.
6. Na área de anexos (_assets_), arraste ou selecione **`EngConvert-v0.1.0-Windows.zip`**.
7. Confira se o ZIP foi anexado à versão correta e publique a Release.
8. Abra a página pública da Release e faça o download do ZIP para verificar a experiência do usuário.

**Exemplo de notas para a Release:**

```markdown
## EngConvert v0.1.0 — Windows

Primeira distribuição do EngConvert para Windows.

### Recursos

- Conversões de pressão, comprimento, área, volume e temperatura.
- Navegação por abas e organização das categorias.
- Configurações gerais persistidas em JSON.
- Cadastro de unidades personalizadas.
- Tela About com informações do aplicativo.

### Instalação

1. Baixe `EngConvert-v0.1.0-Windows.zip`.
2. Extraia o conteúdo completo.
3. Execute `EngConvert.exe` na pasta `EngConvert`.

### Observações

- Distribuição portátil para Windows, sem instalador.
- Testada no ambiente Windows documentado no projeto.
```

> A publicação é uma ação na sua conta GitHub: os passos acima devem ser executados pelo aluno. Esta aula não pressupõe que uma Release já tenha sido criada.

## 14. Exercício opcional: testar `--onefile`

**Somente após aprovar o `--onedir`**, experimente:

```powershell
python -m PyInstaller --noconfirm --clean --onefile --windowed --name EngConvert-OneFile --collect-all customtkinter main.py
```

Se quiser usar o ícone no modo `--onefile`, acrescente `--icon=assets\engconvert.ico` ao comando **somente se o arquivo existir**. Teste o executável produzido em `dist/` e compare o tempo de inicialização, o tamanho e o funcionamento do CustomTkinter. Não substitua o ZIP da Release sem validar esse novo modo.

## 15. Checklist de encerramento

- [ ] Projeto integrado da Aula 10.2 validado.
- [ ] `python -m pytest -q` aprovado.
- [ ] `EngConvert.exe` abre e converte corretamente.
- [ ] (Opcional) Ícone `.ico` criado, incluído no comando e conferido no Explorador do Windows.
- [ ] General, Custom, About e JSON testados.
- [ ] Teste fora da pasta original concluído.
- [ ] ZIP íntegro e extraído com sucesso.
- [ ] `.gitignore` revisado e código enviado ao GitHub.
- [ ] Tag de versão criada sem sobrescrever outra.
- [ ] Release publicada com ZIP e instruções.
- [ ] Download público testado.

## 16. Perguntas de fixação

1. Por que a pasta `dist/` não deve ser enviada em commits normais?
2. O que significa `--collect-all customtkinter`?
3. Qual a diferença entre `git push` e anexar um ZIP a uma Release?
4. Por que é necessário testar o ZIP após extraí-lo?
5. O que o usuário precisa instalar para executar a distribuição `--onedir` validada?
6. Qual a diferença entre `.ico` e `.iso`? O que muda ao usar `--icon`?

## 17. Resumo da aula

```text
Código testado → PyInstaller (--onedir) → EngConvert.exe
      ↓                                      ↓
 Git + GitHub                          teste no Windows
      ↓                                      ↓
  tag v0.1.0 ←──────────────────────── ZIP validado
      ↓
 GitHub Release + ZIP → download pelo usuário
```

**Ideia-chave:** o GitHub guarda o histórico do desenvolvimento; a **Release** entrega ao usuário uma versão identificada, documentada e testada do aplicativo.

---

<sub>© 2026 <b>Wilson Luciano</b> · Programação para Engenharia Mecânica · EngConvert · Material didático · Versão 1.0</sub>
