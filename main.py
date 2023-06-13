# Importing libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
from streamlit_timeline import timeline
from streamlit_option_menu import option_menu
import pydeck as pdk
import core.texts_image as TXT_IMG
import free_experiments.attenuation as ATT
import book.exp_guiado.page01 as page01 
import book.exp_guiado.page02 as page02
import book.exp_guiado.page03 as page03
import book.exp_guiado.page04 as page04
import book.exp_guiado.page05 as page05
import book.exp_guiado.page06 as page06
import book.exp_guiado.page07 as page07
import book.exp_guiado.page08 as page08
from streamlit_image_comparison import image_comparison
from streamlit_star_rating import st_star_rating
import extra_streamlit_components as stx
from streamlit.components.v1.components import CustomComponent
from typing import List
# from streamlit_modal import Modal
# import streamlit.components.v1 as components

#Session States
if 'default' not in st.session_state:
    st.session_state['default'] = 0

if 'val' not in st.session_state:
    st.session_state['val'] = 0

# Stepper bar function
def stepper_bar(steps: List[str], is_vertical: bool = False, lock_sequence: bool = True) -> CustomComponent:
    component_value = stx.StepperBar._component_func(steps=steps, is_vertical=is_vertical, lock_sequence=lock_sequence, default=st.session_state['default'])
    return component_value

# Page Setup
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = 40, 12
st.set_page_config(page_title="LabFisMed - UFCSPA", page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Nuclear_symbol.svg/600px-Nuclear_symbol.svg.png?20131012175551", layout="wide",
                   initial_sidebar_state="expanded")

# Styling with css file
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Sidebar config
with st.sidebar: 
    file_ = open('gif_png/UFCSPAlogotipo_preto.png', 'rb')
    contents_2 = file_.read()
    data_url2 = base64.b64encode(contents_2).decode("utf-8")
    file_.close()
    html = f'<a href="https://www.ufcspa.edu.br/" target="_blank"><div class="fade-in"><img src="data:image/gif;base64,{data_url2}" alt="logo" style="height: 100%; width: 90%; object-fit: contain"></div></a>'
    ls1, ls2, ls3 = st.columns([1, 3, 1])
    with ls2:
        st.markdown(html, unsafe_allow_html=True)
    selected = option_menu('Menu', ["Home", "Atenuação da Radiação",  "Decaimento Radioativo"], 
    icons=['house', 'radioactive', "radioactive", 'files'], 
    menu_icon="cast", default_index=0, orientation="vertical",
    styles={
        "container": {"padding": "0!important", "background-color": "#EEEEEE"},
        "icon": {"color": "orange", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#ffd2d0"},
        "nav-link-selected": {"background-color": "#C15C58"}})
    
    st.warning("LabFISMED está sob a Licença Apache 2.0")
    with st.form(key='feedback'):
        TXT_IMG.texto("Qual sua experiência utilizando este aplicativo web?", 18, 'black')
        stars = st_star_rating(label='', maxValue = 5, size=40, 
                           defaultValue = 5, emoticons = False, key = "rating", dark_theme = True )
        submit_feedback = st.form_submit_button("Enviar feedback", help="Clique aqui para enviar seu feedback")
        if submit_feedback:
            st.success("Feedback enviado")
    if stars != 5:
        with st.form(key='text_feedback'):
            txt_feedback = st.text_input("O que podemos melhorar na sua opinião?")
            submit_feedback2 = st.form_submit_button("Enviar feedback", help="Clique aqui para enviar sua sugestão")
        if submit_feedback2:
            st.success("Sugestão enviada")
    

    st.write("")
    st.write("")
    st.write("")
    st.write("")
       
    #TXT_IMG.texto("Qual sua experiência utilizando este aplicativo web?", 14, 'black')
    #st.info("Desenvolvido e mantido por Samara Prass dos Santos")
    st.markdown('''
    <div class="footer">
    <center><p>Desenvolvido e mantido por <a style='display: block' href="https://www.linkedin.com/in/samaraprass" target="_blank">Samara Prass dos Santos</a></p></center>
    </div>
    ''', unsafe_allow_html=True)
    

if selected == "Home": #Home function
    #Lab Logo
    file_lab = open('gif_png/logo_3.1.png', 'rb')
    contents = file_lab.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_lab.close()
    html = f'<img src="data:image/gif;base64,{data_url}" alt="logo_ufcspa" class="center" style="height: 80%; width: 80%; object-fit: contain">'
    st.markdown(html, unsafe_allow_html=True)
    file_animation= open('gif_png/animation_640.gif', 'rb')
    content_animation = file_animation.read()
    data_url_animation = base64.b64encode(content_animation).decode("utf-8")
    file_animation.close()
    st.markdown(f'<img src="data:image/gif;base64,{data_url_animation}" alt="cat gif" class="center" style="height: 20%; width: 35%; object-fit: contain">',
                unsafe_allow_html=True,)
    a1, a2, a3 = st.columns([1,5,1])
    with a2:
        st.markdown('''
        <style>div.card_f{background-color: rgba(255, 255, 0, 0.3);  text-align:center; padding: 15px; border-radius: 3px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
        <div class="card_f">
        <div class="container">
        <h3 style="color:#254565">Sejam bem vindos ao LabFISMED!</h3>
        </div></div>
        ''', unsafe_allow_html=True)
    st.write("")
    st.write("")
    
    t1 = '''Buscando facilitar o acesso à informação, este laboratório foi criado a partir de um Projeto de Iniciação à Docência desenvolvido na UFCSPA, cujo objetivo é implementar um laboratório
    virtual de Física Médica com atividades que simulam experimentos reais e que apresentam
    pouco prejuízo advindo da falta de contato com os equipamentos utilizados nesses experimentos. O uso de simulações computacionais que representam experimentos reais de
    Física Médica é uma excelente alternativa para diminuir custos e proporcionar uma maior
    variedade de experimentos que utilizam radiações ionizantes.'''

    
    st.markdown('''
    <style>div.card{background-color: rgba(92, 182, 212, 0.5);  text-align:center; padding: 15px; border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;}</style>
    <div class="card">
    <div class="container">
    <p style="color:#254565">Buscando facilitar o acesso à informação, este laboratório foi criado a partir de um Projeto de Iniciação à Docência desenvolvido na UFCSPA, cujo objetivo é implementar um laboratório
    virtual de Física Médica com atividades que simulam experimentos reais e que apresentam
    pouco prejuízo advindo da falta de contato com os equipamentos utilizados nesses experimentos. O uso de simulações computacionais que representam experimentos reais de
    Física Médica é uma excelente alternativa para diminuir custos e proporcionar uma maior
    variedade de experimentos que utilizam radiações ionizantes.</p>
    </div></div>
    ''', unsafe_allow_html=True)
    
    st.write("")
    file_gif = open('gif_png/gif_lab_home.gif', 'rb')
    content_gif = file_gif.read()
    data_url_gif = base64.b64encode(content_gif).decode("utf-8")
    file_gif.close()
    st.markdown(f'<img src="data:image/gif;base64,{data_url_gif}" alt="cat gif" class="center" style="height: 20%; width: 50%; object-fit: contain">',
                unsafe_allow_html=True,)

    st.write("")

    st.subheader("Sobre a UFCSPA")
    t2 = '''A Universidade Federal de Ciências da Saúde de Porto Alegre foi reconhecida como tal em 11 de janeiro de 2008, sendo originária da Fundação Faculdade Federal de Ciências
    Médicas de Porto Alegre. Desde sua fundação, a atenção integral à saúde está presente em sua missão e visão institucional, propulcionando sua existência desde então, além de ser 
    única e visionária na especialização em saúde no ambiente de instituições federais de ensino superior. Atualmente, a UFCSPA oferece 16 cursos de graduação, 64 programas de 
    Residência Médica, quatro programas de Residência Multiprofissional, nove cursos de Especializção e 12 programas de Pós-Graduação Stricto Sensu.    
    '''
    t3 = '''A UFCSPA está localizada ao lado da Santa Casa de Misericórdia de Porto Alegre, no Centro Histórico da capital do Rio Grande do Sul. Sua infraestrutura de qualidade compõe salas de aula 
    climatizada e com equipamentos multimídia, bem como possui laboratórios completos e atualizados de acordo com as necessidades de cada curso de graduação e pós-graduação, além de oportunizar espaços 
    para convivência acadêmica e para alimentação.'''
    TXT_IMG.texto(t2, 16, 'black')
    TXT_IMG.texto(t3, 16, 'black')
    
    #m1, m2 = st.columns(2)
    #with m1:
        #st.image('gif_png/UFCSPA.png')
        
    #with m2:
        #hight = 250

        #df = pd.DataFrame([[-30.031353983201605, -51.2207610122685]], columns=['lat', 'lon'])


        #st.map(df, zoom=15.5)
        #st.pydeck_chart(pdk.Deck(map_style='mapbox://styles/mapbox/light-v9', initial_view_state=pdk.ViewState(latitude=-30.031353983201605, 
                                #longitude=-51.2207610122685, zoom=15.5, height=hight), layers=[pdk.Layer('ScatterplotLayer',
                                #data=df, get_position='[lon, lat]', get_color='[200, 30, 0, 160]', get_radius=25, auto_highlight=True)]))
    #st.write('')

    st.subheader('Sobre o Projeto')
    t4 = '''O Programa de Iniciação à Docência - PID da UFCSPA busca influenciar no desenvolvimento do ensino na graduação com a atuação de alunos de graduação como 
    bolsistas na elaboração e execução de Projetos de Ensino. De acordo com o <a style='text-align: center;' href="https://www.ufcspa.edu.br/sobre-a-ufcspa/normas/prograd/1207-regulamento-do-programa-de-iniciacao-a-docencia-pid?highlight=WyJpbmljaWFjYW8iLCJhIiwiJ2EiLCJkb2NlbmNpYSIsImluaWNpYWNhbyBhIiwiaW5pY2lhY2FvIGEgZG9jZW5jaWEiLCJhIGRvY2VuY2lhIl0=" target=>regulamento do programa</a>, seus objetivos são:'''
    t5 = '''• Despertar no aluno o gosto pela carreira docente em atividades de ensino, pesquisa e extensão;'''
    t6 = '''• Promover a cooperação entre o corpo docente e o corpo discente;'''
    t7 = '''• Contribuir para a melhoria da qualidade de ensino da graduação através do estabelecimento de novas práticas e experiências pedagógicas.'''
    TXT_IMG.texto(t4, 16, 'black')
    TXT_IMG.texto(t5, 16, 'black')
    TXT_IMG.texto(t6, 16, 'black')
    TXT_IMG.texto(t7, 16, 'black')

    t8 = '''O projeto PID "Laboratório Virtual de Física Médica" iniciou em 2020, no contexto de afastamento das atividades acadêmicas presenciais. Dessa forma,
    reuniões virtuais semanais eram realizadas com todos integrantes, na qual eram debatidas as melhores abordagens para um ensino virtual e as melhores ferramentas para 
    a implementação da ideia. A partir da entrega semanal de tarefas dos estudantes envolvidos, o laboratório foi sendo construído sem abrir mão da compreensão de todos objetivos
    de um Programa de Iniciação à Docência.'''

    t9 = '''A criação dessa plataforma é uma abordagem verdadeiramente inovadora para a educação, particularmente no campo da física. Tradicionalmente, os alunos realizariam 
    experimentos em um laboratório físico, o que pode ser caro, demorado e potencialmente perigoso. No entanto, com o advento dos laboratórios virtuais, os alunos já podem realizar experimentos 
    em um ambiente seguro e controlado, sem a necessidade de equipamentos caros ou instalações especializadas.'''

    t10 = '''Além dos benefícios práticos, os laboratórios virtuais também oferecem uma série de vantagens pedagógicas. Por exemplo, eles podem fornecer aos alunos uma plataforma para explorar e testar conceitos teóricos, permitindo-lhes obter 
    uma compreensão mais profunda dos princípios subjacentes da física. Eles também podem fornecer aos alunos feedback instantâneo sobre seus experimentos, permitindo que eles ajustem sua abordagem e refinem suas hipóteses em tempo real.'''
    
    TXT_IMG.texto(t8, 16, 'black')
    TXT_IMG.texto(t9, 16, 'black')
    TXT_IMG.texto(t10, 16, 'black')

    TXT_IMG.texto("Conheça nossa equipe", 25, '#696969')
    t11 = '''• <a href="http://lattes.cnpq.br/6663802572618837" target=> Cibele Cruz Marques</a>: Elaboração de roteiros para os experimentos guiados do módulo básico e avançado;'''
    t13 = '''• <a href="https://lattes.cnpq.br/3536359835543055" taget=> Gustavo de Carvalho</a>: Elaboração de artes e animações, confecção do avatar dos membros do projeto e pesquisa do contexto histórico;'''
    t12 = '''• <a href="http://lattes.cnpq.br/6113418229155107" target=> Felipe Fernando Muller dos Santos</a>: Pesquisa e elaboração de textos sobre o conceito histórico, seleção de imagens históricas, criação de templates para linha do tempo;'''
    t14 = '''• <a href="http://lattes.cnpq.br/4640225746109996" target=> Henrique Trombini</a>: Coordenador do projeto;'''
    t15 = '''• <a href="http://lattes.cnpq.br/2490332310814507" target=> Maíra Tiemi Yoshizumi</a>: Sugestões de conteúdos e revisão dos roteiros;'''
    t16 = '''• <a href="http://lattes.cnpq.br/5022501224204788" target=> Raquel Solares Soares</a>: Elaboração de roteiros para os experimentos, pesquisa de bibliotecas em Python para a implementação do laboratório virtual, elaboração de artigo científico, levantamento das características dos materiais e energias;'''
    t17 = '''• <a href="http://lattes.cnpq.br/9679712535577946" target=> Samara Prass dos Santos</a>: Pesquisa de bibliotecas em Python para implementação do laboratório virtual, elaboração de identidade visual, escrita do código dos experimentos de atenuação da radiação ionizante na matéria e decaimento radioativo; desenvolvimento e manutenção do LabFISMED utilizando a biblioteca Streamlit e Visual Studio Code;'''
    t18 = '''• <a href="http://lattes.cnpq.br/6545287935099792" target=> Thatiane Alves Pianoschi</a>: Sugestões de conteúdos e revisão dos roteiros.'''

    t_c1, t_c2, t_c3 = st.columns([2,0.1,2])
    with t_c1:
        TXT_IMG.texto(t11, 16, 'black')
        TXT_IMG.texto(t12, 16, 'black')
        TXT_IMG.texto(t13, 16, 'black')
        TXT_IMG.texto(t14, 16, 'black')
        TXT_IMG.texto(t15, 16, 'black')
        TXT_IMG.texto(t18, 16, 'black')
        
    with t_c3:
        TXT_IMG.texto(t16, 16, 'black')
        TXT_IMG.texto(t17, 16, 'black')



if selected == 'Atenuação da Radiação':
    #Lab Logo
    file_lab = open('gif_png/logo_3.1.png', 'rb')
    contents = file_lab.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_lab.close()
    html = f'<img src="data:image/gif;base64,{data_url}" alt="logo_ufcspa" class="center" style="height: 50%; width: 50%; object-fit: contain">'
    st.markdown(html, unsafe_allow_html=True)
    st.write("")
    st.write("")
    #Menu Experimentos
    # selected2 = option_menu(menu_title = None, options=['Experimento Guiado', 'Experimento livre', 'Contexto Histórico'], icons=['book', 'book-half', 'book-fill'], 
    # menu_icon=None, default_index=0, orientation="horizontal",
    # styles={
    #     "container": {"padding": "0!important", "background-color": "#eee"},
    #     "icon": {"color": "orange", "font-size": "15px"}, 
    #     "nav-link": {"font-size": "15px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
    #     "nav-link-selected": {"background-color": "#254565"},
    # })
    selected2 = stx.tab_bar(data=[
    stx.TabBarItemData(id=1, title="Guiado Básico", description="Experimento guiado básico"),
    stx.TabBarItemData(id=2, title="Guiado Avançado", description="Experimento guiado avançado"),
    stx.TabBarItemData(id=3, title="Livre", description="Experimento Livre"),
    stx.TabBarItemData(id=4, title="Contexto Histórico", description="Linha do Tempo"),
    ], default=1)
    # stb.set_book_config(options=['Experimento Guiado', 'Experimento livre', 'Contexto Histórico', 'Relatório'], paths=["book/exp_guiado.py", 'book/01chapter.md'], menu_title="Selecione o desejado", orientation='horizontal')
    
    if selected2 == '1':
        TXT_IMG.texto("Siga os módulos abaixo para completar o experimento:", 18, '#696969')
        # c1, c2, c3, c4, c5 = st.columns([1,3.2,0.001,3.2,1])
        # with c2:
        #     st.session_state['option1'] = st.button("Experimento guiado básico", use_container_width=True)
        # with c4:
        #     option2 = st.button("Experimento guiado avançado", use_container_width=True)
        #option = st_btn_select(('Experimento guiado básico', 'Experimento guiado avançado'), index=0)
       
        #if option == "Experimento guiado básico":
            # Streamit book properties
            # stb.set_chapter_config(path='book/exp_guiado', toc=False, button='bottom', button_previous='⬅️', button_next='➡️', 
            # button_refresh='🔄', on_load_header=None, on_load_footer=None, save_answers=False)

        st.session_state['val'] = stepper_bar(steps=["Módulo 1", "Módulo 2", "Módulo 3", "Módulo 4", "Módulo 5", "Módulo 6", "Módulo 7", "Módulo 8"], lock_sequence=False) 

        if st.session_state['val'] == 0:
            st.markdown("### Imagine que você está andando de bicicleta...")
            # Streamit book properties
            # book1 = stb.set_chapter_config(path='book/exp_guiado/modulo_1', toc=False, button='bottom', button_previous='⬅️', button_next='➡️', 
            # button_refresh='🔄', on_load_header=None, on_load_footer=None, save_answers=False, display_page_info=False)
            page01.page1_func()
            next1 = st.button("Próximo módulo", key="next1", type="primary", help="Clique aqui para mudar de módulo. Caso não funcione, vá ao topo da página e escolha o módulo respectivo.")
            if next1:
                st.session_state['default'] = 1
                st.experimental_rerun()

        if st.session_state['val'] == 1:
            # book2 = stb.set_chapter_config(path='book/exp_guiado/modulo_2', toc=False, button='bottom', button_previous='⬅️', button_next='➡️', 
            # button_refresh='🔄', on_load_header=None, on_load_footer=None, save_answers=False, display_page_info=False)
            page02.page2_func()
            next2 = st.button("Próximo módulo", key="next2", type="primary", help="Clique aqui para mudar de módulo. Caso não funcione, vá ao topo da página e escolha o módulo respectivo.")
            if next2:
                st.session_state['default'] = 2
                st.experimental_rerun()

        if st.session_state['val'] == 2:
            st.session_state['page_number'] = 0
            page03.page3_func()
            next3 = st.button("Próximo módulo", key="next3", type="primary", help="Clique aqui para mudar de módulo. Caso não funcione, vá ao topo da página e escolha o módulo respectivo.")
            if next3:
                st.session_state['default'] = 3
                st.experimental_rerun()
        
        if st.session_state['val'] == 3:
            page04.page4_func()
            next4 = st.button("Próximo módulo", key="next4", type="primary", help="Clique aqui para mudar de módulo. Caso não funcione, vá ao topo da página e escolha o módulo respectivo.")
            if next4:
                st.session_state['default'] = 4
                st.experimental_rerun()
            
        
        if st.session_state['val'] == 4:
            page05.page5_func()
            next5 = st.button("Próximo módulo", key="next5", type="primary", help="Clique aqui para mudar de módulo. Caso não funcione, vá ao topo da página e escolha o módulo respectivo.")
            if next5:
                st.session_state['default'] = 5
                st.experimental_rerun()

        if st.session_state['val'] == 5:
            page06.page6_func()
            next6 = st.button("Próximo módulo", key="next6", type="primary", help="Clique aqui para mudar de módulo. Caso não funcione, vá ao topo da página e escolha o módulo respectivo.")
            if next6:
                st.session_state['default'] = 6
                st.experimental_rerun()

        if st.session_state['val'] == 6:
            page07.page7_func()
            next7 = st.button("Finalizar experimento", key="next7", type="primary", help="Clique aqui para finalizar o experimento. Caso não funcione, vá ao topo da página e escolha o módulo respectivo.")
            if next7:
                st.session_state['default'] = 7
                st.experimental_rerun()
        
        if st.session_state['val'] == 7:
            page08.page8_func()
        #st.session_state

    if selected2 == '2':
        TXT_IMG.texto2("Página em desenvolvimento...", 20, '#696969')
        file_gif_d = open('gif_png/99087-web-development.gif', 'rb')
        content_gif_d = file_gif_d.read()
        data_url_gif_d = base64.b64encode(content_gif_d).decode("utf-8")
        file_gif_d.close()
        st.markdown(f'<img src="data:image/gif;base64,{data_url_gif_d}" alt="cat gif" class="center" style="height: 20%; width: 50%; object-fit: contain">',
                    unsafe_allow_html=True,)
    
    if selected2 == '3':
        ATT.attenuation()
    
    if selected2 == "4":
        # load data
        with open('timeline.json', "r") as f:
            data = f.read()

        # render timeline
        timeline(data, height=650)

if selected == "Decaimento Radioativo":
    # Lab Logo
    file_lab = open('gif_png/logo_3.1.png', 'rb')
    contents = file_lab.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_lab.close()
    html = f'<img src="data:image/gif;base64,{data_url}" alt="logo_ufcspa" class="center" style="height: 50%; width: 50%; object-fit: contain">'
    st.markdown(html, unsafe_allow_html=True)
    st.write(" ")
    TXT_IMG.texto2("Página em desenvolvimento...", 20, '#696969')
    file_gif_d = open('gif_png/99087-web-development.gif', 'rb')
    content_gif_d = file_gif_d.read()
    data_url_gif_d = base64.b64encode(content_gif_d).decode("utf-8")
    file_gif_d.close()
    st.markdown(f'<img src="data:image/gif;base64,{data_url_gif_d}" alt="cat gif" class="center" style="height: 20%; width: 50%; object-fit: contain">',
                unsafe_allow_html=True,)
