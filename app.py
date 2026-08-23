import streamlit as st

from project import app


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="💼",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.hero {
    text-align: center;
    padding: 20px 0 30px 0;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 5px;
}

.hero p {
    font-size: 18px;
    color: #6b7280;
}

.post-card {
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #ddd;
    background-color: #fafafa;
    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="hero">

<h1>💼 LinkedIn Post Generator</h1>

<p>
AI-powered LinkedIn content creation with
iterative review and refinement
</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("🔄 Workflow")

    st.markdown("""
    **1. 🧠 Writer**

    Mistral creates the post.

    **2. 🔎 Research**

    Tavily provides fresh information when needed.

    **3. 🧐 Reviewer**

    Groq evaluates the draft.

    **4. ✍️ Refinement**

    Rejected posts are rewritten.

    **5. ✅ Final Post**

    The best version is returned.
    """)

    st.divider()

    st.caption(
        "Powered by LangGraph • Mistral • Groq • Tavily"
    )


# --------------------------------------------------
# INPUT
# --------------------------------------------------

st.subheader("📝 What should your LinkedIn post be about?")

topic = st.text_area(
    "Enter your topic",
    placeholder="Example: Is machine learning really dead?",
    height=120
)


# --------------------------------------------------
# GENERATE
# --------------------------------------------------

if st.button(
    "🚀 Generate LinkedIn Post",
    type="primary",
    use_container_width=True
):

    if not topic.strip():

        st.warning("Please enter a topic.")

    else:

        initial_state = {
            "topic": topic.strip(),
            "messages": [],
            "draft": "",
            "review_feedback": "",
            "is_approved": False,
            "attempt": 0,
        }

        # ------------------------------------------
        # RUN LANGGRAPH
        # ------------------------------------------

        with st.spinner(
            "🧠 Writing, reviewing and refining your post..."
        ):

            try:

                final_state = app.invoke(initial_state)

            except Exception as e:

                st.error("❌ Generation failed.")

                st.exception(e)

                st.stop()


        # ------------------------------------------
        # RESULTS
        # ------------------------------------------

        st.divider()

        st.subheader("📊 Generation Results")

        col1, col2, col3 = st.columns(3)

        with col1:

            if final_state["is_approved"]:

                st.success("✅ APPROVED")

            else:

                st.error("❌ REJECTED")


        with col2:

            st.metric(
                "🔄 Attempts",
                final_state["attempt"]
            )


        with col3:

            st.metric(
                "📝 Topic Length",
                len(topic)
            )


        # ------------------------------------------
        # FINAL POST
        # ------------------------------------------

        st.subheader("✨ Generated LinkedIn Post")

        final_post = final_state.get("draft", "")

        if final_post:

            st.markdown(
                f"""
                <div class="post-card">

                {final_post}

                </div>
                """,
                unsafe_allow_html=True
            )

            st.download_button(
                "📥 Download Post",
                data=final_post,
                file_name="linkedin_post.txt",
                mime="text/plain",
                use_container_width=True
            )

            st.text_area(
                "📋 Copy your post",
                final_post,
                height=300
            )

        else:

            st.warning(
                "The workflow finished, but no draft was returned."
            )


        # ------------------------------------------
        # REVIEW FEEDBACK
        # ------------------------------------------

        feedback = final_state.get(
            "review_feedback",
            ""
        )

        if feedback:

            st.subheader("🧐 Latest Reviewer Feedback")

            if final_state["is_approved"]:

                st.success(feedback)

            else:

                st.warning(feedback)


        # ------------------------------------------
        # DEBUG INFORMATION
        # ------------------------------------------

        with st.expander("🔧 LangGraph State"):

            st.json(
                {
                    "topic": final_state.get("topic"),
                    "draft": final_state.get("draft"),
                    "review_feedback": final_state.get(
                        "review_feedback"
                    ),
                    "is_approved": final_state.get(
                        "is_approved"
                    ),
                    "attempt": final_state.get(
                        "attempt"
                    )
                }
            )