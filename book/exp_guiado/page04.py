import streamlit as st

def page4_func():
    st.subheader('Melhorando as imagens...')
    i1, i2, i3  = st.columns([0.5,5,0.5])
    with i2:
        st.write(" ")
        st.image('book/05.png', use_column_width=True)
        st.image('book/06.png', use_column_width=True)
    i_1, i_2 = st.columns(2)
    with i_1:
        st.image('book/07.png', use_column_width=True)
    with i_2:
        st.image('book/08.png', use_column_width=True)
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
    
    return



