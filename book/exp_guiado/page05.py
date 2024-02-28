import streamlit as st
import base64

def page5_func():
    st.subheader('Dependência com o número atômico do material...')

    i1, i2, i3  = st.columns([0.5,5,0.5])
    with i2:
        st.write(" ")
        st.image('book/Slide1.PNG', use_column_width=True)
        st.image('book/Slide2.PNG', use_column_width=True)
        st.image('book/Slide3.PNG', use_column_width=True)

    c_1, c_2, c_3 = st.columns([1,3,1])
    with c_2:
        #st_lottie(requests.get('https://assets2.lottiefiles.com/private_files/lf30_6ocpfdil.json').json(), key="hello", loop = True, height=150)

        with st.form(key='pergunta_guiado', clear_on_submit=False):
            st.markdown('''
            <style>div.card_f{background-color: rgba(255, 255, 0, 0.3);  text-align:center; padding: 20px; border-radius: 3px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
            <div class="card_f">
            <div class="container">
            <h6> Responda. Qual das estruturas abaixo você acha que atenuou mais radiação? </h6>
            </div></div>
            ''', unsafe_allow_html=True)

            exp = st.radio(' ', ('Coração (tecido mole)', 'Pulmões (ar)', 'Costelas (tecido denso)'))

            button_p1 = st.form_submit_button("Responder")
            
        file_animation_w= open('gif_png/wrong_animation.gif', 'rb')
        content_animation_w = file_animation_w.read()
        data_url_animation_w = base64.b64encode(content_animation_w).decode("utf-8")
        file_animation_w.close()

        file_animation_r= open('gif_png/right_animation.gif', 'rb')
        content_animation_r = file_animation_r.read()
        data_url_animation_r = base64.b64encode(content_animation_r).decode("utf-8")
        file_animation_r.close()

        if button_p1:
            if exp == 'Coração (tecido mole)':
                st.markdown(f'<img src="data:image/gif;base64,{data_url_animation_w}" alt="cat gif" class="center" style="width: 30%; object-fit: contain">',
                            unsafe_allow_html=True)
                #st_lottie(requests.get('https://assets4.lottiefiles.com/private_files/lf30_jq4i7W.json').json(), key="correct", loop = True, height=150)
                st.error('Resposta errada! Tente novamente...')
                st.info('Dica: se temos um material com maior número atômico (Z) vai passar menos raios X nesse material do que se tivéssemos um material com menor Z.')
            if exp == 'Pulmões (ar)':
                st.markdown(f'<img src="data:image/gif;base64,{data_url_animation_w}" alt="cat gif" class="center" style="width: 30%; object-fit: contain">',
                            unsafe_allow_html=True)
                #st_lottie(requests.get('https://assets4.lottiefiles.com/private_files/lf30_jq4i7W.json').json(), key="correct", loop = True, height=150)
                st.error('Resposta errada!Tente novamente...')
                st.info('Dica: se temos um material com maior número atômico (Z) vai passar menos raios X nesse material do que se tivéssemos um material com menor Z.')
            if exp == 'Costelas (tecido denso)':
                st.markdown(f'<img src="data:image/gif;base64,{data_url_animation_r}" alt="cat gif" class="center" style="width: 30%; object-fit: contain">',
                            unsafe_allow_html=True)
                #st_lottie(requests.get('https://assets4.lottiefiles.com/packages/lf20_9aa9jkxv.json').json(), key="correct", loop = True, height=150)
                st.success('Resposta Certa!')
                st.info('Tecidos densos e compostos por elementos com número atômico (Z) mais elevado, como das costelas, atenuam mais a radiação em comparação com os tecidos moles,' 
                        ' como o coração e os pulmões. Na imagem radiográfica, os tecidos que absorvem mais radiação aparecem mais claros (cor branca) enquanto, os tecidos que absorvem' 
                        ' pouca radiação aparecem mais escuros (cor preta). Tecidos que absorvem os raios X de forma moderada irão aparecer na imagem radiográfica em tons de cinza. Por esse motivo,'
                        ' em uma radiografia visualizamos os ossos (mais densos e com elementos de alto Z), pulmões (pouco densos e com elementos de baixo Z) e os tecidos moles (densidade intermediária'
                        ' e elementos de baixo Z) como o coração nas cores branca, preto e cinza, respectivamente. É nesta diferença de atenuação que está o contraste da imagem radiográfica.')
        
        return
