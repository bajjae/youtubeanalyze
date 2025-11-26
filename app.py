import streamlit as st
import random
import pandas as pd
from urllib.parse import urlparse

st.set_page_config(page_title="📊 유튜브 채널 분석기", page_icon="📺", layout="centered")
st.title("📊 유튜브 채널 분석기 (샘플 데이터)")
st.write("유튜브 채널 링크를 입력하면 분석 결과를 카드 스타일로 보여줍니다! 🎨")

# CSS 카드 스타일
st.markdown("""
<style>
.card {
    background-color: #FFF0F5;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 10px;
    border: 2px solid #FF69B4;
}
h2 {
    color: #FF1493;
}
</style>
""", unsafe_allow_html=True)

channel_url = st.text_input("유튜브 채널 링크 입력 (예: https://www.youtube.com/@qodmsco.09)")

def extract_channel_id(url):
    """
    URL에서 채널 ID 또는 @사용자 이름 추출
    """
    try:
        parsed = urlparse(url)
        path_parts = parsed.path.split('/')
        for part in path_parts:
            if part.startswith('@') or part == 'channel' or part == 'c':
                return part  # @사용자이름 또는 채널 ID 반환
        return path_parts[-1]  # 그 외 마지막 경로 반환
    except:
        return None

if st.button("분석 시작") and channel_url:
    channel_id = extract_channel_id(channel_url)
    
    if channel_id:
        # 샘플 통계
        channel_name = f"샘플 채널 {random.randint(1,100)}"
        subscriber_count = random.randint(1000, 1000000)
        video_count = random.randint(10, 200)
        total_views = random.randint(10000, 5000000)
        
        # 채널 정보 카드
        st.markdown(f"""
        <div class="card">
        <h2>📺 채널 정보</h2>
        <p><b>채널명:</b> {channel_name}</p>
        <p><b>채널 ID/사용자명:</b> {channel_id}</p>
        <p><b>구독자 수:</b> {subscriber_count}</p>
        <p><b>총 동영상 수:</b> {video_count}</p>
        <p><b>총 조회수:</b> {total_views}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 샘플 영상 리스트
        videos = []
        for i in range(10):
            videos.append({
                "title": f"샘플 영상 {i+1}",
                "views": random.randint(100, 50000),
                "likes": random.randint(10, 5000),
                "publishedAt": f"2025-11-{random.randint(1,28):02d}"
            })
        df = pd.DataFrame(videos)
        
        # 최근 5개 영상 카드
        st.markdown(f"<div class='card'><h2>📌 최근 업로드 동영상 (Top5)</h2>", unsafe_allow_html=True)
        recent = df.sort_values("publishedAt", ascending=False).head(5)
        for idx, row in recent.iterrows():
            st.markdown(f"- {row['title']} | 조회수: {row['views']} | 좋아요: {row['likes']} | 업로드: {row['publishedAt']}", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # 인기 영상 Top3 카드
        st.markdown(f"<div class='card'><h2>🔥 인기 영상 Top3</h2>", unsafe_allow_html=True)
        top3 = df.sort_values("views", ascending=False).head(3)
        for idx, row in top3.iterrows():
            st.markdown(f"- {row['title']} | 조회수: {row['views']} | 좋아요: {row['likes']}", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # 평균 통계 카드
        st.markdown(f"""
        <div class="card">
        <h2>📊 평균 통계</h2>
        <p>평균 조회수: {int(df['views'].mean())}</p>
        <p>평균 좋아요 수: {int(df['likes'].mean())}</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.error("채널 ID를 URL에서 추출할 수 없습니다. 올바른 링크를 입력하세요.")
