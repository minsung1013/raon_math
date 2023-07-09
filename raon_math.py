import streamlit as st

st.title('최상위 수학 4-2')

mon = '월요일 PAGE 28-30'
corrects = ['99', '4/9', '3+1/4', '7', '31', '6/19,9/19,14/19', '103']
problems = ['2','3','4','5','6','7','8',]

tue = '화요일_PAGE 34-37'
corrects_tue = ['18','둔각삼각혁','4','7','45', '120', '110','4','60','12','80']
problems_tue = ['1-4', '1-5', '1-6', '2-1-(1)', '2-1-(2)', '2-2', '2-3', '2-4', '2-5-(1)', '2-5-(2)','2-6']

wed = '수요일_PAGE 38-41'
corrects_wed = ['65','7','25','80','12','70','150','6','105','55','35','60']
problems_wed = ['1-1','1-2','1-3','2-1','2-2','2-3','3-1','3-2','3-3','4-1','4-2','4-3']

thu = "목요일_PAGE 42-44"
corrects_thu = ['84','44','9','7','16','16','6','68','68','360']
problems_thu = ['5-1','5-2','5-3','6-1','6-2','6-3', '심화7_1','심화7_2','심화7_3', '7']

fri = "금요일_PAGE 45-48 Level up Test"
corrects_fri = ['29','100','4','38','85','12','8','38','232','70','64','540','20' ]
problems_fri = ['1','2','3','4','5','6: 긴 변','6: 짧은 변','7','8','9','10','11','12']

with st.expander(mon):
    answers = []
    if len(corrects) != len(problems):
        st.write('프로그램에 에러가 있습니다. 관리자에게 문의하세요')

    for i in range(len(problems)):
        form = st.form(problems[i] + 'mon')
        answers.append(form.text_input(problems[i]))

        if answers[i] == corrects[i]:
            form.subheader('good job')
        else:
            form.write('sorry, try again')

        form.form_submit_button("Submit")

    if corrects == answers:
        st.balloons()


with st.expander(tue):
    answers_tue = []
    if len(corrects_tue) != len(problems_tue):
        st.write('프로그램에 에러가 있습니다. 관리자에게 문의하세요')

    for i in range(len(problems_tue)):
        form = st.form(problems_tue[i] + 'tue')
        answers_tue.append(form.text_input(problems_tue[i]))

        if answers_tue[i] == corrects_tue[i]:
            form.subheader('good job')
        else:
            form.write('sorry, try again')

        form.form_submit_button("Submit")

    if corrects_tue == answers_tue:
        st.balloons()


with st.expander(wed):
    answers_wed = []
    if len(corrects_wed) != len(problems_wed):
        st.write('프로그램에 에러가 있습니다. 관리자에게 문의하세요')

    for i in range(len(problems_wed)):
        form = st.form(problems_wed[i] + 'wed')
        answers_wed.append(form.text_input(problems_wed[i]))

        if answers_wed[i] == corrects_wed[i]:
            form.subheader('good job')
        else:
            form.write('sorry, try again')

        form.form_submit_button("Submit")

    if corrects_wed == answers_wed:
        st.balloons()


with st.expander(thu):
    answers_thu = []
    if len(corrects_thu) != len(problems_thu):
        st.write('프로그램에 에러가 있습니다. 관리자에게 문의하세요')

    for i in range(len(problems_thu)):
        form = st.form(problems_thu[i] + 'thu')
        answers_thu.append(form.text_input(problems_thu[i]))

        if answers_thu[i] == corrects_thu[i]:
            form.subheader('good job')
        else:
            form.write('sorry, try again')

        form.form_submit_button("Submit")

    if corrects_thu == answers_thu:
        st.balloons()

with st.expander(fri):
    answers_fri = []
    if len(corrects_fri) != len(problems_fri):
        st.write('프로그램에 에러가 있습니다. 관리자에게 문의하세요')

    for i in range(len(problems_fri)):
        form = st.form(problems_fri[i] + 'fri')
        answers_fri.append(form.text_input(problems_fri[i]))

        if answers_fri[i] == corrects_fri[i]:
            form.subheadere('good job')
        else:
            form.write('sorry, try again')

        form.form_submit_button("Submit")

    if corrects_fri == answers_fri:
        st.balloons()