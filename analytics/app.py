if st.button("🧠 Explain this stock with AI"):
    try:
        with st.spinner("Analyzing with Gemini AI..."):
            explanation = explain_stock(ticker, data)
            st.markdown("### 🧠 AI Insight")
            st.write(explanation)
    except Exception as e:
        st.error(f"AI Error: {e}")
