# Sprint 09 — Navegação e Tabs do EngConvert

**Projeto:** EngConvert  
**Etapa:** 10 — Interface Completa  
**Sprint:** 09  
**Branch:** `feature-tabs`  
**Status:** Planejada

## 1. Objetivo

Implementar uma interface de navegação com abas, permitindo selecionar, ocultar e reorganizar as cinco categorias de grandezas do EngConvert, preservando as regras matemáticas existentes.

## 2. Funcionalidades previstas

- Criar as abas **Favoritas** e **Todas as grandezas**.
- Permitir selecionar uma grandeza por meio das abas.
- Criar a janela **Categorias**.
- Permitir mostrar ou ocultar categorias.
- Permitir alterar a ordem de apresentação.
- Implementar os comandos **Subir**, **Descer**, **Restaurar**, **Salvar** e **Cancelar**.
- Preservar as conversões existentes.

## 3. Checklist de desenvolvimento

### Preparação

- [ ] Confirmar que o EngConvert funciona antes das alterações.
- [ ] Executar os testes existentes.
- [ ] Criar a branch `feature-tabs`.

### Implementação

- [ ] Adicionar o componente `CTkTabview`.
- [ ] Criar a aba Favoritas.
- [ ] Criar a aba Todas as grandezas.
- [ ] Implementar a seleção de grandezas.
- [ ] Implementar a janela Categorias.
- [ ] Implementar a visibilidade das categorias.
- [ ] Implementar a ordenação das categorias.
- [ ] Implementar Restaurar, Salvar e Cancelar.
- [ ] Permitir converter pressionando Enter e posicionar o foco no campo de valor.
- [ ] Limpar o resultado anterior ao inverter as unidades.
- [ ] Permitir rolagem na aba Todas as grandezas.

### Validação

- [ ] Verificar a navegação pelas abas.
- [ ] Confirmar que ocultar uma categoria não exclui seus dados.
- [ ] Confirmar que Cancelar descarta alterações.
- [ ] Impedir que todas as categorias sejam ocultadas.
- [ ] Executar os testes com `pytest`.
- [ ] Conferir manualmente a interface.
- [ ] Testar Enter, inversão de unidades e rolagem da aba Todas as grandezas.

### Git e documentação

- [ ] Atualizar a documentação da Sprint.
- [ ] Registrar as alterações em commit.
- [ ] Integrar a branch à `main`, após validação.
- [ ] Enviar as alterações ao GitHub.

## 4. Critérios de aceitação

A Sprint será considerada concluída quando:

1. As abas estiverem funcionando corretamente.
2. As cinco categorias originais permanecerem disponíveis no catálogo.
3. A visibilidade e a ordenação funcionarem conforme planejado.
4. As conversões matemáticas anteriores continuarem corretas.
5. Os testes automatizados forem aprovados.
6. As alterações estiverem registradas no Git.

## 5. Limitações desta Sprint

As preferências de navegação serão mantidas apenas durante a execução do aplicativo.

O armazenamento permanente em JSON, as configurações numéricas e as unidades personalizadas serão desenvolvidos em Sprints posteriores.

## 6. Resultado final

**Status:** Pendente de validação.

**Testes automatizados:** Ainda não executados nesta Sprint.

**Observações:** Preencher após a implementação e os testes.
