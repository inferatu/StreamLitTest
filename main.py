import streamlit as st


def calculate(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return 'Нельзя делить на 0'
    except ZeroDivisionError:
        return 'Нельзя делить на 0'


def main():
    st.title('Simple Calculator')

    num1 = st.number_input('Enter first number')
    num2 = st.number_input('Enter second number')
    operator = st.selectbox('Select operator', ['+', '-', '*', '/'])

    if st.button('Calculate'):
        result = calculate(num1, num2, operator)
        st.success(f'Result: {result}')


if __name__ == '__main__':
    main()
