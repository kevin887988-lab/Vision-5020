import streamlit as st
import pandas as pd

# 모바일 1화면 꽉 차게 표시하기 위한 CSS 설정
st.set_page_config(page_title="MY VISON 2050", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        /* 모바일 여백 최소화 및 모바일 뷰포트 최적화 */
        .block-container { padding-top: 1rem; padding-bottom: 1rem; padding-left: 0.8rem; padding-right: 0.8rem; }
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* 캡처 전용 모바일 카드 스타일 */
        .app-card {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            border: 1px solid #eaeeef;
            margin-bottom: 10px;
        }
        .header-title { text-align: center; font-weight: 800; font-size: 1.25rem; color: #1a1a1a; margin-bottom: 12px; }
        
        /* 표 스타일 최적화 */
        table { width: 100% !important; border-collapse: collapse; font-size: 0.85rem; }
        th { background-color: #f4f6f8; text-align: center !important; font-weight: bold; padding: 6px; }
        td { text-align: right; padding: 6px; border-bottom: 1px solid #f0f0f0; }
        td:first-child { text-align: left; font-weight: 600; }
        .summary-box { background-color: #eef6ff; padding: 10px; border-radius: 8px; font-weight: bold; text-align: center; margin-top: 8px; }
    </style>
""", unsafe_allow_html=True)

# 상단 시트 전환 탭
tab1, tab2, tab3 = st.tabs(["📊 1. 금융포트폴리오", "🏠 2. VISON2050", "👶 3. 자녀증여"])

# ----------------------------------------------------
# TAB 1: 금융자산 포트폴리오
# ----------------------------------------------------
with tab1:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">금융자산 포트폴리오</div>', unsafe_allow_html=True)
    
    # 예시 데이터 (구글 시트 연동 시 st.connection으로 체인지)
    data1 = [
        {"구분": "CMA", "종목": "테슬라", "평가금액": "54,138,000", "비율": "26.9%", "계": ""},
        {"구분": "연금저축", "종목": "ACE테슬라밸류체인액티브", "평가금액": "50,313,000", "비율": "25.0%", "계": "52.4%"},
        {"구분": "CMA", "종목": "스페이스X", "평가금액": "920,000", "비율": "0.5%", "계": ""},
        {"구분": "연금저축", "종목": "SOL미국배당다우존스", "평가금액": "27,970,000", "비율": "13.9%", "계": ""},
        {"구분": "IRP", "종목": "SOL미국배당다우존스", "평가금액": "12,222,000", "비율": "6.1%", "계": "26.0%"},
        {"구분": "ISA", "종목": "TIGER미국배당다우존스", "평가금액": "12,131,000", "비율": "6.0%", "계": ""},
        {"구분": "연금저축", "종목": "TIGER배당커버드콜ETF", "평가금액": "16,095,000", "비율": "8.0%", "계": "8.0%"},
        {"구분": "연금저축", "종목": "RISE글로벌리얼티인컴ETF", "평가금액": "741,000", "비율": "0.4%", "계": "0.4%"},
        {"구분": "CMA", "종목": "일드맥스 울트라 옵션 인컴", "평가금액": "21,122,000", "비율": "10.5%", "계": "10.5%"},
        {"구분": "IRP", "종목": "ACE미국30년국채액티브(H)", "평가금액": "5,485,000", "비율": "2.7%", "계": "2.7%"},
    ]
    df1 = pd.DataFrame(data1)
    st.table(df1)
    
    st.markdown('<div class="summary-box">총액: 201,137,000 원</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 2: VISON2050 (종합자산현황)
# ----------------------------------------------------
with tab2:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">VISON 2050 (종합 자산)</div>', unsafe_allow_html=True)
    
    st.caption("1. 금융자산")
    df2_1 = pd.DataFrame([
        {"구분": "단기 주식", "평가금": "76,180,000", "수익률": "1.6%"},
        {"구분": "연금 저축", "평가금": "94,378,000", "수익률": "108.3%"},
        {"구분": "퇴직 연금", "평가금": "17,707,000", "수익률": "45.5%"},
        {"구분": "ISA", "평가금": "12,131,000", "수익률": "21.3%"},
        {"구분": "자녀 증여 합계", "평가금": "50,693,000", "수익률": "82.4%"},
    ])
    st.table(df2_1)
    
    st.caption("2. 부채 & 부동산 & 퇴직금")
    df2_2 = pd.DataFrame([
        {"항목": "부채 (마통+주담대)", "금액": "-272,000,000 원"},
        {"항목": "부동산 실거래가", "금액": "613,840,000 원"},
        {"항목": "예상 퇴직금", "금액": "151,000,000 원"},
    ])
    st.table(df2_2)
    
    st.markdown('<div class="summary-box" style="background-color:#e6f4ea; color:#137333;">총 자산 (순자산): 753,174,108 원</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 3: 자녀 증여 로드맵
# ----------------------------------------------------
with tab3:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">자녀 증여 장기 로드맵</div>', unsafe_allow_html=True)
    
    df3 = pd.DataFrame([
        {"연도": "2024 (8/5세)", "김윤서": "29,299,969", "김윤찬": "17,420,077"},
        {"연도": "2025 (9/6세)", "김윤서": "33,707,000", "김윤찬": "21,688,000"},
        {"연도": "2026 (10/7세)", "김윤서": "30,678,000", "김윤찬": "20,015,000"},
        {"연도": "2027 (11/8세)", "김윤서": "34,946,640", "김윤찬": "26,430,600"},
        {"연도": "2028 (12/9세)", "김윤서": "39,686,371", "김윤찬": "30,489,048"},
        {"연도": "2029 (13/10세)", "김윤서": "44,934,881", "김윤찬": "35,001,772"},
        {"연도": "2030 (14/11세)", "김윤서": "50,732,871", "김윤찬": "40,005,114"},
    ])
    st.table(df3)
    
    st.info("💡 10년 비과세 주기: 김윤서(2035년 만19세), 김윤찬(2038년 만19세) 성년 전환 시 5천만원 비과세 한도 확대")
    st.markdown('</div>', unsafe_allow_html=True)
