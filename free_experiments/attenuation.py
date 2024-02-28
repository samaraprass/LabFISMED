import streamlit as st
import core.texts_image as TXT_IMG
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO


def attenuation():
    #st.subheader("Atenuação dos Raios X na Matéria")

    # exp = st.selectbox("Selecione o que você deseja fazer:",
    #                    ("Realizar Experimento", "Contexto Histórico", "Relatório"), key="atenuacao")

    # if exp == "Realizar Experimento":
    st.subheader("Realizando o Experimento Livre")
    t = '''
    Este experimento é livre, portanto você possui total liberdade de escolher os valores e materiais que deseja. 
    Inicialmente, você poderá escolher as características do meio e do feixe, o que lhe retornará o número 
    de fótons detectados ao atravessar a blindagem do material que você escolheu. Após isso, você poderá ver a Tabela da Atenuação do feixe,
    que lhe mostrará o número de fótons detectados para cada espessura. No final da página você encontrará os gráficos do experimento, os quais serão 
    atualizados sempre que você escolher novos valores e novos materiais na etapa 1.  
    '''
    TXT_IMG.texto(t, 19, 'black')

    st.warning('⚠️ Importante: para rodar o experimento com os valores que você escolheu, sempre clique no botão "Aplicar Escolhas" ao final do formulário.')
    
    with st.form(key="form1"):
        TXT_IMG.title2("\n1 - DEFININDO AS CARACTERÍSTICAS DO MEIO E DO FEIXE")
        a1_col1, a1_col2 = st.columns(2)
        with a1_col1:
            n0 = st.number_input("\nDefina o número de fótons iniciais para a simulação: ", min_value=0,
                                    max_value=5000,
                                    value=1000)
            st.write("Número de fótons iniciais escolhido: ", str(n0))

            E = float(st.select_slider('Defina a energia do feixe (em keV)', options=[17, 30, 60, 150, 300, 500, 1250, 6000, 10000]))
            st.write("Energia do feixe escolhida: ", str(E), "keV")

        with a1_col2:
            e = [17, 30, 60, 150, 300, 500, 1250, 6000, 10000]
            esp = st.number_input("\nInforme a espessura da blindagem, em centímetros: ", min_value=0,
                                    max_value=5000,
                                    value=60, help="Min=0, Max=5000")
            st.write("Espessura escolhida: ", str(esp), "cm")

            # Definição do material e do coef de atenuação linear
            material = st.selectbox("Defina o material que deseja utilizar na simulação: ",
                                    ("Alumínio", 'Chumbo', 'Concreto', 'Urânio', 'Concreto Baritado', 'Mama',
                                        'Acrílico', 'Músculo', 'Osso', 'Tecido Mole', 'Tecido Adiposo', 'Água'))
            if material == 'Alumínio':
                coef = [6.21350365, 3.044472, 0.7414492, 0.3719222, 0.2912359, 0.22793055, 0.13511194, 0.07165945, 0.06256292]

            elif material == 'Chumbo':
                coef = [136.490736, 3.44132, 5.69935, 2.29599, 0.4575195, 0.193199, 0.066926, 0.04993795, 0.0564322]

            elif material == 'Concreto':
                coef = [4.6599949, 2.20923, 0.6119, 0.3736, 0.25231, 0.205045, 0.133561, 0.062031, 0.052394]

            elif material == 'Urânio':
                coef = [47.2497367, 79.2256, 13.331325, 4.909945, 0.99394, 0.374452, 0.1207115, 0.292355, 0.09944525]

            elif material == 'Concreto Baritado':
                coef = [27.910219, 19.59595, 13.97905, 1.491705, 0.4991, 0.3119515, 0.191034, 0.105927, 0.105123]

            elif material == 'Mama':
                coef = [1.07495799, 0.347106, 0.3026, 0.152296, 0.120259, 0.0992362, 0.0641274, 0.0279562, 0.0221239]

            elif material == 'Acrílico':
                coef = [0.95397423, 0.3600909, 0.229956, 0.173264, 0.13709, 0.111979, 0.0731017, 0.0316421, 0.0250495]

            elif material == 'Músculo':
                coef = [1.33211679, 0.397215, 0.21504, 0.1566, 0.12349, 0.100779, 0.0657925, 0.0297905, 0.023016]

            elif material == 'Osso':
                coef = [6.9377316, 2.55552, 0.604416, 0.29416, 0.213696, 0.1732224, 0.1127232, 0.0524929, 0.044429]

            elif material == 'Tecido Mole':
                coef = [1.30109499, 0.401741, 0.21709, 0.159152, 0.12455, 0.101739, 0.066409, 0.0290546, 0.0232459]

            elif material == 'Tecido adiposo':
                coef = [0.959366096, 0.290995, 0.19753, 0.1425, 0.12765, 0.092112, 0.060135, 0.025975, 0.0203775]

            elif material == 'Água':
                coef = [1.30109499, 0.3756, 0.2059, 0.1505, 0.1196, 0.09697, 0.06323, 0.0277, 0.02219]

            for i in range(0, 9):
                if E == e[i]:
                    mi = coef[i]

            st.write("O coeficiente de atenuação linear para este material é:", f'{mi:.5}', '/cm')
            # Solução analitica para atenuação de fótons na matéria
            n = float(n0) * np.exp(-mi * float(esp))

        submitted = st.form_submit_button("Aplicar escolhas", help="Clique aqui para ver os resultados do experimento com os valores que você escolheu")

        TXT_IMG.title('\n RESULTADO - O número de fótons detectados ao atravessar a blindagem é: ' + f'{n:.4e}' +
                " fótons", 17, 'black')
    
    st.write("---")

    with st.form(key="form2"):
        TXT_IMG.title2("\n2 - TABELA DA ATENUAÇÃO DO FEIXE")
        p = float(st.select_slider('Defina o passo para a distância (em cm): ', options=[5, 10, 15, 20], value=10))
        st.write("\nVariação da espessura escolhida: ", str(p), "cm")
        st.write("\nA tabela abaixo nos retorna o número de fótons que atravessaram o material de acordo "
                    "com a energia e a espessura")
        use_column_width = st.checkbox("Usar a largura da página",
                                        help=(
                                            "Selecione e clique em 'Aplicar Escolha' para ampliar o tamanho da tabela "
                                            "e fazer o download em alta resolução. Clique "
                                            "com o botão direito sobre a imagem e escolha "
                                            "'Salvar imagem como'."))

        submitted2 = st.form_submit_button("Aplicar escolha", help="Clique aqui para ver a tabela do experimento com os valores de distância que você escolheu")


        # Definindo a função para criar a tabela:
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

        # Criando a tabela
        X = np.arange(0, esp + p, p)
        ne = n0 * np.exp(-mi * X)
        t = pd.DataFrame(ne, columns=["N (para " + str(E) + " keV)"])
        t.insert(0, "Espessura (cm)", X, True)
        tab = t.round(decimals=6)

        fig, ax = render_mpl_table(tab)
        buf = BytesIO()
        fig.savefig(buf, bbox_inches='tight', dpi=600, format="png", transparent=True)
        st.image(buf, width=300, use_column_width=use_column_width)

    st.write("---")

    # Graphs plotting
    col_1, col_2 = st.columns(2)
    with col_1:
        TXT_IMG.title2("\n3 - GRÁFICO DA ATENUAÇÃO DO FEIXE")
        st.write("")
        st.write(
            '\nO gráfico abaixo nos mostra a atenuação do feixe e o número de fótons absorvidos, de acordo com o material escolhido.\n')
        st.write("")

        x = np.linspace(0, esp, 100)  # espessura do material em centímetros
        ne = n0 * np.exp(-mi * x)

        nabs = n0 - ne

        fig2, ax2 = plt.subplots(figsize=(10, 5))
        ax2.plot(x, ne, label="Fótons Detectados")
        ax2.plot(x, nabs, label="Fótons Absorvidos")
        plt.xlabel('Espessura (cm)')
        plt.ylabel('Número de fótons')
        plt.title('Atenuação de um feixe de ' + str(E) + " keV - " + str(material))
        ax2.legend()
        st.pyplot(fig2)

    with col_2:
        TXT_IMG.title2("\n4 - GRÁFICO DA ATENUAÇÃO DO FEIXE PARA CADA ENERGIA DISPONÍVEL\n")
        st.write(
            "\nO gráfico abaixo nos mostra a atenuação do feixe para as respectivas energias, de acordo com o material escolhido.\n")
        atenuado = []
        for i in range(0, 9):
            nf = n0 * (np.exp(-(x * coef[i])))
            atenuado.append(nf)

        e = [17, 30, 60, 150, 300, 500, 1250, 6000, 10000]  # energias disponíveis
        fig3, ax3 = plt.subplots(figsize=(10, 5))
        for i in range(0, 9):
            ax3.plot(x, atenuado[i], label=str(e[i]) + "kev")
            plt.xlabel('Espessura (cm)')
            plt.ylabel('Número de fótons')
            plt.title('Atenuação do feixe - ' + str(material))
            ax3.legend()
        # fig3.tight_layout()
        st.pyplot(fig3)
