# 파일명 예: profit_calculator_web.py

import streamlit as st

st.set_page_config(page_title="수익 계산기", layout="centered")

st.title("🧮 나의 수익 계산기")

symbol = st.text_input("종목명")
buy_price = st.number_input("매수가", step=0.01)
sell_price = st.number_input("매도가", step=0.01)
quantity = st.number_input("수량", step=1)
exchange_rate = st.number_input("환율 (예: 1390)", value=1390.0)

if st.button("📊 계산하기"):
    try:
        profit = (sell_price - buy_price) * quantity
        profit_rate = ((sell_price - buy_price) / buy_price) * 100
        profit_krw = profit * exchange_rate
        tax = profit_krw * 0.22
        net_profit = profit_krw - tax

        st.success(f"{symbol} 수익: {profit:.2f}달러 ({profit_rate:.2f}%)")
        st.info(
            f"💵 원화 수익: {profit_krw:,.0f}원\n"
            f"💸 세금 (22%): {tax:,.0f}원\n"
            f"✅ 세후 수익: {net_profit:,.0f}원"
        )
    except:
        st.error("입력값이 잘못되었습니다. 숫자를 확인해주세요.")
