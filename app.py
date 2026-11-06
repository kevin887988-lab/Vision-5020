import streamlit as st
import pandas as pd
import json
import os

# ----------------------------------------------------
# 1. 모바일 전용 뷰포트 및 여백 최적화
# ----------------------------------------------------
st.set_page_config(page_title="MY VISON 2050", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .block-container { padding-top: 0.1rem !important; padding-bottom: 0.1rem !important; padding-left: 0.1rem !important; padding-right: 0.1rem !important; }
        footer { display: none !important; }
        header { display: none !important; }
        .app-card { background-color: #ffffff; border-radius: 6px; padding: 4px 4px !important; box-shadow: 0 1px 4px rgba(0,0,0,0.05); border: 1px solid #eaeeef; }
        .header-title { text-align: center; font-weight: 800; font-size: 0.95rem; color: #1a1a1a; margin-bottom: 2px; }
        .section-subtitle { font-weight: 700; font-size: 0.72rem; color: #1a73e8; margin-top: 2px; margin-bottom: 1px; }
        div[data-testid="stVerticalBlock"] > div { gap: 0.1rem !important; }
        .stDataFrame { font-size: 0.68rem !important; }
        .stDataFrame td, .stDataFrame th { padding: 2px 2px !important; white-space: nowrap !important; }
        .summary-box { background-color: #eef6ff; padding: 4px; border-radius: 4px; font-weight: bold; text-align: center; margin-top: 4px; color: #1a73e8; font-size: 0.78rem; }
        .net-asset-box { background-color: #e6f4ea; padding: 5px; border-radius: 4px; font-weight: bold; text-align: center; margin-top: 4px; color: #137333; font-size: 0.88rem; }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 2. 영구 파일 저장/불러오기 로직
# ----------------------------------------------------
DATA_FILE = "portfolio_data.json"

def get_default_data():
    return {
        "df1_data": [
            {"구분": "CMA", "종목": "일드맥스 울트라 옵션 인컴", "평가금액": 19794000, "그룹": 5},
            {"구분": "CMA", "종목": "테슬라", "평가금액": 51007000, "그룹": 1},
            {"구분": "CMA", "종목": "스페이스X", "평가금액": 1993000, "그룹": 1},
            {"구분": "연금저축", "종목": "SOL미국배당다우존스", "평가금액": 27610000, "그룹": 2},
            {"구분": "연금저축", "종목": "ACE테슬라밸류체인액티브", "평가금액": 49368000, "그룹": 1},
            {"구분": "연금저축", "종목": "TIGER배당커버드콜ETF", "평가금액": 16451000, "그룹": 3},
            {"구분": "연금저축", "종목": "RISE글로벌리얼티인컴ETF", "평가금액": 751000, "그룹": 4},
            {"구분": "ISA", "종목": "TIGER미국배당다우존스", "평가금액": 12006000, "그룹": 2},
            {"구분": "IRP", "종목": "SOL미국배당다우존스", "평가금액": 12065000, "그룹": 2},
            {"구분": "IRP", "종목": "ACE미국30년국채액티브(H)", "평가금액": 5458000, "그룹": 6},
        ],
        "df3_data": [
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
        ],
        "df2_fin_inv": {
            "단기 주식": 75000000,
            "연금 저축": 45300000,
            "퇴직 연금": 12170000,
            "ISA": 10000000,
            "현대푸본연금": 0,
            "김윤서(증여)": 16025000,
            "김윤찬(증여)": 11840000,
            "현대푸본평가금": 9245108
        },
        "df2_debt": [
            {"구분": "마이너스통장", "초기 대출금": 100000000, "상환액": 10000000},
            {"구분": "주택담보대출(자이)", "초기 대출금": 190000000, "상환액": 8000000},
        ],
        "df2_re": [
            {"종목": "고덕 포레스트자이", "매수": 380000000, "실거래가": 580000000},
            {"종목": "우미린 프레스티지", "매수": 33840000, "실거래가": 33840000},
        ],
        "pension_val": 151000000
    }

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return get_default_data()

def save_data():
    saved_payload = {
        "df1_data": st.session_state.df1_data.to_dict(orient="records"),
        "df3_data": st.session_state.df3_data.to_dict(orient="records"),
        "df2_fin_inv": st.session_state.df2_fin_inv,
        "df2_debt": st.session_state.df2_debt.to_dict(orient="records"),
        "df2_re": st.session_state.df2_re.to_dict(orient="records"),
        "pension_val": st.session_state.pension_val
    }
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(saved_payload, f, ensure_ascii=False, indent=2)

# ----------------------------------------------------
# 3. 세션 상태 초기화
# ----------------------------------------------------
if "data_loaded" not in st.session_state:
    loaded_data = load_data()
    st.session_state.df1_data = pd.DataFrame(loaded_data["df1_data"])
    st.session_state.df3_data = pd.DataFrame(loaded_data["df3_data"])
    st.session_state.df2_fin_inv = loaded_data["df2_fin_inv"]
    st.session_state.df2_debt = pd.DataFrame(loaded_data["df2_debt"])
    st.session_state.df2_re = pd.DataFrame(loaded_data["df2_re"])
    st.session_state.pension_val = loaded_data.get("pension_val", 151000000)
    st.session_state.data_loaded = True

# 탭 구성
tab1, tab2, tab3 = st.tabs(["📊 1. 금융포트폴리오", "🏠 2. VISON2050", "👶 3. 자녀증여"])

# ----------------------------------------------------
# TAB 1: 금융자산 포트폴리오 (수동 입력 전용)
# ----------------------------------------------------
with tab1:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">금융자산 포트폴리오</div>', unsafe_allow_html=True)
    
    df1 = st.session_state.df1_data.copy()
    
    for col in ["구분", "종목", "평가금액", "그룹"]:
        if col not in df1.columns:
            df1[col] = "" if col in ["구분", "종목"] else (0 if col == "평가금액" else 1)
            
    total_val1 = df1["평가금액"].sum() if len(df1) > 0 else 0
    
    if total_val1 > 0 and len(df1) > 0:
        raw_ratios = (df1["평가금액"] / total_val1 * 100).round(1)
        df1["비율(%)"] = raw_ratios.map(lambda x: f"{x:.1f}%")
        
        group_totals = raw_ratios.groupby(df1["그룹"]).sum().round(1)
        ke_col = [""] * len(df1)
        seen_groups = set()
        for i, (idx, row) in enumerate(df1.iterrows()):
            g = row["그룹"]
            if g not in seen_groups and g in group_totals:
                ke_col[i] = f"{group_totals[g]:.1f}%"
                seen_groups.add(g)
        df1["계(%)"] = ke_col
    else:
        df1["비율(%)"] = "0.0%"
        df1["계(%)"] = ""
    
    edited_df1 = st.data_editor(
        df1[["구분", "종목", "평가금액", "그룹", "비율(%)", "계(%)"]],
        column_config={
            "구분": st.column_config.SelectboxColumn("구분", options=["CMA", "연금저축", "IRP", "ISA", "일반계좌"], required=True),
            "종목": st.column_config.TextColumn("종목", required=True),
            "평가금액": st.column_config.NumberColumn("평가금액(원)", format="%,d", min_value=0, default=0),
            "그룹": st.column_config.NumberColumn("그룹", format="%d", min_value=1, default=1),
            "비율(%)": st.column_config.TextColumn("비율"),
            "계(%)": st.column_config.TextColumn("계(%)"),
        },
        disabled=["비율(%)", "계(%)"],
        num_rows="dynamic",
        hide_index=True,
        use_container_width=True,
        key="single_tab1_editor"
    )
    
    current_saved_base = st.session_state.df1_data[["구분", "종목", "평가금액", "그룹"]].reset_index(drop=True)
    edited_base = edited_df1[["구분", "종목", "평가금액", "그룹"]].reset_index(drop=True)
    
    if not current_saved_base.equals(edited_base):
        st.session_state.df1_data = edited_df1[["구분", "종목", "평가금액", "그룹"]].copy()
        save_data()
        st.rerun()

    st.markdown(f'<div class="summary-box">총액: {total_val1:,.0f} 원</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 2: VISON 2050 (종합 자산)
# ----------------------------------------------------
with tab2:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">VISON 2050 (종합 자산)</div>', unsafe_allow_html=True)
    
    cma_sum = st.session_state.df1_data[st.session_state.df1_data["구분"] == "CMA"]["평가금액"].sum()
    pension_sum = st.session_state.df1_data[st.session_state.df1_data["구분"] == "연금저축"]["평가금액"].sum()
    irp_sum = st.session_state.df1_data[st.session_state.df1_data["구분"] == "IRP"]["평가금액"].sum()
    isa_sum = st.session_state.df1_data[st.session_state.df1_data["구분"] == "ISA"]["평가금액"].sum()
    
    df3_curr = st.session_state.df3_data[st.session_state.df3_data["연도"] == 2026]
    yunseo_val = df3_curr["윤서금액"].values[0] if len(df3_curr) > 0 else 30678000
    yunchan_val = df3_curr["윤찬금액"].values[0] if len(df3_curr) > 0 else 20015000
    
    st.markdown('<div class="section-subtitle">1. 금융자산 (1번/3번 시트 자동 연동)</div>', unsafe_allow_html=True)
    
    df2_fin = pd.DataFrame([
        {"구분": "단기 주식", "투자금": st.session_state.df2_fin_inv.get("단기 주식", 0), "평가금": cma_sum},
        {"구분": "연금 저축", "투자금": st.session_state.df2_fin_inv.get("연금 저축", 0), "평가금": pension_sum},
        {"구분": "퇴직 연금", "투자금": st.session_state.df2_fin_inv.get("퇴직 연금", 0), "평가금": irp_sum},
        {"구분": "ISA", "투자금": st.session_state.df2_fin_inv.get("ISA", 0), "평가금": isa_sum},
        {"구분": "현대푸본연금", "투자금": st.session_state.df2_fin_inv.get("현대푸본연금", 0), "평가금": st.session_state.df2_fin_inv.get("현대푸본평가금", 0)},
        {"구분": "김윤서(증여)", "투자금": st.session_state.df2_fin_inv.get("김윤서(증여)", 0), "평가금": yunseo_val},
        {"구분": "김윤찬(증여)", "투자금": st.session_state.df2_fin_inv.get("김윤찬(증여)", 0), "평가금": yunchan_val},
    ])
    
    df2_fin["이익"] = df2_fin["평가금"] - df2_fin["투자금"]
    df2_fin["수익률(%)"] = df2_fin.apply(lambda r: round((r["이익"] / r["투자금"] * 100), 1) if r["투자금"] > 0 else 0.0, axis=1)
    
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
    
    fin_changed = False
    for idx, row in edited_fin.iterrows():
        k = row["구분"]
        if k in st.session_state.df2_fin_inv and st.session_state.df2_fin_inv[k] != row["투자금"]:
            st.session_state.df2_fin_inv[k] = row["투자금"]
            fin_changed = True
            
    if fin_changed:
        save_data()
        st.rerun()
            
    fin_total_eval = edited_fin["평가금"].sum()
    
    # 2. 부채
    st.markdown('<div class="section-subtitle">2. 부채</div>', unsafe_allow_html=True)
    
    df2_debt = st.session_state.df2_debt.copy()
    if len(df2_debt) > 0:
        df2_debt["잔여 대출액"] = df2_debt["초기 대출금"] - df2_debt["상환액"]
    else:
        df2_debt = pd.DataFrame(columns=["구분", "초기 대출금", "상환액", "잔여 대출액"])
    
    edited_debt = st.data_editor(
        df2_debt[["구분", "초기 대출금", "상환액", "잔여 대출액"]],
        column_config={
            "구분": st.column_config.TextColumn("구분", required=True),
            "초기 대출금": st.column_config.NumberColumn("초기 대출금", format="%,d", default=0),
            "상환액": st.column_config.NumberColumn("상환액", format="%,d", default=0),
            "잔여 대출액": st.column_config.NumberColumn("잔여 대출액", format="%,d"),
        },
        disabled=["잔여 대출액"],
        num_rows="dynamic",
        hide_index=True,
        use_container_width=True,
        key="compact_debt_editor"
    )
    
    current_debt_base = st.session_state.df2_debt[["구분", "초기 대출금", "상환액"]].reset_index(drop=True)
    edited_debt_base = edited_debt[["구분", "초기 대출금", "상환액"]].reset_index(drop=True)
    
    if not current_debt_base.equals(edited_debt_base):
        st.session_state.df2_debt = edited_debt[["구분", "초기 대출금", "상환액"]].copy()
        save_data()
        st.rerun()
    
    debt_total_rem = edited_debt["잔여 대출액"].sum() if len(edited_debt) > 0 else 0
    
    # 3. 부동산
    st.markdown('<div class="section-subtitle">3. 부동산</div>', unsafe_allow_html=True)
    
    df2_re = st.session_state.df2_re.copy()
    if len(df2_re) > 0:
        df2_re["손익"] = df2_re["실거래가"] - df2_re["매수"]
    else:
        df2_re = pd.DataFrame(columns=["종목", "매수", "실거래가", "손익"])
    
    edited_re = st.data_editor(
        df2_re[["종목", "매수", "실거래가", "손익"]],
        column_config={
            "종목": st.column_config.TextColumn("종목", required=True),
            "매수": st.column_config.NumberColumn("매수", format="%,d", default=0),
            "실거래가": st.column_config.NumberColumn("실거래가", format="%,d", default=0),
            "손익": st.column_config.NumberColumn("손익", format="%,d"),
        },
        disabled=["손익"],
        num_rows="dynamic",
        hide_index=True,
        use_container_width=True,
        key="compact_re_editor"
    )
    
    current_re_base = st.session_state.df2_re[["종목", "매수", "실거래가"]].reset_index(drop=True)
    edited_re_base = edited_re[["종목", "매수", "실거래가"]].reset_index(drop=True)
    
    if not current_re_base.equals(edited_re_base):
        st.session_state.df2_re = edited_re[["종목", "매수", "실거래가"]].copy()
        save_data()
        st.rerun()
    
    re_total_market = edited_re["실거래가"].sum() if len(edited_re) > 0 else 0
    
    # 4. 퇴직금 & 순자산 합계
    st.markdown('<div class="section-subtitle">4. 퇴직금 & 최종 순자산</div>', unsafe_allow_html=True)
    pension_val = st.number_input("예상 퇴직금(원)", value=int(st.session_state.pension_val), step=1000000, format="%d")
    
    if pension_val != st.session_state.pension_val:
        st.session_state.pension_val = pension_val
        save_data()
        st.rerun()
    
    net_asset = fin_total_eval - debt_total_rem + re_total_market + pension_val
    
    st.markdown(f'''
    <div class="net-asset-box">
        총 자산 (순자산): <span style="font-size: 1.05rem; color: #137333;">{net_asset:,.0f} 원</span>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 3: 자녀 증여 로드맵
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
    
    if not st.session_state.df3_data["윤서금액"].equals(edited_df3["윤서금액"]) or \
       not st.session_state.df3_data["윤찬금액"].equals(edited_df3["윤찬금액"]):
        st.session_state.df3_data["윤서금액"] = edited_df3["윤서금액"]
        st.session_state.df3_data["윤찬금액"] = edited_df3["윤찬금액"]
        save_data()
        st.rerun()
    
    st.info("💡 비과세: 윤서(2035년 만19세), 윤찬(2038년 만19세) 성년 전환 시 5천만원 확장")
    st.markdown('</div>', unsafe_allow_html=True)
