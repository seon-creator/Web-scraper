from playwright.sync_api import sync_playwright
import time

# 시작점: Playwright 세션을 시작합니다.
p = sync_playwright().start()

# 브라우저 인스턴스 생성: Playwright를 통해 Chromium 브라우저를 헤드리스 모드가 아닌 상태로 실행합니다.
browser = p.chromium.launch(headless=False)

# 새 페이지 열기: 브라우저에서 새로운 탭을 엽니다.
page = browser.new_page()

# 웹사이트로 이동: 원티드 홈페이지로 이동합니다.
page.goto("https://www.wanted.co.kr/")
# 페이지가 완전히 로드될 때까지 기다립니다.
time.sleep(2)

# 검색 버튼 클릭: 페이지의 특정 검색 버튼을 클릭합니다.
page.click("button.Aside_searchButton__Xhqq3")
# 클릭 반응을 기다립니다.
time.sleep(2)

# 검색어 입력: 검색창에 'flutter'를 입력합니다.
page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
# 입력 반응을 기다립니다.
time.sleep(2)

# 엔터 키 입력: 검색을 위해 키보드 엔터 키를 누릅니다.
page.keyboard.down("Enter")
# 검색 결과 로드를 기다립니다.
time.sleep(3)

# 포지션 탭 클릭: 검색 결과에서 '포지션' 탭을 클릭합니다.
page.click("a#search_tab_position")
# 탭 전환을 기다립니다.
time.sleep(3)

# 페이지 아래로 스크롤: 결과 페이지를 아래로 세 번 스크롤합니다.
for i in range(3):
    # End 키를 눌러 페이지 맨 아래로 스크롤합니다.
    page.keyboard.down("End")
    # 스크롤 후 내용 로드를 위해 잠시 기다립니다.
    time.sleep(3)
