import streamlit as st
import pandas as pd

# 모바일 전용 뷰포트 및 여백 최적화
st.set_page_config(page_title="MY VISON 2050", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .block-container { padding-top: 1rem; padding-bottom: 1rem; padding-left: 0.6rem; padding-right: 0.6rem; }
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .app-card {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 14px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            border: 1px solid #eaeeef;
            margin-bottom: 10px;
        }
        .header-title { text-align: center; font-weight: 800; font-size: 1.25rem; color: #1a1a1a; margin-bottom: 10px; }
        .section-subtitle { font-weight: 700; font-size: 0.95rem; color: #333; margin-top: 10px; margin-bottom: 4px; }
        
        /* 1번 시트 병합 표 스타일 */
        .merged-table { width: 100%; border-collapse: collapse; font-size: 0.82rem; margin-top: 6px; }
        .merged-table th { background-color: #f4f6f8; text-align: center; font-weight: bold; padding: 6px 4px; border: 1px solid #e0e0e0; }
        .merged-table td { text-align: right; padding: 5px 4px; border: 1px solid #e0e0e0; }
        .merged-table td.center { text-align: center; }
        .merged-table td.left { text-align: left; font-weight: 600; }
        .merged-table td.group-bg { background-color: #fafafa; font-weight: bold; vertical-align: middle; text-align: center; }
        
        .summary-box { background-color: #eef6ff; padding: 10px; border-radius: 8px; font-weight: bold; text-align: center; margin-top: 10px; color: #1a73e8; }
        .net-asset-box { background-color: #e6f4ea; padding: 12px; border-radius: 8px; font-weight: bold; text-align: center; margin-top: 10px; color: #137333; font-size: 1.05rem; }
    </style>
""", unsafe_allow_html=True)

# 탭 구성
tab1, tab2, tab3 = st.tabs(["📊 1. 금융포트폴리오", "🏠 2. VISON2050", "👶 3. 자녀증여"])

# ----------------------------------------------------
# TAB 1: 금융자산 포트폴리오 (수정 가능 + 병합 표 지원)
# ----------------------------------------------------
with tab1:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">금융자산 포트폴리오</div>', unsafe_allow_html=True)
    
    st.caption("💡 아래 [평가금액] 숫자를 직접 터치해서 수정하면 비율과 총액이 자동 계산됩니다.")
    
    # 초기 데이터 세팅
    default_portfolio = pd.DataFrame([
        {"구분": "CMA", "종목": "테슬라", "평가금액": 54138000},
        {"구분": "연금저축", "종목": "ACE테슬라밸류체인액티브", "평가금액": 50313000},
        {"구분": "CMA", "종목": "스페이스X", "평가금액": 920000},
        {"구분": "연금저축", "종목": "SOL미국배당다우존스", "평가금액": 27970000},
        {"구분": "IRP", "종목": "SOL미국배당다우존스", "평가금액": 12222000},
        {"구분": "ISA", "종목": "TIGER미국배당다우존스", "평가금액": 12131000},
        {"구분": "연금저축", "종목": "TIGER배당커버드콜ETF", "평가금액": 16095000},
        {"구분": "연금저축", "종목": "RISE글로벌리얼티인컴ETF", "평가금액": 741000},
        {"구분": "CMA", "종목": "일드맥스 울트라 옵션 인컴", "평가금액": 21122000},
        {"구분": "IRP", "종목": "ACE미국30년국채액티브(H)", "평가금액": 5485000},
    ])
    
    # 사용자가 직접 고쳐 적을 수 있는 테이블 (data_editor)
    edited_df1 = st.data_editor(
        default_portfolio,
        column_config={
            "구분": st.column_config.TextColumn("구분", width="small"),
            "종목": st.column_config.TextColumn("종목", width="medium"),
            "평가금액": st.column_config.NumberColumn("평가금액(원)", format="%d", min_value=0),
        },
        hide_index=True,
        use_container_width=True,
        key="portfolio_editor"
    )
    
    # 자동 계산 로직
    total_val1 = edited_df1["평가금액"].sum()
    edited_df1["비율"] = (edited_df1["평가금액"] / total_val1 * 100).round(1) if total_val1 > 0 else 0
    
    # 셀 병합 렌더링용 그룹 비중 계산
    g1 = edited_df1.iloc[0:3]["비율"].sum().round(1) # 테슬라 그룹
    g2 = edited_df1.iloc[3:6]["비율"].sum().round(1) # 배당다우존스 그룹
    
    # 캡처용 병합 표 HTML
    st.markdown(f"""
    <div style="margin-top: 15px;">
        <div style="font-weight: bold; font-size: 0.85rem; color: #555; margin-bottom: 4px;">▼ 캡처용 요약 표 (셀 병합 적용)</div>
        <table class="merged-table">
            <thead>
                <tr><th>구분</th><th>종목</th><th>평가금액</th><th>비율</th><th>계(%)</th></tr>
            </thead>
            <tbody>
                <tr><td class="center">{edited_df1.iloc[0]['구분']}</td><td class="left">{edited_df1.iloc[0]['종목']}</td><td>{edited_df1.iloc[0]['평가금액']:,}</td><td>{edited_df1.iloc[0]['비율']}%</td><td rowspan="3" class="group-bg">{g1}%</td></tr>
                <tr><td class="center">{edited_df1.iloc[1]['구분']}</td><td class="left">{edited_df1.iloc[1]['종목']}</td><td>{edited_df1.iloc[1]['평가금액']:,}</td><td>{edited_df1.iloc[1]['비율']}%</td></tr>
                <tr><td class="center">{edited_df1.iloc[2]['구분']}</td><td class="left">{edited_df1.iloc[2]['종목']}</td><td>{edited_df1.iloc[2]['평가금액']:,}</td><td>{edited_df1.iloc[2]['비율']}%</td></tr>
                <tr><td class="center">{edited_df1.iloc[3]['구분']}</td><td class="left">{edited_df1.iloc[3]['종목']}</td><td>{edited_df1.iloc[3]['평가금액']:,}</td><td>{edited_df1.iloc[3]['비율']}%</td><td rowspan="3" class="group-bg">{g2}%</td></tr>
                <tr><td class="center">{edited_df1.iloc[4]['구분']}</td><td class="left">{edited_df1.iloc[4]['종목']}</td><td>{edited_df1.iloc[4]['평가금액']:,}</td><td>{edited_df1.iloc[4]['비율']}%</td></tr>
                <tr><td class="center">{edited_df1.iloc[5]['구분']}</td><td class="left">{edited_df1.iloc[5]['종목']}</td><td>{edited_df1.iloc[5]['평가금액']:,}</td><td>{edited_df1.iloc[5]['비율']}%</td></tr>
                <tr><td class="center">{edited_df1.iloc[6]['구분']}</td><td class="left">{edited_df1.iloc[6]['종목']}</td><td>{edited_df1.iloc[6]['평가금액']:,}</td><td>{edited_df1.iloc[6]['비율']}%</td><td class="group-bg">{edited_df1.iloc[6]['비율']}%</td></tr>
                <tr><td class="center">{edited_df1.iloc[7]['구분']}</td><td class="left">{edited_df1.iloc[7]['종목']}</td><td>{edited_df1.iloc[7]['평가금액']:,}</td><td>{edited_df1.iloc[7]['비율']}%</td><td class="group-bg">{edited_df1.iloc[7]['비율']}%</td></tr>
                <tr><td class="center">{edited_df1.iloc[8]['구분']}</td><td class="left">{edited_df1.iloc[8]['종목']}</td><td>{edited_df1.iloc[8]['평가금액']:,}</td><td>{edited_df1.iloc[8]['비율']}%</td><td class="group-bg">{edited_df1.iloc[8]['비율']}%</td></tr>
                <tr><td class="center">{edited_df1.iloc[9]['구분']}</td><td class="left">{edited_df1.iloc[9]['종목']}</td><td>{edited_df1.iloc[9]['평가금액']:,}</td><td>{edited_df1.iloc[9]['비율']}%</td><td class="group-bg">{edited_df1.iloc[9]['비율']}%</td></tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<div class="summary-box">총액: {total_val1:,} 원</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 2: VISON 2050 (상세 구분 및 수정 가능)
# ----------------------------------------------------
with tab2:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">VISON 2050 (종합 자산)</div>', unsafe_allow_html=True)
    
    # 1. 금융자산
    st.markdown('<div class="section-subtitle">1. 금융자산</div>', unsafe_allow_html=True)
    default_fin = pd.DataFrame([
        {"구분": "단기 주식", "투자금": 75000000, "평가금": 76180000},
        {"구분": "연금 저축", "투자금": 45300000, "평가금": 94378000},
        {"구분": "퇴직 연금", "투자금": 12170000, "평가금": 17707000},
        {"구분": "ISA", "투자금": 10000000, "평가금": 12131000},
        {"구분": "현대푸본연금", "투자금": 0, "평가금": 9245108},
        {"구분": "김윤서(증여)", "투자금": 16025000, "평가금": 30678000},
        {"구분": "김윤찬(증여)", "투자금": 11840000, "평가금": 20015000},
    ])
    
    edited_fin = st.data_editor(
        default_fin,
        column_config={
            "투자금": st.column_config.NumberColumn(format="%d"),
            "평가금": st.column_config.NumberColumn(format="%d"),
        },
        hide_index=True,
        use_container_width=True,
        key="fin_editor"
    )
    
    edited_fin["이익"] = edited_fin["평가금"] - edited_fin["투자금"]
    edited_fin["수익률(%)"] = edited_fin.apply(
        lambda r: round((r["이익"] / r["투자금"] * 100), 1) if r["투자금"] > 0 else 0.0, axis=1
    )
    
    fin_total_eval = edited_fin["평가금"].sum()
    fin_total_profit = edited_fin["이익"].sum()
    
    # 2. 부채 (마통 / 주담대 분리)
    st.markdown('<div class="section-subtitle">2. 부채</div>', unsafe_allow_html=True)
    default_debt = pd.DataFrame([
        {"구분": "마이너스통장", "초기 대출금": 100000000, "상환액": 10000000},
        {"구분": "주택담보대출(자이)", "초기 대출금": 190000000, "상환액": 8000000},
    ])
    
    edited_debt = st.data_editor(
        default_debt,
        column_config={
            "초기 대출금": st.column_config.NumberColumn(format="%d"),
            "상환액": st.column_config.NumberColumn(format="%d"),
        },
        hide_index=True,
        use_container_width=True,
        key="debt_editor"
    )
    
    edited_debt["잔여 대출액"] = edited_debt["초기 대출금"] - edited_debt["상환액"]
    debt_total_rem = edited_debt["잔여 대출액"].sum()
    
    # 3. 부동산
    st.markdown('<div class="section-subtitle">3. 부동산</div>', unsafe_allow_html=True)
    default_re = pd.DataFrame([
        {"종목": "고덕 포레스트자이(19~)", "매수": 380000000, "실거래가": 580000000},
        {"종목": "우미린 프레스티지", "매수": 33840000, "실거래가": 33840000},
    ])
    
    edited_re = st.data_editor(
        default_re,
        column_config={
            "매수": st.column_config.NumberColumn(format="%d"),
            "실거래가": st.column_config.NumberColumn(format="%d"),
        },
        hide_index=True,
        use_container_width=True,
        key="re_editor"
    )
    
    re_total_market = edited_re["실거래가"].sum()
    
    # 4. 퇴직금
    st.markdown('<div class="section-subtitle">4. 퇴직금</div>', unsafe_allow_html=True)
    pension_val = st.number_input("예상 퇴직금(원)", value=151000000, step=1000000)
    
    # 5. 최종 총 자산 계산
    net_asset = fin_total_eval - debt_total_rem + re_total_market + pension_val
    
    st.markdown(f'''
    <div class="net-asset-box">
        총 자산 (순자산)<br>
        <span style="font-size: 1.25rem;">{net_asset:,} 원</span>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 3: 자녀 증여 로드맵
# ----------------------------------------------------
with tab3:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">자녀 증여 장기 로드맵</div>', unsafe_allow_html=True)
    
    default_roadmap = pd.DataFrame([
        {"연도": 2024, "김철현": 37, "이민주": 41, "김윤서(나이)": 8, "김윤서(평가금)": 29299969, "김윤찬(나이)": 5, "김윤찬(평가금)": 17420077},
        {"연도": 2025, "김철현": 38, "이민주": 42, "김윤서(나이)": 9, "김윤서(평가금)": 33707000, "김윤찬(나이)": 6, "김윤찬(평가금)": 21688000},
        {"연도": 2026, "김철현": 39, "이민주": 43, "김윤서(나이)": 10, "김윤서(평가금)": 30678000, "김윤찬(나이)": 7, "김윤찬(평가금)": 20015000},
        {"연도": 2027, "김철현": 40, "이민주": 44, "김윤서(나이)": 11, "김윤서(평가금)": 34946640, "김윤찬(나이)": 8, "김윤찬(평가금)": 26430600},
        {"연도": 2028, "김철현": 41, "이민주": 45, "김윤서(나이)": 12, "김윤서(평가금)": 39686371, "김윤찬(나이)": 9, "김윤찬(평가금)": 30489048},
        {"연도": 2029, "김철현": 42, "이민주": 46, "김윤서(나이)": 13, "김윤서(평가금)": 44934881, "김윤찬(나이)": 10, "김윤찬(평가금)": 35001772},
        {"연도": 2030, "김철현": 43, "이민주": 47, "김윤서(나이)": 14, "김윤서(평가금)": 50732871, "김윤찬(나이)": 11, "김윤찬(평가금)": 40005114},
    ])
    
    st.data_editor(
        default_roadmap,
        column_config={
            "김윤서(평가금)": st.column_config.NumberColumn(format="%d"),
            "김윤찬(평가금)": st.column_config.NumberColumn(format="%d"),
        },
        hide_index=True,
        use_container_width=True,
        key="roadmap_editor"
    )
    
    st.info("💡 10년 비과세 주기: 김윤서(2035년 만19세), 김윤찬(2038년 만19세) 성년 전환 시 5천만원 비과세 한도 확장")
    st.markdown('</div>', unsafe_allow_html=True)
