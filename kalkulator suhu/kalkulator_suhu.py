# -*- coding: utf-8 -*-
"""Kalkulator_Suhu.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13txC673HVXrFfRVY_P91ji_i1AZvSmJm
"""

import streamlit as st

# Fungsi-fungsi konversi suhu
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Judul aplikasi
st.title("🌡️ Kalkulator Konversi Suhu")
st.write("Pilih jenis suhu dan masukkan nilainya untuk dikonversi.")

# Pilihan suhu asal
suhu_dari = st.selectbox("Konversi dari:", ["Celsius", "Fahrenheit", "Kelvin"])

# Input suhu
nilai = st.number_input(f"Masukkan suhu dalam {suhu_dari}:", value=0.0)

# Konversi
if suhu_dari == "Celsius":
    st.write(f"{nilai}°C = {celsius_to_fahrenheit(nilai):.2f}°F")
    st.write(f"{nilai}°C = {celsius_to_kelvin(nilai):.2f}K")

elif suhu_dari == "Fahrenheit":
    st.write(f"{nilai}°F = {fahrenheit_to_celsius(nilai):.2f}°C")
    st.write(f"{nilai}°F = {fahrenheit_to_kelvin(nilai):.2f}K")

elif suhu_dari == "Kelvin":
    st.write(f"{nilai}K = {kelvin_to_celsius(nilai):.2f}°C")
    st.write(f"{nilai}K = {kelvin_to_fahrenheit(nilai):.2f}°F")