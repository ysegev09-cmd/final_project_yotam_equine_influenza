def  sir_projact(n,beta,gama,S,i,r,I_total,r_total):
    for days in range(100):
        file_a.write(f"{days}\t{S:.6f}\t{I_total:.6f}\t{r_total:.6f}\n")
        i=(beta*i*S)/n
        r=I_total*gama
        if S>i: 
            i=s
        if r>I_total:
            r=I_total
        S=S-i 
        I_total=I_total+i-r
        r_total=r_total+r 

n=200   # הגדרת משתנים
start_sick=25
beta=0.1 #יחידות ליום
gama=0.05 #ימים
num_sick0=n*(start_sick/100)
print(num_sick0)
S=n-num_sick0
i=num_sick0
r=0
r=i*gama
I_total=I_total=I_total+i-r
r_total=0
file_a=open('results/situ_update.py', 'w')
file_a.write("On_day\tS\tI_total\tr_total\n")
#file_a.write(f"{S}\t{i:.6f}\t{r:.6f}\n")

Haracha=sir_projact(n,beta,gama,S,i,r,I_total,r_total)
