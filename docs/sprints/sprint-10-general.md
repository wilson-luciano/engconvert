# Sprint 10 — General e persistência JSON

**Projeto:** EngConvert — Conversor de Unidades de Engenharia  
**Etapa:** 10 — Interface Completa  
**Sprint:** 10 — General e persistência JSON  
**Branch:** `feature-interface-final`  
**Status:** Em andamento

## 1. Objetivo

Implementar preferências gerais do EngConvert e sua persistência em JSON, mantendo as funcionalidades da Sprint 09 e os cálculos de conversão existentes.

## 2. Funcionalidades previstas

- Seleção de tema: Sistema, Claro e Escuro.
- Precisão de exibição de 1 a 12 algarismos significativos.
- Opção de notação científica.
- Aviso para temperatura abaixo do zero absoluto, quando habilitado.
- Persistência de tema, favoritos, ordem, visibilidade e dimensões da interface.
- Gravação das preferências em pasta do usuário, fora do código-fonte.
- Recuperação de valores padrão para configurações ausentes ou inválidas.

## 3. Checklist de desenvolvimento

### Preparação

- [ ] Confirmar a branch `feature-interface-final`.
- [ ] Executar os testes existentes antes das modificações.
- [ ] Verificar a interface da Sprint 09.

### Módulo de configurações

- [ ] Criar `src/engconvert/configuracoes.py`.
- [ ] Implementar valores padrão e validação das preferências.
- [ ] Implementar leitura e gravação de JSON.
- [ ] Criar `tests/test_configuracoes.py`.
- [ ] Executar e registrar o resultado dos testes de configurações.
- [ ] Registrar em commit o módulo, os testes e este documento.

### Integração da interface — Parte III da Aula 10.2

- [ ] Integrar a janela General à `interface.py`.
- [ ] Verificar alteração e restauração do tema.
- [ ] Verificar precisão e notação científica.
- [ ] Verificar o aviso de zero absoluto.
- [ ] Verificar persistência de favoritos, ordem e visibilidade.
- [ ] Verificar persistência de dimensões e altura ajustável.
- [ ] Fechar e reabrir o aplicativo para confirmar a persistência.
- [ ] Verificar que as funcionalidades da Sprint 09 foram preservadas.

## 4. Critérios de aceitação

A Sprint 10 estará funcionalmente concluída quando as preferências forem validadas, gravadas e restauradas após reiniciar o EngConvert; a janela General funcionar; os testes automatizados pertinentes passarem; e a interface da Sprint 09 continuar operante.

## 5. Resultados e evidências

**Testes automatizados:** Pendente de execução/registro.  
**Testes manuais:** Pendentes da integração na Parte III.  
**Commit do módulo de persistência:** Pendente.  
**Pendências ou observações:** Preencher após as verificações.

## 6. Situação da Sprint

**Status:** Em andamento. A implementação da janela General e a validação integrada ocorrerão na Parte III da Aula 10.2.
