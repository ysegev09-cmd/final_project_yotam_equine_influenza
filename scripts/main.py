def  sir_projact(n,beta,gama,S,i,r,I_total,r_total):
    for days in range(10):
        file_a.write(f"{days}\t{round(S,2):.6f}\t{round(I_total,2):.6f}\t{round(r_total,2):.6f}\n")
        i=(beta*i*S)/n
        r=I_total*gama
        if S<i: 
            i=S
        if r>I_total:
            r=I_total
        S=S-i 
        I_total=I_total+i-r
        r_total=r_total+r 


n=300   # הגדרת משתנים
start_sick=10
beta=0.5 #יחידות ליום
gama=0.2 #ימים
num_sick0=n*(start_sick/100)
S=n-num_sick0
i=num_sick0
r=0
I_total=0
I_total=I_total+i-r
r_total=0
file_a=open('results/situ_update.py', 'w')
file_a.write("On_day\tS\tI_total\tr_total\n")

Haracha=sir_projact(n,beta,gama,S,i,r,I_total,r_total)
