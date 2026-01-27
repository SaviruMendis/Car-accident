import streamlit as st
import pandas as pd
import joblib
# ======================================================
# 1. PAGE CONFIGURATION
# ======================================================
st.set_page_config(
    page_title="SafeRoad | National Risk Estimator",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======================================================
# 2. CUSTOM CSS (THE "PROPER WEBPAGE" STYLING)
# ======================================================
st.markdown("""
<style>
    /* RESET AND BASICS */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1e293b;
    }
    
    /* Remove standard Streamlit padding/headers */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 5rem !important;

        /* THIS is the fix */
        padding-left: 2rem !important;
        padding-right: 2rem !important;

        max-width: 1200px;
        margin: 0 auto;
    }

    header {visibility: hidden;}
    footer {
    background-color: #ffffff;
    border-top: 1px solid #e5e7eb;
}
    
    h1, h2, h3 {
    letter-spacing: -0.02em;
    }
    
    /* HERO SECTION */
    .hero-section {
        background: linear-gradient(180deg, #0b1220 0%, #111827 100%);
        padding: 6rem 2rem;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        margin-left: -2rem;
        margin-right: -2rem;
    }
    .hero-title {
        font-size: 3.2rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .hero-subtitle {
        font-size: 1.25rem;
        color: #cbd5e1;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.6;
    }

    /* SECTION CONTAINERS */
    .content-container {
        max-width: 1100px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    .section-header {
        text-align: center;
        margin-top: 4rem;
        margin-bottom: 2rem;
        font-size: 2rem;
        font-weight: 600;
    }
    .section-header h2 {
        font-size: 2.2rem;
        font-weight: 600;
        color: #0f172a;
    }
    .section-header p {
        color: #64748b;
        font-size: 1.1rem;
    }

    /* CARDS FOR "HOW TO USE" */
    .step-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        height: 100%;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s;
    }
    .step-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .step-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
    }

    /* CALCULATOR FORM STYLING */
    .form-container {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 3rem;
        margin-top: 2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    
    .stButton > button {
        width: 100%;
        background-color: #1e40af;
        color: white;
        font-weight: 600;
        font-size: 0.95rem;
        padding: 0.75rem 1rem;
        border-radius: 6px;
        border: none;
        margin-top: 1.5rem;
        letter-spacing: 0.02em;
    }
    .stButton > button:hover {
        background-color: #1d4ed8;
        border: none;
    }
    
    /* PREDICTION BOX */
    .result-box {
        margin-top: 2rem;
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        animation: fadeIn 0.5s ease-in;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(10px);}
        to {opacity: 1; transform: translateY(0);}
    }

</style>
""", unsafe_allow_html=True)

# ======================================================
# 3. LOAD MODEL
# ======================================================
@st.cache_resource
def load_model():
    try:
        return joblib.load("linear_model.pkl")
    except FileNotFoundError:
        return None

pipeline = load_model()

# ======================================================
# 4. HERO SECTION (HTML INJECTION)
# ======================================================
st.markdown("""
<div class="hero-section">
    <div class="hero-title">SafeRoad Predictor</div>
    <div class="hero-subtitle">
        An AI-powered assessment tool for national road safety. 
        Analyze environmental, infrastructural, and temporal factors to estimate accident risks instantly.
    </div>
</div>
""", unsafe_allow_html=True)

# ======================================================
# 5. INTRODUCTION & CONTEXT
# ======================================================
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# Image tag for context
st.write("")

st.markdown("""
<div style="margin-top: 2rem; font-size: 1.1rem; line-height: 1.7; color: #334155;">
    <p>
        <strong>Understanding road risk is the first step toward prevention.</strong> 
        Road accidents are rarely caused by a single factor. They are the result of complex interactions between 
        weather conditions, road infrastructure (curvature, lanes), and human temporal factors (time of day, holidays).
    </p>
    <p>
        This tool aggregates historical traffic data to provide a <strong>Risk Index Score (0.0 - 1.0)</strong>. 
        Civil engineers, policy planners, and safety inspectors can use this simplified interface to model 
        hypothetical scenarios and prioritize safety interventions.
    </p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# 6. HOW TO USE (3-COLUMN LAYOUT)
# ======================================================
st.markdown("""
<div class="section-header">
    <h2>How It Works</h2>
    <p>Three simple steps to generate a risk assessment</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="step-card">
        <span class="step-icon">📝</span>
        <h3>1. Configure</h3>
        <p>Input the road characteristics, including infrastructure type, lane count, and curvature.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="step-card">
        <span class="step-icon">🌤️</span>
        <h3>2. Set Conditions</h3>
        <p>Adjust environmental factors such as weather, lighting, and time of day.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="step-card">
        <span class="step-icon">📊</span>
        <h3>3. Analyze</h3>
        <p>Our algorithm processes the variables and returns an immediate risk probability index.</p>
    </div>
    """, unsafe_allow_html=True)


# ======================================================
# 7. THE CALCULATOR (FORM)
# ======================================================
st.markdown("""
<div class="section-header">
    <hr style="border: none; height: 1px; background: #e5e7eb; margin: 4rem 0;">
    <h2>Risk Calculator</h2>
    <p>Enter the scenario details below</p>
</div>
""", unsafe_allow_html=True)

# We use a container to wrap the form with a white background/border (CSS class: form-container)
with st.container():
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    # --- FORM INPUTS START ---
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("### 🛣️ Infrastructure")
        road_type = st.selectbox("Road Type", ["Urban", "Rural", "Highway"])
        num_lanes = st.slider("Number of Lanes", 1, 4, 2)
        curvature = st.slider("Curvature (0=Straight, 1=Sharp)", 0.0, 1.0, 0.2)
        public_road = st.toggle("Public Road", True)

    with c2:
        st.markdown("### 🌦️ Environment")
        weather = st.selectbox("Weather", ["clear", "rainy", "foggy"])
        lighting = st.selectbox("Lighting", ["daylight", "night"])
        time_of_day = st.selectbox("Time of Day", ["morning", "afternoon", "evening", "night"])

    with c3:
        st.markdown("### ⚠️ Risk Factors")
        high_speed = st.toggle("High Speed (>45 km/h)")
        road_signs = st.toggle("Road Signs Present", True)
        school_season = st.toggle("School Season")
        holiday = st.toggle("Holiday")

    st.markdown("---")
    
    # Calculate Button centered using columns
    b1, b2, b3 = st.columns([1, 2, 1])
    with b2:
        calculate_btn = st.button("CALCULATE RISK SCORE")

    # --- LOGIC & OUTPUT ---
    if calculate_btn:
        if pipeline is None:
            st.error("⚠️ Model file 'linear_model.pkl' not found. Please ensure the file is in the directory.")
        else:
            # Prepare Input
            input_data = pd.DataFrame({
                "road_type": [road_type],
                "weather": [weather],
                "lighting": [lighting],
                "time_of_day": [time_of_day],
                "road_signs_present": [road_signs],
                "high_speed": [high_speed],
                "school_season": [school_season],
                "holiday": [holiday],
                "public_road": [public_road],
                "curvature": [curvature],
                "num_lanes": [num_lanes]
            })

            # Predict
            try:
                prediction = pipeline.predict(input_data)[0]
                
                # Logic for display styling
                if prediction > 0.5:
                    bg_color = "#fef2f2" # Light Red
                    border_color = "#ef4444" # Red
                    text_color = "#b91c1c"
                    status = "CRITICAL RISK DETECTED"
                    icon = "🛑"
                elif prediction > 0.2:
                    bg_color = "#fff7ed" # Light Orange
                    border_color = "#f97316" # Orange
                    text_color = "#c2410c"
                    status = "ELEVATED RISK"
                    icon = "⚠️"
                else:
                    bg_color = "#f0fdf4" # Light Green
                    border_color = "#22c55e" # Green
                    text_color = "#15803d"
                    status = "LOW RISK ENVIRONMENT"
                    icon = "✅"

                # Result Display HTML
                st.markdown(f"""
                <div class="result-box" style="background-color: {bg_color}; border: 2px solid {border_color};">
                    <h3 style="color: {text_color}; margin: 0;">{icon} {status}</h3>
                    <h1 style="font-size: 4rem; margin: 10px 0; color: #0f172a;">{prediction:.4f}</h1>
                    <p style="color: #64748b;">Predicted Risk Probability Index</p>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error during calculation: {e}")

    st.markdown('</div>', unsafe_allow_html=True) # End form container

# Close main content container
st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# 8. FOOTER
# ======================================================
st.markdown("""
<div style="text-align: center; padding: 3rem; background-color: #f1f5f9; color: #94a3b8; margin-top: 4rem;">
    <p>&copy; 2026 National Road Safety Division. All rights reserved.</p>
    <p style="font-size: 0.85rem;">
</div>
""", unsafe_allow_html=True)