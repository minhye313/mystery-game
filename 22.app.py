import streamlit as st
import random

st.set_page_config(page_title="유산의 그림자", page_icon="🕵️", layout="centered")

# 캐릭터 관계
relationships = {
    "박지훈": "피해자의 조카이자 유일한 유산 상속 대상자",
    "박 변호사": "피해자의 법률 자문을 맡던 변호사",
    "이 교수": "피해자의 학문적 라이벌",
    "김 형사": "사건을 담당한 수사 형사"
}

# 용의자 대사
character_lines = {
    "박지훈": [
        "“난 그냥 삼촌을 도우려고 했던 거예요. 물론… 요즘 돈이 좀 급하긴 했지만요. 그렇다고 그런 일까지 할 리 없잖아요?”",
        "“저도 삼촌이 돌아가셔서 충격이 큽니다… 하지만 유산 얘기는 아직 너무 이른 것 같네요.”",
        "“삼촌 연구는 정말 자랑스러웠어요. 그걸 망칠 이유가 왜 있겠어요?”"
    ],
    "박 변호사": [
        "“교수님의 연구는 위험했소. 세상에 나와선 안 될 결과였지. 난 그저... 그분을 보호하고 싶었을 뿐이오.”",
        "“유언장을 작성했지만, 그게 이렇게 문제가 될 줄은 몰랐소. 내 역할은 단지 법적 조언이었소.”",
        "“나는 법을 따랐을 뿐이오. 이 상황이 왜 이렇게 됐는지 나도 안타깝소.”"
    ],
    "이 교수": [
        "“그 연구는 사실 원래 제 것이나 마찬가지였습니다. 교수님은 내 아이디어를 무시했죠. 하지만... 난 살인은 하지 않았어요.”",
        "“나도 슬픕니다. 그러나 학문의 세계에선 경쟁이 당연한 것 아닙니까?”",
        "“그 노트북은 제 연구 정리를 위해 잠시 맡아둔 것뿐입니다.”"
    ],
    "김 형사": [
        "“진실은 결국 드러나게 돼 있죠. 다만, 위에서 수사 그만하라는 압박이 너무 거세서... 쉽지 않네요.”",
        "“형사로서 내 양심에 따라 움직였습니다. 감추려는 자들이 너무 많았을 뿐이죠.”",
        "“이 사건은 단순한 살인이 아니었습니다. 권력과 진실 사이에서 줄타기를 해야 했죠.”"
    ]
}

# 증거
evidences = {
    "박 변호사": "지문: 박 변호사의 지문이 연구실 금고 손잡이에서 검출됨.",
    "박지훈": "금융거래: 박지훈이 교수의 사망 전 거액의 대출을 신청한 내역이 있음.",
    "이 교수": "노트북: 이 교수가 교수의 원본 연구 자료가 담긴 노트북을 무단 보관하고 있었음.",
    "김 형사": "압력편지: 김 형사가 받은 '사건을 더 이상 파지 말라'는 청와대발 익명 편지."
}

# 힌트 (섞어서 중복 방지)
hints = random.sample([
    "박 변호사는 연구 공개를 반대했고, 유언장 내용을 제일 먼저 열람했다.",
    "박지훈은 최근 투자 실패로 거액을 잃고 있었으며, 상속을 노릴 이유가 충분했다.",
    "이 교수는 최 교수의 업적을 자기 것이라 주장해왔다.",
    "김 형사는 상부의 외압을 여러 차례 폭로하려다 수사를 묵살당했다.",
    "유언장이 일부 조작된 흔적이 발견되었고, 박 변호사만 접근 가능했다.",
    "사건 당시, 연구실에 남겨진 발자국이 정장 구두였다는 제보가 있었다.",
    "노트북에서 삭제된 파일이 복구됐고, 암호화된 정치적 메일이 있었다.",
    "박지훈은 알리바이가 확실하지 않다. 사망 시각에 연락 두절 상태였다.",
    "김 형사는 피의자가 아닌 내부 고발자일 가능성이 높아 보인다.",
    "연구 노트 마지막 페이지에 ‘나를 막지 마라. 이건 세상의 이익을 위한 일이다.’라는 글이 남아 있었다."
], k=10)

# 상태 유지
if "hint_index" not in st.session_state:
    st.session_state.hint_index = 0
if "suspect_log" not in st.session_state:
    st.session_state.suspect_log = []
if "game_over" not in st.session_state:
    st.session_state.game_over = False

def show_hint():
    if st.session_state.hint_index < len(hints):
        st.info(f"💡 힌트 {st.session_state.hint_index + 1}: {hints[st.session_state.hint_index]}")
        st.session_state.hint_index += 1

def investigate(name):
    st.subheader(f"🔍 {name} 조사 결과")
    st.write(f"**관계:** {relationships[name]}")
    st.write(f"**대사:** {random.choice(character_lines[name])}")
    if name in evidences:
        st.write(f"**증거:** {evidences[name]}")
    st.success("조사가 완료되었습니다.")
    st.session_state.suspect_log.append(name)

def reveal_result(guess):
    st.session_state.game_over = True
    if guess == "박 변호사":
        st.balloons()
        st.success("✅ 정답입니다! 박 변호사가 진범입니다.")
    else:
        st.error("❌ 오답입니다. 진범은 '박 변호사'였습니다.")

    st.markdown("---")
    st.markdown("""
    📰 **[중앙일보 단독보도] - 고고학과 최 교수 유산 살해사건, 진실은?**

    서울 K대학교 고고학과 최민수 교수의 사망 사건이 ‘계획된 타살’로 드러났다.  
    박 변호사는 고위층의 외압을 이용해 유언장을 조작하고, 연구를 은폐하려 했다.  
    박지훈, 이 교수, 김 형사 등은 각자의 동기를 가졌으나, 살인과는 직접 관련이 없던 것으로 밝혀졌다.

    전문가들은 이번 사건을 '지식과 권력이 얽힌 비극'이라 평가하고 있다.
    """)

# 메인 실행
def main():
    st.title("🕵️ 유산의 그림자")
    st.markdown("고고학과 최 교수의 죽음... 단순한 사고일까요?")
    st.write("단서는 이미 주변에 흩어져 있습니다. 범인을 추리해보세요.")

    if not st.session_state.game_over:
        show_hint()

        st.markdown("### 🔍 용의자 조사하기")
        suspect = st.selectbox("조사할 용의자를 선택하세요", list(relationships.keys()))
        if st.button("조사 시작"):
            investigate(suspect)

        st.markdown("### 🧠 범인 추리하기")
        guess = st.selectbox("범인으로 지목할 사람은?", ["", *relationships.keys()])
        if st.button("범인 지목하기") and guess:
            reveal_result(guess)

if __name__ == "__main__":
    main()
