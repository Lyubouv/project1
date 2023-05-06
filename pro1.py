import streamlit as st


#cover
st.title('Aplikasi Perhitungan Stoikiometri Dasar')
st.write('Oleh Kelompok 2 :')
st.write('Abdul Nazhmi Makarim (2219023)')
st.write('Muhammad Ihsan Aula Hikam (2219115)')
st.write('Chandrika Raysa Mulya (2219053)')
st.write('R Amelia Nurbani Sumarya (2219146)')

#tab
tab1,tab2=st.tabs(['Stoikiometri', 'Perhitungan Stoikiometri Dasar'])

#tab 1
with tab1:
    st.header('Stoikiometri')
    st.write('Stoikiometri berasal dari kata “stoicheion” dalam bahasa Yunani yang berarti mengukur. Dalam ilmu kimia, stoikiometri adalah ilmu yang mempelajari kuantitas suatu zat dalam reaksi kimia. Zat-zat tersebut meliputi massa, jumlah mol, volume, dan jumlah partikel dan molaritas.')
from PIL import Image
st.image('http://2.bp.blogspot.com/-dkCllpwvUhY/VJ0C87FFB3I/AAAAAAAABdo/_D8B2yjQDYY/s1600/ScreenHunter_01%2BMay.%2B02%2B15.45.jpg',caption= 'Rumus Dasar Perhitungan Stoikiometri')

    
#tab 2
with tab2:
    st.header('Perhitungan Stoikiometri Dasar')
    option=st.selectbox(
    'Silahkan pilih satuan konsentrasi yang ingin dicari ',
    ('Molekul (n)','Molaritas (M)','Volume (v)','Partikel'))
        
    if option=='Molekul (n)':
        massa=st.number_input('Masukkan massa zat')
        mr=st.number_input('Masukkan mr larutan')
        if st.button('Hitung'):
            Molekul=massa/mr
            st.success(f'Molekul larutan sebesar {Molekul} M')
    elif option=='Molaritas (M)':
        mol=st.number_input('Masukkan mol zat')
        v=st.number_input('Masukkan volume pelarut')
        if st.button('Hitung'):
            Molaritas=mol/v
            st.success(f'Molaritas larutan sebesar {Molaritas} M')
    elif option=='Volume (v)':
        mol=st.number_input('Masukkan molekul zat')
        if st.button('Hitung'):
            Volume=mol*22.4
            st.success(f'Volume larutan sebesar {Volume}')
    elif option=='Partikel':
        mol=st.number_input('Masukkan molekul zat')
        if st.button('Hitung'):
            Partikel=mol*6.02*10**23
            st.success(f'Partikel larutan sebesar {Partikel}')