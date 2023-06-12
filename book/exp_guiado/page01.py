import streamlit as st

def page1_func():
    i1, i2, i3  = st.columns([0.5,5,0.5])
    with i2:
        # st.markdown('''
        #     <style>div.card_f{background-color: rgba(255, 255, 0, 0.3);  text-align:justify; padding: 20px; border-radius: 3px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
        #     <div class="card_f">
        #     <div class="container">
        #     <h6> Imagine que você estava pedalando em sua bicicleta, até que caiu e se machucou. Você foi ao médico e ele te instruiu a fazer alguns exames de imagem de raio X para se certificar de que não quebrou e nem fraturou nenhum osso </h6>
        #     </div></div>
        #     ''', unsafe_allow_html=True)
        # st.markdown(' ')
        st.write(" ")
        st.image('book/01.jpg', use_column_width=True)
        st.image('book/02_03.png', use_column_width=True)
        st.image('book/04.jpg', use_column_width=True)
        st.write(' ')

        #st.subheader("Pergunta: Porque as imagens estão diferentes?")

    st.write(' ')
    return

# with i3:
#     st.image('book/Dayflow - Riding.png', use_column_width=False, width=250)

# i_1, i_2, i_3 = st.columns([1, 2, 0.85])
# with i_1:
#     st.image('book/coxa.jpg', caption='Raio X do Fêmur')
# with i_2:
#     st.image('book/pé.jpg', caption='Raio X do pé')
# with i_3:
#     st.image('book/tornozelo.jpg', caption='Raio X do tornozelo')


