import streamlit as st

st.title('최상위 수학 4-2')
st.subheader('level up test 13-14')

corrects = ['다가라나', '1:46:40', '3+4/7', '15+1/9', '1+10/12', '15']
problems = ['10', '11: 시간:분:초','12: 숫자+숫자/숫자','13: 숫자+숫자/숫자','14: 숫자+숫자/숫자','15: 숫자+숫자/숫자']
answers = []

for i in range(len(problems)):
    form = st.form(problems[i])
    answers.append(form.text_input(problems[i]))

    if answers[i] == corrects[i]:
        form.write('good job')
    else:
        form.write('sorry, try again')

    form.form_submit_button("Submit")

if corrects == answers:
    st.balloons()