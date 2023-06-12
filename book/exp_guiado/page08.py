import streamlit as st
import base64

def page8_func():
    st.markdown('''
            <style>div.card_f{background-color: rgba(121, 237, 152, 0.3);  text-align:center; padding: 20px; border-radius: 3px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
            <div class="card_f">
            <div class="container">
            <h6> PARABÉNS! Você completou seu primeiro experimento. Agora siga para o experimento guiado avançado ou se aventure no experimento livre. Não esqueça de 
             deixar seu feedback sobre sua experiência no menu lateral. 😊</h6>
            </div></div>
            ''', unsafe_allow_html=True)
    st.write("")
    file_animation_g= open('gif_png/end_animation.gif', 'rb')
    content_animation_g = file_animation_g.read()
    data_url_animation_g = base64.b64encode(content_animation_g).decode("utf-8")
    file_animation_g.close()

    st.markdown(f'<img src="data:image/gif;base64,{data_url_animation_g}" alt="cat gif" class="center" style="width: 50%; object-fit: contain">',
                            unsafe_allow_html=True)

    return