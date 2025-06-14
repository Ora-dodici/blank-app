# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
"""
Questo file implementa una web app con Streamlit chiamata **"I Tre Magi: Consulta i Saggi"**. L'app permette all'utente
di porre una domanda e ricevere tre risposte simulate da tre personaggi virtuali (i Magi), ciascuno con una propria
personalità distinta. Alla fine viene fornita una sintesi automatica della risposta complessiva.

Funzionalità principali:
- Tre personaggi (Melchior, Balthasar, Caspar) con caratteri e stili di risposta diversi:
    • Melchior: scienziato razionale e analitico
    • Balthasar: madre empatica e saggia
    • Caspar: donna pragmatica, visionaria e diretta
- Ogni personaggio risponde alla domanda dell'utente tramite il modello "gpt-4o-mini" di OpenAI, usando un prompt specifico.
- Una logica decisionale aggrega le risposte per fornire un verdetto finale (✅ SÌ, ❌ NO, ❓ Incerto).
- L'interfaccia utente è costruita con Streamlit, con stile personalizzato e colori per ciascun Mago.
- Sicurezza migliorata: la chiave API è caricata in modo sicuro da `st.secrets`.

Componenti principali del file:
1. Importazioni e configurazione API
2. Definizione dei prompt e colori dei Magi
3. Funzione `ask_magi(question)` per interagire con OpenAI
4. Funzione `decision_logic(question, answers)` per sintetizzare una risposta
5. Interfaccia grafica Streamlit: input utente, visualizzazione risposte, decisione finale
6. Footer fisso con crediti

Esempio d'uso:
- Domanda: "Devo cambiare lavoro?"
- I tre Magi rispondono secondo il loro stile
- L'app calcola e mostra una risposta complessiva come "✅ SÌ" o "❌ NO"

Autori: Costa Bruno e Ora_dodici
"""
