def  sir_projact(n,S,i,r,I_total,r_total): # מדמה ההדבקה
    beta=0.2 #יחידות ליום
    gama=0.01 #ימים
    for days in range(50): # לולאה של כמות הימים 
        file_a.write(f"{days}\t{round(S,2):.6f}\t{round(I_total,2):.6f}\t{round(r_total,2):.6f}\n")
        i=(beta*i*S)/n # חישובים של המקדמים
        r=I_total*gama
        if S<i: # תנאי לכדי לוודא להמקדם של נדבקים חדשים לא עולה על הכמות שיכולה לחלות
            i=S
        if r>I_total: # תנאי לוודא שכמות המחלימים לא עולה על הכמות שיכולה להחלים
            r=I_total
        S=S-i  # עדכון הפרמטרים אשר אנו מחפשים
        I_total=I_total+i-r
        r_total=r_total+r 


n=200   # הגדרת משתנים
start_sick=25
num_sick0=n*(start_sick/100)
S=n-num_sick0
i=num_sick0
r=0
I_total=0
I_total=I_total+i-r
r_total=0
file_a=open('results/situ_update.py', 'w')
file_a.write("On_day\tS\tI_total\tr_total\n")

Haracha=sir_projact(n,S,i,r,I_total,r_total)
file_a.close()