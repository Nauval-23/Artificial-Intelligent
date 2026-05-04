import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Mall Customers Visualization", layout="wide")

# Judul
st.title("Visualisasi Dataset Mall Customers")
st.write("Aplikasi visualisasi data menggunakan Streamlit")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Mall_Customers.csv")
    return df

# Membaca data
try:
    df = load_data()

    # Menampilkan dataset
    st.subheader("Dataset")
    st.dataframe(df)

    # Informasi dataset
    st.subheader("Informasi Dataset")
    st.write("Jumlah baris dan kolom:", df.shape)
    st.write("Tipe data:")
    st.write(df.dtypes)

    # Statistik deskriptif
    st.subheader("Statistik Deskriptif")
    st.write(df.describe())

    # Sidebar
    st.sidebar.header("Pilih Visualisasi")
    option = st.sidebar.selectbox(
        "Jenis Visualisasi",
        (
            "Histogram Umur",
            "Histogram Pendapatan",
            "Scatter Plot",
            "Bar Chart Gender",
            "Line Chart"
        )
    )

    # Histogram umur
    if option == "Histogram Umur":
        st.subheader("Histogram Umur Customer")

        fig, ax = plt.subplots()
        ax.hist(df['Age'], bins=10)
        ax.set_xlabel("Umur")
        ax.set_ylabel("Jumlah")
        ax.set_title("Distribusi Umur Customer")

        st.pyplot(fig)

    # Histogram pendapatan
    elif option == "Histogram Pendapatan":
        st.subheader("Histogram Pendapatan Tahunan")

        fig, ax = plt.subplots()
        ax.hist(df['Annual Income (k$)'], bins=10)
        ax.set_xlabel("Pendapatan Tahunan (k$)")
        ax.set_ylabel("Jumlah")
        ax.set_title("Distribusi Pendapatan")

        st.pyplot(fig)

    # Scatter plot
    elif option == "Scatter Plot":
        st.subheader("Scatter Plot Income vs Spending Score")

        fig, ax = plt.subplots()
        ax.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'])
        ax.set_xlabel("Annual Income (k$)")
        ax.set_ylabel("Spending Score")
        ax.set_title("Income vs Spending Score")

        st.pyplot(fig)

    # Bar chart gender
except FileNotFoundError:
    st.error("File Mall_Customers.csv tidak ditemukan. Pastikan file berada di folder yang sama dengan app.py")