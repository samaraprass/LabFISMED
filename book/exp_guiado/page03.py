import streamlit as st
import base64
import numpy as np
from matplotlib import pyplot as plt
from core.texts_image import texto as TXT

def page3_func():
    if 'esp1' not in st.session_state:
        st.session_state['esp1'] = None

    if 'esp2' not in st.session_state:
        st.session_state['esp2'] = None

    if 'esp3' not in st.session_state:
        st.session_state['esp3'] = None

    # 'Tecido Mole'
    # e = [30, 60, 150, 300, 500, 1250, 6000, 10000]
    #coef = [0.401741, 0.217088, 0.158152, 0.12455, 0.1017388, 0.066409, 0.0290546, 0.0232458]

    st.subheader('O comportamento da atenuação dos raios X...')
    text = '''
        Neste módulo, vamos ver graficamente como é o comportamento da atenuação dos raios X para diferentes espessuras considerando que estamos utilizando a mesma energia e o mesmo material atenuador, 
        sendo 20 keV e tecido mole, respectivamente. Para isso, escolha três valores de espessuras abaixo e veja o comportamento do gráfico ao ajustar os pontos. Você pode testar diferentes valores. 
        Após isso, responda o quiz no final da página. 
    '''
    TXT(text, 17, 'black')
    st.info("Note que o primeiro ponto do gráfico sempre representará a ausência do material em questão.")
    st.warning("No eixo y está a porcentagem de fótons detectados após passarem pelo material e no eixo x está a espessura do material.")
    styles = {'material-icons':{'color': 'red'},
            'text-icon-link-close-container': {'box-shadow': '#D24444 0px 5px'},
            'notification-text': {'':''},
            'close-button':{'':''},
            'link':{'':''}}

    # n1, n2, n3 = st.columns([2,8,4])
    # with n2:
    #custom_notification_box(icon='info', textDisplay='  Escolha três espessuras abaixo e veja o comportamento do gráfico!', externalLink=' ', url=' ', styles=styles, key="foo")

    coef = 0.217088
    c1, c2 = st.columns([1,2])
    st.write(" ")

    with c1:
        with st.form(key='thicknesses'):
            st.session_state['esp1'] = st.number_input("Escolha a primeira espessura", 0, 5, value=5, help="Escolha um número de 0 cm a 5 cm.")
            st.session_state['esp2'] = st.number_input("Escolha a segunda espessura", 6, 10, value=10, help="Escolha um número de 10 cm a 20 cm.")
            st.session_state['esp3'] = st.number_input("Ecolha a terceira espessura", 11, 20, value=15, help="Escolha um número de 30 cm a 60 cm.")

            st.session_state['submit_esp'] = st.form_submit_button("Atualizar escolhas")

    with c2:
        # if st.session_state['submit'] == False:
        #     st.markdown('''
        #     <style>div.card_f{background-color: rgba(255, 255, 0, 0.3);  text-align:center; padding: 20px; border-radius: 3px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
        #     <div class="card_f">
        #     <div class="container">
        #     <h6> Escolha as três espessuras ao lado! </h6>
        #     </div></div>
        #     ''', unsafe_allow_html=True)

        # elif st.session_state['submit'] != False:
        l = [0, st.session_state['esp1'], st.session_state['esp2'], st.session_state['esp3']]
        perc0 = np.exp(-coef*l[0])
        perc1 = np.exp(-coef*l[1])
        perc2 = np.exp(-coef*l[2])
        perc3 = np.exp(-coef*l[3])

        percs = [perc0, perc1, perc2, perc3]
        percs = np.round(np.array(percs)*100, 2)

        st.session_state['b'] = st.checkbox('Clique aqui para ajustar os pontos!')
        
        if st.session_state['b']:
            fig1, ax1 = plt.subplots(figsize=(10, 5))
            ax1.scatter(l, percs) #plotando os pontos
            plt.ylabel('Porcentagem (%)')
            plt.xlabel('Espessura (cm)')
            ax1.plot(l, percs) # conectar pontos consecutivos com linha
            # fig_html = mpld3.fig_to_html(fig1)
            # components.html(fig_html, height=600)
            for i,j in zip(l,percs):
                ax1.annotate(str(j),xy=(i,j))
            st.pyplot(fig1)
        else:
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            ax2.scatter(l, percs) #plotando os pontos
            plt.ylabel('Porcentagem (%)')
            plt.xlabel('Espessura (cm)')
            # fig_html = mpld3.fig_to_html(fig2)
            # components.html(fig_html, height=600)
            for i,j in zip(l,percs):
                ax2.annotate(str(j),xy=(i,j))
            st.pyplot(fig2)

    c_1, c_2, c_3 = st.columns([1,3,1])
    with c_2:
        #st_lottie(requests.get('https://assets2.lottiefiles.com/private_files/lf30_6ocpfdil.json').json(), key="hello", loop = True, height=150)
        # checked, correct_answer = stb.single_choice(' ', ['Linear', 'Exponencial', 'Quadrática'], 1, success='', 
        #                                 error='', button='Responder')    
        
        # if checked:
        #     if correct_answer:
        #         st.info("Yes! It's Panel Data, but here's a pandas as a prize just for you!")           
        #         st.image('https://www.stockvault.net/data/2016/06/30/203684/preview16.jpg')
        #         # st.balloons()
            
        #     else:
        #         st.error('Resposta errada. Tente novamente...')
                
        # else:
        #     st.warning('Responda a pergunta acima e siga para a próxima etapa!')

        with st.form(key='pergunta_guiado', clear_on_submit=False):

            st.markdown('''
            <style>div.card_f{background-color: rgba(255, 255, 0, 0.3);  text-align:center; padding: 20px; border-radius: 3px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
            <div class="card_f">
            <div class="container">
            <h6> Após ajustar os pontos no gráfico acima, responda: Qual o comportamento que melhor descreve a absorção dos raios X no material? </h6>
            </div></div>
            ''', unsafe_allow_html=True)

            exp = st.radio(' ', ('Linear', 'Exponencial', 'Quadrática'))

            button_p1 = st.form_submit_button("Responder")
        
    a1, a2 = st.columns([3,2])  

    file_animation_w= open('gif_png/wrong_animation.gif', 'rb')
    content_animation_w = file_animation_w.read()
    data_url_animation_w = base64.b64encode(content_animation_w).decode("utf-8")
    file_animation_w.close()

    file_animation_r= open('gif_png/right_animation.gif', 'rb')
    content_animation_r = file_animation_r.read()
    data_url_animation_r = base64.b64encode(content_animation_r).decode("utf-8")
    file_animation_r.close()

    with a1: 
        if button_p1:
            if exp == 'Linear':
                st.markdown(f'<img src="data:image/gif;base64,{data_url_animation_w}" alt="cat gif" class="center" style="width: 30%; object-fit: contain">',
                            unsafe_allow_html=True)
                #st_lottie(requests.get('https://assets4.lottiefiles.com/private_files/lf30_jq4i7W.json').json(), key="correct", loop = True, height=150)
                st.error('Resposta errada, veja explicação abaixo e tente novamente...')
                st.info('Um ajuste linear representaria uma variação constante entre a intensidade dos raios X e a espessura do material que os raios X atravessaram.')
            if exp == 'Exponencial':
                st.markdown(f'<img src="data:image/gif;base64,{data_url_animation_r}" alt="cat gif" class="center" style="width: 30%; object-fit: contain">',
                            unsafe_allow_html=True)
                st.success('Resposta Certa!')
                #st_lottie(requests.get('https://assets4.lottiefiles.com/packages/lf20_9aa9jkxv.json').json(), key="correct", loop = True, height=150)
                st.info('O melhor ajuste dos pontos é obtido através de uma exponencial, isso ocorre devido à natureza estocástica da interação dos raios X com o material.')
            if exp == 'Quadrática':
                st.markdown(f'<img src="data:image/gif;base64,{data_url_animation_w}" alt="cat gif" class="center" style="width: 30%; object-fit: contain">',
                            unsafe_allow_html=True)
                st.error('Resposta errada, veja explicação abaixo e tente novamente...')
                #st_lottie(requests.get('https://assets4.lottiefiles.com/private_files/lf30_jq4i7W.json').json(), key="correct", loop = True, height=150)
                st.info('Um ajuste quadrático representaria uma variação em forma de "U" ou "parábola" (quadrática) entre a intensidade dos raios X e a espessura do material.')
    with a2:
        if button_p1:
            if exp == 'Linear':
                st.image('book/exemplo-grafico-funcao-linear.jpg')

            if exp == 'Exponencial':
                st.image('book/exponential-function.jpg')

            if exp == 'Quadrática':
                st.image('book/quadratica.jpeg', use_column_width=False, width=350)
    
    return
