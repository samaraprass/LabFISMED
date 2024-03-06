import streamlit as st
import base64

def page4_func():
    st.subheader('Melhorando as imagens...')
    i1, i2, i3  = st.columns([0.5,5,0.5])
    with i2:
        st.write(" ")
        st.image('book/05.PNG', use_column_width=True)
        st.image('book/6.PNG', use_column_width=True)
    i_1, i_2 = st.columns(2)
    with i_1:
        st.image('book/7.PNG', use_column_width=True)
    with i_2:
        st.image('book/8.PNG', use_column_width=True)
    st.write(' ')

    # st.markdown('''
    #     <style>div.card_s{background-color: rgba(255, 255, 0, 0.3);  text-align:center; padding: 20px; border-radius: 3px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
    #     <div class="card_s">
    #     <div class="container">
    #     <h6> Experimente você mesmo: Selecione as imagens correspondentes às energias abaixo e veja o que acontece quando aumentamos a energia dos raios X </h6>
    #     </div></div>
    #     ''', unsafe_allow_html=True)

    # c1, c2 = st.columns([2,2])
    # with c1:
    #     with st.form("E1"):
    #         TXT_IMG.texto("Escolha a imagem que corresponde a Energia 1:", 25, '#696969')
    #         content = """
    #             <a href='#' id='Imagem 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
    #             <a href='#' id='Imagem 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    #             <a href='#' id='Imagem 3'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    #             """
    #         clicked = click_detector(content)
    #         submit_1 = st.form_submit_button("Responder")

    #     if clicked == 'Imagem 2':
    #         st.success(f'Você selecicou a {clicked}. Sua resposta está certa!')

    #     elif clicked == 'Imagem 1' or clicked == 'Imagem 3':
    #         st.error(f'Você selecicou a {clicked}. Tente novamente')
    # with c2:
    #     with st.form("E2"):
    #         TXT_IMG.texto("Escolha a imagem que corresponde a Energia 2:", 25, '#696969')
    #         content2 = """
    #             <a href='#' id='Imagem 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
    #             <a href='#' id='Imagem 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    #             <a href='#' id='Imagem 3'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    #             """
    #         clicked2 = click_detector(content2)
    #         submit_2 = st.form_submit_button("Responder")

    #     if clicked2 == 'Imagem 3':
    #         st.success(f'Você selecicou a {clicked2}. Sua resposta está certa!')

    #     elif clicked2 == 'Imagem 1' or clicked2 == 'Imagem 2':
    #         st.error(f'Você selecicou a {clicked2}. Tente novamente')

    # with c1:

    #     with st.form("E3"):
    #             TXT_IMG.texto("Escolha a imagem que corresponde a Energia 3:", 25, '#696969')
    #             content3 = """
    #                 <a href='#' id='Imagem 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
    #                 <a href='#' id='Imagem 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    #                 <a href='#' id='Imagem 3'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    #                 """
    #             clicked3 = click_detector(content3)
    #             submit_3 = st.form_submit_button("Responder")

    #     if clicked3 == 'Imagem 1':
    #         st.success(f'Você selecicou a {clicked3}. Sua resposta está certa!')

    #     elif clicked3 == 'Imagem 2' or clicked3 == 'Imagem 3':
    #         st.error(f'Você selecicou a {clicked3}. Tente novamente')


    st.markdown('''
        <style>div.card_s2{background-color: rgba(255, 255, 0, 0.3);  text-align:center; padding: 10px; border-radius: 3px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
        <div class="card_s2">
        <div class="container2">
        <h6> Considere que você é o técnico e precisa realizar novamente o exame. Agora, relacione as energias a seguir com as imagens que aparecem e observe o que acontece ao aumentar a energia dos raios X para uma mesma espessura de 20 cm de material atenuador, como tecido mole: </h6>
        </div></div>
        ''', unsafe_allow_html=True)
    st.write("")
    st.info("A direita, é possível observar as energias disponíveis correspondentes às alternativas a, b e c. Relacione as imagens com as energias clicando na opção mais adequada abaixo de cada imagem e clique em 'Responder' para enviar sua resposta")
    with st.form("Energy"):
        c1, c2, c3, c4 = st.columns([2,2,2,1])
        with c1:
            st.image('book/mod_4_1.png', width=200)
            exp1 = st.radio(' ', ('a', 'b', 'c'), horizontal=True, key='1st')
        with c2:
            st.image('book/mod_4_2.png', width=200)
            exp2 = st.radio(' ', ('a', 'b', 'c'), horizontal=True, key='2nd')
        with c3:
            st.image('book/mod_4_3.png', width=200)
            exp3 = st.radio(' ', ('a', 'b', 'c'), horizontal=True, key='3rd')
        with c4:
            st.write("Energias disponíveis:")
            st.write("a) 17 keV")
            st.write("")
            st.write("b) 30 keV")
            st.write("")
            st.write("c) 60 keV")
        
        submit_1 = st.form_submit_button("Responder")

    file_animation_w= open('gif_png/wrong_animation.gif', 'rb')
    content_animation_w = file_animation_w.read()
    data_url_animation_w = base64.b64encode(content_animation_w).decode("utf-8")
    file_animation_w.close()

    file_animation_r= open('gif_png/right_animation.gif', 'rb')
    content_animation_r = file_animation_r.read()
    data_url_animation_r = base64.b64encode(content_animation_r).decode("utf-8")
    file_animation_r.close()

    if submit_1:
        if exp1 == 'a' and exp2 == 'c' and exp3 == 'b':
            st.success('Resposta Certa!')
            st.markdown(f'<img src="data:image/gif;base64,{data_url_animation_r}" alt="cat gif" class="center" style="width: 30%; object-fit: contain">',
                            unsafe_allow_html=True)
            st.info('Como pode ser observado através da simulação, ao aumentar a energia dos raios X estamos aumentando seu poder de penetração. Isso porque,' 
                    'os raios X com maior energia têm menor probabilidade de interagir com o material. Na imagem radiográfica, o número de raios X que alcança '
                    'o receptor determina o enegrecimento da imagem conforme ilustrado na figura acima. ')
        else:
            st.error('Resposta errada, tente novamente...')
            st.markdown(f'<img src="data:image/gif;base64,{data_url_animation_w}" alt="cat gif" class="center" style="width: 30%; object-fit: contain">',
                        unsafe_allow_html=True)
    return
