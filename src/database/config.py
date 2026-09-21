import streamlit as st
import os


from supabase import create_client, Client


def _get_setting(name):
    value = os.getenv(name)
    if value:
        return value

    try:
        return st.secrets.get(name)
    except FileNotFoundError:
        return None


supabase_url = _get_setting("SUPABASE_URL")
supabase_key = _get_setting("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    st.error(
        "Supabase is not configured. Add SUPABASE_URL and SUPABASE_KEY "
        "to Streamlit Cloud Secrets, then restart the app."
    )
    st.stop()

supabase: Client = create_client(supabase_url, supabase_key)