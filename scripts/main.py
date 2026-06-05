def  sir_projact(n,num_sick0,gama,beta): # מדמה ההדבקה
    S=n-num_sick0 # חישוב הלא חולים
    new_infected=num_sick0 # הגדרת הפרמטרים לחישוב
    r=0
    sick_today=0
    I_total=I_total+new_infected-r
    r_total=0
    i_max=0
    day_max=0
    for days in range(50): # לולאה של כמות הימים 
        file_a.write(f"{days}\t{round(S,2):.6f}\t{round(I_total,2):.6f}\t{round(r_total,2):.6f}\n")
        new_infected=(beta*i*S)/n # חישובים של המקדמים
        r=I_total*gama
        print(new_infected)
        if S<new_infected: # תנאי לכדי לוודא להמקדם של נדבקים חדשים לא עולה על הכמות שיכולה לחלות
            new_infected=S
        if r>I_total: # תנאי לוודא שכמות המחלימים לא עולה על הכמות שיכולה להחלים
            r=I_total
        if i_max<new_infected:
            i_max=new_infected
            day_max=days
        S=S-new_infected  # עדכון הפרמטרים אשר אנו מחפשים
        I_total=I_total+new_infected-r
        r_total=r_total+r 
        hakef=(100*(I_total+r_total))/n
    file_a.write("hakef\tday max\tI_max\tbeta\tgamma\tstart sick\tall donkys\n")
    file_a.write(f"{round(hakef,2)}\t{day_max:.6f}\t{round(i_max,2):.6f}\t{beta:.6f}\t{gama:.6f}\t{num_sick0:.6f}\t{round(n,2):.6f}\n")



n=1000  # הגדרת משתנים
start_sick=5
num_sick0=n*(start_sick/100) # חישוב כמה האחוז שאנו נעבוד איתו מהכמות הכוללת
beta=0.75 #יחידות ליום
gama=0.2 #ימים
file_a=open('results/situ_update.py', 'w')
file_a.write("On_day\tS\tI_total\tr_total\n")
Haracha=sir_projact(n,num_sick0,gama,beta)
file_a.close()