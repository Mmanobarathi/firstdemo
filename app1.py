import streamlit as st

def main():
    # Set page title and favicon
    st.set_page_config(
        page_title="Inventory Management App",
        page_icon="📦",
        layout="wide"
    )

    # Title and subtitle with custom styling
    st.title("Inventory Management Dashboard")
    st.markdown(
        """
        Streamlit is **great** for building interactive ML applications!
        """
    )

    # Sidebar with background color and padding
    st.sidebar.title("Settings")
    st.sidebar.markdown("Adjust parameters here:")
    st.sidebar.slider("Parameter 1", 0, 100, 50)
    st.sidebar.selectbox("Parameter 2", ["Option 1", "Option 2", "Option 3"])

    # Main content area with custom background color
    st.markdown("---")
    st.header("Inventory Overview")
    st.subheader("Current Status")
    st.info("Total items in stock: 100")
    st.warning("Low stock alert: 10 items remaining")
    st.success("Top selling item: Product X")

    # Data visualization example with plot
    st.markdown("---")
    st.header("Sales Analysis")
    st.write("Placeholder for charts and graphs")

    # Custom footer with HTML and CSS
    st.markdown("---")
    footer_html = """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f0f0f0;
        padding: 10px 0;
        text-align: center;
        font-size: 14px;
        color: #666;
    }
    </style>
    <div class="footer">
        Streamlit Web App Example &copy; 2024
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
