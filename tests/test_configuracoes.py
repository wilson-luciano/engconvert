import json
from engconvert import configuracoes as cfg


def test_padrao_sem_arquivo(tmp_path):
    assert cfg.carregar(tmp_path / 'ausente.json') == cfg.padrao()


def test_salvar_e_reabrir(tmp_path):
    arquivo = tmp_path / 'preferencias.json'
    preferencias = cfg.padrao()
    preferencias.update(tema='Dark', precisao=8, cientifica=True)
    cfg.salvar(preferencias, arquivo)
    assert cfg.carregar(arquivo)['tema'] == 'Dark'
    assert cfg.carregar(arquivo)['precisao'] == 8


def test_json_corrompido(tmp_path):
    arquivo = tmp_path / 'preferencias.json'
    arquivo.write_text('{invalido', encoding='utf-8')
    assert cfg.carregar(arquivo) == cfg.padrao()


def test_valores_invalidos_sao_normalizados():
    resultado = cfg.validar({'precisao': 0, 'tema': 'Azul', 'visiveis': []})
    assert resultado['precisao'] == 6
    assert resultado['tema'] == 'System'
    assert len(resultado['visiveis']) == 5

def test_favoritos_e_geometria_persistem(tmp_path):
    arquivo = tmp_path / "configuracoes.json"
    dados = cfg.padrao()
    dados.update(favoritas=["Volume", "Pressão"], altura_categorias=180,
                 largura_janela=750, altura_janela=600)
    cfg.salvar(dados, arquivo)
    restaurado = cfg.carregar(arquivo)
    assert set(restaurado["favoritas"]) == {"Volume", "Pressão"}
    assert restaurado["altura_categorias"] == 180
    assert restaurado["largura_janela"] == 750
    assert restaurado["altura_janela"] == 600


def test_geometria_invalida_retorna_ao_padrao():
    dados = cfg.validar({"altura_categorias": -10, "largura_janela": "muito",
                        "altura_janela": 99999, "favoritas": ["Inexistente"]})
    assert dados["altura_categorias"] == 125
    assert dados["largura_janela"] is None
    assert dados["altura_janela"] is None
    assert dados["favoritas"] == []
