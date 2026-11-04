import streamlit as st
import pandas as pd

# 모바일 전용 뷰포트 및 여백 극소화 (스마트폰 1화면 캡처 최적화)
st.set_page_config(page_title="MY VISON 2050", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        /* 모바일 1화면 캡처를 위한 전체 여백 및 간격 극소화 */
        .block-container { 
            padding-top: 0.1rem !important; 
            padding-bottom: 0.1rem !important; 
            padding-left: 0.2rem !important; 
            padding-right: 0.2rem !important; 
        }
        footer { display: none !important; }
        header { display: none !important; }
        
        /* 콤팩트 카드 디자인 */
        .app-card {
            background-color: #ffffff;
            border-radius: 6px;
            padding: 4px 6px !important;
            box-shadow: 0 1px 4px rgba(0,0,0,0.05);
            border: 1px solid #eaeeef;
        }
        .header-title { 
            text-align: center; 
            font-weight: 800; 
            font-size: 0.95rem; 
            color: #1a1a1a; 
            margin-bottom: 2px; 
        }
        .section-subtitle { 
            font-weight: 700; 
            font-size: 0.72rem; 
            color: #1a73e8; 
            margin-top: 2px; 
            margin-bottom: 1px; 
        }
        
        /* Streamlit 기본 요소 간격 극소화 (상하 공백 제거) */
        div[data-testid="stVerticalBlock"] > div {
            gap: 0.1rem !important;
        }
        
        /* 표 폰트 크기 1단계 축소, 여백 최소화, 줄바꿈 방지 */
        .stDataFrame {
            font-size: 0.68rem !important;
        }
        .stDataFrame td, .stDataFrame th {
            padding: 2px 3px !important;
            white-space: nowrap !important;
        }
        
        /* 하단 요약 및 총자산 박스 압축 */
        .summary-box { 
            background-color: #eef6ff; 
            padding: 4px; 
            border-radius: 4px; 
            font-weight: bold; 
            text-align: center; 
            margin-top: 4px; 
            color: #1a73e8; 
            font-size: 0.78rem; 
        }
        .net-asset-box { 
            background-color: #e6f4ea; 
            padding: 5px; 
            border-radius: 4px; 
            font-weight: bold; 
            text-align: center; 
            margin-top: 4px; 
            color: #137333; 
            font-size: 0.88rem; 
        }
    </style>
""", unsafe_allow_html=True)

# 탭 구성
tab1, tab2, tab3 = st.tabs(["📊 1. 금융포트폴리오", "🏠 2. VISON2050", "👶 3. 자녀증여"])

# ----------------------------------------------------
# TAB 1: 금융자산 포트폴리오
# ----------------------------------------------------
with tab1:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">금융자산 포트폴리오</div>', unsafe_allow_html=True)
    
    if "df1_data" not in st.session_state:
        st.session_state.df1_data = pd.DataFrame([
            {"구분": "CMA", "종목": "테슬라", "평가금액": 54138000, "그룹": "테슬라"},
            {"구분": "연금저축", "종목": "ACE테슬라밸류체인액티브", "평가금액": 50313000, "그룹": "테슬라"},
            {"구분": "CMA", "종목": "스페이스X", "평가금액": 920000, "그룹": "테슬라"},
            {"구분": "연금저축", "종목": "SOL미국배당다우존스", "평가금액": 27970000, "그룹": "배당다우"},
            {"구분": "IRP", "종목": "SOL미국배당다우존스", "평가금액": 12222000, "그룹": "배당다우"},
            {"구분": "ISA", "종목": "TIGER미국배당다우존스", "평가금액": 12131000, "그룹": "배당다우"},
            {"구분": "연금저축", "종목": "TIGER배당커버드콜ETF", "평가금액": 16095000, "그룹": "개별1"},
            {"구분": "연금저축", "종목": "RISE글로벌리얼티인컴ETF", "평가금액": 741000, "그룹": "개별2"},
            {"구분": "CMA", "종목": "일드맥스 울트라 옵션 인컴", "평가금액": 21122000, "그룹": "개별3"},
            {"구분": "IRP", "종목": "ACE미국30년국채액티브(H)", "평가금액": 5485000, "그룹": "개별4"},
        ])

    df1 = st.session_state.df1_data.copy()
    total_val1 = df1["평가금액"].sum()
    
    df1["비율(%)"] = (df1["평가금액"] / total_val1 * 100).round(1) if total_val1 > 0 else 0
    group_sums = df1.groupby("그룹")["비율(%)"].transform("sum").round(1)
    df1["계(%)"] = group_sums
    
    edited_df1 = st.data_editor(
        df1[["구분", "종목", "평가금액", "비율(%)", "계(%)"]],
        column_config={
            "구분": st.column_config.TextColumn("구분", width="small"),
            "종목": st.column_config.TextColumn("종목", width="medium"),
            "평가금액": st.column_config.NumberColumn("평가금액(원)", format="%,d", min_value=0),
            "비율(%)": st.column_config.NumberColumn("비율", format="%.1f%%"),
            "계(%)": st.column_config.NumberColumn("계(%)", format="%.1f%%"),
        },
        disabled=["구분", "종목", "비율(%)", "계(%)"],
        hide_index=True,
        use_container_width=True,
        key="single_tab1_editor"
    )
    
    st.session_state.df1_data["평가금액"] = edited_df1["평가금액"]
    st.markdown(f'<div class="summary-box">총액: {total_val1:,.0f} 원</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 2: VISON 2050 (1페이지 캡처용 압축 디자인)
# ----------------------------------------------------
with tab2:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">VISON 2050 (종합 자산)</div>', unsafe_allow_html=True)
    
    # 1. 금융자산
    st.markdown('<div class="section-subtitle">1. 금융자산</div>', unsafe_allow_html=True)
    if "df2_fin" not in st.session_state:
        st.session_state.df2_fin = pd.DataFrame([
            {"구분": "단기 주식", "투자금": 75000000, "평가금": 76180000},
            {"구분": "연금 저축", "투자금": 45300000, "평가금": 94378000},
            {"구분": "퇴직 연금", "투자금": 12170000, "평가금": 17707000},
            {"구분": "ISA", "투자금": 10000000, "평가금": 12131000},
            {"구분": "현대푸본연금", "투자금": 0, "평가금": 9245108},
            {"구분": "김윤서(증여)", "투자금": 16025000, "평가금": 30678000},
            {"구분": "김윤찬(증여)", "투자금": 11840000, "평가금": 20015000},
        ])
    
    df2_fin = st.session_state.df2_fin.copy()
    df2_fin["이익"] = df2_fin["평가금"] - df2_fin["투자금"]
    df2_fin["수익률(%)"] = df2_fin.apply(
        lambda r: round((r["이익"] / r["투자금"] * 100), 1) if r["투자금"] > 0 else 0.0, axis=1
    )
    
    edited_fin = st.data_editor(
        df2_fin[["구분", "투자금", "평가금", "이익", "수익률(%)"]],
        column_config={
            "투자금": st.column_config.NumberColumn("투자금", format="%,d"),
            "평가금": st.column_config.NumberColumn("평가금", format="%,d"),
            "이익": st.column_config.NumberColumn("이익", format="%,d"),
            "수익률(%)": st.column_config.NumberColumn("수익률", format="%.1f%%"),
        },
        disabled=["구분", "이익", "수익률(%)"],
        hide_index=True,
        use_container_width=True,
        key="compact_fin_editor"
    )
    st.session_state.df2_fin["투자금"] = edited_fin["투자금"]
    st.session_state.df2_fin["평가금"] = edited_fin["평가금"]
    
    fin_total_eval = edited_fin["평가금"].sum()
    
    # 2. 부채
    st.markdown('<div class="section-subtitle">2. 부채</div>', unsafe_allow_html=True)
    if "df2_debt" not in st.session_state:
        st.session_state.df2_debt = pd.DataFrame([
            {"구분": "마이너스통장", "초기 대출금": 100000000, "상환액": 10000000},
            {"구분": "주택담보대출(자이)", "초기 대출금": 190000000, "상환액": 8000000},
        ])
    
    df2_debt = st.session_state.df2_debt.copy()
    df2_debt["잔여 대출액"] = df2_debt["초기 대출금"] - df2_debt["상환액"]
    
    edited_debt = st.data_editor(
        df2_debt[["구분", "초기 대출금", "상환액", "잔여 대출액"]],
        column_config={
            "초기 대출금": st.column_config.NumberColumn("초기 대출금", format="%,d"),
            "상환액": st.column_config.NumberColumn("상환액", format="%,d"),
            "잔여 대출액": st.column_config.NumberColumn("잔여 대출액", format="%,d"),
        },
        disabled=["구분", "잔여 대출액"],
        hide_index=True,
        use_container_width=True,
        key="compact_debt_editor"
    )
    st.session_state.df2_debt["초기 대출금"] = edited_debt["초기 대출금"]
    st.session_state.df2_debt["상환액"] = edited_debt["상환액"]
    
    debt_total_rem = edited_debt["잔여 대출액"].sum()
    
    # 3. 부동산
    st.markdown('<div class="section-subtitle">3. 부동산</div>', unsafe_allow_html=True)
    if "df2_re" not in st.session_state:
        st.session_state.df2_re = pd.DataFrame([
            {"종목": "고덕 포레스트자이", "매수": 380000000, "실거래가": 580000000},
            {"종목": "우미린 프레스티지", "매수": 33840000, "실거래가": 33840000},
        ])
    
    df2_re = st.session_state.df2_re.copy()
    df2_re["손익"] = df2_re["실거래가"] - df2_re["매수"]
    
    edited_re = st.data_editor(
        df2_re[["종목", "매수", "실거래가", "손익"]],
        column_config={
            "매수": st.column_config.NumberColumn("매수", format="%,d"),
            "실거래가": st.column_config.NumberColumn("실거래가", format="%,d"),
            "손익": st.column_config.NumberColumn("손익", format="%,d"),
        },
        disabled=["종목", "손익"],
        hide_index=True,
        use_container_width=True,
        key="compact_re_editor"
    )
    st.session_state.df2_re["매수"] = edited_re["매수"]
    st.session_state.df2_re["실거래가"] = edited_re["실거래가"]
    
    re_total_market = edited_re["실거래가"].sum()
    
    # 4. 퇴직금 & 순자산 합계
    st.markdown('<div class="section-subtitle">4. 퇴직금 & 최종 순자산</div>', unsafe_allow_html=True)
    pension_val = st.number_input("예상 퇴직금(원)", value=151000000, step=1000000, format="%d")
    
    net_asset = fin_total_eval - debt_total_rem + re_total_market + pension_val
    
    st.markdown(f'''
    <div class="net-asset-box">
        총 자산 (순자산): <span style="font-size: 1.05rem; color: #137333;">{net_asset:,.0f} 원</span>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 3: 자녀 증여 로드맵 (괄호 명칭 간소화 & 가로 폭 축소)
# ----------------------------------------------------
with tab3:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">자녀 증여 장기 로드맵</div>', unsafe_allow_html=True)
    
    if "df3_data" not in st.session_state:
        st.session_state.df3_data = pd.DataFrame([
            {"연도": 2021, "김철현": 34, "이민주": 38, "윤서": 5, "윤서금액": 4989172, "윤찬": 2, "윤찬금액": 3744170},
            {"연도": 2022, "김철현": 35, "이민주": 39, "윤서": 6, "윤서금액": 5403917, "윤찬": 3, "윤찬금액": 4120631},
            {"연도": 2023, "김철현": 36, "이민주": 40, "윤서": 7, "윤서금액": 8103905, "윤찬": 4, "윤찬금액": 6691746},
            {"연도": 2024, "김철현": 37, "이민주": 41, "윤서": 8, "윤서금액": 29299969, "윤찬": 5, "윤찬금액": 17420077},
            {"연도": 2025, "김철현": 38, "이민주": 42, "윤서": 9, "윤서금액": 33707000, "윤찬": 6, "윤찬금액": 21688000},
            {"연도": 2026, "김철현": 39, "이민주": 43, "윤서": 10, "윤서금액": 30678000, "윤찬": 7, "윤찬금액": 20015000},
            {"연도": 2027, "김철현": 40, "이민주": 44, "윤서": 11, "윤서금액": 34946640, "윤찬": 8, "윤찬금액": 26430600},
            {"연도": 2028, "김철현": 41, "이민주": 45, "윤서": 12, "윤서금액": 39686371, "윤찬": 9, "윤찬금액": 30489048},
            {"연도": 2029, "김철현": 42, "이민주": 46, "윤서": 13, "윤서금액": 44934881, "윤찬": 10, "윤찬금액": 35001772},
            {"연도": 2030, "김철현": 43, "이민주": 47, "윤서": 14, "윤서금액": 50732871, "윤찬": 11, "윤찬금액": 40005114},
        ])
    
    edited_df3 = st.data_editor(
        st.session_state.df3_data,
        column_config={
            "연도": st.column_config.NumberColumn("연도", format="%d"),
            "김철현": st.column_config.NumberColumn("철현", format="%d세"),
            "이민주": st.column_config.NumberColumn("민주", format="%d세"),
            "윤서": st.column_config.NumberColumn("윤서", format="%d세"),
            "윤서금액": st.column_config.NumberColumn("윤서금액", format="%,d"),
            "윤찬": st.column_config.NumberColumn("윤찬", format="%d세"),
            "윤찬금액": st.column_config.NumberColumn("윤찬금액", format="%,d"),
        },
        disabled=["연도", "김철현", "이민주", "윤서", "윤찬"],
        hide_index=True,
        use_container_width=True,
        key="fixed_roadmap_editor"
    )
    
    st.session_state.df3_data["윤서금액"] = edited_df3["윤서금액"]
    st.session_state.df3_data["윤찬금액"] = edited_df3["윤찬금액"]
    
    st.info("💡 비과세: 윤서(2035년 만19세), 윤찬(2038년 만19세) 성년 전환 시 5천만원 확대")
    st.markdown('</div>', unsafe_allow_html=True)
