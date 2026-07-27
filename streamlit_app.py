import streamlit as st
import streamlit.components.v1 as components
import requests
import base64
from pathlib import Path
import datetime

# ==========================
# Backend URL
# ==========================

BASE_URL = "http://localhost:8000"

# ==========================
# Page Config
# ==========================

st.set_page_config(
    page_title="AI Trip Planner",
    page_icon="✈️",
    layout="wide"
)

# ==========================
# Load CSS
# ==========================

def load_css():

    css_path = Path("frontend/styles.css")

    with open(css_path, "r", encoding="utf-8") as f:

        return f.read()


# ==========================
# Convert image to Base64
# ==========================

def image_to_base64(image_path):

    with open(image_path, "rb") as img:

        return base64.b64encode(img.read()).decode()


# ==========================
# Display Gallery
# ==========================

def display_gallery():

    # Load HTML

    with open(
        "frontend/gallery.html",
        "r",
        encoding="utf-8"
    ) as f:

        html = f.read()

    # Inject CSS

    css = load_css()

    html = html.replace(
        "</head>",
        f"<style>{css}</style></head>"
    )

    # Load Images

    image_folder = Path("frontend/assets")

    image_files = sorted(
        image_folder.glob("travel*.jpg"),
        key=lambda x: int(x.stem.replace("travel", ""))
    )[:6]

    # Replace placeholders

    for i, image in enumerate(image_files, start=1):

        encoded = image_to_base64(image)

        html = html.replace(

            f"__IMAGE_{i}__",

            f"data:image/jpeg;base64,{encoded}"

        )

    # Show gallery

    components.html(
        html,
        height=700,
        scrolling=False,
    )


# ==========================
# Hero Title
# ==========================

st.markdown("""
<div style="text-align:center; margin-top:20px; margin-bottom:30px;">

<h1 style="
font-size:52px;
font-weight:700;
margin-bottom:10px;
color:#1F2937;">
✈️ AI Trip Planner
</h1>

<p style="
font-size:22px;
color:#6B7280;
margin:0;">
Plan Smarter. Travel Better.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# Gallery
# ==========================

display_gallery()

st.markdown("---")

# ==========================
# Query Form
# ==========================

with st.form(
    "trip_form",
    clear_on_submit=True
):

    question = st.text_input(

        "Where would you like to travel?",

        placeholder="Example: Plan a 7-day trip to Switzerland under $2500"

    )

    submitted = st.form_submit_button(
        "Generate Itinerary"
    )

# ==========================
# Backend Call
# ==========================

if submitted and question:

    with st.spinner("Bot is thinking..."):

        payload = {

            "question": question

        }

        response = requests.post(

            f"{BASE_URL}/query",

            json=payload

        )

    if response.status_code == 200:

        answer = response.json()["answer"]

        st.markdown("## Your Travel Plan")

        st.markdown(answer)

    else:

        st.error(response.text)

# ==========================
# Footer
# ==========================

st.markdown("---")

st.markdown(
    f"""
    <div style="
        text-align:center;
        margin-top:25px;
        margin-bottom:15px;
        color:#6B7280;
        font-size:15px;
    ">
        Generated on {datetime.datetime.now().strftime('%B %d, %Y %I:%M %p')}
    </div>
    """,
    unsafe_allow_html=True,
)