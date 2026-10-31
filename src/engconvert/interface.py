
"""Interface integrada do EngConvert — Sprints 09 a 12."""
import tkinter as tk
import math
from tkinter import messagebox
import customtkinter as ctk
from .dados import lista_grandezas
from . import configuracoes as cfg
from . import personalizadas as pers

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
        janela = ctk.CTkToplevel(app)
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
        janela = ctk.CTkToplevel(app)
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
        janela = ctk.CTkToplevel(app)
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
        janela = ctk.CTkToplevel(app)
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