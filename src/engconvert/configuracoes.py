"""Preferências persistentes do EngConvert, sem dependência da GUI."""
import json
import os
from pathlib import Path


def pasta_usuario():
    """Pasta gravável por usuário, inclusive quando houver um .exe."""
    base = os.environ.get('APPDATA')
    return (Path(base) if base else Path.home() / '.config') / 'EngConvert'


def caminho_configuracoes():
    return pasta_usuario() / 'configuracoes.json'


def padrao():
    return {'versao_esquema': 1, 'tema': 'System', 'precisao': 6,
            'cientifica': False, 'avisar_zero_absoluto': True,
            'ordem': ['Pressão', 'Comprimento', 'Área', 'Volume', 'Temperatura'],
            'visiveis': ['Pressão', 'Comprimento', 'Área', 'Volume', 'Temperatura'],
            'favoritas': ['Pressão', 'Temperatura'], 'altura_categorias': 125,
            'largura_janela': None, 'altura_janela': None}


def validar(dados):
    """Normaliza o JSON recebido sem confiar em tipos ou valores externos."""
    resultado = padrao()
    if not isinstance(dados, dict):
        return resultado
    if dados.get('tema') in ('System', 'Light', 'Dark'):
        resultado['tema'] = dados['tema']
    if type(dados.get('precisao')) is int and 1 <= dados['precisao'] <= 12:
        resultado['precisao'] = dados['precisao']
    for chave in ('cientifica', 'avisar_zero_absoluto'):
        if type(dados.get(chave)) is bool:
            resultado[chave] = dados[chave]
    originais = padrao()['ordem']
    ordem = dados.get('ordem')
    if isinstance(ordem, list) and len(ordem) == len(originais) and set(map(str, ordem)) == set(originais) and all(isinstance(x, str) for x in ordem):
        resultado['ordem'] = ordem.copy()
    visiveis = dados.get('visiveis')
    if isinstance(visiveis, list) and visiveis and all(isinstance(x, str) for x in visiveis):
        filtradas = [x for x in resultado['ordem'] if x in visiveis]
        if filtradas:
            resultado['visiveis'] = filtradas
    favoritas = dados.get('favoritas')
    if isinstance(favoritas, list) and all(isinstance(x, str) for x in favoritas):
        resultado['favoritas'] = [x for x in resultado['ordem']
                                if x in favoritas and x in resultado['visiveis']]
    altura = dados.get('altura_categorias')
    if type(altura) is int and 100 <= altura <= 320:
        resultado['altura_categorias'] = altura
    for chave in ('largura_janela', 'altura_janela'):
        valor = dados.get(chave)
        if type(valor) is int and 420 <= valor <= 3000:
            resultado[chave] = valor
    return resultado


def carregar(caminho=None):
    destino = Path(caminho) if caminho is not None else caminho_configuracoes()
    try:
        return validar(json.loads(destino.read_text(encoding='utf-8')))
    except (OSError, UnicodeError, ValueError, TypeError):
        return padrao()


def salvar(dados, caminho=None):
    destino = Path(caminho) if caminho is not None else caminho_configuracoes()
    destino.parent.mkdir(parents=True, exist_ok=True)
    temporario = destino.with_suffix('.tmp')
    temporario.write_text(json.dumps(validar(dados), ensure_ascii=False, indent=2), encoding='utf-8')
    temporario.replace(destino)
