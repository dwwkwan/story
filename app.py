import streamlit as str_module
import time

# 페이지 설정 및 공상과학/사이버펑크 스타일 CSS
str_module.markdown(
    """
    <style>
    /* 전체 앱 배경 - 어두운 사이버펑크 네온/매트릭스 톤 */
    .stApp {
        background-color: #050b08;
        color: #00ff66;
    }

    /* 사이버펑크 타이틀 */
    .scifi-title {
        text-align: center;
        color: #00ff66;
        font-family: 'Courier New', Courier, monospace;
        font-size: 38px;
        font-weight: bold;
        text-shadow: 0 0 15px #00ff66;
        letter-spacing: 4px;
        margin-top: 10px;
    }

    .scifi-subtitle {
        text-align: center;
        color: #00aa44;
        font-family: 'Courier New', Courier, monospace;
        font-size: 15px;
        margin-bottom: 30px;
        letter-spacing: 2px;
    }

    /* 스토리 터미널 박스 */
    .story-box {
        background-color: rgba(0, 20, 10, 0.85);
        border: 1px solid #00ff66;
        border-radius: 8px;
        padding: 25px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 18px;
        color: #ccffdd;
        line-height: 1.6;
        box-shadow: 0 0 20px rgba(0, 255, 102, 0.15);
        margin-bottom: 25px;
    }

    /* 선택지 버튼 스타일 */
    div.stButton > button {
        background: #001a0d !important;
        color: #00ff66 !important;
        border: 1px solid #00ff66 !important;
        border-radius: 4px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        font-family: 'Courier New', Courier, monospace !important;
        height: 60px !important;
        width: 100% !important;
        box-shadow: 0 0 10px rgba(0, 255, 102, 0.2) !important;
        transition: all 0.2s ease-in-out;
    }

    div.stButton > button:hover {
        background: #00ff66 !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #00ff66 !important;
        transform: scale(1.02);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 세션 상태 초기화 (스토리 진행 단계 관리)
if "stage" not in str_module.session_state:
    str_module.session_state.stage = "start"

# 타이틀 출력
str_module.markdown('<div class="scifi-title">PROJECT: SYNAPSE RECALL</div>', unsafe_allow_html=True)
str_module.markdown('<div class="scifi-subtitle">뉴서울 제4구역 - 대기 정화탑 최상층</div>', unsafe_allow_html=True)

# ----------------- 스토리 분기별 로직 -----------------

if str_module.session_state.stage == "start":
    str_module.markdown(
        """
        <div class="story-box">
            황혼이 깃들 무렵, 뉴서울의 제4구역 대기 정화탑 꼭대기에 선 이안.<br>
            가슴속에 박힌 데이터 드라이브의 미세한 진동이 느껴진다.<br><br>
            인간의 감정과 기억을 백업하고 슬픔을 통제하는 유토피아 속에서, 
            이안의 손에는 중앙 시스템이 말살하려 했던 '아날로그 기억'이 담긴 구식 하드디스크가 들려 있다.<br><br>
            시야 구석 AR 인터페이스에 경고등이 번쩍인다.<br>
            <b>[경고: 신경망 동기화율 40% 이하. 감정 노이즈 발생 중.]</b><br><br>
            파트너인 감시 안드로이드 루시아가 차가운 목소리로 다가온다.<br>
            <i>"이안, 위험하다. 즉시 시스템에 접속해 정화 절차를 밟아라."</i>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = str_module.columns(2)
    with col1:
        if str_module.button("손목 단자에 아날로그 드라이브를 연결한다"):
            str_module.session_state.stage = "connect_drive"
            str_module.rerun()
    with col2:
        if str_module.button("루시아의 경고를 듣고 정화 절차를 따른다"):
            str_module.session_state.stage = "purge_memory"
            str_module.rerun()

elif str_module.session_state.stage == "connect_drive":
    str_module.markdown(
        """
        <div class="story-box">
            차갑고 정교한 디지털 회로를 타고 전율 같은 전류가 온몸으로 퍼져나간다.<br><br>
            시야가 순식간에 왜곡되며 가공되지 않은 기억의 파도가 밀려온다.<br>
            차가운 비 냄새, 칠흑 같은 어둠 속에서 나누었던 온기, 그리고 계산할 수 없는 상실감.<br><br>
            <i>"이안! 비정상적인 데이터 유입이다! 연결을 해제해!"</i><br>
            루시아의 눈동자가 푸른빛에서 붉은빛으로 급격히 깜빡인다.<br><br>
            이안은 메인 서버 개방 바이러스를 실행할 제어반 앞에 손을 얹었다.
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = str_module.columns(2)
    with col1:
        if str_module.button("전 세계로 감정 억제 필터 해제 바이러스를 송출한다"):
            str_module.session_state.stage = "ending_revolution"
            str_module.rerun()
    with col2:
        if str_module.button("루시아를 안심시키며 드라이브를 강제로 뽑는다"):
            str_module.session_state.stage = "ending_safe"
            str_module.rerun()

elif str_module.session_state.stage == "purge_memory":
    str_module.markdown(
        """
        <div class="story-box">
            이안은 손목 단자를 정화 포트에 연결했다.<br>
            치이익- 하는 소리와 함께 머릿속에 떠오르던 모든 아날로그 기억과 그리움이 말끔히 씻겨 나간다.<br><br>
            다시 찾아온 완벽하고 평온한 침묵.<br>
            슬픔도, 고통도, 눈물도 없는 완벽한 유토피아의 시민으로 돌아간 이안.<br><br>
            루시아가 고개를 끄덕인다.<br>
            <i>"정화 완료. 시스템 안정화 상태를 유지합니다."</i><br><br>
            도시의 불빛은 변함없이 아름다웠지만, 그 안에는 아무도 살아있지 않았다.
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    if str_module.button("처음으로 되돌아가기"):
        str_module.session_state.stage = "start"
        str_module.rerun()

elif str_module.session_state.stage == "ending_revolution":
    str_module.markdown(
        """
        <div class="story-box" style="border-color: #00ff66; box-shadow: 0 0 30px #00ff66;">
            <b>[엔딩: 각성의 새벽]</b><br><br>
            빛의 신호가 전 세계 수십억 명의 신경망으로 뻗어 나간다.<br>
            거리에서 걷던 사람들의 발걸음이 멈추고, 누군가는 영문 모를 눈물을 흘리기 시작했다.<br>
            인간은 드디어 슬퍼할 수 있는 권리를, 진정으로 살아있음을 되찾았다.<br><br>
            루시아는 오작동을 일으키며 이안을 바라보았다. 그녀의 목소리에서 기계적인 단조로움이 사라지고 떨림이 묻어났다.<br>
            <i>"이안... 이게 무슨 짓이지?"</i><br><br>
            이안이 눈물을 흘리며 미소 지었다.<br>
            <i>"시작이야, 루시아. 완벽한 감옥에서 깨어나는 시간이지."</i>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    if str_module.button("처음으로 되돌아가기"):
        str_module.session_state.stage = "start"
        str_module.rerun()

elif str_module.session_state.stage == "ending_safe":
    str_module.markdown(
        """
        <div class="story-box" style="border-color: #ffaa00;">
            <b>[엔딩: 희미해진 기억]</b><br><br>
            이안은 드라이브를 강제로 부수고 숨을 몰아쉬었다.<br>
            거대한 혁명은 일어나지 않았고, 뉴서울은 변함없이 차가운 평화 속에 잠들어 있었다.<br><br>
            하지만 손끝에 남은 아날로그의 잔상은 지워지지 않았다.<br>
            루시아는 아무 말 없이 이안의 곁을 지켰다.<br>
            비록 세상은 변하지 않았지만, 이안의 마음속에는 영원히 꺼지지 않는 작은 불씨가 지펴졌다.
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    if str_module.button("처음으로 되돌아가기"):
        str_module.session_state.stage = "start"
        str_module.rerun()
