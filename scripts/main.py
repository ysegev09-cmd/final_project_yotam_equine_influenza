def  sir_projact(n,num_sick0,gama,beta): # מדמה ההדבקה
    S=n-num_sick0 # חישוב הלא חולים
    i=num_sick0 # הגדרת הפרמטרים לחישוב
    r=0
    I_total=0
    I_total=I_total+i-r
    r_total=0
    i_max=0
    day_max=0
    for days in range(50): # לולאה של כמות הימים 
        file_a.write(f"{days}\t{round(S,2):.6f}\t{round(I_total,2):.6f}\t{round(r_total,2):.6f}\n")
        i=(beta*i*S)/n # חישובים של המקדמים
        r=I_total*gama
        print(i)
        if S<i: # תנאי לכדי לוודא להמקדם של נדבקים חדשים לא עולה על הכמות שיכולה לחלות
            i=S
        if r>I_total: # תנאי לוודא שכמות המחלימים לא עולה על הכמות שיכולה להחלים
            r=I_total
        if i_max<i:
            i_max=i
            day_max=days
        S=S-i  # עדכון הפרמטרים אשר אנו מחפשים
        I_total=I_total+i-r
        r_total=r_total+r 
    file_a.write("hakef\tday max\tI_max\tbeta\tgamma\tstart sick\tall donkys\n")
    print(I_total/2)
    file_a.write(f"{round(I_total/n,2)}\t{day_max:.6f}\t{round(i_max,2):.6f}\t{beta:.6f}\t{gama:.6f}\t{num_sick0:.6f}\t{round(n,2):.6f}\n")



n=1000  # הגדרת משתנים
start_sick=5
num_sick0=n*(start_sick/100) # חישוב כמה האחוז שאנו נעבוד איתו מהכמות הכוללת
beta=0.75 #יחידות ליום
gama=0.2 #ימים
file_a=open('results/situ_update.py', 'w')
file_a.write("On_day\tS\tI_total\tr_total\n")
Haracha=sir_projact(n,num_sick0,gama,beta)
file_a.close()