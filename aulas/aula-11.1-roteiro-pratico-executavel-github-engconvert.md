# Aula 11.1 — Roteiro Prático: Gerar o EngConvert.exe e Publicar no GitHub

**Disciplina:** Programação para Engenharia Mecânica  
**Projeto:** EngConvert — Conversor de Unidades de Engenharia  
**Etapa 11:** Empacotamento e distribuição  
**Pré-requisitos:** Aula 10.2 e Aula 11.0

> **Objetivo:** gerar uma distribuição Windows do EngConvert com PyInstaller, validá-la, criar um ZIP e publicá-la como arquivo de uma **GitHub Release**. Esta aula **não cria um instalador** e não modifica as funcionalidades concluídas na Etapa 10. Também formaliza o licenciamento MIT antes da distribuição.

---

## 1. Resultado esperado

Nesta aula, a **primeira opção** é gerar um único executável Windows (`--onefile`) com os ícones de tema incluídos. Como alternativa, também será apresentado o formato em pasta (`--onedir`), que contém a pasta `_internal`.

**Opção prioritária — arquivo único:**

```text
dist/
└── EngConvert.exe
```

**Opção alternativa — pasta:**

```text
dist/
└── EngConvert/
    ├── EngConvert.exe
    └── _internal/       ← dependências; não apagar
```

O arquivo `LICENSE` deverá acompanhar a distribuição na publicação: para `--onefile`, forneça-o como arquivo adicional na Release ou no ZIP; para `--onedir`, inclua-o no ZIP da distribuição. O `.exe` não é um instalador.

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

Confira se as Sprints 10, 11 e 12 já estão integradas à `main`. No caso acompanhado em aula, `main` estava sincronizada com `origin/main`, mas havia **uma alteração local na Aula 10.2 e duas aulas novas ainda não rastreadas**. Isso não impede a criação de uma branch, porém **não descarte nem sobrescreva esses arquivos**.

Se você já está na `main` e ela está atualizada, **não é necessário repetir** `git switch main` ou `git pull` neste momento. Se precisar atualizar uma `main` sem alterações locais, confira primeiro o estado do Git; nunca execute um `pull` às cegas sobre trabalho pendente.

Crie a branch de distribuição (somente se ainda não existir):

```powershell
git switch -c chore-distribuicao
git status
git branch --show-current
```

O comando preserva normalmente as alterações locais e arquivos não rastreados ao criar a nova branch. Se a branch já existir, verifique-a antes de trocar de branch; não force a criação. **A Aula 10.2 já foi congelada:** antes de incluir sua modificação em qualquer commit, confira `git diff -- aulas/aula-10.2-roteiro-pratico-interface-completa-engconvert.md`.

## 4. Criar ou revisar `.gitignore`

No VSCode, abra o `.gitignore` já existente na raiz do EngConvert. **Não crie outro arquivo nem substitua regras úteis.** Para este projeto, a versão revisada é:

```gitignore
# Ambientes virtuais
.venv/
venv/

# Python
*.py[cod]
*.egg-info/

# Testes e caches
__pycache__/
.pytest_cache/

# Arquivos de configuração locais
.env
.env.*
!.env.example

# Saídas do PyInstaller
build/
dist/

# Arquivos gerados
.vscode/
*.log

# Preferências pessoais
configuracoes.json
unidades_personalizadas.json

# Pacotes gerados para download
EngConvert-v*-Windows.zip
```

**Correção importante:** a regra `*.spec` foi retirada para permitir versionar `EngConvert.spec`, se decidirmos adotar a configuração de empacotamento. A pasta `.vscode/` continua ignorada, pois pode conter ajustes pessoais; caso a turma precise compartilhar configurações do editor, essa regra deverá ser reavaliada. Arquivos já rastreados não deixam de ser rastreados só porque foram incluídos no `.gitignore`.

Confira a alteração:

```powershell
git diff -- .gitignore
git status
```

Não ignore `src/`, `tests/`, `docs/`, `main.py`, `pyproject.toml` nem `LICENSE`.

## 4A. Licenciar o EngConvert sob a MIT

Esta atividade é **obrigatória e anterior à publicação**. O texto abaixo corresponde ao arquivo `LICENSE` fornecido para esta revisão.

### 4A.1. Criar o arquivo na raiz

No PowerShell, confirme a pasta do projeto e verifique se o arquivo já existe:

```powershell
Get-Location
Test-Path .\LICENSE
code .\LICENSE
```

O comando `code .\LICENSE` abre o arquivo no VSCode e permite criá-lo ao salvar, caso ainda não exista. **Se já existir, examine o conteúdo antes de substituir.** Não crie `LICENSE.txt` por engano.

### 4A.2. Texto integral da licença MIT

Copie para o arquivo `LICENSE`, sem acrescentar comentários ao texto legal:

```text
MIT License

Copyright (c) 2026 Wilson Luciano

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

O ano e o nome identificam o aviso de direitos autorais do projeto. Não remova os avisos exigidos por licenças de bibliotecas de terceiros.

### 4A.3. Conferir `pyproject.toml`

Abra o arquivo e localize a seção `[project]`:

```powershell
code .\pyproject.toml
```

Verifique se há uma declaração compatível com a licença adotada:

```toml
license = "MIT"
```

**Atenção:** acrescente a linha **dentro da seção `[project]` existente**, somente se necessário e compatível com a configuração de empacotamento usada no projeto. Não duplique a chave `license`, não crie outra seção `[project]` e não substitua o restante do arquivo. O `LICENSE` contém os termos jurídicos; `license = "MIT"` é o metadado do pacote.

### 4A.4. Registrar a licença no GitHub

Depois de salvar os arquivos, confira e registre somente os arquivos pertinentes:

```powershell
git status
git diff --check
git add LICENSE pyproject.toml
git diff --cached --check
git diff --cached --stat
git commit -m "docs: adiciona licenca MIT ao EngConvert"
```

Se `pyproject.toml` não tiver sido alterado, o `git add` apenas mantém seu estado atual. Se não houver mudanças a registrar, não force um commit vazio. A licença será enviada ao GitHub ao integrar a branch e executar o `git push` na Seção 11.

### 4A.5. Verificar o reconhecimento no GitHub

Depois do `git push`, abra a página principal do repositório, confira o arquivo `LICENSE` na raiz e verifique se o GitHub identifica **MIT** na área de licença (a posição visual pode variar). O reconhecimento pode não ser imediato; a presença e o conteúdo corretos do arquivo são a verificação principal.

### 4A.6. Relação com o executável e suas dependências

O ZIP da Release também deverá conter o arquivo `LICENSE`. Isso atende à necessidade de conservar o aviso de direitos autorais e o texto de permissão do EngConvert. Além disso, revise as licenças dos pacotes de terceiros incluídos pelo PyInstaller: elas podem impor obrigações próprias de aviso e redistribuição.

---

## 5. Instalar o PyInstaller

No `.venv` ativo:

```powershell
python -m pip install pyinstaller
python -m PyInstaller --version
```

O PyInstaller é uma ferramenta **de desenvolvimento**; não é necessário adicioná-lo às dependências de execução em `[project].dependencies` do `pyproject.toml`. Para permitir reprodução exata, registre a versão instalada na documentação ou em um arquivo de dependências de desenvolvimento, conforme a política do projeto.

## 5.1. Atividade opcional — preparar o ícone do EngConvert

O ícone do Windows utiliza a extensão **`.ico`**, diferente de `.iso` (imagem de disco). O uso de um ícone personalizado é opcional: o PyInstaller pode gerar o executável com o ícone padrão.

**No projeto do professor, `assets\engconvert.ico` já existe.** Nesse caso, siga diretamente para a Seção 5.1.1 e depois para a Seção 6. **Para o aluno que ainda não possui o arquivo**, a Seção 5.1.2 ensina a criá-lo.

### 5.1.1. Conferir um ícone existente

Na raiz `C:\Projetos\engconvert`, execute no PowerShell:

```powershell
Get-Location
Test-Path .\assets\engconvert.ico
Get-Item .\assets\engconvert.ico
```

`Test-Path` deve retornar `True`. Se o arquivo estiver presente, **não é necessário instalar Pillow nem criar outro ícone**.

### 5.1.2. Criar o ícone, caso ainda não exista (opcional)

1. Crie uma imagem quadrada simples, preferencialmente de **256 × 256 pixels**, em um editor de sua escolha. Por exemplo, duas setas em sentidos opostos para representar conversão de unidades.
2. Salve-a como `assets\engconvert.png`. Se a pasta `assets` ainda não existir, crie-a:

```powershell
New-Item -ItemType Directory -Path .\assets -Force
```

3. Para gerar um `.ico` multirresolução localmente, instale Pillow no ambiente virtual:

```powershell
python -m pip install pillow
```

4. Crie o arquivo temporário `criar_icone.py` na raiz do projeto com o código completo:

```python
"""Converte o PNG do EngConvert em um ícone Windows multirresolução."""
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
        raise ValueError("O PNG deve ser quadrado.")
    imagem = imagem.resize((256, 256), Image.Resampling.LANCZOS)
    imagem.save(
        destino,
        format="ICO",
        sizes=[(16, 16), (24, 24), (32, 32), (48, 48),
               (64, 64), (128, 128), (256, 256)],
    )

print(f"Ícone criado: {destino}")
```

5. Execute e confira:

```powershell
python .\criar_icone.py
Test-Path .\assets\engconvert.ico
```

O script `criar_icone.py` é apenas um recurso de preparação. O PNG e o ICO podem ser versionados no Git; o script também pode ser mantido, se for útil à documentação, ou removido depois de usado.

### 5.1.3. Ícones do executável e das janelas — claro e escuro

Há duas configurações independentes: `--icon` incorpora **um ícone fixo ao arquivo `.exe`**, enquanto `iconbitmap(...)` altera o ícone exibido nas barras de título. Para que o aplicativo alterne o ícone conforme o tema, é preciso **empacotar os arquivos de ícone usados em tempo de execução**.

Organize a pasta `assets`:

```text
assets/
├── engconvert.ico          ← ícone fixo do executável
├── engconvert-claro.ico    ← ícone das janelas no tema claro
└── engconvert-escuro.ico   ← ícone das janelas no tema escuro
```

Se ainda não houver `engconvert.ico`, pode-se copiar o arquivo claro:

```powershell
Copy-Item .\assets\engconvert-claro.ico .\assets\engconvert.ico
```

**Não substitua um arquivo existente sem antes conferir se deseja preservá-lo.** Se os ícones claro e escuro ainda não existirem, prepare-os antes de aplicar a alternância. A atividade opcional de criação de ICO das Seções 5.1.1 e 5.1.2 continua válida.

No `src/engconvert/interface.py` da versão mais recente deste roteiro, a função `caminho_icone(tema=None)` resolve o caminho dentro do projeto ou do executável empacotado. A aplicação usa:

- **Janela principal:** ícone claro ou escuro conforme o tema efetivo.
- **Configurações gerais:** também acompanha o tema.
- **Preferências — Categorias, Unidades personalizadas e Sobre:** sempre o ícone claro.

O **Anexo A** contém o código completo de referência atualizado. Se o seu arquivo local já tiver essas funcionalidades, **não o substitua desnecessariamente**; compare as alterações com `git diff`. Caso precise adotar a implementação do anexo, faça uma cópia de segurança do seu arquivo atual.

**Teste antes do empacotamento:**

```powershell
python -m pytest -q
python main.py
```

Abra as cinco janelas e alterne os temas. O tema Sistema segue a aparência detectada pelo CustomTkinter no momento da atualização; mudanças externas no Windows podem exigir reabrir o aplicativo.

**Por que `--add-data "assets;assets"`?** O PyInstaller deve levar **os três arquivos** para dentro do pacote. O parâmetro `--icon=assets\engconvert.ico` sozinho não disponibiliza os outros arquivos para `iconbitmap(...)`. No Windows, o `;` separa a origem do destino de `--add-data`.

## 6. Gerar o executável — primeiro `--onefile`, depois `--onedir`

### 6.1. Opção prioritária: um único `.exe` (`--onefile`)

Na raiz `C:\Projetos\engconvert`, com os três arquivos ICO disponíveis em `assets`, execute:

```powershell
python -m PyInstaller --noconfirm --clean --onefile --windowed --name EngConvert --icon=assets\engconvert.ico --add-data "assets;assets" --collect-all customtkinter main.py
```

O resultado esperado é `dist\EngConvert.exe`. **Não é necessária a pasta `_internal` ao lado desse executável**: o PyInstaller extrai os componentes necessários para um diretório temporário durante a execução. O primeiro início pode ser mais demorado.

**Se não houver ícones personalizados:** o comando abaixo gera um executável com ícone padrão; o código da interface deve tolerar a ausência dos arquivos ICO:

```powershell
python -m PyInstaller --noconfirm --clean --onefile --windowed --name EngConvert --collect-all customtkinter main.py
```

### 6.2. Alternativa: pasta com `_internal` (`--onedir`)

Para facilitar a inspeção dos arquivos e a depuração, também é possível gerar:

```powershell
python -m PyInstaller --noconfirm --clean --onedir --windowed --name EngConvert --icon=assets\engconvert.ico --add-data "assets;assets" --collect-all customtkinter main.py
```

O resultado será `dist\EngConvert\EngConvert.exe`, acompanhado da pasta `_internal`. **Distribua a pasta inteira**, nunca apenas o `.exe` desse modo.

Sem ícone personalizado:

```powershell
python -m PyInstaller --noconfirm --clean --onedir --windowed --name EngConvert --collect-all customtkinter main.py
```

### 6.3. Comparação dos formatos

| Critério            | `--onefile`                                                         | `--onedir`                              |
| ------------------- | ------------------------------------------------------------------- | --------------------------------------- |
| Distribuição        | Um `.exe`                                                           | Pasta com `.exe` e `_internal`          |
| Facilidade de envio | Mais simples                                                        | Exige manter a pasta completa           |
| Inicialização       | Pode ser mais lenta, por extração temporária                        | Geralmente mais rápida                  |
| Diagnóstico         | Recursos ficam dentro do pacote                                     | Dependências mais fáceis de inspecionar |
| Ícones de tema      | Funcionam se `assets` for incluída e os caminhos estiverem corretos | Mesma exigência                         |

### 6.4. Entender os parâmetros

| Parâmetro                      | Finalidade                                                                |
| ------------------------------ | ------------------------------------------------------------------------- |
| `--noconfirm`                  | Autoriza substituir saídas de compilação com o mesmo nome.                |
| `--clean`                      | Limpa o cache de construção do PyInstaller.                               |
| `--onefile` / `--onedir`       | Escolhe **um** formato por compilação.                                    |
| `--windowed`                   | Oculta o console para a aplicação gráfica.                                |
| `--name`                       | Define o nome do executável.                                              |
| `--icon=assets\engconvert.ico` | Define o ícone fixo do arquivo `.exe`.                                    |
| `--add-data "assets;assets"`   | Inclui a pasta de recursos para os ícones da janela em tempo de execução. |
| `--collect-all customtkinter`  | Coleta recursos do CustomTkinter necessários à distribuição.              |
| `main.py`                      | Ponto de entrada do programa.                                             |

**Atenção:** incluir `assets` não configura automaticamente a janela; o `interface.py` precisa localizar os arquivos empacotados e chamar `iconbitmap(...)`. Não use `--onefile` e `--onedir` juntos. O arquivo `.spec` gerado pode ser mantido no Git se for utilizado para reproduzir o empacotamento.

## 7. Executar o programa empacotado

```powershell
# Opção prioritária: --onefile
.\dist\EngConvert.exe

# Somente se você tiver gerado a alternativa --onedir:
# .\dist\EngConvert\EngConvert.exe
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

### 7.1. O ícone continua genérico ou antigo: diagnóstico e cache do Windows

**Primeiro identifique onde está o problema.** Se o ícone está correto no Explorador, mas genérico **na barra de título**, a causa provável é a ausência da chamada `app.iconbitmap(...)` ou do recurso `--add-data`; **limpar o cache não corrige isso**. Se o ícone está antigo **no Explorador**, pode ser o cache do Windows.

1. Confira se o ICO existe e se a compilação usou `--icon` (e `--add-data`, quando a janela o utiliza). Verifique também se está abrindo o **novo** `dist\EngConvert\EngConvert.exe`, e não um atalho antigo.
2. Pressione **F5** no Explorador, feche e reabra a pasta. Teste copiar o executável para uma pasta temporária com outro nome; isso ajuda a distinguir cache de ícone não incorporado.
3. Se necessário, reinicie apenas o Explorador pelo **Gerenciador de Tarefas → Windows Explorer → Reiniciar**. A barra de tarefas pode desaparecer brevemente e reaparecer.
4. Se o problema persistir, **salve seu trabalho** e experimente sair da conta do Windows e entrar novamente, ou reiniciar o computador.
5. **Somente como último recurso**, reconstrua o cache de ícones do seu perfil. Feche o EngConvert e janelas do Explorador, salve outros trabalhos e execute no PowerShell:

```powershell
# Identifique os arquivos de cache; este comando não exclui nada.
Get-ChildItem "$env:LOCALAPPDATA\Microsoft\Windows\Explorer\iconcache_*.db" -ErrorAction SilentlyContinue
Get-Item "$env:LOCALAPPDATA\IconCache.db" -ErrorAction SilentlyContinue
```

Se for realmente necessário apagar **somente** esses arquivos de cache, use os comandos abaixo. O Explorador será encerrado temporariamente e reiniciado; ícones poderão demorar a reaparecer. Arquivos em uso podem impedir a exclusão — nesse caso, reinicie o Windows e não force exclusões indiscriminadas.

```powershell
Stop-Process -Name explorer -Force -ErrorAction SilentlyContinue
Remove-Item "$env:LOCALAPPDATA\IconCache.db" -Force -ErrorAction SilentlyContinue
Remove-Item "$env:LOCALAPPDATA\Microsoft\Windows\Explorer\iconcache_*.db" -Force -ErrorAction SilentlyContinue
Start-Process explorer.exe
```

**Não apague outras pastas do Windows**, não desative o antivírus e não confunda o cache de ícones do Windows com o cache de compilação do PyInstaller (`--clean`). A reconstrução do cache pode não resolver um ICO inválido ou um executável compilado sem o parâmetro correto.

### 7.2. Se o `.exe` não abrir

1. Refaça `python main.py` para distinguir falha do projeto e falha do empacotamento.
2. Confira mensagens de erro do PyInstaller no terminal.
3. Gere **temporariamente** uma versão de diagnóstico, sem `--windowed`, em outro nome:

```powershell
python -m PyInstaller --noconfirm --clean --onedir --console --name EngConvert-Debug --add-data "assets;assets" --collect-all customtkinter main.py
.\dist\EngConvert-Debug\EngConvert-Debug.exe
```

4. Leia o erro exibido no terminal. Depois de corrigir a causa, refaça a distribuição final `EngConvert` com `--windowed`.

> Não copie DLLs aleatórias da internet nem desative o antivírus como solução padrão.

### 7.3. Refazer a distribuição: quais pastas apagar e como apagar no PowerShell

Se o resultado do PyInstaller **não ficou como você queria** — por exemplo, o executável foi gerado sem o ícone correto, a distribuição apresentou erro ou você decidiu trocar de `--onedir` para `--onefile` — pode ser útil limpar os **arquivos gerados** e compilar novamente. Isso **não apaga nem corrige o código-fonte**.

| Caminho na raiz do projeto                                         | O que contém                                                                                   | Pode apagar para recompilar?                                                |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `build/`                                                           | Arquivos intermediários e temporários do PyInstaller                                           | **Sim**, após encerrar a compilação.                                        |
| `dist/`                                                            | Distribuições prontas, inclusive a pasta `EngConvert/`, `_internal/` e executáveis `--onefile` | **Sim**, mas somente após guardar qualquer executável que queira conservar. |
| `EngConvert.spec` e outros `*.spec`                                | Configurações de empacotamento                                                                 | **Preservar**, principalmente se foram personalizadas ou versionadas.       |
| `assets/` e `assets/engconvert.ico`                                | Ícone e demais recursos originais                                                              | **Não apagar**.                                                             |
| `src/`, `main.py`, `tests/`, `.venv/`, `LICENSE`, `pyproject.toml` | Código, testes, ambiente e documentação/licença                                                | **Não apagar** para refazer o executável.                                   |

**Passo 1 — Fechar o aplicativo e conferir a pasta atual.** Feche as janelas do EngConvert e aguarde o término do PyInstaller. No PowerShell, execute:

```powershell
cd C:\Projetos\engconvert
Get-Location
Get-ChildItem .\build, .\dist -ErrorAction SilentlyContinue
```

Confirme que `Get-Location` aponta para `C:\Projetos\engconvert`. **Não prossiga se estiver em outra pasta** ou se houver arquivos pessoais dentro de `dist/` que ainda não foram copiados.

**Passo 2 — Excluir apenas as duas pastas geradas.** Os comandos seguintes só atuam em `build` e `dist` **dentro da pasta atual**:

```powershell
if (Test-Path .\build) { Remove-Item .\build -Recurse -Force }
if (Test-Path .\dist)  { Remove-Item .\dist  -Recurse -Force }
```

O `Test-Path` verifica se a pasta existe; `Remove-Item` a exclui; `-Recurse` inclui o conteúdo e `-Force` permite remover itens ocultos ou somente leitura. **A exclusão não vai para a Lixeira**. Se aparecer erro de arquivo em uso, feche o executável e tente novamente; não force a exclusão de outras pastas.

**Passo 3 — Verificar a limpeza.**

```powershell
Test-Path .\build
Test-Path .\dist
```

O resultado esperado para ambas é `False`. Caso queira conservar uma distribuição antiga para comparação, **copie-a para outro local antes do Passo 2**, ou simplesmente mantenha as pastas e use `--noconfirm --clean` na próxima compilação.

**Passo 4 — Gerar novamente o formato escolhido.** Para o modo **pasta (`--onedir`)**, com o ícone do executável e o arquivo ICO disponível também para a janela:

```powershell
python -m PyInstaller --noconfirm --clean --onedir --windowed --name EngConvert --icon=assets\engconvert.ico --add-data "assets;assets" --collect-all customtkinter main.py
```

Para o modo **arquivo único (`--onefile`)**, se já tiver aplicado o código de ícone da janela da Seção 5.1.3:

```powershell
python -m PyInstaller --noconfirm --clean --onefile --windowed --name EngConvert --icon=assets\engconvert.ico --add-data "assets;assets" --collect-all customtkinter main.py
```

Escolha **um comando por vez**. Os comandos com `--icon` e `--add-data` pressupõem a existência de `assets\engconvert.ico`; para quem não possui o ícone, use as alternativas sem ícone descritas nas seções anteriores. Se o arquivo `.spec` já tiver configurações próprias que você pretende reutilizar, revise-o antes de reconstruir, em vez de substituí-lo inadvertidamente.

**Passo 5 — Testar antes de publicar.** Execute o novo `.exe`, confira o ícone no Explorador **e** na barra de título, as conversões e a persistência das preferências. Se o ícone do Explorador continuar antigo, siga o diagnóstico de **cache de ícones do Windows** da Seção 7.1; apagar `build/` e `dist/` não limpa esse cache. Se você já tinha criado um ZIP, **gere-o novamente**, pois ele não é atualizado automaticamente pela recompilação.

> **Nota para o aluno:** `--clean` limpa caches de construção do PyInstaller, enquanto os comandos acima removem as pastas de saída `build/` e `dist/`. São operações diferentes. No PowerShell, não use `rmdir /s /q`, que é sintaxe do CMD.

## 8. Testar fora da pasta do projeto

Para a opção prioritária, copie **somente** `dist\EngConvert.exe` para outra pasta do Windows; na opção `--onedir`, copie a pasta **inteira** `dist\EngConvert`. Faça o teste ou, preferencialmente, outro computador Windows compatível. Abra `EngConvert.exe` de lá. Esse teste ajuda a detectar dependências acidentais do projeto, do `.venv` ou do VSCode.

**Critério de aceitação:** em ambos os formatos, o programa deve abrir e executar as conversões principais sem o usuário precisar instalar Python ou CustomTkinter. Não confunda esse requisito com compatibilidade garantida com toda versão do Windows.

## 9. Gerar o ZIP para publicação

**Opção prioritária (`--onefile`):** inclua o executável `EngConvert.exe` e o arquivo `LICENSE` na raiz do ZIP:

```powershell
Compress-Archive -Path .\dist\EngConvert.exe, .\LICENSE -DestinationPath .\EngConvert-v0.1.0-Windows.zip -Force
```

A estrutura esperada após a extração é:

```text
EngConvert.exe
LICENSE
```

**Alternativa (`--onedir`):** se optar por esse formato, execute a compilação correspondente da Seção 6.2 e gere um ZIP com outro nome, para não confundir as distribuições:

```powershell
Compress-Archive -Path .\dist\EngConvert, .\LICENSE -DestinationPath .\EngConvert-v0.1.0-Windows-Onedir.zip -Force
```

Nesse caso, a estrutura extraída contém `EngConvert/EngConvert.exe`, `EngConvert/_internal/` e `LICENSE` na raiz. **Não misture os dois formatos no mesmo diretório `dist` sem conferir qual compilação foi executada por último.**

Confirme o ZIP, extraia-o em outra pasta e execute o programa fora do projeto:

```powershell
Get-Item .\EngConvert-v0.1.0-Windows.zip
```

## 10. Preparar o `README.md`

O README deve apresentar a identidade visual do EngConvert com **imagens adaptativas aos temas claro e escuro** e explicar como baixar e executar a distribuição `--onefile`. O texto integral, pronto para copiar, está no **Anexo B** desta aula.

Salve `EngConvert_Claro.png` e `EngConvert_Escuro.png` em `assets/` com esses nomes exatos. O trecho `<picture>` utiliza `prefers-color-scheme` para selecionar a imagem conforme o tema usado na visualização do GitHub. Confira as imagens na visualização do README antes do commit.

A seção de download deve corresponder à estrutura do ZIP gerado: no modo prioritário, o usuário extrai o ZIP e executa `EngConvert.exe` diretamente na pasta de extração, **sem precisar abrir uma subpasta `EngConvert`**. A alternativa `--onedir` tem instruções diferentes, porque contém uma pasta com `_internal`.

## 11. Registrar a entrega no Git e integrar a branch com segurança

### 11.1. Conferir o estado do repositório

No PowerShell, na raiz `C:\Projetos\engconvert`:

```powershell
git status
git branch --show-current
git diff --stat
git log -1 --oneline --decorate
```

Identifique se está na branch de trabalho `chore-distribuicao`. O nome é um exemplo didático: use o nome efetivo de sua branch. Antes de preparar o commit, **não inclua automaticamente** aulas ainda em revisão, saídas de `build/` ou `dist/`, arquivos de preferências do usuário nem arquivos `.spec` não revisados.

### 11.2. Preparar somente os arquivos aprovados

```powershell
git add .gitignore README.md
git add src/engconvert/interface.py
git add LICENSE
git add assets/engconvert.ico assets/engconvert-claro.ico assets/engconvert-escuro.ico
git add assets/EngConvert_Claro.png assets/EngConvert_Escuro.png
# Se pyproject.toml foi realmente alterado: git add pyproject.toml
# Se o arquivo .spec foi conferido e adotado: git add EngConvert.spec

git diff --cached --check
git diff --cached --stat
git status
```

Adapte os caminhos aos arquivos existentes. Se um arquivo não existir, não tente adicioná-lo. Revise o conteúdo preparado com `git diff --cached`. Depois de testar a aplicação e conferir a seleção:

```powershell
git commit -m "build: prepara distribuicao Windows do EngConvert"
git log -1 --oneline --decorate
```

**Importante:** um commit já existente não deve ser repetido. No exemplo real da aula, o commit da distribuição recebeu o identificador abreviado `ce34aea`.

### 11.3. Comparar a branch de trabalho com a `main`

```powershell
git fetch origin
git log --oneline --decorate -5
git log --oneline main..chore-distribuicao
git status -sb
```

O terceiro comando mostra os commits presentes na branch de distribuição e ausentes da `main`. No exemplo de referência, apareceu apenas:

```text
ce34aea build: prepara distribuicao Windows do EngConvert
```

Se houver alterações locais ainda não aprovadas, guarde-as temporariamente **antes de trocar de branch**:

```powershell
git stash push -u -m "WIP: aulas em revisao e arquivos spec"
git status -sb
git stash list
```

`-u` inclui arquivos não rastreados (por exemplo, aulas em elaboração e `.spec`). O `stash` não inclui arquivos ignorados por padrão e não deve ser usado como substituto de backup permanente. A saída esperada é uma árvore de trabalho limpa e uma entrada `stash@{0}`.

### 11.4. Atualizar a `main` sem criar um merge desnecessário

```powershell
git switch main
git merge --ff-only chore-distribuicao
git log -1 --oneline --decorate
git status -sb
```

`--ff-only` permite o avanço direto e interrompe a operação se for necessário resolver divergências. Se o Git responder `Already up to date`, isso **não é erro**: a `main` já contém os commits. No exemplo real, `main`, `origin/main`, `chore-distribuicao` e a tag `v0.1.0` já apontavam para `ce34aea`.

Depois de confirmar os testes e o commit:

```powershell
git push origin main
```

Se `origin/main` já aponta para o mesmo commit, o envio pode informar `Everything up-to-date`.

## 12. Verificar e publicar a tag da versão

A tag associa um nome de versão a um commit; **não é o ZIP** e **não é a Release**. Confira o remoto e a tag:

```powershell
git remote -v
git tag --list v0.1.0
git show --no-patch --oneline v0.1.0
```

**Somente se a tag ainda não existir** e a versão estiver validada, crie-a a partir da `main` no commit correto:

```powershell
git tag -a v0.1.0 -m "EngConvert v0.1.0 - primeira distribuicao Windows"
```

Publique ou confirme a tag:

```powershell
git push origin v0.1.0
```

A mensagem `Everything up-to-date` significa que a tag já está publicada. **Não recrie, mova ou force a tag `v0.1.0`** se ela já foi divulgada. Se a Release já tiver sido criada no GitHub, não crie uma segunda: apenas verifique sua tag e o ZIP anexado.

### 12.1. Recuperar os arquivos de trabalho guardados

Depois de publicar a `main` e a tag, retorne à branch de desenvolvimento e restaure os arquivos:

```powershell
git switch chore-distribuicao
git stash pop
git status -sb
```

Se o `stash pop` for bem-sucedido, é normal aparecer `Dropped refs/stash@{0}`: a entrada temporária foi retirada depois da restauração. No exemplo real, reapareceram a Aula 10.2 modificada, as Aulas 11.0 e 11.1 não rastreadas e os arquivos `.spec`. **Esses arquivos não foram enviados à `main` nem incluídos na Release.**

Em caso de conflito, interrompa o procedimento e analise os arquivos antes de executar outros comandos. Não use `git reset --hard` nem `git clean -fd` para tentar resolver o problema.

## 13. Publicar no GitHub Releases (navegador)

1. Abra a página do repositório EngConvert no GitHub.
2. Localize **Releases** e selecione **Draft a new release** ou **Create a new release** (a interface pode variar).
3. Em **Choose a tag**, selecione a tag existente `v0.1.0` (ou crie-a apenas se ainda não existir e o commit estiver correto).
4. Informe o título `EngConvert v0.1.0 — Windows`.
5. Preencha as notas de lançamento com os recursos realmente testados.
6. Na área de anexos (_assets_), arraste ou selecione **`EngConvert-v0.1.0-Windows.zip`**.
7. Confira se o ZIP foi anexado à versão correta e publique a Release.
8. Abra a página pública da Release e faça o download do ZIP para verificar a experiência do usuário.

**Conferência após publicar:** verifique que `main` e a tag `v0.1.0` apontam para o commit utilizado na compilação; em **Assets**, confirme que `EngConvert-v0.1.0-Windows.zip` está anexado. Os arquivos automáticos `Source code (zip)` e `Source code (tar.gz)` **não substituem** o ZIP contendo o executável. Extraia o ZIP baixado em uma pasta diferente e execute `EngConvert.exe`.

**Se a Release já existir:** não a duplique; abra a publicação existente e confira a tag, o anexo e as notas.

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
3. Execute `EngConvert.exe` na pasta em que extraiu o ZIP (distribuição `--onefile`).

### Observações

- Distribuição portátil para Windows, sem instalador.
- Testada no ambiente Windows documentado no projeto.
```

> A publicação é uma ação na sua conta GitHub: os passos acima devem ser executados pelo aluno. Esta aula não pressupõe que uma Release já tenha sido criada.

## 14. Conferência final das duas opções

Os comandos completos para **`--onefile` (prioritário)** e **`--onedir` (alternativo)** já estão na Seção 6, próximos à explicação de cada formato. Não é necessário procurá-los no final da aula.

Depois de compilar, teste o executável correspondente:

```powershell
# Opção prioritária:
.\dist\EngConvert.exe

# Opção alternativa, se tiver sido gerada:
.\dist\EngConvert\EngConvert.exe
```

Confira as conversões, o salvamento das preferências, a alternância entre ícones claro/escuro na janela principal e em Configurações gerais e o ícone claro nas outras três janelas. Se a interface estiver correta no Python, mas não no executável, confira **primeiro** se `--add-data "assets;assets"` foi usado. Limpar o cache de ícones do Windows não substitui a inclusão desses recursos.

**Importante:** alterações em `interface.py` devem ser testadas e registradas no Git antes da tag correspondente à Release.

## 15. Checklist de encerramento

- [ ] Projeto integrado da Aula 10.2 validado.
- [ ] `python -m pytest -q` aprovado.
- [ ] `EngConvert.exe` abre e converte corretamente.
- [ ] Ícone existente `assets/engconvert.ico` verificado, incluído no comando e conferido no Explorador do Windows.
- [ ] Ícone da barra de título testado com `app.iconbitmap(...)` e recurso `--add-data`.
- [ ] Se o ícone não atualizar, diagnosticar antes de reconstruir o cache do Windows.
- [ ] Modificações em `interface.py` testadas e incluídas no commit antes da tag.
- [ ] (Opcional) `--onefile` testado fora do projeto, sem depender de `_internal`.
- [ ] General, Custom, About e JSON testados.
- [ ] Teste fora da pasta original concluído.
- [ ] ZIP íntegro e extraído com sucesso.
- [ ] `LICENSE` MIT criado, metadados de `pyproject.toml` conferidos e avisos de dependências revisados.
- [ ] GitHub reconhece a licença MIT no repositório.
- [ ] ZIP inclui `LICENSE` na raiz.
- [ ] `.gitignore` revisado e código enviado ao GitHub.
- [ ] Tag de versão criada sem sobrescrever outra.
- [ ] Branch `main` sincronizada, tag conferida e Release publicada com o ZIP correto em **Assets**.
- [ ] Arquivos didáticos ainda em revisão preservados; se `stash` foi usado, restauração conferida.
- [ ] Download público testado.

## 16. Perguntas de fixação

1. Por que a pasta `dist/` não deve ser enviada em commits normais?
2. O que significa `--collect-all customtkinter`?
3. Qual a diferença entre `git push` e anexar um ZIP a uma Release?
4. Por que é necessário testar o ZIP após extraí-lo?
5. O que o usuário precisa instalar para executar a distribuição `--onedir` validada?
6. Qual a diferença entre o ícone do executável (`--icon`) e o ícone da janela CustomTkinter?
7. Por que `--add-data` é necessário para carregar o ICO na janela, mas não para incorporar o ícone ao `.exe`?
8. Qual a diferença entre `--onedir` e `--onefile`, e por que não se deve apagar `_internal` no primeiro modo?
9. Quando a reconstrução do cache de ícones do Windows é pertinente?

10. Por que o arquivo `LICENSE` deve acompanhar a distribuição e não ser substituído apenas por `license = "MIT"`?
11. Quais pastas podem ser excluídas para refazer o executável e por que devemos preservar `assets/` e os arquivos `.spec`?

## 17. Resumo da aula

```text
Código licenciado e testado → PyInstaller (--onefile) → EngConvert.exe
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

---

## Anexo A — Código completo de `src/engconvert/interface.py` com ícones por tema

O código abaixo corresponde à revisão que aplica ícones conforme o tema à janela principal e a Configurações gerais, mantendo o ícone claro nas outras três janelas. Compare com a sua versão antes de substituir arquivos locais.

```python

"""Interface integrada do EngConvert — Sprints 09 a 12."""
import tkinter as tk
import math
from tkinter import messagebox
import customtkinter as ctk
from .dados import lista_grandezas
from . import configuracoes as cfg
from . import personalizadas as pers

import sys
from pathlib import Path


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

def caminho_icone(tema=None):
    """Localiza o ícone da janela conforme o tema efetivo do CustomTkinter.

    No tema Sistema, get_appearance_mode() informa se o Windows está
    efetivamente em modo claro ou escuro.
    """
    if getattr(sys, "frozen", False):
        raiz = Path(sys._MEIPASS)
    else:
        # interface.py está em src/engconvert; parents[2] é a raiz do projeto.
        raiz = Path(__file__).resolve().parents[2]

    modo = tema or ctk.get_appearance_mode()
    nome = "engconvert-escuro.ico" if modo == "Dark" else "engconvert-claro.ico"
    icone = raiz / "assets" / nome
    if not icone.is_file():
        icone = raiz / "assets" / "engconvert.ico"
    return icone


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
    # A janela principal e Configurações gerais acompanham o tema.
    # As demais janelas auxiliares mantêm sempre o ícone claro.
    # O ícone incorporado ao executável pelo PyInstaller é independente.
    def aplicar_icone(janela):
        if not janela.winfo_exists():
            return
        icone = caminho_icone(None if janela is app or getattr(janela, "_icone_acompanha_tema", False) else "Light")
        if icone.is_file():
            try:
                janela.iconbitmap(str(icone))
            except tk.TclError:
                pass  # Um arquivo ICO inválido não deve encerrar o programa.

    def atualizar_icone_janela():
        aplicar_icone(app)
        for janela in app.winfo_children():
            if isinstance(janela, ctk.CTkToplevel):
                aplicar_icone(janela)

    def criar_janela_auxiliar(acompanhar_tema=False):
        janela = ctk.CTkToplevel(app)
        janela._icone_acompanha_tema = acompanhar_tema
        aplicar_icone(janela)
        # CustomTkinter pode redefinir o ícone após criar a janela.
        janela.after(300, lambda j=janela: aplicar_icone(j))
        return janela

    atualizar_icone_janela()
    app.after(350, atualizar_icone_janela)
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
        janela = criar_janela_auxiliar()
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
        janela = criar_janela_auxiliar(acompanhar_tema=True)
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
                atualizar_icone_janela()
                app.after(350, atualizar_icone_janela)
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
        janela = criar_janela_auxiliar()
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
        janela = criar_janela_auxiliar()
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

## Anexo B — `README.md` completo com imagens adaptativas e download Windows

O conteúdo a seguir corresponde ao README atualizado. **Copie somente o conteúdo do bloco Markdown para o arquivo `README.md` na raiz do projeto**, preservando os nomes dos arquivos de imagem em `assets/`.

````markdown
# EngConvert

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/EngConvert_Escuro.png">
    <source media="(prefers-color-scheme: light)" srcset="assets/EngConvert_Claro.png">
    <img src="assets/EngConvert_Claro.png" alt="Logotipo do EngConvert" width="280">
  </picture>
</p>

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

| Aulas             | Tema                                                       |
| ----------------- | ---------------------------------------------------------- |
| 01.0 e 01.1       | VSCode, estrutura do projeto e ambiente de desenvolvimento |
| 02.0 e 02.1       | Fundamentos de GUI, roadmap e Sprints                      |
| 03.0 e 03.1       | Widgets e eventos                                          |
| 04.0 e 04.1       | Primeiro conversor                                         |
| 05.0 e 05.1       | Conversor de pressão                                       |
| 06.0 e 06.1       | Novas grandezas e conversor multicategorias                |
| 07.0 e 07.1       | Git, GitHub e controle de versão                           |
| 07.2              | README de perfil do GitHub                                 |
| 08.0 e 08.1       | Modularização do EngConvert                                |
| 09.0 e 09.1       | Fundamentos e prática de testes de software                |
| 10.0, 10.1 e 10.2 | Interface completa e roteiros práticos                     |
| 11.0 e 11.1       | Fundamentos de empacotamento e geração de executável       |

> **Nota:** algumas aulas podem estar em preparação ou disponíveis apenas na cópia local do projeto, antes de sua publicação no GitHub.

Consulte também o [`roadmap`](docs/roadmap.md) e a documentação das Sprints em `docs/sprints/`.

## Estrutura do projeto

```text
engconvert/
├── assets/                # Imagens e ícones do aplicativo
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

## Download do EngConvert para Windows

Acesse a seção **Releases** deste repositório e baixe o arquivo
`EngConvert-v0.1.0-Windows.zip` da versão correspondente.

1. Extraia **todo** o conteúdo do ZIP para uma pasta de sua preferência.
2. Abra a pasta em que os arquivos foram extraídos.
3. Execute `EngConvert.exe`.

O ZIP da versão prioritária (`--onefile`) contém `EngConvert.exe` e `LICENSE` na raiz. Não há pasta `_internal` nem é necessário instalar Python separadamente. O programa foi desenvolvido em Python e CustomTkinter.

O EngConvert é disponibilizado sob a licença MIT (consulte o arquivo `LICENSE` no repositório e no ZIP). As preferências são salvas na pasta de dados do usuário do Windows.

> O executável é destinado ao Windows. Esta versão é distribuída sem instalador e pode exibir avisos de reputação do sistema caso não esteja assinada digitalmente. Verifique a procedência do download.
````
