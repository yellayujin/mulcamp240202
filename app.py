import streamlit as st 
import pandas as pd 
import requests 
import json 
import pandas as pd 

@st.cache_data
def load_data():
    SEOUL_PUBLIC_API = st.secrets["api_credentials"]["SEOUL_PUBLIC_API"]
    st.write(SEOUL_PUBLIC_API)
    URL = f'http://openapi.seoul.go.kr:8088/{SEOUL_PUBLIC_API}/json/tbLnOpendataRtmsV/1/100/'
    st.write(URL)
    content = requests.get(URL).json()
    data = pd.DataFrame(content['tbLnOpendataRtmsV']['row'])
    return data

def main():
    result = load_data()
    st.data_editor(result)
    SGG_NM = st.selectbox("지역구를 선택하세요", sorted(list(result['SGG_NM'].unique())))
    st.write(SGG_NM)

    st.data_editor(result.loc[result['SGG_NM'] == SGG_NM, :])

if __name__ == "__main__":
    main()