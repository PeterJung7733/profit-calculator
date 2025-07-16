import streamlit as st

st.set_page_config(page_title="수익 계산기", layout="centered")

st.title("🧮 나의 수익 계산기")

symbol = st.text_input("종목명")

buy_price = st.text_input("매수가 (숫자 입력)", "")
sell_price = st.text_input("매도가 (숫자 입력)", "")
quantity = st.text_input("수량 (숫자 입력)", "")
exchange_rate = st.text_input("환율 (예: 1390)", "")

if st.button("📊 계산하기"):
    try:
        # 문자열 → 숫자 변환
        buy_price = float(buy_price)
        sell_price = float(sell_price)
        quantity = int(quantity)
        exchange_rate = float(exchange_rate)

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
        st.error("❗ 입력값을 모두 숫자로 정확히 입력해주세요.")
