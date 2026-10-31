# Aula inicial — Meu perfil profissional no GitHub

## Criando um README com identidade própria e versões clara e escura

**Disciplina:** Programação para Engenharia Mecânica  
**Professor:** Wilson Luciano — Universidade Federal de Sergipe (UFS)  
**Pré-requisitos:** conta pessoal no GitHub, navegador e acesso à internet.  
**Resultado:** perfil público com apresentação, interesses, projetos e um banner que acompanha o tema claro ou escuro do GitHub.

> Primeiro, publique o perfil pelo navegador (seções 1 a 8). Depois, pratique a atualização local com Git Bash e VSCode (seção 9). Para essa segunda etapa, é necessário ter Git e VSCode instalados. O mesmo repositório será utilizado nas duas etapas.

**Percurso:** criar o repositório → publicar uma apresentação simples → criar os banners → colar e personalizar o modelo completo → clonar no computador → editar e enviar uma atualização com Git → conferir o perfil.

**Ao final, o estudante deverá conseguir:** distinguir perfil de projeto, editar Markdown, organizar imagens, testar os dois temas e explicar a sequência `status`, `add`, `commit` e `push`.

## 1. O que vamos construir?

O GitHub permite apresentar um texto de boas-vindas diretamente no perfil. Esse conteúdo é escrito em um arquivo chamado `README.md`, armazenado em um repositório especial.

Um **repositório** organiza arquivos e o histórico de suas alterações. Um **README** apresenta informações para quem visita um perfil ou projeto. A extensão `.md` indica um arquivo Markdown: texto com marcações simples para títulos, listas, links e imagens.

### Referência do professor

Acesse: [github.com/wilson-luciano](https://github.com/wilson-luciano).

Observe a apresentação, a organização por assuntos e a integração entre engenharia, programação e tecnologia. O arquivo de referência usado na preparação desta aula foi `README.md`, com a identidade **Future Engineering System**.

| Na referência do professor | Na página do estudante                |
| -------------------------- | ------------------------------------- |
| Apresentação profissional  | Apresentação como estudante           |
| ENGINEER_IDENTITY          | Sobre mim                             |
| ENGINEERING_CORE           | Áreas de interesse                    |
| TECHNOLOGY_STACK           | Tecnologias que estou aprendendo      |
| RESEARCH_EDUCATION         | Estudos e projetos acadêmicos         |
| SYSTEM_CONNECT             | Links e contato profissional          |
| Banner claro e escuro      | Banner personalizado com duas versões |

Use a organização como inspiração e escreva sua própria trajetória. Diferencie conhecimentos que já utiliza de assuntos que ainda está aprendendo.

## 2. Entendendo a regra do repositório especial

O nome do repositório precisa corresponder ao **nome de usuário do GitHub**. Não use o nome completo exibido no perfil, a menos que ele também seja seu usuário.

| Item                         | Exemplo fictício                               |
| ---------------------------- | ---------------------------------------------- |
| Usuário                      | `ana-mecanica`                                 |
| Perfil                       | `https://github.com/ana-mecanica`              |
| Nome do repositório especial | `ana-mecanica`                                 |
| Endereço do repositório      | `https://github.com/ana-mecanica/ana-mecanica` |
| Arquivo de apresentação      | `README.md`, na raiz                           |

O repositório deve ser **público** e o `README.md` precisa conter conteúdo para aparecer no perfil.

> O README de um projeto, como o EngConvert, explica o projeto. O README do perfil apresenta a pessoa. São arquivos com finalidades diferentes, mesmo tendo o mesmo nome.

## 3. Criando o repositório pelo navegador

1. Entre na sua conta em [github.com](https://github.com).
2. Confira seu usuário no endereço de **Your profile** (Seu perfil).
3. Clique no botão **+** e depois em **New repository** (Novo repositório).
4. Em **Owner**, mantenha sua conta pessoal.
5. Em **Repository name**, digite exatamente seu usuário.
6. Em **Description**, escreva: `Meu perfil acadêmico e meus projetos de engenharia e programação.`
7. Selecione **Public**.
8. Ative **Add README** ou **Add a README file**, conforme a interface exibida.
9. Clique em **Create repository**.

Se o repositório já existir, abra-o e continue pela edição do README. Não é necessário recriá-lo.

### Primeira edição

1. Abra `README.md` e clique no lápis para editar, ou use **Edit README**.
2. Substitua o conteúdo inicial por:

```markdown
# Olá! Eu sou Ana 👋

Sou estudante de Engenharia Mecânica e estou aprendendo Python.

## Meus interesses

- Engenharia Mecânica
- Programação aplicada à engenharia
- Automação
```

3. Troque o nome e os interesses pelos seus.
4. Use **Preview** (Visualização) para conferir a formatação.
5. Clique em **Commit changes**.
6. Escreva a mensagem `docs: adicionar apresentação inicial ao perfil`.
7. Confirme a gravação. Se houver a escolha, grave diretamente na branch principal para esta atividade individual.
8. Abra seu perfil e confira a apresentação.

**Commit** é um registro de alterações no histórico. Sua mensagem explica o que mudou. O prefixo `docs:` é uma convenção de organização usada nesta aula, não uma exigência do GitHub.

## 4. Markdown essencial

| O que queremos   | Como escrever                                     |
| ---------------- | ------------------------------------------------- |
| Título principal | `# Meu nome`                                      |
| Título de seção  | `## Sobre mim`                                    |
| Negrito          | `**Engenharia Mecânica**`                         |
| Item de lista    | `- Estou aprendendo Python`                       |
| Link             | `[Meu perfil](https://github.com/SEU_USUARIO)`    |
| Código curto     | Texto entre crases, como `Python`                 |
| Imagem           | `![Descrição da imagem](assets/banner-claro.svg)` |

Deixe uma linha vazia entre títulos, parágrafos e listas. Use **Preview** após editar.

## 5. Tema claro e escuro: quem controla o fundo?

Há duas configurações diferentes:

| Elemento                  | Como funciona                                        |
| ------------------------- | ---------------------------------------------------- |
| Fundo da página do GitHub | Depende do tema escolhido por quem está visualizando |
| Cores do texto Markdown   | São adaptadas pelo GitHub ao tema                    |
| Fundo e cores do banner   | Fazem parte do próprio arquivo de imagem             |
| Troca do banner           | Pode acompanhar o tema usando `<picture>`            |

O autor do README não força o fundo de toda a página para os visitantes. Também não cria, no README, um botão funcional com JavaScript para trocar o tema. Nesta aula, o visitante escolhe o tema nas configurações do GitHub e o banner acompanha essa escolha.

### Alterando o tema para testar

1. Clique na sua foto de perfil.
2. Entre em **Settings** (Configurações).
3. Abra **Appearance** (Aparência).
4. Em **Theme mode**, selecione a opção de tema único, quando necessário.
5. Escolha um tema **Light** (claro).
6. Volte ao seu perfil para observar o resultado.
7. Repita escolhendo um tema **Dark** (escuro).

Também é possível configurar o GitHub para acompanhar o tema do sistema operacional.

## 6. Criando dois banners simples

Vamos usar SVG: um formato de imagem vetorial escrito em texto. Você poderá personalizar os exemplos abaixo sem instalar um editor de imagens.

**Estrutura final:** o repositório terá `README.md` na raiz e a pasta `assets` contendo `banner-claro.svg` e `banner-escuro.svg`.

### O que significa o endereço do W3C?

Em `xmlns="http://www.w3.org/2000/svg"`, `xmlns` declara o espaço de nomes SVG. O endereço identifica o padrão de gráficos vetoriais do W3C; não é uma imagem para baixar nem exige abrir esse site. Mantenha esse trecho como está. Você personalizará os textos e as cores.

### 6.1 Banner claro

1. Volte à página do seu repositório especial.
2. Clique em **Add file → Create new file**.
3. No campo do nome, digite `assets/banner-claro.svg`.
4. A barra `/` indica que o arquivo ficará dentro da pasta `assets`.
5. Cole o código abaixo e substitua `SEU NOME` pelo seu nome.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320">
  <!-- Fundo claro do banner -->
  <rect width="1200" height="320" rx="20" fill="#F1F5F9"/>
  <!-- Faixa decorativa azul -->
  <rect x="40" y="48" width="8" height="224" rx="4" fill="#2563EB"/>
  <!-- Nome: prefira um nome curto para caber no espaço -->
  <text x="80" y="125" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="#0F172A">SEU NOME</text>
  <text x="80" y="185" font-family="Arial, sans-serif" font-size="28" fill="#1D4ED8">ENGENHARIA MECÂNICA</text>
  <text x="80" y="235" font-family="Arial, sans-serif" font-size="23" fill="#334155">Aprendendo • Programando • Construindo soluções</text>
</svg>
```

6. Clique em **Commit changes**.
7. Use a mensagem `docs: adicionar banner claro` e confirme.

### 6.2 Banner escuro

Repita **Add file → Create new file**, agora com o nome `assets/banner-escuro.svg`. Se estiver navegando dentro de `assets`, crie apenas `banner-escuro.svg`, para não formar uma pasta `assets/assets`.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320">
  <!-- Fundo escuro do banner -->
  <rect width="1200" height="320" rx="20" fill="#0F172A"/>
  <!-- Faixa decorativa azul -->
  <rect x="40" y="48" width="8" height="224" rx="4" fill="#60A5FA"/>
  <!-- Mantenha o mesmo nome da versão clara -->
  <text x="80" y="125" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="#F8FAFC">SEU NOME</text>
  <text x="80" y="185" font-family="Arial, sans-serif" font-size="28" fill="#60A5FA">ENGENHARIA MECÂNICA</text>
  <text x="80" y="235" font-family="Arial, sans-serif" font-size="23" fill="#CBD5E1">Aprendendo • Programando • Construindo soluções</text>
</svg>
```

Grave com a mensagem `docs: adicionar banner escuro`.

**Personalização:** `fill` define cores; `font-size` define o tamanho do texto; `x` e `y` posicionam o texto. Nomes longos podem exigir redução do tamanho da fonte. Ao escrever texto em SVG, use `&amp;` no lugar de um `&` literal.

Você também pode criar duas imagens PNG em um editor gráfico. Nesse caso, envie os arquivos para `assets` e ajuste os nomes e as extensões no README. As duas versões devem ter dimensões e conteúdo equivalentes.

## 7. Modelo completo para o estudante

Edite o `README.md` e substitua seu conteúdo pelo modelo abaixo. Copie apenas o conteúdo interno do bloco. Troque `SEU NOME`, `SEU_USUARIO` e as informações de exemplo.

```markdown
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-escuro.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-claro.svg">
  <img alt="SEU NOME — Engenharia Mecânica e Programação" src="assets/banner-claro.svg" width="100%">
</picture>

# Olá! Eu sou SEU NOME 👋

### Estudante de Engenharia Mecânica | Python e Tecnologia

Sou estudante de **Engenharia Mecânica na Universidade Federal de Sergipe (UFS)**.
Estou aprendendo a usar programação para analisar dados, automatizar cálculos
e desenvolver soluções para problemas de engenharia.

> 🎯 **Meu propósito:** conectar os fundamentos da engenharia às ferramentas digitais.

## 🧭 01 | MINHA IDENTIDADE

- 🎓 **Formação em andamento:** Engenharia Mecânica — UFS.
- 📚 **Estudos atuais:** programação com Python, Git e GitHub.
- ⚙️ **Interesses:** energia, fabricação e automação.
- 🛠️ **Objetivo:** desenvolver projetos acadêmicos e documentar meu aprendizado.

## ⚙️ 02 | ENGENHARIA E INTERESSES

### Energia e sistemas térmicos

Tenho interesse em compreender a conversão de energia e o funcionamento de máquinas térmicas.

### Fabricação e sistemas industriais

Quero conhecer processos de fabricação, equipamentos e aplicações de automação na indústria.

### Engenharia e programação

Pretendo utilizar programação em cálculos, conversões de unidades e análise de dados experimentais.

## 💻 03 | TECNOLOGIAS EM APRENDIZADO

| Tecnologia   | O que estou estudando                     | Aplicação pretendida                     |
| ------------ | ----------------------------------------- | ---------------------------------------- |
| Python       | Variáveis, decisões, repetições e funções | Cálculos e análise de dados              |
| Git e GitHub | Commits e repositórios                    | Histórico e compartilhamento de projetos |
| Markdown     | Títulos, listas, links e tabelas          | Documentação técnica                     |
| VSCode       | Edição de arquivos e terminal             | Organização do trabalho de programação   |

## 🤖 04 | ENGENHARIA E TECNOLOGIA DIGITAL

Quero explorar como programação, dados e automação podem apoiar a Engenharia Mecânica.
Estou no início dessa trajetória e vou registrar aqui minha evolução.

`ENGENHARIA MECÂNICA` • `PYTHON` • `DADOS` • `AUTOMAÇÃO`

## 🛠️ 05 | ESTUDOS E PROJETOS

| Projeto ou atividade  | Descrição                                         | Situação           |
| --------------------- | ------------------------------------------------- | ------------------ |
| Exercícios de Python  | Algoritmos aplicados à engenharia                 | Em desenvolvimento |
| Conversor de unidades | Conversões de grandezas de engenharia             | Planejado          |
| Análise de medições   | Organização e visualização de dados experimentais | Planejado          |

Os projetos marcados como planejados representam objetivos de estudo.
Acrescentarei links conforme os repositórios forem publicados.

## 🎯 06 | PRÓXIMOS PASSOS

- Praticar funções e estruturas de dados em Python.
- Organizar e documentar meus exercícios.
- Publicar um projeto aplicado à Engenharia Mecânica.
- Atualizar este perfil conforme meu aprendizado evoluir.

## 🔗 07 | CONEXÕES

[Meu perfil no GitHub](https://github.com/SEU_USUARIO)

[Meus repositórios](https://github.com/SEU_USUARIO?tab=repositories)

---

**ENGENHARIA • EDUCAÇÃO • PROGRAMAÇÃO • TECNOLOGIA**

Perfil desenvolvido na disciplina de Programação para Engenharia Mecânica,
com inspiração na organização do perfil do professor
[Wilson Luciano](https://github.com/wilson-luciano).
```

Adapte a instituição se necessário. Remova projetos que não pretende desenvolver ou descreva-os com o estado correto. Acrescente LinkedIn ou outros contatos profissionais somente se desejar divulgá-los.

Antes de gravar, confira cada substituição:

| Campo                    | O que colocar                                              |
| ------------------------ | ---------------------------------------------------------- |
| `SEU NOME`               | Seu nome de apresentação, inclusive na descrição da imagem |
| `SEU_USUARIO`            | Seu usuário real do GitHub, sem espaços                    |
| Instituição e formação   | Seu curso e sua instituição                                |
| Interesses e tecnologias | Assuntos que representam sua trajetória                    |
| Projetos e situação      | Atividades reais ou explicitamente planejadas              |

**O bloco acima é um README completo:** copie do `<picture>` até o último link do professor, sem copiar as linhas com três crases. Os dois SVGs são arquivos separados, criados na seção 6; eles não devem ser colados dentro do README.

Grave com a mensagem `docs: personalizar README do perfil`. Abra **Your profile** e confira antes de iniciar a etapa local.

## 8. Entendendo o trecho que troca as imagens

| Trecho                        | Função                                          |
| ----------------------------- | ----------------------------------------------- |
| `<picture>`                   | Agrupa alternativas de uma imagem               |
| `<source>`                    | Indica uma alternativa e a condição para usá-la |
| `prefers-color-scheme: dark`  | Seleciona a versão para o tema escuro           |
| `prefers-color-scheme: light` | Seleciona a versão para o tema claro            |
| `srcset`                      | Informa o caminho da imagem alternativa         |
| `<img>`                       | Define a imagem padrão e sua descrição          |
| `alt`                         | Descreve a imagem em texto para acessibilidade  |
| `width="100%"`                | Ajusta a largura da imagem ao espaço disponível |

Os caminhos são relativos ao README. Como ele está na raiz, `assets/banner-claro.svg` aponta para o arquivo dentro de `assets`.

O bloco usa HTML compatível com o GitHub dentro de um documento Markdown. Não é necessário aprender uma página HTML completa para utilizar esse recurso.

## 9. Atualizando o perfil com Git Bash e VSCode

Até aqui, os arquivos foram gravados diretamente no GitHub. Agora vamos copiar o repositório para o computador e praticar uma atualização local.

**Git** controla versões no computador. **GitHub** hospeda o repositório remoto. Salvar no VSCode, criar um commit e enviar ao GitHub são ações diferentes.

### 9.1 Preparar o Git Bash

Abra o **Git Bash**. Execute um comando por vez, pressionando Enter ao final. Copie somente os comandos, sem os indicadores de terminal `$`, `>` ou `PS`.

```bash
git --version
```

Se o comando não for reconhecido, instale o Git pelo [site oficial](https://git-scm.com/downloads/win), reabra o Git Bash e teste novamente.

Confira a identidade usada nos commits:

```bash
git config --global user.name
git config --global user.email
```

Se necessário, configure com seus dados reais:

```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu-email-vinculado-ao-github"
```

O nome identifica o autor; não precisa ser igual ao usuário do GitHub. Use um e-mail associado à sua conta ou o endereço de privacidade fornecido pelo GitHub em **Settings → Emails**. Essa configuração não realiza login. `--global` vale para os repositórios da sua conta do Windows; em computador compartilhado, use sua sessão pessoal.

### 9.2 Clonar o repositório que já existe no GitHub

No Git Bash, o caminho `C:\Projetos` é escrito como `/c/Projetos`.

```bash
mkdir -p /c/Projetos
cd /c/Projetos
```

`mkdir -p` cria a pasta se necessário. `cd` entra nela.

No site do GitHub, abra seu repositório especial, clique em **Code → HTTPS** e copie o endereço. No comando abaixo, substitua **as duas ocorrências** de `SEU_USUARIO`:

```bash
git clone https://github.com/SEU_USUARIO/SEU_USUARIO.git
cd SEU_USUARIO
```

O primeiro comando baixa arquivos e histórico. O segundo entra na pasta criada pelo clone.

> Como o repositório foi criado com README no GitHub, usamos `clone`. Não execute `git init` nem `git remote add origin`: o clone já configura o repositório local e o remoto `origin`.

Se a pasta já existir, não repita o clone sobre ela. Entre na cópia existente e confira os comandos abaixo. Se for outra pasta, escolha um diretório diferente para clonar.

```bash
git rev-parse --show-toplevel
git remote -v
git branch --show-current
git status
```

Confira se a raiz é a pasta do seu perfil e se `origin` aponta para `SEU_USUARIO/SEU_USUARIO`. A branch padrão costuma ser `main`; se o comando mostrar outro nome, use esse nome nos comandos de envio desta aula.

**Não faça essa atividade dentro de `C:\Projetos\engconvert`: são dois repositórios distintos.**

### 9.3 Abrir e editar no VSCode

```bash
code .
```

O ponto significa **a pasta atual**. Se `code` não for reconhecido, abra o VSCode e use **File → Open Folder** para selecionar a pasta clonada.

1. Abra o `README.md` na raiz.
2. Faça uma alteração real, por exemplo, personalize um objetivo em **Próximos passos**.
3. Se quiser substituir todo o conteúdo, use o modelo da seção 7 e personalize-o.
4. Confira os dois arquivos SVG em `assets`.
5. Salve cada arquivo alterado com **Ctrl+S**.
6. Para visualizar o Markdown no VSCode, use **Ctrl+Shift+V**. O teste definitivo da troca de tema será feito no GitHub.

Volte ao Git Bash, mantendo a pasta do repositório aberta. Se preferir usar o terminal integrado, selecione o perfil **Git Bash** e confira a pasta com `pwd`.

### 9.4 Verificar o que mudou — git status

```bash
git status
```

Depois de editar apenas o README, uma saída possível é:

```text
On branch main
Changes not staged for commit:
  modified:   README.md
```

- `modified` indica um arquivo alterado.
- `Changes not staged for commit` significa que as mudanças ainda não foram selecionadas para o próximo commit.
- `Untracked files`, quando aparece, indica arquivos novos ainda não acompanhados pelo Git.

Se aparecer `nothing to commit, working tree clean` antes de selecionar os arquivos, confira se você salvou a edição e está no repositório correto. Essa mensagem sozinha não comprova que os commits foram enviados.

### 9.5 Ler as alterações antes de selecionar

```bash
git diff -- README.md
```

Linhas com `-` representam conteúdo removido; linhas com `+` representam conteúdo acrescentado. Se aparecer `(END)`, pressione **q** para voltar ao terminal. `git diff` não mostra o conteúdo de arquivos novos ainda não rastreados; abra esses arquivos no editor para conferir.

### 9.6 Selecionar os arquivos — git add

Se alterou apenas o README:

```bash
git add README.md
```

Se também criou ou alterou os banners, execute adicionalmente:

```bash
git add assets/banner-claro.svg assets/banner-escuro.svg
```

`git add` coloca a versão atual dos arquivos na **área de preparação** (_staging area_): a seleção que entrará no próximo commit. Não envia arquivos ao GitHub.

Confira a seleção:

```bash
git status
```

Agora o README deve aparecer em `Changes to be committed`. Um banner novo pode aparecer como `new file`.

> Se editar novamente um arquivo depois do `git add`, salve e execute `git add` para ele outra vez. O commit usa o conteúdo que foi preparado.

Nesta aula, selecionamos os arquivos pelo nome para deixar claro o que será incluído. `git add .` seleciona mudanças abaixo da pasta atual e exige conferir se todos os arquivos fazem parte da entrega.

### 9.7 Criar o registro local — git commit

```bash
git commit -m "docs: atualizar apresentacao do perfil"
```

- `commit` registra os arquivos preparados no histórico local.
- `-m` permite escrever a mensagem diretamente no comando.
- As aspas agrupam a mensagem completa.

Uma saída possível inclui `[main a1b2c3d] docs: atualizar apresentacao do perfil`. O código varia: ele identifica o commit.

Confira novamente:

```bash
git status
```

É possível aparecer:

```text
Your branch is ahead of 'origin/main' by 1 commit.
nothing to commit, working tree clean
```

Isso significa que existe um commit local ainda não enviado, segundo a referência remota conhecida pelo Git. **Commit não é push.**

### 9.8 Enviar os commits — git push

```bash
git push origin main
```

`origin` é o nome do remoto criado pelo clone; `main` é a branch que será enviada. Se a sua branch tiver outro nome, substitua `main` por ele.

No primeiro envio, o Git pode solicitar autenticação. Siga o fluxo de entrada da sua conta apresentado pelo gerenciador de credenciais, possivelmente em uma janela do navegador. A senha comum da conta GitHub não é aceita como senha para operações Git por HTTPS. Se o terminal exigir credenciais sem abrir esse fluxo, consulte a orientação de autenticação indicada nas fontes ou solicite ajuda ao professor.

Uma saída como `main -> main` indica atualização da branch remota. `Everything up-to-date` indica que não há novos commits para enviar; confira se você realmente salvou, adicionou e criou o commit esperado.

Se o Git informar que falta uma branch de acompanhamento (_upstream_), use:

```bash
git push -u origin main
```

`-u` registra a associação entre a branch local e a remota. Em um clone normal essa associação já existe; nas próximas atualizações, `git push` sozinho costuma ser suficiente.

### 9.9 Conferir no terminal e no site

```bash
git status
```

Após um envio bem-sucedido, espera-se uma indicação de sincronização com `origin/main` e a árvore de trabalho limpa. O `status` usa as informações remotas disponíveis localmente; não consulta o site a cada execução.

1. Abra o repositório no navegador e atualize a página.
2. Confira o texto e a mensagem do último commit.
3. Abra seu perfil: `https://github.com/SEU_USUARIO`.
4. Teste os temas claro e escuro em **Settings → Appearance**.
5. Confira imagens, nome, links e tabelas.

### 9.10 Sequência de consulta para as próximas atualizações

Use depois de editar e salvar o README, dentro da pasta correta:

```bash
git status
git diff -- README.md
git add README.md
git status
git commit -m "docs: atualizar perfil"
git push origin main
git status
```

Se os banners também mudarem, inclua-os no `git add` antes do commit.

| Etapa            | Onde ocorre         | Resultado                                  |
| ---------------- | ------------------- | ------------------------------------------ |
| Salvar no editor | Computador          | Atualiza o arquivo em disco                |
| `git status`     | Computador          | Mostra a situação dos arquivos e da branch |
| `git add`        | Computador          | Seleciona o conteúdo para o commit         |
| `git commit`     | Computador          | Registra a alteração no histórico local    |
| `git push`       | Computador → GitHub | Envia commits para o remoto                |

### 9.11 Se você também editar pelo navegador

Antes de começar outra sessão local, estando sem alterações pendentes:

```bash
git status
git pull --ff-only
```

O segundo comando busca as atualizações e avança a branch local quando não há divergência. Depois, edite e siga a sequência normal.

Se o push for rejeitado com `non-fast-forward`, e você já tiver commits locais prontos e a árvore limpa, tente:

```bash
git pull --rebase origin main
```

Se terminar sem conflito, execute o push novamente. Se houver conflito, interrompa a sequência de publicação e peça orientação ao professor para revisar os trechos em conflito. Para cancelar esse rebase e voltar ao estado anterior à tentativa, use `git rebase --abort`. Não use `git push --force` para contornar a rejeição desta atividade.

## 10. Conferindo o resultado

- [ ] O repositório tem o mesmo nome do meu usuário.
- [ ] O repositório é público.
- [ ] O arquivo se chama `README.md` e está na raiz.
- [ ] Meu nome e minha apresentação estão corretos.
- [ ] Removi todos os textos de substituição, como `SEU_USUARIO`.
- [ ] Os links abrem os destinos corretos.
- [ ] As imagens estão na pasta `assets`.
- [ ] O banner claro aparece ao selecionar o tema claro no GitHub.
- [ ] O banner escuro aparece ao selecionar o tema escuro no GitHub.
- [ ] Realizei uma atualização local com `git add`, `git commit` e `git push`.
- [ ] Confirmei no site que o commit e o texto foram publicados.
- [ ] Meu texto diferencia estudos em andamento de conhecimentos já adquiridos.

## 11. Problemas comuns

| Problema                                                      | O que verificar                                                                      |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| O README aparece no repositório, mas não no perfil            | Nome do repositório, visibilidade pública e README preenchido na raiz                |
| O GitHub informa que o nome já existe                         | Abra o repositório existente e edite seu README                                      |
| Aparece um ícone de imagem quebrada                           | Nome, extensão, maiúsculas/minúsculas e caminho do arquivo                           |
| O banner não muda                                             | Verifique o bloco `<picture>`, as duas imagens e o tema selecionado em Appearance    |
| As duas versões parecem iguais                                | Confira se os arquivos realmente têm cores diferentes                                |
| O banner claro aparece, mas o fundo da página continua escuro | A imagem e o tema da página são configurações distintas; teste a aparência do GitHub |
| O texto aparece como código                                   | Remova as crases externas copiadas junto com o modelo                                |
| O nome ficou cortado no banner                                | Reduza `font-size` ou use um nome mais curto nos dois SVGs                           |
| Editei, mas o perfil não mudou                                | Confirme o commit na branch padrão e atualize a página                               |
| `fatal: not a git repository`                                 | Entre na pasta clonada e confirme a raiz com `git rev-parse --show-toplevel`         |
| `Author identity unknown`                                     | Configure `user.name` e `user.email` antes de repetir o commit                       |
| `src refspec main does not match any`                         | Confira o nome da branch com `git branch --show-current` e se existe um commit       |
| Push negado por permissão                                     | Confira `git remote -v` e se a autenticação corresponde à conta dona do repositório  |
| `non-fast-forward`                                            | Veja a seção 9.11; não force o envio                                                 |

## 12. Atividade de entrega

Entregue o link do seu perfil, por exemplo: `https://github.com/ana-mecanica`.

Seu perfil deverá conter apresentação própria, pelo menos três interesses, tecnologias em aprendizado, uma tabela com atividades reais ou planejadas e um banner com duas versões.

Na apresentação em sala, mostre os dois temas e explique:

1. Por que o repositório recebeu o mesmo nome do usuário?
2. Qual é a função do `README.md`?
3. O que fica registrado em um commit?
4. Quem escolhe o tema da página?
5. Como o `<picture>` seleciona o banner?
6. Qual é a diferença entre salvar, executar `git add`, criar um commit e fazer push?

**Desafio opcional:** acrescente o link de um repositório de exercícios que você já tenha criado. Teste o link depois de salvar.

## 13. Revisão do percurso

Você começou com uma apresentação simples, aprendeu as marcações necessárias e montou um perfil completo. Depois, trouxe o mesmo repositório para o computador e publicou uma alteração usando Git.

**Verificação prática final:** acrescente um objetivo pessoal ao README pelo VSCode e publique seguindo a seção 9.10. A atividade só termina quando o novo objetivo aparecer no seu perfil no navegador.

## Fontes e consulta

- [Referência do professor — Wilson Luciano](https://github.com/wilson-luciano)
- [GitHub Docs — Gerenciamento do README de perfil](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)
- [GitHub Docs — Configuração de temas](https://docs.github.com/en/get-started/accessibility/managing-your-theme-settings)
- [GitHub — Imagens conforme o tema com picture](https://github.blog/changelog/2022-08-15-specify-theme-context-for-images-in-markdown-ga/)

- [GitHub — Git add](https://github.com/git-guides/git-add)
- [GitHub — Git push](https://github.com/git-guides/git-push)
- [Git — git status](https://git-scm.com/docs/git-status)
- [GitHub — Autenticação](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)
- [VSCode — Trabalhar com GitHub](https://code.visualstudio.com/docs/sourcecontrol/github)

<hr>

<sub>
© 2026 <b>Wilson Luciano</b> ·
Programação para Engenharia Mecânica · EngConvert ·
Material didático ·
Versão 1.0
</sub>
