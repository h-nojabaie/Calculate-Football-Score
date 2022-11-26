# آزمون تستی
# external link:https://quera.org/contest/assignments/44345/problems/148511
q_num=int(input())
correct_ans=str(input())
paper_num=int(input())
students_exam=[]
for i in range(paper_num):
    qus=[]
    for j in range(q_num):
        qus.append(str(input()))
    students_exam.append(qus)
# print(students_exam)
        
t=int(0)
f=int(0)
for stu in students_exam:
    t=int(0)
    f=int(0)
    for i in range(len(stu)):
        if ("#" not in stu[i]):
            continue;
        if ((stu[i]=="#000" and correct_ans[i]=="A") or (stu[i]=="0#00" and correct_ans[i]=="B") or (stu[i]=="00#0" and correct_ans[i]=="C") or (stu[i]=="000#" and correct_ans[i]=="D")):
            t=t+1
        else:
            f=f+1
    print(t*3-f)
            
