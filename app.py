import streamlit as st
import pandas as pd

# 모바일 전용 뷰포트 및 여백 최소화 (스마트폰 1화면 캡처 최적화)
st.set_page_config(page_title="MY VISON 2050", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        /* 모바일 1화면 캡처를 위한 전체 여백 및 간격 대폭 축소 */
        .block-container { 
            padding-top: 0.3rem !important; 
            padding-bottom: 0.3rem !important; 
            padding-left: 0.4rem !important; 
            padding-right: 0.4rem !important; 
        }
        footer { visibility: hidden; }
        header { visibility: hidden; }
        
        /* 콤팩트 카드 디자인 */
        .app-card {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 8px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            border: 1px solid #eaeeef;
        }
        .header-title { 
            text-align: center; 
            font-weight: 800; 
            font-size: 1.05rem; 
            color: #1a1a1a; 
            margin-bottom: 4px; 
        }
        .section-subtitle { 
            font-weight: 700; 
            font-size: 0.78rem; 
            color: #1a73e8; 
            margin-top: 4px; 
            margin-bottom: 2px; 
        }
        
        /* Streamlit 기본 요소 간격 축소 */
        div[data-testid="stVerticalBlock"] > div {
            gap: 0.2rem !important;
        }
        
        /* 표 폰트 사이즈 조절 */
        .stDataFrame {
            font-size: 0.75rem !important;
        }
        
        /* 하단 요약 및 총자산 박스 */
        .summary-box { 
            background-color: #eef6ff; 
            padding: 6px; 
            border-radius: 6px; 
            font-weight: bold; 
            text-align: center; 
            margin-top: 6px; 
            color: #1a73e8; 
            font-size: 0.85rem; 
        }
        .net-asset-box { 
            background-color: #e6f4ea; 
            padding: 8px; 
            border-radius: 6px; 
            font-weight: bold; 
            text-align: center; 
            margin-top: 6px; 
            color: #137333; 
            font-size: 0.95rem; 
        }
    </style>
""", unsafe_allow_html=True)

# 탭 구성
tab1, tab2, tab3 = st.tabs(["📊 1. 금융포트폴리오", "🏠 2. VISON2050", "👶 3. 자녀증여"])

# ----------------------------------------------------
# TAB 1: 금융자산 포트폴리오 (단일 표로 통합 & 콤마 표기)
# ----------------------------------------------------
with tab1:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">금융자산 포트폴리오</div>', unsafe_allow_html=True)
    
    # 세션 상태 초기화 (수치 변경 유지)
    if "df
