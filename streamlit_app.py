import streamlit as st
from openai import OpenAI

# Chiave API per OpenAI (ricordati di proteggerla bene!)
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=OPENAI_API_KEY)

# Prompt per ogni mago
SYSTEM_PROMPTS = {
    "Melchior": "Sei Melchior, scienziato razionale e analitico. Rispondi con logica e dati.",
    "Balthasar": "Sei Balthasar, madre empatica e saggia. Rispondi con calore e comprensione.",
    "Caspar": "Sei Caspar, donna pragmatica, visionaria e diretta. Rispondi con intuizione e concretezza."
}

MAGI_COLORS = {
    "Melchior": "#4DA6FF",
    "Balthasar": "#66FF66",
    "Caspar": "#DDA0DD"
}

def ask_magi(question):
    responses = {}
    for name, prompt in SYSTEM_PROMPTS.items():
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": question}
        ]
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.7,
                max_tokens=300
            )
            responses[name] = completion.choices[0].message.content.strip()
        except Exception as e:
            responses[name] = f"Errore: {e}"
    return responses

def decision_logic(question, answers):
    triggers = ["meglio", "vero", "deve", "posso", "si può", "dovrei"]
    if any(word in question.lower() for word in triggers):
        pos = sum(any(p in a.lower() for p in ["sì", "certamente", "ovviamente", "assolutamente"]) for a in answers.values())
        neg = sum(any(n in a.lower() for n in ["no", "mai", "impossibile", "non"]) for a in answers.values())
        if pos > neg:
            return "✅ SÌ"
        elif neg > pos:
            return "❌ NO"
        else:
            return "❓ Incerto"
    return "↪️ Non applicabile"

# --- Streamlit UI ---

st.set_page_config(page_title="I Tre Magi", layout="wide")
st.title("🔮 I Tre Magi: Consulta i Saggi")

st.info("⚠️ Le domande NON vengono salvate.")

question = st.text_input("Fai una domanda ai Magi:", placeholder="Es. Devo cambiare lavoro?")

if question:
    with st.spinner("I Magi stanno riflettendo..."):
        responses = ask_magi(question)
        final_decision = decision_logic(question, responses)

    cols = st.columns(3)
    for i, name in enumerate(["Melchior", "Balthasar", "Caspar"]):
        with cols[i]:
            st.markdown(f"### {name}")
            st.markdown(f"<div style='color:{MAGI_COLORS[name]}'>{responses[name]}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"### 🧭 Risposta finale: **{final_decision}**")

# --- Footer fisso, non modificabile dall'interfaccia ---
st.markdown(
    """
    <hr style="margin-top: 50px;">
    <div style='text-align: center; color: grey; font-size: 0.85em;'>
        Fatto da <strong>Costa Bruno e Ora_dodici</strong>
    </div>
    """,
    unsafe_allow_html=True
)
