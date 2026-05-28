import streamlit as st
import os

# Configurazione della pagina
st.set_page_config(
    page_title="Erasmus+ Portogallo - Liceo G. Berto",
    page_icon="🇵🇹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS PERSONALIZZATO PER EFFETTO LIQUID GLASS E COLORI DEL PORTOGALLO ---
st.markdown("""
    <style>
    /* Sfondo globale con sfumatura morbida ispirata ai colori del Portogallo (verde, rosso cupo, accenni d'oro) */
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
        border-bottom: 2px solid rgba(212, 175, 55, 0.4); /* Linea dorata sfumata */
        padding-bottom: 10px;
    }
    
    .glass-card h2 {
        color: #ffd700; /* Oro per i sottotitoli istituzionali */
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
    <div class="glass-card" style="text-align: center; padding: 20px; margin-bottom: 30px;">
        <p style="letter-spacing: 2px; font-size: 14px; color: #ffd700; margin-bottom: 5px; font-weight: 600;">
            MINISTERO DELL'ISTRUZIONE E DEL MERITO
        </p>
        <h2 style="margin: 0; color: #ffffff; font-size: 26px; font-weight: 700;">
            LICEO SCIENTIFICO STATALE "G. BERTO"
        </h2>
        <p style="font-size: 14px; color: #e9ecef; margin-top: 2px;">Vibo Valentia (VV)</p>
        <h1 style="font-size: 36px; margin-top: 15px; color: #ffffff; border-bottom: none; padding-bottom: 0;">
            Programma Erasmus+ • Mobilità Portogallo
        </h1>
    </div>
""", unsafe_allow_html=True)

# --- CREAZIONE DELLE TAB NAVIGAZIONALI ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Home / Presentazione", 
    "📋 Il Progetto", 
    "🗺️ Diario di Bordo", 
    "📸 Galleria Fotografica", 
    "🌟 Impatto & Competenze"
])

# --- TAB 1: HOME / PRESENTAZIONE ---
with tab1:
    st.markdown("""
        <div class="glass-card">
            <h1>Benvenuti nel Report Multimediale</h1>
            <p style="font-size: 18px; line-height: 1.6;">
                Questo spazio istituzionale è dedicato alla documentazione e alla valorizzazione dell'esperienza 
                di mobilità internazionale promossa dal programma <b>Erasmus+</b>, che ha visto la partecipazione 
                degli studenti del Liceo Scientifico "G. Berto" presso la suggestiva cornice di <b>Coimbra, Portogallo</b>, 
                nel mese di <b>Marzo 2026</b>.
            </p>
            <p style="font-size: 18px; line-height: 1.6;">
                Attraverso questo portale, strutturato secondo i criteri di trasparenza e disseminazione dei progetti europei, 
                è possibile ripercorrere le tappe fondamentali del viaggio, gli obiettivi didattici raggiunti e l'impatto 
                formativo che l'esperienza ha generato sul percorso di crescita studentesca.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card" style="border-left: 5px solid #ffd700; background: rgba(255,255,255,0.04);">
            <h2>Il Pensiero</h2>
            <p style="font-style: italic; font-size: 20px; line-height: 1.6; color: #f1f3f5;">
                "L'Erasmus non è semplicemente un viaggio di studio, ma un'immersione profonda in un mare di nuove prospettive. 
                Camminare tra la storia millenaria di Coimbra e confrontarsi ogni giorno con contesti e compagni da tutta Europa 
                mi ha insegnato che i confini esistono solo sulle mappe geografiche. La vera crescita nasce dalla condivisione, 
                dalla capacità di adattarsi e dallo scoprire che le nostre differenze sono la risorsa più grande per costruire 
                un futuro comune."
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 2: IL PROGETTO ---
with tab2:
    st.markdown("""
        <div class="glass-card">
            <h1>Quadro Progettuale ed Obiettivi</h1>
            <h2>L'Iniziativa Europea</h2>
            <p style="font-size: 16px; line-height: 1.6;">
                Il progetto si colloca all'interno delle azioni chiave del programma Erasmus+, volte a favorire 
                la mobilità transnazionale degli studenti della scuola secondaria superiore. L'obiettivo principale 
                è lo sviluppo di competenze chiave europee, l'inclusione sociale, la sostenibilità e la comprensione 
                delle dinamiche interculturali.
            </p>
            <h2>Macro-Obiettivi Formativi:</h2>
            <ul style="font-size: 16px; line-height: 1.7; color: #f8f9fa;">
                <li><b>Potenziamento Linguistico:</b> Utilizzo pratico e immersivo della lingua inglese come strumento di comunicazione ed apprendimento comune.</li>
                <li><b>Cittadinanza Attiva:</b> Consapevolezza della propria identità europea attraverso il confronto diretto con la cultura, le leggi e le tradizioni del paese ospitante.</li>
                <li><b>Soft Skills:</b> Incremento dello spirito d'iniziativa, della capacità di problem solving in contesti non familiari e dell'autonomia personale lontano dall'ambiente domestico.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 3: DIARIO DI BORDO ---
with tab3:
    st.markdown("""
        <div class="glass-card">
            <h1>Le Attività e l'Itinerario Culturale</h1>
            <p style="font-size: 16px; line-height: 1.6;">
                La mobilità ha saputo coniugare rigorosi momenti di formazione a una fitta agenda di scambi culturali, 
                aventi come fulcro la città di Coimbra, celebre per la sua prestigiosa tradizione universitaria e storica.
            </p>
            
            <h2>🏛️ Visite Culturali Fondamentali</h2>
            <p style="font-size: 16px; line-height: 1.6;">
                Il percorso antropico e storico ha previsto l'esplorazione critica del patrimonio locale. Dalle storiche 
                mura dell'Università di Coimbra (Patrimonio UNESCO) fino ai vicoli della città vecchia, ogni visita è stata 
                strutturata come un laboratorio a cielo aperto per comprendere le radici culturali e scientifiche che legano 
                la penisola iberica al resto del continente.
            </p>
            
            <h2>👥 Attività di Gruppo e Cooperative Learning</h2>
            <p style="font-size: 16px; line-height: 1.6;">
                Il cuore didattico della mobilità si è sviluppato attraverso workshop collaborativi. Gli studenti, divisi in 
                team internazionali, hanno affrontato compiti di realtà e project work focalizzati sulla condivisione di buone 
                pratiche scolastiche, l'analisi del territorio e lo sviluppo di idee innovative per la sostenibilità dei sistemi 
                scolastici europei.
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 4: GALLERIA FOTOGRAFICA ---
with tab4:
    st.markdown("""
        <div class="glass-card">
            <h1>Galleria della Mobilità</h1>
            <p style="font-size: 16px; margin-bottom: 20px;">
                Di seguito sono riportate le sezioni fotografiche dedicate ai tre soggetti principali dell'esperienza. 
                <i>(Sostituisci i file segnaposto nella cartella del progetto per visualizzare le tue foto reali).</i>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="glass-card" style="padding: 15px; text-align: center;"><h3>La Città Ospitante</h3>', unsafe_allow_html=True)
        if os.path.exists("foto_citta.jpg"):
            st.image("foto_citta.jpg", caption="Scorci storici di Coimbra", use_container_width=True)
        else:
            st.warning("Carica un'immagine nominata 'foto_citta.jpg' per vederla qui.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="glass-card" style="padding: 15px; text-align: center;"><h3>Il Gruppo</h3>', unsafe_allow_html=True)
        if os.path.exists("foto_gruppo.jpg"):
            st.image("foto_gruppo.jpg", caption="Il team del Liceo Berto in Portogallo", use_container_width=True)
        else:
            st.warning("Carica un'immagine nominata 'foto_gruppo.jpg' per vederla qui.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="glass-card" style="padding: 15px; text-align: center;"><h3>Le Attività</h3>', unsafe_allow_html=True)
        if os.path.exists("foto_attivita.jpg"):
            st.image("foto_attivita.jpg", caption="Momenti di workshop e visite culturali", use_container_width=True)
        else:
            st.warning("Carica un'immagine nominata 'foto_attivita.jpg' per vederla qui.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 5: IMPATTO PERSONALE & COMPETENZE ---
with tab5:
    st.markdown("""
        <div class="glass-card">
            <h1>Impatto e Competenze Acquisite</h1>
            <h2>Bilancio delle Competenze (Europass Mobility)</h2>
            <p style="font-size: 16px; line-height: 1.6;">
                In coerenza con gli standard europei di trasparenza delle qualifiche, l'esperienza ha permesso 
                la maturazione e la validazione di specifiche competenze trasversali (soft skills), formalmente riconosciute 
                nel contesto del percorso scolastico:
            </p>
            
            <table style="width:100%; border-collapse: collapse; margin-top: 15px; font-size: 16px;">
                <tr style="background: rgba(255,255,255,0.1); border-bottom: 2px solid rgba(255,255,255,0.2);">
                    <th style="padding: 12px; text-align: left; color: #ffd700;">Area di Competenza</th>
                    <th style="padding: 12px; text-align: left; color: #ffd700;">Evidenze ed Abilità Sviluppate</th>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 12px; font-weight: bold;">Comunicazione Interculturale</td>
                    <td style="padding: 12px;">Capacità di interagire efficacemente in contesti multilingue, superando barriere culturali ed esprimendo idee complesse in lingua inglese.</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 12px; font-weight: bold;">Spirito di Adattamento</td>
                    <td style="padding: 12px;">Gestione autonoma delle routine quotidiane e logistiche in un contesto internazionale, dimostrando flessibilità e resilienza.</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 12px; font-weight: bold;">Team Working Transnazionale</td>
                    <td style="padding: 12px;">Cooperazione all'interno di gruppi di lavoro eterogenei per il raggiungimento di obiettivi progettuali comuni durante i workshop.</td>
                </tr>
            </table>
        </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div style="text-align: center; margin-top: 40px; padding: 20px; color: rgba(255,255,255,0.5); font-size: 12px;">
        © 2026 Liceo Scientifico Statale "G. Berto" - Progetto Erasmus+ Portogallo. Tutti i diritti riservati.<br>
        Sito sviluppato con framework Streamlit & Custom Glassmorphism Engine.
    </div>
""", unsafe_allow_html=True)
