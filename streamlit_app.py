import streamlit as st
import os

# Configurazione della pagina
st.set_page_config(
    page_title="Il mio Erasmus in Portogallo",
    page_icon="🇵🇹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS PERSONALIZZATO PER EFFETTO LIQUID GLASS E COLORI DEL PORTOGALLO ---
st.markdown("""
<style>
/* Sfondo globale con sfumatura morbida ispirata ai colori del Portogallo */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #14361f 0%, #1e4629 30%, #5c1e1e 70%, #3a1010 100%);
    background-attachment: fixed;
}

/* Rende trasparente l'header superiore di Streamlit */
[data-testid="stHeader"] {
    background: transparent;
}

/* Stile per i contenitori Liquid Glass */
.glass-card {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
    padding: 30px;
    margin-bottom: 25px;
    color: #f8f9fa;
}

/* Stile per i titoli all'interno del vetro */
.glass-card h1 {
    color: #ffffff;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-weight: 700;
    border-bottom: 2px solid rgba(212, 175, 55, 0.4);
    padding-bottom: 10px;
}

.glass-card h2 {
    color: #ffd700;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-weight: 600;
    margin-top: 15px;
}

.glass-card h3 {
    color: #e9ecef;
    font-weight: 500;
}

/* Personalizzazione delle Tab istituzionali */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    background-color: rgba(0, 0, 0, 0.2);
    padding: 8px;
    border-radius: 12px;
}

.stTabs [data-baseweb="tab"] {
    height: 45px;
    white-space: pre-wrap;
    background-color: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    color: #ffffff !important;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 0px 20px;
}

.stTabs [data-baseweb="tab"]:hover {
    background-color: rgba(255, 255, 255, 0.15);
    border-color: rgba(212, 175, 55, 0.5);
}

.stTabs [aria-selected="true"] {
    background-color: rgba(255, 255, 255, 0.15) !important;
    border-color: #ffd700 !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ISTITUZIONALE ---
st.markdown("""
<div class="glass-card" style="text-align: center; padding: 25px; margin-bottom: 30px;">
<p style="letter-spacing: 2px; font-size: 20px; color: #ffd700; margin-bottom: 5px; font-weight: 600;">
Erasmus +
</p>
<h2 style="margin: 0; color: #ffffff; font-size: 26px; font-weight: 700;">
LICEO SCIENTIFICO STATALE "G. BERTO"
</h2>
<p style="font-size: 14px; color: #e9ecef; margin-top: 2px; margin-bottom: 12px;">Vibo Valentia (VV)</p>

<div style="display: inline-block; background: rgba(0, 0, 0, 0.25); padding: 8px 20px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 5px;">
<p style="margin: 0; font-size: 14px; color: #ffffff;">
🏫 In collaborazione con: <span style="color: #ffd700; font-weight: 600;">Agrupamento de Escolas de Santa Comba Dão AESCD</span>
</p>
</div>

<h1 style="font-size: 36px; margin-top: 15px; color: #ffffff; border-bottom: none; padding-bottom: 0;">
La mia esperienza con il progetto Erasmus+ • Mobilità Portogallo
</h1>
</div>
""", unsafe_allow_html=True)

# --- CREAZIONE DELLE TAB NAVIGAZIONALI ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Ciao! (Home)", 
    "📋 Perché sono partito", 
    "🗺️ Il mio Diario", 
    "📸 I miei Ricordi", 
    "🌟 Cosa mi porto a casa"
])

# --- TAB 1: HOME / PRESENTAZIONE ---
with tab1:
    st.markdown("""
<div class="glass-card">
<h1>Benvenuti nel mio Diario di Viaggio</h1>
<p style="font-size: 18px; line-height: 1.6;">
Ho creato questo spazio per raccontare e condividere la mia fantastica esperienza con il programma <b>Erasmus+</b>. 
Nel mese di <b>Marzo 2026</b> ho avuto l'incredibile opportunità di viaggiare in Portogallo, un'avventura che mi ha permesso di 
uscire dalla mia zona di comfort e di rappresentare il Liceo "G. Berto" all'estero.
</p>
<p style="font-size: 18px; line-height: 1.6;">
Attraverso le pagine di questo sito, voglio portarvi con me: vi mostrerò le tappe fondamentali del mio viaggio, gli obiettivi 
che mi ero prefissato e, soprattutto, come questa esperienza mi abbia fatto crescere sia come studente che come persona.
</p>
</div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
<div class="glass-card" style="border-left: 5px solid #ffd700; background: rgba(255,255,255,0.04);">
<h2>Il mio Pensiero</h2>
<p style="font-style: italic; font-size: 20px; line-height: 1.6; color: #f1f3f5;">
"L'Erasmus non è stato semplicemente un viaggio di studio, ma un'immersione profonda in un mare di nuove prospettive. 
Camminare tra le strade portoghesi e confrontarmi ogni giorno con contesti e ragazzi da tutta Europa mi ha insegnato 
che i confini esistono solo sulle mappe geografiche. Ho capito che la vera crescita nasce dalla condivisione e dalla 
capacità di adattarsi."
</p>
</div>
    """, unsafe_allow_html=True)

# --- TAB 2: IL PROGETTO ---
with tab2:
    st.markdown("""
<div class="glass-card">
<h1>I miei Obiettivi</h1>
<h2>Perché ho scelto di partecipare?</h2>
<p style="font-size: 16px; line-height: 1.6;">
Quando ho deciso di mettermi in gioco con l'Erasmus+, volevo vivere un'esperienza che andasse oltre la classica gita scolastica. 
Il mio obiettivo era mettermi alla prova in un contesto totalmente nuovo, conoscere persone di altre culture e capire 
cosa significa davvero sentirsi cittadini europei attivi.
</p>
<h2>Cosa mi ero prefissato:</h2>
<ul style="font-size: 16px; line-height: 1.7; color: #f8f9fa;">
<li><b>Migliorare il mio inglese:</b> Volevo sforzarmi di comunicare costantemente in una lingua diversa, usandola per fare amicizia e collaborare nei progetti.</li>
<li><b>Scoprire una nuova cultura:</b> Volevo immergermi nelle tradizioni, nel cibo e nello stile di vita portoghese, confrontandoli con i nostri.</li>
<li><b>Crescere in autonomia (Soft Skills):</b> Imparare a cavarmela da solo lontano da casa, migliorare la mia capacità di risolvere piccoli imprevisti e lavorare in un team internazionale.</li>
</ul>
</div>
    """, unsafe_allow_html=True)

# --- TAB 3: DIARIO DI BORDO ---
with tab3:
    st.markdown("""
<div class="glass-card">
<h1>Le mie giornate in Portogallo</h1>
<p style="font-size: 16px; line-height: 1.6;">
Il mio viaggio è stato un mix perfetto tra momenti di lavoro, laboratori scolastici e la scoperta di posti meravigliosi. 
Insieme ai compagni d'avventura (un saluto speciale a Nicole e Alessia che hanno condiviso con me questa esperienza!), abbiamo vissuto giornate intense e indimenticabili.
</p>

<h2>🏛️ I posti che ho visitato</h2>
<p style="font-size: 16px; line-height: 1.6;">
Camminare per i centri storici e ammirare il patrimonio locale è stato affascinante. Ogni visita non era solo 
una passeggiata turistica, ma un modo per comprendere le radici culturali che ci legano al resto del continente. 
Ho scattato decine di foto per ricordarmi ogni dettaglio!
</p>

<h2>👥 Il lavoro di squadra e i Workshop</h2>
<p style="font-size: 16px; line-height: 1.6;">
La parte più stimolante? Lavorare con i ragazzi portoghesi e degli altri paesi. Divisi in team, abbiamo affrontato 
compiti di realtà e project work. Non è stato sempre facile capirsi subito, ma collaborare per trovare idee innovative 
sulla sostenibilità e scambiarci opinioni sul nostro modo di vivere la scuola è stato illuminante.
</p>
</div>
    """, unsafe_allow_html=True)

# --- TAB 4: GALLERIA FOTOGRAFICA ---
with tab4:
    st.markdown("""
<div class="glass-card">
<h1>I miei Ricordi Fotografici</h1>
<p style="font-size: 16px; margin-bottom: 20px;">
Ecco alcuni degli scatti a cui tengo di più. Un'immagine vale più di mille parole per raccontare i posti che ho visto 
e le persone fantastiche che ho incontrato.
</p>
</div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="glass-card" style="padding: 15px; text-align: center;"><h3>I luoghi che ho amato</h3>', unsafe_allow_html=True)
        if os.path.exists("foto_citta.jpg"):
            st.image("foto_citta.jpg", caption="Scorci indimenticabili del Portogallo", use_container_width=True)
        else:
            st.warning("Carica un'immagine nominata 'foto_citta.jpg' per vederla qui.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="glass-card" style="padding: 15px; text-align: center;"><h3>Io e il gruppo</h3>', unsafe_allow_html=True)
        if os.path.exists("foto_gruppo.jpg"):
            st.image("foto_gruppo.jpg", caption="La mia 'famiglia' Erasmus", use_container_width=True)
        else:
            st.warning("Carica un'immagine nominata 'foto_gruppo.jpg' per vederla qui.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="glass-card" style="padding: 15px; text-align: center;"><h3>Al lavoro!</h3>', unsafe_allow_html=True)
        if os.path.exists("foto_attivita.jpg"):
            st.image("foto_attivita.jpg", caption="Momenti durante i workshop", use_container_width=True)
        else:
            st.warning("Carica un'immagine nominata 'foto_attivita.jpg' per vederla qui.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 5: IMPATTO PERSONALE & COMPETENZE ---
with tab5:
    st.markdown("""
<div class="glass-card">
<h1>Come sono cambiato</h1>
<h2>Le mie nuove competenze (Europass Mobility)</h2>
<p style="font-size: 16px; line-height: 1.6;">
Se guardo indietro a prima di partire, mi rendo conto di quante cose ho imparato a fare senza nemmeno accorgermene. 
Questa esperienza mi ha permesso di sviluppare abilità che nessun libro di testo avrebbe potuto insegnarmi così bene:
</p>

<table style="width:100%; border-collapse: collapse; margin-top: 15px; font-size: 16px;">
    <tr style="background: rgba(255,255,255,0.1); border-bottom: 2px solid rgba(255,255,255,0.2);">
        <th style="padding: 12px; text-align: left; color: #ffd700;">In cosa sono migliorato</th>
        <th style="padding: 12px; text-align: left; color: #ffd700;">Cosa ho imparato a fare concretamente</th>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
        <td style="padding: 12px; font-weight: bold;">Comunicare in lingua straniera</td>
        <td style="padding: 12px;">Ho superato la timidezza di parlare in inglese, riuscendo a esprimere le mie idee e a scherzare con ragazzi di altre nazionalità.</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
        <td style="padding: 12px; font-weight: bold;">Spirito di Adattamento</td>
        <td style="padding: 12px;">Ho imparato a gestire i miei tempi, gli spostamenti e le routine quotidiane in un paese che non conoscevo, diventando molto più indipendente.</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
        <td style="padding: 12px; font-weight: bold;">Lavoro di Squadra</td>
        <td style="padding: 12px;">Ho capito come collaborare in un gruppo eterogeneo, ascoltando le idee degli altri e trovando compromessi per portare a termine i progetti.</td>
    </tr>
</table>
</div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; margin-top: 40px; padding: 20px; color: rgba(255,255,255,0.5); font-size: 12px;">
© 2026 Liceo Scientifico Statale "G. Berto" - Progetto Erasmus+ Portogallo.<br>
Sito interamente sviluppato e raccontato da Antonio Mazza 2AQ.
</div>
""", unsafe_allow_html=True)
