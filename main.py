# Importa a biblioteca CustomTkinter.
import customtkinter as ctk


# ---------------------------------------------------------
# DADOS
# ---------------------------------------------------------

# Fatores de pressão em relação ao pascal.
fatores_pressao = {
    "Pa": 1,
    "kPa": 1_000,
    "MPa": 1_000_000,
    "bar": 100_000,
    "mbar": 100,
    "kgf/cm²": 98_066.5,
    "psi": 6_894.757,
    "atm": 101_325,
    "m.c.a.": 9_806.65
}


# Fatores de comprimento em relação ao metro.
fatores_comprimento = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1_000,
    "in": 0.0254,
    "ft": 0.3048
}


# Fatores de área em relação ao metro quadrado.
fatores_area = {
    "mm²": 0.000001,
    "cm²": 0.0001,
    "m²": 1,
    "in²": 0.00064516,
    "ft²": 0.09290304
}


# Fatores de volume em relação ao metro cúbico.
fatores_volume = {
    "mL": 0.000001,
    "cm³": 0.000001,
    "L": 0.001,
    "m³": 1,
    "in³": 0.000016387064,
    "ft³": 0.028316846592,
    "gal (US)": 0.003785411784,
    "gal (UK)": 0.00454609
}


# Organiza as grandezas com conversão multiplicativa.
grandezas = {
    "Pressão": fatores_pressao,
    "Comprimento": fatores_comprimento,
    "Área": fatores_area,
    "Volume": fatores_volume
}


# Unidades disponíveis para temperatura.
unidades_temperatura = [
    "°C",
    "°F",
    "K",
    "°R"
]


# Lista apresentada no seletor de grandeza.
lista_grandezas = [
    "Pressão",
    "Comprimento",
    "Área",
    "Volume",
    "Temperatura"
]


# ---------------------------------------------------------
# FUNÇÕES
# ---------------------------------------------------------

# Converte temperaturas utilizando kelvin como referência.
def converter_temperatura(valor, unidade_de, unidade_para):

    # Converte a origem para kelvin.
    if unidade_de == "°C":
        valor_k = valor + 273.15

    elif unidade_de == "°F":
        valor_k = (valor - 32) * 5 / 9 + 273.15

    elif unidade_de == "K":
        valor_k = valor

    elif unidade_de == "°R":
        valor_k = valor * 5 / 9

    # Converte de kelvin para o destino.
    if unidade_para == "°C":
        return valor_k - 273.15

    elif unidade_para == "°F":
        return (valor_k - 273.15) * 9 / 5 + 32

    elif unidade_para == "K":
        return valor_k

    elif unidade_para == "°R":
        return valor_k * 9 / 5


# Retorna as unidades da grandeza selecionada.
def obter_unidades(grandeza):

    if grandeza == "Temperatura":
        return unidades_temperatura

    return list(grandezas[grandeza].keys())


# Atualiza os ComboBox quando a grandeza muda.
def atualizar_unidades(grandeza_selecionada):

    unidades = obter_unidades(grandeza_selecionada)

    combo_de.configure(values=unidades)
    combo_para.configure(values=unidades)

    combo_de.set(unidades[0])
    combo_para.set(unidades[1])

    resultado.configure(text="Resultado")


# Realiza a conversão.
def converter():

    try:

        valor = float(entrada.get())

        grandeza = combo_grandeza.get()

        unidade_de = combo_de.get()
        unidade_para = combo_para.get()

        # Temperatura possui conversão específica.
        if grandeza == "Temperatura":

            valor_convertido = converter_temperatura(
                valor,
                unidade_de,
                unidade_para
            )

        # As demais grandezas utilizam fatores.
        else:

            fatores = grandezas[grandeza]

            valor_referencia = (
                valor * fatores[unidade_de]
            )

            valor_convertido = (
                valor_referencia
                / fatores[unidade_para]
            )

        resultado.configure(
            text=f"{valor_convertido:.6g} {unidade_para}"
        )

    except ValueError:

        resultado.configure(
            text="Digite um valor numérico válido."
        )


# Inverte as unidades.
def inverter_unidades():

    unidade_de = combo_de.get()
    unidade_para = combo_para.get()

    combo_de.set(unidade_para)
    combo_para.set(unidade_de)


# ---------------------------------------------------------
# CONFIGURAÇÃO DA INTERFACE
# ---------------------------------------------------------

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
    command=converter
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


# Inicia o loop principal de eventos.
app.mainloop()
