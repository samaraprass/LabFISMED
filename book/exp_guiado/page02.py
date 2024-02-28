import streamlit as st

def page2_func():
    st.markdown('''
            <style>div.card_f{background-color: rgba(255, 255, 0, 0.3);  text-align:justify; padding: 20px; border-radius: 3px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
            <div class="card_f">
            <div class="container">
            <h6> Você estava com um machucado na perna. O técnico em radiologia, com pouca experiência no equipamento, cometeu um engano e realizou a radiografia em diferentes partes dos membros inferiores utilizando a mesma técnica radiográfica. As imagens obtidas foram: </h6>
            </div></div>
            ''', unsafe_allow_html=True)
    st.write(' ')

    i_1, i_2, i_3 = st.columns([1.5,1.5,1.8])
    with i_1:
        st.image('book\\tíbia.png', use_column_width=True)

    with i_2:
        st.image('book\\tíbia.png', use_column_width=True)

    with i_3:
        st.image('book\\pé.png', use_column_width=True)


    # ii1, ii2, ii3 = st.columns([1,2,1])
    # with ii2:
    e1, e2 = st.columns([2.5,1])
    with e1:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown('''
            <style>div.card_s{background-color: rgba(247, 187, 171, 1);  text-align:center; padding: 20px; border-radius: 3px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
            <div class="card_s">
            <div class="container">
            <h6> ⚠️ Note que as imagens estão diferentes. Por qual motivo? </h6>
            </div></div>
            ''', unsafe_allow_html=True)

        st.markdown('')
        st.markdown('')
        st.markdown('''
            <style>div.card_f2{background-color: rgba(166, 193, 237, 0.3);  text-align:justify; padding: 20px; border-radius: 3px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
            <div class="card_f2">
            <div class="container">
            <h6> Como as regiões anatômicas possuem diferentes espessuras, a intensidade de raios X que chega no receptor de imagem, para uma mesma técnica radiográfica, irá produzir imagens com um grau de enegrecimento diferente! </h6>
            </div></div>
            ''', unsafe_allow_html=True)
        st.write(' ')

    with e2:
        st.image('book\\Perna profundidade.png', use_column_width=False, width=300)
    
    return
