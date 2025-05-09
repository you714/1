import streamlit as st
# 페이지 구조용 제목 출력
st.title("메인 제목입니다")
st.header("중간 제목입니다")
st.subheader("하위 제목입")
st.title("🎈 김하은")
st.info(
    "안녕하세요 송내고 김하은입니다."
)
st.write(" 안녕하세요 저는 김하은입니다.")
st.image("https://cdn.royalcanin-weshare-online.io/mDLz-m8BN5A8uWWAYDRj/v1/ktca1s1-r-maine-coon-kitten-sitting-outside-on-a-wooden-table")

# st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
with col2:
    st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성
# st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용
    # st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
with st.expander("ℹ️ 자세한 설명 보기"):
    st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")
    # st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write("선택한 옵션:", option)
name=st.text_area("dkssud")
st.write(name+"안녕하세요")
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)

if name=="rhrnak":
    st.success(name+"님 반갑습니다다")
else: 
    st.error("rhrnakskak")
image_data = st.camera_input("사진을 찍어보세요")
if image_data:
    st.image(image_data)
st.code("""
import streamlit as st
st.title('Hello World')
""", language="python")

import openai

user_api_key = st.text_input("키를 입력해주세요.")

from openai import OpenAI

client = OpenAI(api_key = user_api_key)
prompt = st.text_input("프롬프트를 입력해주세요.")

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user","content": prompt}]
)
st.markdown("### 💡 GPT의 답변:")
st.write(completion.choices[0].message.content)

# import streamlit as st
# import openai

# # 앱 타이틀
# st.set_page_config(page_title="GPT-4o 대화 앱", page_icon="💬")
# st.title("💬 GPT-4o와 대화해보세요!")
# st.markdown("OpenAI GPT-4o 모델에게 질문하고 바로 답변을 받아보는 간단한 앱입니다.")

# # API 키 입력
# st.sidebar.header("🔐 API 설정")
# # user_api_key=st.secrets["openai"]["api_key"]
# user_api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")

# # 프롬프트 입력
# prompt = st.text_area("✍️ 프롬프트를 입력하세요", placeholder="예: 내일 날씨에 대해 알려줘")

# # 버튼 클릭 시 GPT 호출
# if st.button("🚀 GPT에게 물어보기"):
#     if not user_api_key:
#         st.warning("API 키를 입력해주세요!")
#     elif not prompt:
#         st.warning("프롬프트를 입력해주세요!")
#     else:
#         try:
#             openai.api_key = user_api_key

#             response = openai.ChatCompletion.create(
#                 model="gpt-4o",
#                 messages=[{"role": "user", "content": prompt}]
#             )

#             st.success("✅ GPT의 답변이 도착했어요!")
#             st.markdown("### 💡 GPT의 답변:")
#             st.write(response.choices[0].message["content"])

#         except Exception as e:
#             st.error(f"❗ 오류가 발생했어요: {e}")

# # 하단 안내
# st.markdown("---")
# st.caption("ⓒ 2025. Streamlit GPT 앱 만들기 도움봇 🤖")