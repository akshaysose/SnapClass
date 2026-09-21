import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div class="snap-header snap-header-home">
            <img src='{logo_url}' alt='SnapClass logo' />
            <div class="home-brand-title">SNAP<br/>CLASS</div>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div class="snap-header">
            <img src='{logo_url}' alt='SnapClass logo' />
            <h2>SNAP<br/>CLASS</h2>
        </div>   
                
                """, unsafe_allow_html=True)
