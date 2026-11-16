# EDU Revolution Assistant (Streamlit)

A Streamlit chatbot powered by the Google Gemini API and the EDU Revolution
knowledge guide supplied with the project.

## 1. Requirements
- Python 3.10 or newer
- A Gemini API key

## 2. Install dependencies

Open a terminal in this project folder and run:

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

## 3. Configure the API key

Open `.streamlit/secrets.toml` and replace the placeholder:

```toml
GEMINI_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"
```

with your own Gemini API key. Keep this file private. Do not upload it to
GitHub or share it publicly.

## 4. Run the chatbot

```bash
streamlit run app.py
```

Streamlit will print a local address (usually http://localhost:8501) to open
in your browser.

## Notes
- The chatbot keeps conversation history for the current browser session.
- The guide is embedded in `app.py`; update the `MANUAL` text to change its
  knowledge base.
- The model name is set to `gemini-3.5-flash-lite` to match the supplied code.
  If that model is unavailable for your Gemini API project, change the `model`
  value in `app.py` to a model enabled for your account.
- This is an informational assistant, not an official LPU approval system.
- The supplied guide includes policy thresholds. Verify current rules with
  the University before making academic decisions.
