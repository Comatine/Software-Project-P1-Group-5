import tkinter as tk

# 메인 윈도우 생성
window = tk.Tk()
window.title("☆ 청춘 일상 다이어트 총력전 ☆")
# place 레이아웃 고정을 위해 창 크기 변경을 제한합니다.
window.geometry("600x820")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

# 전체적인 폰트 스타일 정의
FONT_REGULAR = ("Malgun Gothic", 11)
FONT_BOLD = ("Malgun Gothic", 11, "bold")
FONT_RESULT = ("Malgun Gothic", 14, "bold")

# --- 1. 상단 입력 영역 (X좌표 라벨: 25, 입력필드: 140) ---

# 날짜
lbl_date = tk.Label(window, text="날짜 :", font=FONT_REGULAR, bg="#f0f0f0", anchor="w")
lbl_date.place(x=25, y=25, width=100, height=30)

entry_date = tk.Entry(window, font=FONT_REGULAR, bd=1, relief="sunken")
entry_date.insert(0, "2026-09-05")
entry_date.place(x=140, y=25, width=190, height=30)

btn_search = tk.Button(
    window, text="조회", font=FONT_REGULAR, bg="#e0e0e0", relief="raised"
)
btn_search.place(x=345, y=25, width=80, height=30)

# 음식명
lbl_food = tk.Label(
    window, text="음식명 :", font=FONT_REGULAR, bg="#f0f0f0", anchor="w"
)
lbl_food.place(x=25, y=70, width=100, height=30)

entry_food = tk.Entry(window, font=FONT_REGULAR, bd=1, relief="sunken")
entry_food.insert(0, "밥")
entry_food.place(x=140, y=70, width=285, height=30)

# 섭취 칼로리
lbl_cal = tk.Label(
    window, text="섭취 칼로리 :", font=FONT_REGULAR, bg="#f0f0f0", anchor="w"
)
lbl_cal.place(x=25, y=115, width=100, height=30)

entry_cal = tk.Entry(window, font=FONT_REGULAR, bd=1, relief="sunken")
entry_cal.insert(0, "300")
entry_cal.place(x=140, y=115, width=190, height=30)

lbl_unit1 = tk.Label(window, text="kcal", font=FONT_REGULAR, bg="#f0f0f0", anchor="w")
lbl_unit1.place(x=345, y=115, width=50, height=30)

# 식사 시간
lbl_time = tk.Label(
    window, text="식사 시간 :", font=FONT_REGULAR, bg="#f0f0f0", anchor="w"
)
lbl_time.place(x=25, y=160, width=100, height=30)

selected_time = tk.StringVar(value="점심")
opt_time = tk.OptionMenu(window, selected_time, "아침", "점심", "저녁", "야식")
opt_time.config(font=FONT_REGULAR, bg="white", indicatoron=True, relief="groove")
opt_time.place(x=140, y=160, width=285, height=30)


# --- 2. 식단 등록 / 식단 삭제 버튼 영역 ---
btn_add = tk.Button(window, text="식단 등록", font=FONT_REGULAR, bg="#e0e0e0")
btn_add.place(x=25, y=210, width=270, height=35)

btn_del = tk.Button(window, text="식단 삭제", font=FONT_REGULAR, bg="#e0e0e0")
btn_del.place(x=305, y=210, width=270, height=35)


# --- 3. 중하단 프레임 그룹 (LabelFrame 및 내부 요소 전체 place 처리) ---

# 식단 기록 섹션
lf_record = tk.LabelFrame(window, text="식단 기록", font=FONT_REGULAR, bg="#f0f0f0")
lf_record.place(x=25, y=265, width=550, height=140)

record_text = (
    " 아침 : 계란 / 150 kcal\n 점심 : 밥 / 300 kcal\n 저녁 : 없음\n 야식 : 없음"
)
lbl_record_content = tk.Label(
    lf_record,
    text=record_text,
    font=FONT_REGULAR,
    bg="white",
    anchor="nw",
    justify="left",
    relief="sunken",
    bd=1,
    padx=10,
    pady=8,
)
# LabelFrame 내부에서의 상대 좌표 배치
lbl_record_content.place(x=15, y=10, width=516, height=100)


# 체중 섹션
lf_weight = tk.LabelFrame(window, text="체중", font=FONT_REGULAR, bg="#f0f0f0")
lf_weight.place(x=25, y=420, width=550, height=75)

lbl_w = tk.Label(lf_weight, text="체중 : ", font=FONT_REGULAR, bg="#f0f0f0")
lbl_w.place(x=15, y=12, width=50, height=30)

entry_weight = tk.Entry(lf_weight, font=FONT_REGULAR, bd=1, relief="sunken")
entry_weight.insert(0, "92.3")
entry_weight.place(x=70, y=12, width=190, height=30)

lbl_unit2 = tk.Label(lf_weight, text="kg", font=FONT_REGULAR, bg="#f0f0f0", anchor="w")
lbl_unit2.place(x=270, y=12, width=50, height=30)

btn_weight_save = tk.Button(
    lf_weight, text="체중 저장", font=FONT_REGULAR, bg="#e0e0e0"
)
btn_weight_save.place(x=380, y=10, width=150, height=32)


# 일일 총 섭취 칼로리 섹션
lf_total_cal = tk.LabelFrame(
    window, text="일일 총 섭취 칼로리", font=FONT_REGULAR, bg="#f0f0f0"
)
lf_total_cal.place(x=25, y=510, width=550, height=75)

lbl_total_cal_val = tk.Label(
    lf_total_cal,
    text=" 450 / 1800 kcal",
    font=FONT_REGULAR,
    bg="white",
    anchor="w",
    relief="sunken",
    bd=1,
    padx=10,
)
lbl_total_cal_val.place(x=15, y=10, width=516, height=35)


# 최근 체중 변화 섹션
lf_weight_chg = tk.LabelFrame(
    window, text="최근 체중 변화", font=FONT_REGULAR, bg="#f0f0f0"
)
lf_weight_chg.place(x=25, y=600, width=550, height=95)

chg_text = " 7일 전 93.1 kg → 현재 92.3 kg\n 0.8 kg 감소"
lbl_weight_chg_val = tk.Label(
    lf_weight_chg,
    text=chg_text,
    font=FONT_REGULAR,
    bg="white",
    anchor="nw",
    justify="left",
    relief="sunken",
    bd=1,
    padx=10,
    pady=5,
)
lbl_weight_chg_val.place(x=15, y=10, width=516, height=55)


# 결과 섹션
lf_result = tk.LabelFrame(window, text="결과", font=FONT_REGULAR, bg="#f0f0f0")
lf_result.place(x=25, y=710, width=550, height=75)

lbl_result_val = tk.Label(
    lf_result,
    text="목표 달성 성공!",
    font=FONT_RESULT,
    fg="green",
    bg="#e8f5e9",
    highlightthickness=1,
    highlightbackground="green",
)
lbl_result_val.place(x=15, y=10, width=516, height=35)

# 프로그램 실행
window.mainloop()


# https://share.google/aimode/Z9p91uF0gCXxIZlJe
# ai 사용 내역 7일동안만 유효
# 기본 배치도를 저렇게 하고 gui_manager에다가 다시 맞추어서 삽입
