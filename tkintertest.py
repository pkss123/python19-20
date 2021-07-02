# gui프로그래밍을 위한 tkinter 임포트
from tkinter import *

# 창 만들고 유지하기
root = Tk()

# 창 크기 설정
root.configure(width="75m", height="100m")

# 함수 배치 부분
def test():
    print("Hello Python")
    
def test2():
    value = E1.get()
    print(value)

def exchange():
    value = int(E1.get())
    result = value / 38.61
    print("원화" + str(value) + "원 : " + str(result)+ "NTD 입니다")

def onselect(evt):
    w = evt.widget
    index = w.curselection()
    value = w.get(index)
    print(index, value)
    
# 창 부품 배치부분
Button(root, text="테스트버튼",command="test").place(
    x = 10, y = 10, width = 100, height = 30)

Button(root, text="entry버튼",command="test2").place(
    x = 150, y = 10, width = 100, height = 30)

Button(root, text="환율 버튼",command=exchange).place(
    x = 10, y = 60, width = 100, height = 30)

Button(root, text="환율 버튼",command=exchange).place(
    x = 850, y = 60, width = 100, height = 30)

E1 = Entry(root)
E1.place(x = 10, y = 130, width = 100, height = 30)

L1 = Listbox(root)
L1.place(x = 130, y = 130, width = 100, height = 150)
L1.insert(0, "치킨")
L1.insert(1, "족발")
L1.insert(2, "라면")

# Listbox의 이벤트 세팅
L1.bind('<<ListboxSelect>>', onselect)

Lb1 = Label(root, text="메뉴판")
Lb1.place(x = 130, y = 110, width = 100, height = 20)

Sb1 = Spinbox(root, from_=1, to=5)
Sb1.place(x = 10, y = 170, width = 100, height = 30)

option1 = ["파이썬", "자바", "C++"] # 옵션에 넣을것들
variable = StringVar(root)
variable.set(option1[1]) # 메뉴창에 초기에 설정된 값은 "파이썬"
op1=OptionMenu(root, variable, *option1)
op1.place(x = 10, y = 210, width = 100, height = 35)

# gui 프로그래밍의 마지막 지점에 항상 작성되어 있어야 한다
root.mainloop()