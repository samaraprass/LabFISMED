import streamlit as st
import base64

def page6_func():
    st.subheader("Contraste da imagem...")

    i1, i2  = st.columns([2,1])
    with i1:
        st.image('book/Slide4.png', use_column_width=True)

    with i2:
        with st.form(key='pergunta_guiado_06', clear_on_submit=False):
            st.markdown('''
            <style>div.card_f{background-color: rgba(255, 255, 0, 0.3);  text-align:center; padding: 20px; border-radius: 3px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
            <div class="card_f">
            <div class="container">
            <h6> Você acha que o metal atenuaria mais ou menos a radiação em comparação com os tecidos anteriores (coração, pulmões e costelas)? </h6>
            </div></div>
            ''', unsafe_allow_html=True)

            exp = st.radio(' ', ('Atenuaria mais', 'Atenuaria menos'))

            button_p1 = st.form_submit_button("Responder")

    c_1, c_2, c_3 = st.columns([1,3,1])

    file_animation_w= open('gif_png/wrong_animation.gif', 'rb')
    content_animation_w = file_animation_w.read()
    data_url_animation_w = base64.b64encode(content_animation_w).decode("utf-8")
    file_animation_w.close()

    file_animation_r= open('gif_png/right_animation.gif', 'rb')
    content_animation_r = file_animation_r.read()
    data_url_animation_r = base64.b64encode(content_animation_r).decode("utf-8")
    file_animation_r.close()

    with c_2:
        if button_p1:
            if exp == 'Atenuaria menos':
                #st_lottie(requests.get('https://assets4.lottiefiles.com/private_files/lf30_jq4i7W.json').json(), key="correct", loop = True, height=90)
                st.markdown(f'<img src="data:image/gif;base64,{data_url_animation_w}" alt="cat gif" class="center" style="width: 30%; object-fit: contain">',
                            unsafe_allow_html=True)
                st.error('Resposta errada! Tente novamente...')
                st.info('Dica: o metal possui maior número atômico.')
            if exp == 'Atenuaria mais':
                #st_lottie(requests.get('https://assets4.lottiefiles.com/packages/lf20_9aa9jkxv.json').json(), key="correct", loop = True, height=90)
                st.markdown(f'<img src="data:image/gif;base64,{data_url_animation_r}" alt="cat gif" class="center" style="width: 30%; object-fit: contain">',
                            unsafe_allow_html=True)
                st.success('Resposta Certa!')
                st.info("O colar de prata do Felipe vai atenuar mais radiação devido ao seu maior número atômico Z.")

    # c1, c2 = st.columns(2)
    # with c1:
    st.image('book/Slide5.png', use_column_width=True)      
    st.image('book/Slide6.png', use_column_width=True)
   
    return