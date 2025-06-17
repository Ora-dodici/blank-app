# Importa Streamlit per creare l'interfaccia web
import streamlit as st

# Importa il client OpenAI per interagire con i modelli GPT
from openai import OpenAI

# Recupera in modo sicuro la chiave API da secrets (file .streamlit/secrets.toml)
# Questo evita di scrivere direttamente la chiave nel codice (buona pratica di sicurezza)
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=OPENAI_API_KEY)

# Definisce i prompt personalizzati per ciascuno dei tre Magi
# Ogni prompt serve per "istruire" il modello su come deve rispondere
SYSTEM_PROMPTS = {
    "Melchior": "Sei Melchior, scienziato razionale e analitico. Rispondi con logica e dati. rispondi in 40 parole",
    "Balthasar": "Sei Balthasar, madre empatica e saggia. Rispondi con calore e comprensione.rispondi in 40 parol",
    "Caspar": "Sei Caspar, donna pragmatica, visionaria e diretta. Rispondi con intuizione e concretezza.rispondi in 40 parol"
}

# Colori associati a ciascun Mago per la visualizzazione nella UI
MAGI_COLORS = {
    "Melchior": "#4DA6FF",   # Blu
    "Balthasar": "#66FF66",  # Verde
    "Caspar": "#DDA0DD"      # Viola
}

# Funzione che invia la domanda dell'utente a ciascun Mago e raccoglie le risposte
def ask_magi(question):
    responses = {}
    for name, prompt in SYSTEM_PROMPTS.items():
        messages = [
            {"role": "system", "content": prompt},  # Prompt personalizzato
            {"role": "user", "content": question}   # Domanda dell'utente
        ]
        try:
            # Richiesta al modello GPT-4o-mini di OpenAI
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.7,    # Creatività controllata
                max_tokens=300      # Limite massimo per ogni risposta
            )
            # Salva la risposta del Mago
            responses[name] = completion.choices[0].message.content.strip()
        except Exception as e:
            # Gestione errore: salva il messaggio di errore come risposta
            responses[name] = f"Errore: {e}"
    return responses

# Funzione che sintetizza una decisione finale in base alle risposte dei Magi
def decision_logic(question, answers):
    # Parole chiave che indicano una domanda decisionale
    triggers = ["meglio", "vero", "deve", "posso", "si può", "dovrei"]
    
    # Se nella domanda c'è un trigger, valuta il senso delle risposte
    if any(word in question.lower() for word in triggers):
        # Conta quante risposte contengono segnali positivi
        pos = sum(any(p in a.lower() for p in ["sì", "certamente", "ovviamente", "assolutamente"]) for a in answers.values())
        # Conta quante risposte contengono segnali negativi
        neg = sum(any(n in a.lower() for n in ["no", "mai", "impossibile", "non"]) for a in answers.values())

        # Determina la decisione finale
        if pos > neg:
            return "✅ SÌ"
        elif neg > pos:
            return "❌ NO"
        else:
            return "❓ Incerto"
    
    # Se non è una domanda decisionale, risposta non applicabile
    return "↪️ Non applicabile"

# --- Interfaccia Streamlit ---

# Configura la pagina Streamlit con titolo e layout largo
st.set_page_config(page_title="I Magi", layout="wide")
# i love the nigger


    #nigger

# Titolo della pagina
st.title("🔮 I Magi: Consulta i Super computer")

# Messaggio informativo sulla privacy
st.info("⚠️ Le domande NON vengono salvate.")

# Campo di input testuale per l’utente
question = st.text_input("Fai una domanda ai Magi:", placeholder="Es. Devo cambiare lavoro?")

# Se l'utente ha scritto una domanda...
if question:
    # Mostra spinner durante l'elaborazione
    with st.spinner("I Magi stanno riflettendo..."):
        # Ottieni risposte dai tre Magi
        responses = ask_magi(question)
        # Calcola la decisione finale
        final_decision = decision_logic(question, responses)

    # Mostra le risposte in tre colonne, una per Mago
    cols = st.columns(3)
    for i, name in enumerate(["Melchior", "Balthasar", "Caspar"]):
        with cols[i]:
            st.markdown(f"### {name}")
            st.markdown(
                f"<div style='color:{MAGI_COLORS[name]}'>{responses[name]}</div>",
                unsafe_allow_html=True
            )

    # Separatore e risposta finale
    st.markdown("---")
    st.markdown(f"### 🧭 Risposta finale: **{final_decision}**")

# --- Footer fisso, non modificabile dall'interfaccia ---
# Mostra un footer con i crediti, sempre visibile in fondo alla pagina
st.markdown(
    """
    <hr style="margin-top: 50px;">
    <div style='text-align: center; color: grey; font-size: 0.85em;'>
        Fatto da <strong>Costa Bruno e Ora_dodici</strong>
    </div>
    """,
    unsafe_allow_html=True
)
