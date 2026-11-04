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
    
    # 비율 및 그룹 계(%) 자동 계산
    df1["비율(%)"] = (df1["평가금액"] / total_val1 * 100).round(1) if total_val1 > 0 else 0
    group_sums = df1.groupby("그룹")["비율(%)"].transform("sum").round(1)
    df1["계(%)"] = group_sums
    
    # 통합 편집 표 (단 하나만 출력)
    edited_df1 = st.data_editor(
        df1[["구분", "종목", "평가금액", "비율(%)", "계(%)"]],
        column_config={
            "구분": st.column_config.TextColumn("구분", width="small"),
            "종목": st.column_config.TextColumn("종목", width="medium"),
            "평가금액": st.column_config.NumberColumn("평가금액(원)", format="%,d", min_value=0),
            "비율(%)": st.column_config.NumberColumn("비율", format="%.1f%%"),
            "계(%)": st.column_config.NumberColumn("계(%)", format="%.1f%%"),
        },
        disabled=["구분", "종목", "비율(%)", "계(%)"], # 평가금액만 수정 가능
        hide_index=True,
        use_container_width=True,
        key="single_tab1_editor"
    )
    
    # 값 업데이트 저장
    st.session_state.df1_data["평가금액"] = edited_df1["평가금액"]

    st.markdown(f'<div class="summary-box">총액: {total_val1:,.0f} 원</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 2: VISON 2050 (한 화면 캡처용 압축 디자인)
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
    
    # 2. 부채 (마통/주담대 상세 분리)
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
        총 자산 (순자산): <span style="font-size: 1.15rem; color: #137333;">{net_asset:,.0f} 원</span>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 3: 자녀 증여 로드맵 (연도/나이 고정)
# ----------------------------------------------------
with tab3:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">자녀 증여 장기 로드맵</div>', unsafe_allow_html=True)
    
    if "df3_data" not in st.session_state:
        st.session_state.df3_data = pd.DataFrame([
            {"연도": 2021, "김철현": 34, "이민주": 38, "김윤서(나이)": 5, "김윤서(평가금)": 4989172, "김윤찬(나이)": 2, "김윤찬(평가금)": 3744170},
            {"연도": 2022, "김철현": 35, "이민주": 39, "김윤서(나이)": 6, "김윤서(평가금)": 5403917, "김윤찬(나이)": 3, "김윤찬(평가금)": 4120631},
            {"연도": 2023, "김철현": 36, "이민주": 40, "김윤서(나이)": 7, "김윤서(평가금)": 8103905, "김윤찬(나이)": 4, "김윤찬(평가금)": 6691746},
            {"연도": 2024, "김철현": 37, "이민주": 41, "김윤서(나이)": 8, "김윤서(평가금)": 29299969, "김윤찬(나이)": 5, "김윤찬(평가금)": 17420077},
            {"연도": 2025, "김철현": 38, "이민주": 42, "김윤서(나이)": 9, "김윤서(평가금)": 33707000, "김윤찬(나이)": 6, "김윤찬(평가금)": 21688000},
            {"연도": 2026, "김철현": 39, "이민주": 43, "김윤서(나이)": 10, "김윤서(평가금)": 30678000, "김윤찬(나이)": 7, "김윤찬(평가금)": 20015000},
            {"연도": 2027, "김철현": 40, "이민주": 44, "김윤서(나이)": 11, "김윤서(평가금)": 34946640, "김윤찬(나이)": 8, "김윤찬(평가금)": 26430600},
            {"연도": 2028, "김철현": 41, "이민주": 45, "김윤서(나이)": 12, "김윤서(평가금)": 39686371, "김윤찬(나이)": 9, "김윤찬(평가금)": 30489048},
            {"연도": 2029, "김철현": 42, "이민주": 46, "김윤서(나이)": 13, "김윤서(평가금)": 44934881, "김윤찬(나이)": 10, "김윤찬(평가금)": 35001772},
            {"연도": 2030, "김철현": 43, "이민주": 47, "김윤서(나이)": 14, "김윤서(평가금)": 50732871, "김윤찬(나이)": 11, "김윤찬(평가금)": 40005114},
        ])
    
    # 연도 및 나이 컬럼 수정 불가(disabled) 설정
    edited_df3 = st.data_editor(
        st.session_state.df3_data,
        column_config={
            "연도": st.column_config.NumberColumn("연도", format="%d"),
            "김철현": st.column_config.NumberColumn("김철현", format="%d세"),
            "이민주": st.column_config.NumberColumn("이민주", format="%d세"),
            "김윤서(나이)": st.column_config.NumberColumn("윤서(나이)", format="%d세"),
            "김윤서(평가금)": st.column_config.NumberColumn("윤서(평가금)", format="%,d"),
            "김윤찬(나이)": st.column_config.NumberColumn("윤찬(나이)", format="%d세"),
            "김윤찬(평가금)": st.column_config.NumberColumn("윤찬(평가금)", format="%,d"),
        },
        disabled=["연도", "김철현", "이민주", "김윤서(나이)", "김윤찬(나이)"], # 연도와 나이 고정
        hide_index=True,
        use_container_width=True,
        key="fixed_roadmap_editor"
    )
    
    st.session_state.df3_data["김윤서(평가금)"] = edited_df3["김윤서(평가금)"]
    st.session_state.df3_data["김윤찬(평가금)"] = edited_df3["김윤찬(평가금)"]
    
    st.info("💡 비과세 안내: 김윤서(2035년 만19세), 김윤찬(2038년 만19세) 성년 전환 시 5천만원 비과세 한도 확장")
    st.markdown('</div>', unsafe_allow_html=True)
