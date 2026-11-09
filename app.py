
import streamlit as st

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Jessel Veril | Video Editor Portfolio",
    page_icon="🦋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# PERSONAL INFORMATION
# EDIT THESE DETAILS
# ==========================================

NAME = "Jessel Veril"
ROLE = "Video Editor & Creative Content Creator"

TAGLINE = "Turning ideas into engaging visual stories."

EMAIL = "yourname@email.com"

LOCATION = "Philippines"

ABOUT = """
Hello! I'm Jessel, an aspiring Video Editor and Creative
Content Creator who enjoys turning ideas into engaging
visual content.

I enjoy working on short-form videos, creative advertisements,
and AI-assisted content. I'm continuously improving my
editing skills and exploring new ways to make videos
more engaging, polished, and visually appealing.

I'm open to learning, collaboration, and opportunities
to grow through creative projects.
"""

# Add your actual social media links
INSTAGRAM = ""
FACEBOOK = ""
TIKTOK = ""


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(
        135deg,
        #f7f8ff 0%,
        #eff2ff 50%,
        #f7f2ff 100%
    );
    color: #46516f;
    font-family: 'Poppins', sans-serif;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: #e3eaff;
    border-right: 1px solid #d5def5;
}

[data-testid="stSidebar"] h1 {
    color: #7089c4 !important;
}

[data-testid="stSidebar"] p {
    color: #68799d;
}

/* HEADINGS */
h1, h2, h3 {
    color: #718bc5 !important;
}

h1 {
    font-weight: 700;
    letter-spacing: -1px;
}

h2, h3 {
    font-weight: 600;
}

/* HERO */
.hero {
    background: linear-gradient(
        120deg,
        #dceaff,
        #e9e2fa,
        #f4eaff
    );
    padding: 75px 30px;
    border-radius: 30px;
    text-align: center;
    border: 1px solid white;
    box-shadow: 0 8px 30px rgba(130, 150, 200, 0.13);
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 48px;
    margin: 15px 0;
}

.hero h3 {
    color: #9582bd !important;
    font-weight: 500;
}

.hero p {
    color: #63749b;
    font-size: 17px;
}

.eyebrow {
    color: #9a89c7;
    font-size: 12px;
    letter-spacing: 3px;
    font-weight: 700;
}

/* CARDS */
.portfolio-card {
    background: rgba(255,255,255,0.92);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #e4e8f5;
    box-shadow: 0 5px 20px rgba(130,150,200,0.10);
    margin-bottom: 18px;
    min-height: 140px;
}

.portfolio-card h3 {
    color: #8c7db9 !important;
}

.portfolio-card p {
    color: #68748f;
    line-height: 1.8;
}

/* BUTTONS */
.stButton > button {
    background: #8da9df;
    color: white;
    border: none;
    border-radius: 25px;
    padding: 10px 25px;
    transition: 0.3s;
}

.stButton > button:hover {
    background: #a18bce;
    color: white;
    border: none;
}

/* LINKS */
a {
    color: #718bc5 !important;
}

/* DIVIDERS */
hr {
    border-color: #dce3f3;
}

/* FOOTER */
.footer {
    text-align: center;
    padding: 30px;
    color: #8793b0;
    font-size: 13px;
}

/* RESPONSIVE */
@media(max-width: 768px) {
    .hero {
        padding: 40px 15px;
    }

    .hero h1 {
        font-size: 32px;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

with st.sidebar:

    st.markdown("# 🦋 Jessel.")

    st.caption("VIDEO EDITOR PORTFOLIO")

    st.divider()

    page = st.radio(
        "EXPLORE",
        [
            "Home",
            "About Me",
            "Services",
            "Portfolio",
            "Skills & Tools",
            "Experience",
            "Contact"
        ]
    )

    st.divider()

    st.markdown(
        f"""
        <div style="text-align:center;">
            <p>Creative mind. Visual stories.</p>
            <small>© 2026 {NAME}</small>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# HOME
# ==========================================

if page == "Home":

   
        st.html("""
    <div class="hero">
        <div class="eyebrow">
            VIDEO EDITOR • CREATIVE CONTENT
        </div>

        <h1>Hi, I'm Jessel! ♡</h1>

        <h3>Video Editor & Creative Content Creator</h3>

        <p>
            Turning ideas into engaging visual stories.
        </p>
    </div>
    """)
    unsafe_allow_html=True)

    col1, col2 = st.columns([1.3, 1])

    with col1:

        st.markdown(
            '<div class="eyebrow">WELCOME TO MY CREATIVE SPACE</div>',
            unsafe_allow_html=True
        )

        st.title("Let's Create Something Amazing.")

        st.write("""
        I create and explore engaging video content,
        short-form advertisements, and creative visual stories.

        I'm passionate about learning new editing techniques,
        experimenting with creative concepts, and bringing
        ideas to life through video.
        """)

        st.info("Creative ideas deserve beautiful execution. 💙")

        st.markdown("**Currently exploring:**")

        st.write(
            "🎬 Short-form video editing\n\n"
            "✨ AI-assisted video production\n\n"
            "🎨 Creative visual storytelling"
        )

    with col2:

        st.image(
            "https://placehold.co/600x650/e3eaff/718bc5?text=Your+Profile+Photo",
            use_container_width=True
        )

    st.divider()

    st.subheader("What I Create")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="portfolio-card">
            <h3>🎬 Video Editing</h3>
            <p>
            Engaging short-form videos with
            creative cuts, transitions, and captions.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="portfolio-card">
            <h3>📱 Social Media Content</h3>
            <p>
            Creative video content designed
            for digital platforms and audiences.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class="portfolio-card">
            <h3>✨ AI Content Creation</h3>
            <p>
            Exploring AI-assisted advertisements
            and visual storytelling.
            </p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# ABOUT ME
# ==========================================

elif page == "About Me":

    st.markdown(
        '<div class="eyebrow">A LITTLE ABOUT MYSELF</div>',
        unsafe_allow_html=True
    )

    st.title("Get to Know Me ♡")

    st.write(ABOUT)

    st.divider()

    st.subheader("My Creative Approach")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="portfolio-card">
            <h3>🎯 Attention to Detail</h3>
            <p>
            I value clean editing, proper timing,
            visual consistency, and smooth transitions.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="portfolio-card">
            <h3>🌷 Creativity</h3>
            <p>
            I enjoy exploring fresh concepts
            and different editing styles.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="portfolio-card">
            <h3>🤝 Adaptability</h3>
            <p>
            I am willing to learn new tools,
            follow instructions, and accept feedback.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="portfolio-card">
            <h3>💙 Commitment</h3>
            <p>
            I value responsibility, communication,
            and continuous improvement.
            </p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# SERVICES
# ==========================================

elif page == "Services":

    st.markdown(
        '<div class="eyebrow">WHAT I CAN HELP CREATE</div>',
        unsafe_allow_html=True
    )

    st.title("My Services 🎬")

    services = [
        (
            "🎬",
            "Short-Form Video Editing",
            "Editing engaging vertical videos for TikTok, "
            "Instagram Reels, and YouTube Shorts."
        ),
        (
            "📢",
            "UGC-Style Advertisements",
            "Creating creative advertisement edits "
            "and product-focused visual content."
        ),
        (
            "✨",
            "AI-Assisted Video Content",
            "Exploring AI-generated scenes, "
            "creative concepts, and video production."
        ),
        (
            "💬",
            "Captions & Subtitles",
            "Adding readable captions, text overlays, "
            "and properly timed subtitles."
        ),
        (
            "🎨",
            "Creative Video Design",
            "Applying visual elements, transitions, "
            "and aesthetic editing styles."
        ),
        (
            "📱",
            "Social Media Content",
            "Preparing videos in vertical formats "
            "suitable for social media platforms."
        )
    ]

    for i in range(0, len(services), 2):

        col1, col2 = st.columns(2)

        for col, item in zip(
            [col1, col2],
            services[i:i+2]
        ):

            with col:

                icon, title, description = item

                st.markdown(
                    f"""
                    <div class="portfolio-card">
                        <h3>{icon} {title}</h3>
                        <p>{description}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# ==========================================
# PORTFOLIO
# ==========================================

elif page == "Portfolio":

    st.markdown(
        '<div class="eyebrow">SELECTED CREATIVE WORKS</div>',
        unsafe_allow_html=True
    )

    st.title("My Video Portfolio")

    st.write("""
    A collection of creative video projects,
    advertisement concepts, and editing samples.
    """)

    st.info(
        "Replace these sample projects with your actual "
        "video samples before sharing your portfolio."
    )

    projects = [

        {
            "title": "UGC Advertisement",
            "category": "Product Advertising",
            "description": "A short-form product advertisement concept.",
            "video": ""
        },

        {
            "title": "AI Creative Advertisement",
            "category": "AI Video Production",
            "description": "An AI-assisted visual storytelling project.",
            "video": ""
        },

        {
            "title": "Social Media Video",
            "category": "Short-Form Content",
            "description": "A creative video designed for social media.",
            "video": ""
        },

        {
            "title": "Product Video Editing",
            "category": "Commercial Editing",
            "description": "A product-focused video editing sample.",
            "video": ""
        }
    ]

    col1, col2 = st.columns(2)

    for index, project in enumerate(projects):

        current_col = col1 if index % 2 == 0 else col2

        with current_col:

            st.markdown(
                f"""
                <div class="portfolio-card">
                    <div class="eyebrow">
                        {project["category"]}
                    </div>
                    <h3>{project["title"]}</h3>
                    <p>{project["description"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if project["video"]:

                st.video(project["video"])

            else:

                st.caption(
                    "Your video preview will appear here."
                )


# ==========================================
# SKILLS & TOOLS
# ==========================================

elif page == "Skills & Tools":

    st.markdown(
        '<div class="eyebrow">MY CREATIVE TOOLKIT</div>',
        unsafe_allow_html=True
    )

    st.title("Skills & Tools")

    st.subheader("Editing Skills")

    skills = [
        "Video Cutting & Trimming",
        "Transitions & Effects",
        "Text Overlays & Captions",
        "Basic Color Adjustments",
        "Audio Synchronization",
        "Short-Form Video Formatting",
        "Creative Storytelling"
    ]

    for skill in skills:

        st.markdown(
            f"""
            <div class="portfolio-card"
                 style="min-height:55px;padding:15px 20px;">
                <p>✦ {skill}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("Software & Tools")

    tools = [
        ("🎬", "CapCut PC"),
        ("🎨", "Canva"),
        ("✨", "Google Flow"),
        ("🤖", "AI Creative Tools")
    ]

    cols = st.columns(4)

    for col, item in zip(cols, tools):

        with col:

            icon, name = item

            st.markdown(
                f"""
                <div class="portfolio-card"
                     style="text-align:center;">
                    <h3>{icon}</h3>
                    <p><b>{name}</b></p>
                </div>
                """,
                unsafe_allow_html=True
            )


# ==========================================
# EXPERIENCE
# ==========================================

elif page == "Experience":

    st.markdown(
        '<div class="eyebrow">MY BACKGROUND</div>',
        unsafe_allow_html=True
    )

    st.title("Experience & Background")

    st.markdown("""
    <div class="portfolio-card">
        <h3>🎬 Creative Video Projects</h3>
        <p>
        Exploring short-form advertisements,
        AI-assisted video concepts, and
        social media content creation.
        </p>
    </div>

    <div class="portfolio-card">
        <h3>💼 Student Work Immersion</h3>
        <p>
        Gained practical workplace experience
        involving sales support, inventory encoding,
        documentation, and event assistance.
        </p>
    </div>

    <div class="portfolio-card">
        <h3>🌷 Continuous Learning</h3>
        <p>
        Developing editing skills by practicing,
        exploring creative tools, and learning
        different approaches to video production.
        </p>
    </div>
    """, unsafe_allow_html=True)



# ==========================================
# CONTACT
# ==========================================

elif page == "Contact":

    st.markdown(
        """<div class="eyebrow">LET'S WORK TOGETHER</div>""",
        unsafe_allow_html=True
    )

    st.title("Get in Touch 💌")

    st.write("""
    Have a creative project or an opportunity in mind?

    I'd be happy to connect and discuss how I can help.
    """)

    st.markdown(
        f"""
        <div class="portfolio-card">
            <h3>📧 Email Me</h3>
            <p>{EMAIL}</p>
            <a href="mailto:{EMAIL}">
                Send an Email →
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Find Me Online")

    if INSTAGRAM:
        st.markdown(f"[Instagram Profile]({INSTAGRAM})")

    if FACEBOOK:
        st.markdown(f"[Facebook Profile]({FACEBOOK})")

    if TIKTOK:
        st.markdown(f"[TikTok Profile]({TIKTOK})")

    if not any([INSTAGRAM, FACEBOOK, TIKTOK]):
        st.caption(
            "Your social media links will appear here once added."
        )



# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown("""
<div class="footer">
    <p>Creating with passion. Editing with purpose. ♡</p>
    <p>© 2026 Jessel Veril | Video Editor Portfolio</p>
    <p>Designed with Python & Streamlit 🦋</p>
</div>
""", unsafe_allow_html=True)
