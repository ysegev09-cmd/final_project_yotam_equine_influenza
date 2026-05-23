def  sir_projact(n,S,i,r,I_total,r_total):
    beta=0.2 #יחידות ליום
    gama=0.01 #ימים
    for days in range(50):
        file_a.write(f"{days}\t{round(S,2):.6f}\t{round(I_total,2):.6f}\t{round(r_total,2):.6f}\n")
        i=(beta*i*S)/n
        r=I_total*gama
        if S<i: 
            i=S
            S=0
        if r>I_total:
            r=I_total
            I_total=0
        S=S-i 
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