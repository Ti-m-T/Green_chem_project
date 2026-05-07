import streamlit as st
st.set_page_config(page_title="Green Chemistry Calculator", page_icon=":leaves:")
st.title("🌿 Green Chemistry Calculator")
st.header("Welcome to Green Chemistry Calculator a powerful tool that can calculate the greenness of your reaction!")
st.divider()
if "page_active" not in st.session_state: st.session_state.page_active="Home"

def go_to(page_name):
    st.session_state.page_active= page_name

st.sidebar.title("Menu")

if st.sidebar.button("🏠 Home"):
    go_to('Home')

if st.sidebar.button("🧪 Stoichiometry"):
    go_to('Stoichiometry')
    st.title("Stoichiometry")
    st.write("Write the chemical formula of your reactants, products and solvent to get the correct stoichiometry of the reaction!")

if st.sidebar.button("⚛️ Molecular visulization"):
     go_to("Molecular visualization")

if st.session_state.page_active == 'Molecular visualization':
    st.title("Draw Molecule")
    st.write("Draw your molecule to get started.")
    tab1, tab2, tab3 = ["Reactants", "Solvent/Catalyst", "Products"]

    if "number_reagents" not in st.session_state:
        st.session_state.number_reagents=1

    def add_reagents():
        if st.session_state.number_reagents <5:
            st.session_state.number_reagents +=1

    def remove_reagents():
        if st.session_state.number_reagents >1:
            st.session_state.number_reagents -=1

    col1, col2 = st.columns(2)
    with col1:
        st.button("➕ Add Reagent", on_click=add_reagents)
    with col2:
        st.button("➖ Remove Reagent", on_click=remove_reagents)

    tabs = st.tabs([f"Reagent {i+1}" for i in range(st.session_state.number_reagents)])

    from streamlit_ketcher import st_ketcher
    for i, tab in enumerate(tabs):
        with tab:
            smiles = st_ketcher(key=f"editor_reagente_{i}")
            
            if smiles and smiles.strip() != "":
                st.success(f"**SMILES Reagent {i+1}:** `{smiles}`")
            else:
                st.info(f"Please draw Reagent {i+1} above.")
    
    if "number_solvent_and_catalyst" not in st.session_state:
        st.session_state.number_solvent_and_catalyst=1

    def add_solvent_and_catalyst():
        if st.session_state.number_solvent_and_catlyst <5:
            st.session_state.number_solvent_and_catalyst +=1

    def remove_solvent_and_catalyst():
        if st.session_state.number_solvent_and_catalyst >1:
            st.session_state.number_solvent_and_catalyst -=1

    col1, col2 = st.columns(2)
    with col1:
        st.button("➕ Add Solvent and/or Catalyst", on_click=add_solvent_and_catalyst)
    with col2:
        st.button("➖ Remove Solvent and/or Catalyst", on_click=remove_solvent_and_catalyst)

    tabs = st.tabs([f"Solvent {i+1}" for i in range(st.session_state.number_solvent_and_catalyst)])

    from streamlit_ketcher import st_ketcher
    for i, tab in enumerate(tabs):
        with tab:
            smiles = st_ketcher(key=f"editor_solvent_and_catakyst_{i}")
            
            if smiles and smiles.strip() != "":
                st.success(f"**SMILES Reagent/Catalyst {i+1}:** `{smiles}`")
            else:
                st.info(f"Please draw Reagent/Catalyst {i+1} above.")
    
    if "number_products" not in st.session_state:
        st.session_state.number_products=1

    def add_products():
        if st.session_state.number_products <5:
            st.session_state.number_products +=1

    def remove_products():
        if st.session_state.number_products >1:
            st.session_state.number_products -=1

    col1, col2 = st.columns(2)
    with col1:
        st.button("➕ Add Product", on_click=add_products)
    with col2:
        st.button("➖ Remove Product", on_click=remove_products)

    tabs = st.tabs([f"Product {i+1}" for i in range(st.session_state.number_reagents)])

    from streamlit_ketcher import st_ketcher
    for i, tab in enumerate(tabs):
        with tab:
            smiles = st_ketcher(key=f"editor_product_{i}")
            
            if smiles and smiles.strip() != "":
                st.success(f"**SMILES Product {i+1}:** `{smiles}`")
            else:
                st.info(f"Please draw Product {i+1} above.")
