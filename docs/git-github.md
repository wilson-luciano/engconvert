# Git e GitHub — guia rápido do EngConvert

## Git não é GitHub

- **Git:** sistema de controle de versão executado localmente.
- **GitHub:** plataforma que hospeda repositórios Git e facilita colaboração.

## Primeiro ciclo

```powershell
git init
git status
git add .
git commit -m "feat: cria versão inicial do EngConvert"
```

Depois de criar o repositório remoto no GitHub, conecte-o seguindo os comandos exibidos pelo próprio GitHub e faça o primeiro `push`.

## Ciclo cotidiano

```text
Editar → git status → git add → git commit → git push
```

## Convenção simples de commits

```text
feat: nova funcionalidade
fix: correção
docs: documentação
refactor: reorganização sem alterar a funcionalidade
 test: testes
```

Exemplos:

```powershell
git commit -m "feat: adiciona conversão de pressão"
git commit -m "docs: adiciona aula sobre CustomTkinter"
git commit -m "fix: trata entrada não numérica"
```
