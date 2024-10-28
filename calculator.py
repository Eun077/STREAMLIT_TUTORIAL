import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calculator():
    st.title("계산기")
    
    choice = st.radio("연산자 선택", ["덧셈", "뺄셈", "곱셈", "나눗셈"])
    
    num1 = st.number_input("첫 번째 숫자를 입력하세요:", format="%.2f")
    num2 = st.number_input("두 번째 숫자를 입력하세요:", format="%.2f")

    if st.button("계산하기"):
        if choice == "덧셈":
            result = add(num1, num2)
        elif choice == "뺄셈":
            result = subtract(num1, num2)
        elif choice == "곱셈":
            result = multiply(num1, num2)
        elif choice == "나눗셈":
            result = divide(num1, num2)
        
        st.write(f"결과: {result}")

if __name__ == "__main__":
    calculator()
