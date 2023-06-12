import streamlit as st
import core.texts_image as TXT_IMG
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import base64
from io import BytesIO

def r_decay():
    # Decaimento Radioativo
    st.subheader("Decaimento Radioativo")

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    exp = st.selectbox("Selecione o que você deseja fazer:",
                       ("Realizar Experimento", "Contexto Histórico"), key="decaimento")

    # Realizando experimento                  
    if exp == "Realizar Experimento":
        st.subheader("Realizando o Experimento")

        with st.form(key="dform1"):
            TXT_IMG.title2("\n1 - DEFININDO AS CARACTERÍSTICAS DO RADIOISÓTOPO")
            d_col1, d_col2 = st.columns(2)

            with open('style.css') as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
            with d_col1:
                n_0 = st.number_input("\nDefina o número de átomos iniciais para a simulação: ", min_value=0, max_value=5000,
                                      value=1000, help="Min=0, Max=5000")
                st.write("Número de radionuclídeos iniciais escolhido: ", f'{float(n_0):.5}')

            with d_col2:

                material = st.selectbox("Defina o elemento que deseja utilizar na simulação: ",
                                        ('Carbono-14', 'Césio-137', 'Cobalto-60', 'Flúor-18', 'Fósforo-32', 'Iodo-131',
                                         'Rádio-226', 'Samário-153', 'Sódio-24', 'Tálio-201', 'Tecnécio-99m', "Urânio-235",
                                         "Xenônio-135"), index=1)

                if material == 'Urânio-235':
                    m = 4.5 * (10 ** 9)
                    tempo = "anos"

                elif material == 'Rádio-226':
                    m = 1.6 * (10 ** 3)
                    tempo = "anos"

                elif material == 'Césio-137':
                    m = 30.17
                    tempo = "anos"
                elif material == 'Cobalto-60':
                    m = 5.26
                    tempo = "anos"
                elif material == 'Carbono-14':
                    m = 5730
                    tempo = "anos"

                elif material == 'Fósforo-32':
                    m = 32
                    tempo = "dias"
                elif material == 'Iodo-131':
                    m = 8.02
                    tempo = "dias"

                elif material == 'Tálio-201':
                    m = 73.1
                    tempo = "dias"

                elif material == 'Tecnécio-99m':
                    m = 6.02
                    tempo = 'horas'

                elif material == 'Xenônio-135':
                    m = 9
                    tempo = "horas"

                elif material == 'Samário-153':
                    m = 46.7
                    tempo = "horas"

                elif material == 'Sódio-24':
                    m = 14.96
                    tempo = "horas"

                elif material == 'Flúor-18':
                    m = 109.77
                    tempo = "minutos"

                st.write("A meia vida deste elemento é: ", str(m), tempo)

            t = st.number_input("\nInforme o tempo, em " + str(tempo) + ":", min_value=float(1), max_value=float(10 * m),
                                step=float(1), value=float(5 * m), help=("O valor mínimo aceito é 1 e o valor "
                                                                         "máximo é 10 vezes a meia vida"))
            st.write("O tempo escolhido foi de: ", f'{t:.5}', tempo)

            # Solução analítica
            lam = np.log(2) / m
            n = n_0 * np.exp(-lam * t)

            # st.write("O número de átomos do radionuclídeo após transcorrido"
            # "o tempo informado é: ", str(n))

            TXT_IMG.title('\n O número de átomos do radionuclídeo após transcorrido o tempo informado é: : ' + f'{n:.4e}' +
                  "átomos", 17, 'black')

            submitted = st.form_submit_button("Aplicar escolhas")

        with st.form(key="dform2"):
            TXT_IMG.title2("\n2 - TABELA DO DECAIMENTO RADIOATIVO")
            if material == 'Urânio-235' or material == 'Rádio-226' or material == "Carbono-14":
                p = float(
                    st.select_slider('Defina o passo para o tempo: ', options=[50, 100, 200, 300, 400, 500, 600, 700, 800,
                                                                               900, 1000], value=500))
                st.write("\nVariação do tempo escolhido: ", str(p), tempo)
                st.write("\nA tabela abaixo nos retorna o número de átomos do radionuclídeo de acordo "
                         "o tempo.")
            else:
                p = float(st.select_slider('Defina o passo para o tempo: ', options=[1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35,
                                                                                     40, 45, 50, 100, 200, 300], value=50))
                st.write("\nVariação do tempo escolhido: ", str(p), tempo)
                st.write("\nA tabela abaixo nos retorna o número de átomos do radionuclídeo de acordo "
                         "o tempo.")


            def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                                 header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                                 bbox=[0, 0, 1, 1], header_columns=0,
                                 ax=None, **kwargs):
                if ax is None:
                    size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
                    fig, ax = plt.subplots(figsize=size)
                    ax.axis('off')
                mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
                mpl_table.auto_set_font_size(False)
                mpl_table.set_fontsize(font_size)

                for k, cell in mpl_table._cells.items():
                    cell.set_edgecolor(edge_color)
                    if k[0] == 0 or k[1] < header_columns:
                        cell.set_text_props(weight='bold', color='w')
                        cell.set_facecolor(header_color)
                    else:
                        cell.set_facecolor(row_colors[k[0] % len(row_colors)])
                return ax.get_figure(), ax


            X = np.arange(0, t + p, p)
            ne = n_0 * np.exp(-lam * X)
            t_d = pd.DataFrame(ne, columns=["N (para " + material + ")"])
            t_d.insert(0, "Tempo", X, True)
            tab2 = t_d.round(decimals=6)
            use_column_width = st.checkbox("Usar a largura da página", help=("Selecione para ampliar o tamanho da tabela "
                                                                             "e fazer o download em alta resolução. Clique "
                                                                             "com o botão direito sobre a imagem e escolha "
                                                                             "'Salvar imagem como'."))
            fig, ax = render_mpl_table(tab2)
            buf = BytesIO()
            fig.savefig(buf, bbox_inches='tight', dpi=300, format="png", transparent=True)
            st.image(buf, width=300, use_column_width=use_column_width)
            submitted = st.form_submit_button("Aplicar escolhas")

        TXT_IMG.title2("\n3 - GRÁFICO DO DECAIMENTO RADIOATIVO")
        st.write("\nO gráfico abaixo nos mostra o decaimento radioativo do radionuclídeo.\n")

        T = np.linspace(0, t, 1000)
        nf = n_0 * np.exp(-lam * T)

        fig4, ax4 = plt.subplots(figsize=(10, 5))
        ax4.plot(T, nf)
        plt.ylabel("Número de átomos")
        plt.xlabel("Tempo (" + str(tempo) + ")")
        plt.title("Decaimento do radionuclídeo " + material)
        fig.tight_layout()
        d1, d2, d3 = st.columns([1, 5, 1])
        with d2:
            st.pyplot(fig4)
    
    # Contexto histórico
    elif exp == "Contexto Histórico":
        st.subheader("Contexto Histórico")
        with open('timeline_decai.json', "r") as f:
            data = f.read()

        # # render timeline
        # timeline(data, height=800)


