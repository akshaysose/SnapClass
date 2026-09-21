import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <article class="subject-card">
        <h3>{name}</h3>
        <p>Code: <span class="subject-code">{code}</span> <span aria-hidden="true">|</span> Section: {section}</p>
        
        """
    
    if stats:
        html+= """
        <div class="subject-stats">
        """
        for icon, label, value in stats:
            html+= f'<div class="subject-stat">{icon} <b>{value}</b> {label}</div>'
        
        html+= "</div>"

    html += "</article>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
