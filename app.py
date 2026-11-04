import streamlit as st
import pandas as pd

# 모바일 전용 뷰포트 및 여백 최적화 (스마트폰 1화면 캡처)
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
        
        /* 표 폰트 크기 축소, 여백 최소화, 줄바꿈 방지 */
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

# ----------------------------------------------------
# 세션 상태 초기화 (데이터베이스 역할)
# ----------------------------------------------------
if "df1_data" not in st.session_state:
    st.session_state.df1_data = pd.DataFrame([
        {"구분": "CMA", "종목": "테슬라", "평가금액": 54138000, "그룹": 1},
        {"구분": "연금저축", "종목": "ACE테슬라밸류체인액티브", "평가금액": 50313000, "그룹": 1},
        {"구분": "CMA", "종목": "스페이스X", "평가금액": 920000, "그룹": 1},
        {"구분": "연금저축", "종목": "SOL미국배당다우존스", "평가금액": 27970000, "그룹": 2},
        {"구분": "IRP", "종목": "SOL미국배당다우존스", "평가금액": 12222000, "그룹": 2},
        {"구분": "ISA", "종목": "TIGER미국배당다우존스", "평가금액": 12131000, "그룹": 2},
        {"구분": "연금저축", "종목": "TIGER배당커버드콜ETF", "평가금액": 16095000, "그룹": 3},
        {"구분": "연금저축", "종목": "RISE글로벌리얼티인컴ETF", "평가금액": 741000, "그룹": 4},
        {"구분": "CMA", "종목": "일드맥스 울트라 옵션 인컴", "평가금액": 21122000, "그룹": 5},
        {"구분": "IRP", "종목": "ACE미국30년국채액티브(H)", "평가금액": 5485000, "그룹": 6},
    ])

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
        {"연도": 2031, "김철현": 44, "이민주": 48, "윤서": 15, "윤서금액": 57124301, "윤찬": 12, "윤찬금액": 45538323},
        {"연도": 2032, "김철현": 45, "이민주": 49, "윤서": 16, "윤서금액": 64156645, "윤찬": 13, "윤찬금액": 51643788},
        {"연도": 2033, "김철현": 46, "이민주": 50, "윤서": 17, "윤서금액": 69884477, "윤찬": 14, "윤찬금액": 56745978},
        {"연도": 2034, "김철현": 47, "이민주": 51, "윤서": 18, "윤서금액": 76024701, "윤찬": 15, "윤찬금액": 62229277},
        {"연도": 2035, "김철현": 48, "이민주": 52, "윤서": 19, "윤서금액": 82597936, "윤찬": 16, "윤찬금액": 68112741},
        {"연도": 2036, "김철현": 49, "이민주": 53, "윤서": 20, "윤서금액": 92186571, "윤찬": 17, "윤찬금액": 74416378},
        {"연도": 2037, "김철현": 50, "이민주": 54, "윤서": 21, "윤서금액": 0, "윤찬": 18, "윤찬금액": 81161197},
        {"연도": 2038, "김철현": 51, "이민주": 55, "윤서": 22, "윤서금액": 0, "윤찬": 19, "윤찬금액": 88369256},
        {"연도": 2039, "김철현": 52, "이민주": 56, "윤서": 23, "윤서금액": 0, "윤찬": 20, "윤찬금액": 96063719},
        {"연도": 2040, "김철현": 53, "이민주": 57, "윤서": 24, "윤서금액": 0, "윤찬": 21, "윤찬금액": 0},
    ])

# 탭 구성
tab1, tab2, tab3 = st.tabs(["📊 1. 금융포트폴리오", "🏠 2. VISON2050", "👶 3. 자녀증여"])

# ----------------------------------------------------
# TAB 1: 금융자산 포트폴리오
# ----------------------------------------------------
with tab1:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">금융자산 포트폴리오</div>', unsafe_allow_html=True)
    
    df1 = st.session_state.df1_data.copy()
    total_val1 = df1["평가금액"].sum()
    
    # 비율(%) 계산
    raw_ratios = (df1["평가금액"] / total_val1 * 100).round(1) if total_val1 > 0 else 0
    df1["비율(%)"] = raw_ratios.map(lambda x: f"{x:.1f}%")
    
    # 그룹별 계(%) 정확한 위치 지정 표기 (None 대신 빈 문자열 "")
    group_totals = raw_ratios.groupby(df1["그룹"]).sum().round(1)
    ke_col = [""] * len(df1)
    ke_col[1] = f"{group_totals[1]:.1f}%" # 테슬라 그룹 (row 2)
    ke_col[4] = f"{group_totals[2]:.1f}%" # 미국배당다우존스 그룹 (row 5)
    ke_col[6] = f"{group_totals[3]:.1f}%" # TIGER배당커버드콜
    ke_col[7] = f"{group_totals[4]:.1f}%" # RISE글로벌리얼티인컴
    ke_col[8] = f"{group_totals[5]:.1f}%" # 일드맥스
    ke_col[9] = f"{group_totals[6]:.1f}%" # ACE미국30년국채
    
    df1["계(%)"] = ke_col
    
    # 너비 배치를 조정하여 종목 옆 공간 제거
    edited_df1 = st.data_editor(
        df1[["구분", "종목", "평가금액", "비율(%)", "계(%)"]],
        column_config={
            "구분": st.column_config.TextColumn("구분", width="small"),
            "종목": st.column_config.TextColumn("종목", width="large"), # 종목 너비 확대하여 우측 빈 공간 흡수
            "평가금액": st.column_config.NumberColumn("평가금액(원)", format="%,d", min_value=0, width="medium"),
            "비율(%)": st.column_config.TextColumn("비율", width="small"),
            "계(%)": st.column_config.TextColumn("계(%)", width="small"),
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
# TAB 2: VISON 2050 (1번 시트 및 3번 시트 자동 연동)
# ----------------------------------------------------
with tab2:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">VISON 2050 (종합 자산)</div>', unsafe_allow_html=True)
    
    # 1번 시트 평가금액 자동 합산 계산
    cma_sum = st.session_state.df1_data[st.session_state.df1_data["구분"] == "CMA"]["평가금액"].sum()
    pension_sum = st.session_state.df1_data[st.session_state.df1_data["구분"] == "연금저축"]["평가금액"].sum()
    irp_sum = st.session_state.df1_data[st.session_state.df1_data["구분"] == "IRP"]["평가금액"].sum()
    isa_sum = st.session_state.df1_data[st.session_state.df1_data["구분"] == "ISA"]["평가금액"].sum()
    
    # 3번 시트 2026년 자녀 증여 평가금 자동 동기화
    df3_curr = st.session_state.df3_data[st.session_state.df3_data["연도"] == 2026]
    yunseo_val = df3_curr["윤서금액"].values[0] if len(df3_curr) > 0 else 30678000
    yunchan_val = df3_curr["윤찬금액"].values[0] if len(df3_curr) > 0 else 20015000
    
    st.markdown('<div class="section-subtitle">1. 금융자산 (1번/3번 시트 자동 연동)</div>', unsafe_allow_html=True)
    if "df2_fin_inv" not in st.session_state:
        st.session_state.df2_fin_inv = {
            "단기 주식": 75000000,
            "연금 저축": 45300000,
            "퇴직 연금": 12170000,
            "ISA": 10000000,
            "현대푸본연금": 0,
            "김윤서(증여)": 16025000,
            "김윤찬(증여)": 11840000,
            "현대푸본평가금": 9245108
        }
    
    df2_fin = pd.DataFrame([
        {"구분": "단기 주식", "투자금": st.session_state.df2_fin_inv["단기 주식"], "평가금": cma_sum},
        {"구분": "연금 저축", "투자금": st.session_state.df2_fin_inv["연금 저축"], "평가금": pension_sum},
        {"구분": "퇴직 연금", "투자금": st.session_state.df2_fin_inv["퇴직 연금"], "평가금": irp_sum},
        {"구분": "ISA", "투자금": st.session_state.df2_fin_inv["ISA"], "평가금": isa_sum},
        {"구분": "현대푸본연금", "투자금": st.session_state.df2_fin_inv["현대푸본연금"], "평가금": st.session_state.df2_fin_inv["현대푸본평가금"]},
        {"구분": "김윤서(증여)", "투자금": st.session_state.df2_fin_inv["김윤서(증여)"], "평가금": yunseo_val},
        {"구분": "김윤찬(증여)", "투자금": st.session_state.df2_fin_inv["김윤찬(증여)"], "평가금": yunchan_val},
    ])
    
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
        disabled=["구분", "평가금", "이익", "수익률(%)"],
        hide_index=True,
        use_container_width=True,
        key="compact_fin_editor"
    )
    
    for idx, row in edited_fin.iterrows():
        k = row["구분"]
        if k in st.session_state.df2_fin_inv:
            st.session_state.df2_fin_inv[k] = row["투자금"]
            
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
# TAB 3: 자녀 증여 로드맵 (2040년까지 확장)
# ----------------------------------------------------
with tab3:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">자녀 증여 장기 로드맵 (2021~2040년)</div>', unsafe_allow_html=True)
    
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
    
    st.info("💡 비과세: 윤서(2035년 만19세), 윤찬(2038년 만19세) 성년 전환 시 5천만원 확장")
    st.markdown('</div>', unsafe_allow_html=True)
