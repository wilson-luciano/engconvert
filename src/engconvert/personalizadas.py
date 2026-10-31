"""Unidades multiplicativas personalizadas, isoladas da interface."""
import json
import math
from pathlib import Path
from .configuracoes import pasta_usuario
from .dados import grandezas


def caminho_unidades():
    return pasta_usuario() / 'unidades_personalizadas.json'


def validar_unidade(categoria, nome, fator, existentes=None):
    if categoria not in grandezas:
        raise ValueError('Escolha uma grandeza multiplicativa válida; temperatura não é aceita.')
    if not isinstance(nome, str) or not nome.strip() or len(nome.strip()) > 30:
        raise ValueError('O nome deve ter de 1 a 30 caracteres.')
    nome = nome.strip()
    if nome.casefold() in {u.casefold() for u in grandezas[categoria]}:
        raise ValueError('Essa unidade já existe no catálogo original.')
    if existentes and nome.casefold() in {u.casefold() for u in existentes.get(categoria, {})}:
        raise ValueError('Essa unidade personalizada já existe.')
    if isinstance(fator, bool):
        raise ValueError('O fator deve ser numérico, não booleano.')
    try:
        numero = float(fator)
    except (TypeError, ValueError, OverflowError):
        raise ValueError('Informe um fator numérico válido.') from None
    if not math.isfinite(numero) or numero <= 0:
        raise ValueError('O fator deve ser positivo e finito.')
    return nome, numero


def adicionar(unidades, categoria, nome, fator):
    nome, numero = validar_unidade(categoria, nome, fator, unidades)
    novo = {cat: valores.copy() for cat, valores in unidades.items()}
    novo.setdefault(categoria, {})[nome] = numero
    return novo


def excluir(unidades, categoria, nome):
    novo = {cat: valores.copy() for cat, valores in unidades.items()}
    if nome not in novo.get(categoria, {}):
        raise ValueError('Unidade personalizada não encontrada.')
    del novo[categoria][nome]
    return novo


def carregar(caminho=None):
    destino = Path(caminho) if caminho is not None else caminho_unidades()
    try:
        bruto = json.loads(destino.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, ValueError, TypeError):
        return {}
    if not isinstance(bruto, dict) or bruto.get('versao_esquema') != 1 or not isinstance(bruto.get('unidades'), dict):
        return {}
    resultado = {}
    for categoria, itens in bruto['unidades'].items():
        if not isinstance(itens, dict):
            continue
        for nome, fator in itens.items():
            try:
                resultado = adicionar(resultado, categoria, nome, fator)
            except (ValueError, TypeError):
                continue
    return resultado


def salvar(unidades, caminho=None):
    destino = Path(caminho) if caminho is not None else caminho_unidades()
    # Revalidar antes de persistir dados.
    validas = {}
    for categoria, itens in unidades.items():
        for nome, fator in itens.items():
            validas = adicionar(validas, categoria, nome, fator)
    destino.parent.mkdir(parents=True, exist_ok=True)
    temporario = destino.with_suffix('.tmp')
    temporario.write_text(json.dumps({'versao_esquema': 1, 'unidades': validas}, ensure_ascii=False, indent=2), encoding='utf-8')
    temporario.replace(destino)


def unidades_disponiveis(categoria, personalizadas):
    if categoria == 'Temperatura':
        from .dados import unidades_temperatura
        return list(unidades_temperatura)
    return list(grandezas[categoria]) + list(personalizadas.get(categoria, {}))


def converter(valor, categoria, origem, destino, personalizadas):
    from .conversoes import converter as converter_original
    if categoria == 'Temperatura':
        return converter_original(valor, categoria, origem, destino)
    fatores = dict(grandezas[categoria])
    fatores.update(personalizadas.get(categoria, {}))
    return valor * fatores[origem] / fatores[destino]
