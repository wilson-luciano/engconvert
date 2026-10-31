"""Interface gráfica do EngConvert — Sprint 09: navegação e categorias.

Mantém o cabeçalho compacto da janela Categorias (v6), a área de categorias
redimensionável (v8) e a matemática no módulo conversoes.py. Preferências persistentes e
cadastro de unidades serão implementados em Sprints posteriores.
"""
import tkinter as tk
import customtkinter as ctk
from .dados import lista_grandezas
from .conversoes import converter, obter_unidades


def iniciar_aplicacao():
    """Monta a janela e associa eventos aos controles."""
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()
    app.title("EngConvert — Sprint 09")
    # Geometria compacta: usa as dimensões do próprio Tk, evitando misturar
    # coordenadas físicas do Windows (ctypes) com pixels lógicos do Tk.
    # Reserva uma margem generosa para a barra de tarefas e escala de tela.
    largura_tela = app.winfo_screenwidth()
    altura_tela = app.winfo_screenheight()
    largura_inicial = min(790, max(420, largura_tela - 60))
    altura_inicial = min(620, max(420, altura_tela - 160))
    pos_x = max(0, (largura_tela - largura_inicial) // 2)
    pos_y = 20
    app.geometry(f"{largura_inicial}x{altura_inicial}+{pos_x}+{pos_y}")
    app.minsize(min(580, largura_inicial), min(520, altura_inicial))

    # Estado da navegação: somente preferências da sessão atual.
    ordem = list(lista_grandezas)
    visiveis = list(lista_grandezas)
    favoritas = ["Pressão", "Temperatura"]
    colunas_grade = 3

    def categorias_disponiveis():
        return [nome for nome in ordem if nome in visiveis]

    def atualizar_unidades(_=None):
        unidades = obter_unidades(combo_grandeza.get())
        combo_de.configure(values=unidades)
        combo_para.configure(values=unidades)
        combo_de.set(unidades[0])
        combo_para.set(unidades[1] if len(unidades) > 1 else unidades[0])
        resultado.configure(text="—", text_color=("#1769aa", "#8ac7ff"))

    def selecionar_grandeza(nome):
        if nome not in categorias_disponiveis():
            return
        combo_grandeza.set(nome)
        atualizar_unidades()

    def atualizar_navegacao():
        disponiveis = categorias_disponiveis()
        if not disponiveis:
            # Uma categoria deve permanecer visível para evitar estado vazio.
            visiveis.append(ordem[0])
            disponiveis = categorias_disponiveis()
        combo_grandeza.configure(values=disponiveis)
        if combo_grandeza.get() not in disponiveis:
            combo_grandeza.set(disponiveis[0])
            atualizar_unidades()
        for quadro in (quadro_favoritas, quadro_todas):
            for widget in quadro.winfo_children():
                widget.destroy()

        def montar_grade(quadro, nomes):
            for coluna in range(colunas_grade):
                quadro.grid_columnconfigure(coluna, weight=1, uniform="categorias")
            for indice, nome in enumerate(nomes):
                linha, coluna = divmod(indice, colunas_grade)
                ctk.CTkButton(
                    quadro, text=nome, height=34,
                    command=lambda n=nome: selecionar_grandeza(n)
                ).grid(row=linha, column=coluna, padx=5, pady=5, sticky="ew")

        fav = [nome for nome in disponiveis if nome in favoritas]
        if not fav:
            ctk.CTkLabel(quadro_favoritas, text="Nenhuma favorita visível.").grid(
                row=0, column=0, padx=10, pady=15
            )
        else:
            montar_grade(quadro_favoritas, fav)
        montar_grade(quadro_todas, disponiveis)

    def abrir_categorias():
        janela = ctk.CTkToplevel(app)
        janela.title("Preferências — Categorias")
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
            titulos, text="↑↓  Categoria", anchor="w",
            font=ctk.CTkFont(size=13, weight="bold")
        ).grid(row=0, column=0, sticky="w", padx=(4, 0))
        ctk.CTkLabel(
            titulos, text="★ Favorito", width=90,
            font=ctk.CTkFont(size=12, weight="bold")
        ).grid(row=0, column=1, padx=0)
        ctk.CTkLabel(
            titulos, text="👁 Mostrar", width=82,
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

                ctk.CTkRadioButton(
                    linha, text=nome, variable=selecionada, value=nome,
                    command=destacar, width=150
                ).grid(row=0, column=0, sticky="w", padx=(4, 2), pady=4)
                if selecionada.get() == nome:
                    linha.configure(fg_color=("#d6e9fa", "#264b69"))

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

                ctk.CTkCheckBox(
                    linha, text="", variable=favorito_var, width=28,
                    state="normal" if nome in visiveis_temp else "disabled",
                    command=alterar_favorito
                ).grid(row=0, column=1, padx=(4, 34), sticky="e")
                ctk.CTkCheckBox(
                    linha, text="", variable=mostrar_var, width=28,
                    command=alterar_mostrar
                ).grid(row=0, column=2, padx=(0, 20), sticky="e")

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
                aviso.configure(text="Mantenha pelo menos uma categoria visível.")
                return
            ordem[:] = ordem_temp
            visiveis[:] = visiveis_temp
            favoritas[:] = [n for n in favoritas_temp if n in visiveis_temp]
            atualizar_navegacao()
            janela.destroy()

        desenhar()
        comandos = ctk.CTkFrame(janela)
        comandos.pack(padx=15, pady=4)
        ctk.CTkButton(comandos, text="Subir", width=75, command=lambda: mover(-1)).pack(side="left", padx=3)
        ctk.CTkButton(comandos, text="Descer", width=75, command=lambda: mover(1)).pack(side="left", padx=3)
        ctk.CTkButton(comandos, text="Restaurar", width=90, command=restaurar).pack(side="left", padx=3)
        aviso = ctk.CTkLabel(janela, text="")
        aviso.pack()
        rodape = ctk.CTkFrame(janela, fg_color="transparent")
        rodape.pack(pady=8)
        ctk.CTkButton(rodape, text="Salvar", command=salvar).pack(side="left", padx=5)
        ctk.CTkButton(rodape, text="Cancelar", command=janela.destroy).pack(side="left", padx=5)
        janela.grab_set()

    def inverter_unidades():
        de, para = combo_de.get(), combo_para.get()
        combo_de.set(para)
        combo_para.set(de)
        # O resultado anterior pertence à direção de conversão antiga.
        resultado.configure(text="—", text_color=("#1769aa", "#8ac7ff"))

    def ao_converter():
        try:
            valor = float(entrada.get().strip().replace(",", "."))
            convertido = converter(valor, combo_grandeza.get(), combo_de.get(), combo_para.get())
            resultado.configure(text=f"{convertido:.6g} {combo_para.get()}", text_color=("#1769aa", "#8ac7ff"))
        except (ValueError, KeyError, ZeroDivisionError):
            resultado.configure(text="Verifique o valor e as unidades selecionadas.",
                                text_color=("#b42318", "#ff9c94"))

    cabecalho = ctk.CTkFrame(app)
    cabecalho.pack(fill="x", padx=22, pady=(10, 7))
    ctk.CTkLabel(cabecalho, text="EngConvert", font=("Arial", 26, "bold")).pack(
        side="left", padx=15, pady=10
    )
    ctk.CTkButton(cabecalho, text="⚙ Categorias", command=abrir_categorias).pack(
        side="right", padx=(5, 12)
    )

    # Menu nativo, compacto, aberto ao clicar no ícone de aparência.
    # A escolha vale somente para a sessão atual (sem persistência em JSON).
    tema_atual = tk.StringVar(value="Sistema")
    temas = {"Sistema": "System", "Claro": "Light", "Escuro": "Dark"}

    def alterar_tema(escolha):
        tema_atual.set(escolha)
        ctk.set_appearance_mode(temas[escolha])

    menu_tema = tk.Menu(app, tearoff=False)
    for nome in ("Sistema", "Claro", "Escuro"):
        menu_tema.add_radiobutton(
            label=nome,
            variable=tema_atual,
            value=nome,
            command=lambda n=nome: alterar_tema(n),
        )

    def abrir_menu_tema():
        # Exibe o menu abaixo do botão, respeitando a posição na tela.
        x = botao_tema.winfo_rootx()
        y = botao_tema.winfo_rooty() + botao_tema.winfo_height()
        try:
            menu_tema.tk_popup(x, y)
        finally:
            menu_tema.grab_release()

    botao_tema = ctk.CTkButton(
        cabecalho, text="◐", width=36, height=32,
        fg_color="transparent", text_color=("#333333", "#eeeeee"),
        hover_color=("#c8c8c8", "#454545"),
        command=abrir_menu_tema,
    )
    botao_tema.pack(side="right", padx=(4, 6))

    # Sprint 09: altura ajustável da navegação, sem salvar em JSON.
    # A persistência será implementada na Aula 10.2.
    ALTURA_INICIAL = 125
    ALTURA_MINIMA = 100
    ALTURA_MAXIMA = 320
    ALTURA_MINIMA_CONVERSOR = 350

    painel_navegacao = ctk.CTkFrame(app, height=ALTURA_INICIAL)
    painel_navegacao.pack(fill="x", padx=22, pady=(2, 0))
    painel_navegacao.pack_propagate(False)

    abas = ctk.CTkTabview(painel_navegacao)
    abas.pack(fill="both", expand=True, padx=12, pady=(7, 5))
    aba_favoritas = abas.add("Favoritas")
    aba_todas = abas.add("Todas as grandezas")
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
        divisor, text="━━  arraste para ajustar a altura  ━━",
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
        controle.bind("<ButtonPress-1>", iniciar_arraste)
        controle.bind("<B1-Motion>", mover_divisor)
    app.bind("<Configure>", ao_redimensionar, add="+")

    ctk.CTkLabel(corpo, text="Grandeza", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(7, 3))
    combo_grandeza = ctk.CTkComboBox(
        corpo, values=ordem, width=270, height=40,
        font=ctk.CTkFont(size=20), dropdown_font=ctk.CTkFont(size=17),
        command=atualizar_unidades, state="readonly"
    )
    combo_grandeza.pack()
    combo_grandeza.set("Pressão")
    linha = ctk.CTkFrame(corpo, fg_color="transparent")
    linha.pack(pady=6)
    combo_de = ctk.CTkComboBox(
        linha, width=155, height=40, state="readonly",
        font=ctk.CTkFont(size=20), dropdown_font=ctk.CTkFont(size=17)
    )
    combo_de.pack(side="left", padx=8)
    ctk.CTkButton(
        linha, text="↔", width=46, height=40,
        font=ctk.CTkFont(size=21), command=inverter_unidades
    ).pack(side="left", padx=4)
    combo_para = ctk.CTkComboBox(
        linha, width=155, height=40, state="readonly",
        font=ctk.CTkFont(size=20), dropdown_font=ctk.CTkFont(size=17)
    )
    combo_para.pack(side="left", padx=8)
    entrada = ctk.CTkEntry(
        corpo, width=240, height=42, placeholder_text="Digite o valor",
        font=ctk.CTkFont(size=21), justify="center"
    )
    entrada.pack(pady=3)
    ctk.CTkButton(
        corpo, text="Converter", width=175, height=40,
        font=ctk.CTkFont(size=18), command=ao_converter
    ).pack(pady=5)
    painel_resultado = ctk.CTkFrame(
        corpo, fg_color=("#e3f0fa", "#264b69"), corner_radius=10
    )
    painel_resultado.pack(fill="x", padx=24, pady=(2, 4))
    ctk.CTkLabel(
        painel_resultado, text="RESULTADO DA CONVERSÃO",
        font=ctk.CTkFont(size=11, weight="bold"),
        text_color=("#476a86", "#c4d8ec")
    ).pack(pady=(5, 0))
    resultado = ctk.CTkLabel(
        painel_resultado, text="—", font=ctk.CTkFont(size=24, weight="bold"),
        wraplength=520, text_color=("#1769aa", "#8ac7ff")
    )
    resultado.pack(pady=(0, 5))
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
    app.mainloop()