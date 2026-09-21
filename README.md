# SnapClass

AI-assisted attendance built with Streamlit, Supabase, face recognition, and voice recognition.

## Run locally

1. Install dependencies:

	```bash
	pip install -r requirements.txt
	```

2. Create `.streamlit/secrets.toml` locally:

	```toml
	SUPABASE_URL = "your-supabase-url"
	SUPABASE_KEY = "your-supabase-key"
	```

3. Start the app:

	```bash
	streamlit run app.py
	```

## Deploy on Streamlit Cloud

In the app's **Manage app > Settings > Secrets** panel, add:

```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"
```

Do not commit `secrets.toml` or expose Supabase credentials in source control. After saving the secrets, restart the deployed app.