"""Interface gráfica do EngConvert em CustomTkinter."""

import customtkinter as ctk

from .dados import fatores_pressao, lista_grandezas
from .conversoes import converter, obter_unidades


def iniciar_aplicacao():
    """Cria os widgets, registra eventos e inicia a aplicação."""
    # Atualiza as unidades quando a categoria é alterada.
    def atualizar_unidades(grandeza_selecionada):
        unidades = obter_unidades(grandeza_selecionada)
        combo_de.configure(values=unidades)
        combo_para.configure(values=unidades)
        combo_de.set(unidades[0])
        combo_para.set(unidades[1])
        resultado.configure(text="Resultado")

    # Evento do botão Converter: recebe dados, chama o cálculo e mostra a saída.
    def ao_converter():
        try:
            valor = float(entrada.get())
            grandeza = combo_grandeza.get()
            unidade_de = combo_de.get()
            unidade_para = combo_para.get()
            valor_convertido = converter(valor, grandeza, unidade_de, unidade_para)
            resultado.configure(text=f"{valor_convertido:.6g} {unidade_para}")
        except ValueError:
            resultado.configure(text="Digite um valor numérico válido.")

    # Inverte as unidades selecionadas.
    def inverter_unidades():
        unidade_de = combo_de.get()
        unidade_para = combo_para.get()
        combo_de.set(unidade_para)
        combo_para.set(unidade_de)

    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")


    # Cria a janela principal.
    app = ctk.CTk()

    app.title("EngConvert")
    app.geometry("700x650")


    # Cria o frame principal.
    container = ctk.CTkFrame(app)

    container.pack(
        padx=30,
        pady=30,
        fill="both",
        expand=True
    )


    # Título.
    titulo = ctk.CTkLabel(
        container,
        text="EngConvert",
        font=("Arial", 28, "bold")
    )

    titulo.pack(pady=(25, 5))


    # Subtítulo.
    subtitulo = ctk.CTkLabel(
        container,
        text="Conversor de Unidades de Engenharia"
    )

    subtitulo.pack(pady=(0, 15))


    # ---------------------------------------------------------
    # SELETOR DE GRANDEZA
    # ---------------------------------------------------------

    label_grandeza = ctk.CTkLabel(
        container,
        text="Grandeza"
    )

    label_grandeza.pack(pady=(10, 5))


    combo_grandeza = ctk.CTkComboBox(
        container,
        values=lista_grandezas,
        width=300,
        command=atualizar_unidades
    )

    combo_grandeza.pack(pady=(0, 15))

    combo_grandeza.set("Pressão")


    # ---------------------------------------------------------
    # SELETORES DE UNIDADE
    # ---------------------------------------------------------

    frame_unidades = ctk.CTkFrame(
        container,
        fg_color="transparent"
    )

    frame_unidades.pack(pady=10)


    # Unidade de origem.
    frame_de = ctk.CTkFrame(
        frame_unidades,
        fg_color="transparent"
    )

    frame_de.pack(
        side="left",
        padx=10
    )


    label_de = ctk.CTkLabel(
        frame_de,
        text="De"
    )

    label_de.pack(pady=(0, 5))


    combo_de = ctk.CTkComboBox(
        frame_de,
        values=list(fatores_pressao.keys()),
        width=180
    )

    combo_de.pack()
    combo_de.set("bar")


    # Botão de inversão.
    botao_inverter = ctk.CTkButton(
        frame_unidades,
        text="↔",
        width=50,
        command=inverter_unidades
    )

    botao_inverter.pack(
        side="left",
        padx=5,
        pady=(25, 0)
    )


    # Unidade de destino.
    frame_para = ctk.CTkFrame(
        frame_unidades,
        fg_color="transparent"
    )

    frame_para.pack(
        side="left",
        padx=10
    )


    label_para = ctk.CTkLabel(
        frame_para,
        text="Para"
    )

    label_para.pack(pady=(0, 5))


    combo_para = ctk.CTkComboBox(
        frame_para,
        values=list(fatores_pressao.keys()),
        width=180
    )

    combo_para.pack()
    combo_para.set("kPa")


    # ---------------------------------------------------------
    # ENTRADA
    # ---------------------------------------------------------

    label_entrada = ctk.CTkLabel(
        container,
        text="Entrada"
    )

    label_entrada.pack(pady=(15, 5))


    entrada = ctk.CTkEntry(
        container,
        width=300,
        placeholder_text="Digite o valor"
    )

    entrada.pack(pady=(0, 10))


    # ---------------------------------------------------------
    # BOTÃO CONVERTER
    # ---------------------------------------------------------

    botao_converter = ctk.CTkButton(
        container,
        text="Converter",
        command=ao_converter
    )

    botao_converter.pack(pady=15)


    # ---------------------------------------------------------
    # SAÍDA
    # ---------------------------------------------------------

    label_saida = ctk.CTkLabel(
        container,
        text="Saída"
    )

    label_saida.pack(pady=(10, 5))


    resultado = ctk.CTkLabel(
        container,
        text="Resultado",
        font=("Arial", 20, "bold")
    )

    resultado.pack(pady=(0, 20))

    # Mantém a janela aberta e processa os eventos do usuário.
    app.mainloop()
