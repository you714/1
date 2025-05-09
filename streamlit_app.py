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