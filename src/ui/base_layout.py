import streamlit as st



def style_background_home():

    st.markdown("""
        <style>
                :root {
                    --snap-blue: #5865F2;
                    --snap-lavender: #E0E3FF;
                    --snap-pink: #EB459E;
                    --snap-ink: #25243A;
                    --snap-slate: #64748B;
                    --snap-warning: #E9EACB;
                }

                .stApp {
                    background: var(--snap-blue) !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: var(--snap-lavender) !important;
                    padding: clamp(1.25rem, 4vw, 2.5rem) !important;
                    border-radius: clamp(2rem, 7vw, 5rem) !important;
                    }

                .stApp div[data-testid="stColumn"] h2 {
                    color: var(--snap-ink) !important;
                }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                width: min(100% - 2rem, 1100px) !important;
                padding-top:1.5rem !important;
                padding-bottom:2rem !important;
            }

            .snap-header {
                align-items: center;
                display: flex;
                gap: 10px;
                justify-content: center;
                min-height: 85px;
            }

            .snap-header img {
                height: 85px;
                max-width: 100%;
                object-fit: contain;
            }

            .snap-header-home {
                flex-direction: column;
                margin: 1.5rem 0 2rem;
            }

            .snap-header-home img {
                height: 100px;
            }

            .home-brand-title {
                color: #E0E3FF !important;
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: clamp(3rem, 8vw, 5rem) !important;
                font-weight: 900 !important;
                letter-spacing: 0 !important;
                line-height: .78 !important;
                text-align: center;
            }

            .snap-header h1,
            .snap-header h2 {
                color: #5865F2 !important;
                line-height: .85 !important;
                margin: 0 !important;
            }

            .snap-footer {
                align-items: center;
                display: flex;
                gap: 6px;
                justify-content: center;
                margin-top: 2rem;
            }

            .snap-footer p {
                color: #25243A !important;
                font-weight: 600;
                margin: 0;
            }

            .snap-footer-home p {
                color: #FFFFFF !important;
            }

            .auth-title {
                color: #25243A !important;
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: clamp(2rem, 5vw, 2.6rem) !important;
                line-height: 1 !important;
                margin: 1.5rem 0 2.5rem !important;
                text-align: center !important;
            }

            .subject-card {
                background: #FFFFFF;
                border: 1px solid #25243A;
                border-left: 8px solid #EB459E;
                border-radius: .75rem;
                box-sizing: border-box;
                margin-bottom: 1.25rem;
                padding: 1.25rem;
                width: 100%;
            }

            .subject-card h3 {
                color: #25243A !important;
                font-size: 1.35rem;
                margin: 0;
                overflow-wrap: anywhere;
            }

            .subject-card p {
                color: #64748B !important;
                margin: .65rem 0;
                overflow-wrap: anywhere;
            }

            .subject-code {
                background: #E0E3FF;
                border-radius: .35rem;
                color: #5865F2;
                display: inline-block;
                font-weight: 600;
                padding: .15rem .5rem;
            }

            .subject-stats {
                display: flex;
                flex-wrap: wrap;
                gap: .5rem;
            }

            .subject-stat {
                background: rgba(235, 69, 158, .08);
                border-radius: .6rem;
                color: #25243A;
                font-family: 'Outfit', sans-serif;
                font-size: .9rem;
                padding: .35rem .7rem;
            }

            div[data-testid="stTextInput"] label,
            div[data-testid="stCameraInput"] label,
            div[data-testid="stAudioInput"] label,
            div[data-testid="stSelectbox"] label {
                color: #25243A !important;
                font-family: 'Outfit', sans-serif !important;
                font-size: .9rem !important;
                font-weight: 600 !important;
            }

            div[data-testid="stTextInput"] input,
            div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
                background: #FFFFFF !important;
                border: 1px solid #D5D6E5 !important;
                border-radius: .4rem !important;
                color: #25243A !important;
                min-height: 2.7rem !important;
            }

            div[data-testid="stSelectbox"] [data-baseweb="select"],
            div[data-testid="stSelectbox"] [data-baseweb="select"] *,
            div[data-testid="stSelectbox"] input,
            div[data-testid="stSelectbox"] button {
                background: #FFFFFF !important;
                color: #25243A !important;
            }

            div[data-testid="stSelectbox"] [data-baseweb="select"] svg {
                fill: #5865F2 !important;
            }

            div[data-testid="stSelectbox"] input::placeholder,
            div[data-testid="stTextInput"] input::placeholder,
            [role="dialog"] input::placeholder {
                color: #64748B !important;
                opacity: 1 !important;
            }

            [data-baseweb="popover"],
            [data-baseweb="menu"],
            [data-baseweb="popover"] ul,
            [data-baseweb="menu"] ul {
                background: #FFFFFF !important;
                color: #25243A !important;
            }

            [data-baseweb="menu"] li,
            [data-baseweb="menu"] li * {
                color: #25243A !important;
            }

            [data-baseweb="menu"] li:hover {
                background: #E0E3FF !important;
            }

            div[data-testid="stTextInput"] input:focus,
            div[data-testid="stTextInput"] input:focus-visible {
                border-color: #EB459E !important;
                box-shadow: 0 0 0 1px #EB459E !important;
            }

            [data-testid="stAlert"] {
                border-radius: .75rem !important;
            }

            [data-testid="stAlert"] p {
                font-family: 'Outfit', sans-serif !important;
                color: #25243A !important;
            }

            [data-testid="stAlert"] [data-testid="stMarkdownContainer"] {
                color: #25243A !important;
            }

            [data-testid="stHeading"] h1,
            [data-testid="stHeading"] h2,
            [data-testid="stHeading"] h3,
            [data-testid="stHeading"] h4 {
                color: #25243A !important;
            }

            [data-testid="stDialog"] {
                background: #FFFFFF !important;
                border: 1px solid #D5D6E5 !important;
                border-radius: 1rem !important;
                box-shadow: 0 1rem 2.5rem rgba(37, 36, 58, .22) !important;
            }

            [data-testid="stDialog"] > div,
            [data-testid="stDialog"] section,
            .stDialog,
            .stDialog > div,
            div[role="dialog"] {
                background: #FFFFFF !important;
                color: #25243A !important;
            }

            [data-testid="stDialog"] [data-testid="stMarkdownContainer"] p,
            [data-testid="stDialog"] label,
            [data-testid="stDialog"] [data-testid="stWidgetLabel"] {
                color: #25243A !important;
            }

            [data-testid="stDialog"] h1,
            [data-testid="stDialog"] h2,
            [data-testid="stDialog"] h3 {
                color: #25243A !important;
            }

            [role="dialog"] {
                background: #FFFFFF !important;
                border: 1px solid #D5D6E5 !important;
                border-radius: 1rem !important;
                color: #25243A !important;
            }

            [role="dialog"] h1,
            [role="dialog"] h2,
            [role="dialog"] h3,
            [role="dialog"] p,
            [role="dialog"] label,
            [role="dialog"] [data-testid="stMarkdownContainer"],
            [role="dialog"] [data-testid="stWidgetLabel"] {
                color: #25243A !important;
            }

            [role="dialog"] input,
            [role="dialog"] textarea,
            [role="dialog"] [data-baseweb="select"],
            [role="dialog"] [data-baseweb="select"] > div,
            [role="dialog"] [data-baseweb="select"] input {
                background: #FFFFFF !important;
                color: #25243A !important;
                border-color: #D5D6E5 !important;
            }

            .stDialog input,
            .stDialog textarea,
            .stDialog [data-baseweb="select"],
            .stDialog [data-baseweb="select"] > div {
                background: #FFFFFF !important;
                color: #25243A !important;
                border-color: #D5D6E5 !important;
            }

            [role="dialog"] pre,
            [role="dialog"] code {
                background: #E0E3FF !important;
                color: #25243A !important;
                border-color: #D5D6E5 !important;
            }

            [role="dialog"] [data-testid="stAlert"],
            [data-testid="stDialog"] [data-testid="stAlert"] {
                background: #E0E3FF !important;
                color: #25243A !important;
            }

            [data-testid="stDialog"] input,
            [data-testid="stDialog"] textarea,
            [data-testid="stDialog"] [data-baseweb="select"] > div {
                background: #FFFFFF !important;
                color: #25243A !important;
                border-color: #D5D6E5 !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                min-height: 2.7rem !important;
                transition: transform 0.2s ease-in-out, filter 0.2s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                filter: brightness(1.05) !important;
                transform :scale(1.02)}

            button:focus-visible {
                box-shadow: 0 0 0 3px #FFFFFF, 0 0 0 5px #25243A !important;
            }

            @media (max-width: 700px) {
                .block-container {
                    width: calc(100% - 1rem) !important;
                    padding-top: .75rem !important;
                }

                .snap-header {
                    justify-content: flex-start;
                }

                .snap-header img {
                    height: 64px;
                }

                .snap-header-home img {
                    height: 80px;
                }

                .home-brand-title {
                    font-size: 3rem !important;
                }

                .snap-header h1,
                .snap-header h2 {
                    font-size: 1.45rem !important;
                }

                .auth-title {
                    margin-bottom: 1.5rem !important;
                }
            }
        </style>  

                """
            ,unsafe_allow_html=True)