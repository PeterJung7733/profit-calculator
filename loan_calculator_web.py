import streamlit as st

st.title("🏦 대출 이자 계산기")

principal = st.text_input("대출 원금 (예: 30,000,000)", "")
rate = st.text_input("연 이자율 (%)", "")
months = st.text_input("대출 기간 (개월)", "")

if st.button("🧮 계산하기"):
    try:
        # , 제거 후 숫자 변환
        principal = float(principal.replace(",", ""))
        rate = float(rate)
        months = int(months)

        monthly_interest = (principal * (rate / 100)) / 12
        total_interest = monthly_interest * months
        total_repayment = principal + total_interest

        st.success("💸 계산 결과")
        st.write(f"🏦 대출 원금: {principal:,.0f}원")
        st.write(f"📆 월 이자: {monthly_interest:,.0f}원")
        st.write(f"💰 총 이자: {total_interest:,.0f}원")
        st.write(f"📦 총 상환금액: {total_repayment:,.0f}원")

    except:
        st.error("❗ 숫자를 정확히 입력해주세요. 콤마 포함 가능!")
