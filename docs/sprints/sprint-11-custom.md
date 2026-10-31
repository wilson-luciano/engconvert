# Sprint 11 — Unidades personalizadas (Custom)

**Projeto:** EngConvert — Conversor de Unidades de Engenharia

**Etapa:** 10 — Interface Completa

**Branch:** `feature-interface-final`

**Status:** Em andamento

## 1. Objetivo

Implementar cadastro, validação, exclusão, conversão e persistência em JSON de unidades multiplicativas personalizadas, preservando as unidades originais.

## 2. Escopo

- Grandezas permitidas: Pressão, Comprimento, Área e Volume.
- Fatores positivos, finitos e relativos a Pa, m, m² e m³.
- Proibição de nomes vazios, nomes duplicados e escalas de Temperatura.
- Arquivo de dados na pasta do usuário, fora do repositório.

## 3. Checklist

### Módulo e testes — Parte II

- [ ] Criar `src/engconvert/personalizadas.py`.
- [ ] Validar nomes e fatores de conversão.
- [ ] Impedir duplicatas e cadastro de Temperatura.
- [ ] Implementar adição, exclusão e persistência JSON.
- [ ] Criar `tests/test_personalizadas.py`.
- [ ] Executar os dez testes previstos e registrar o resultado real.
- [ ] Registrar o commit parcial do módulo, testes e documentação.

### Interface — Parte III

- [ ] Integrar a janela Custom à `interface.py`.
- [ ] Cadastrar uma unidade e utilizá-la em uma conversão.
- [ ] Confirmar persistência após fechar e reabrir o EngConvert.
- [ ] Excluir uma unidade personalizada sem afetar o catálogo original.
- [ ] Verificar mensagens para fatores inválidos e nomes duplicados.

## 4. Critérios de aceitação

A Sprint 11 será concluída quando o módulo e os testes funcionarem, a janela Custom permitir cadastro e exclusão, as unidades participarem corretamente das conversões e os dados persistirem após reiniciar o aplicativo.

## 5. Resultados e evidências

**Testes automatizados:** Pendente de registro.

**Testes manuais da interface:** Pendentes da Parte III.

**Commit parcial:** Pendente.

**Observações:** Preencher com os resultados efetivamente observados.

## 6. Situação

**Status:** Em andamento até a integração e validação manual da janela Custom.
