n=200
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
file_a=open('results/CF_freq.fasta', 'w')
file_a.write("S\ti\tr\n")
file_a.write(f"{S}\t{i:.6f}\t{r:.6f}\n")
for days in range(100):
    S=S-i 
    i=(beta*i*S)/n
    r=I_total*gama
    if S>i: #לא ידוע איך להתעסק אם הסכומים זה לא נכון לצורה זאת
        I_total=I_total+i-r
        r_total=r_total+r
        file_a.write(f"{S}\t{i:.6f}\t{r:.6f}\n")
    else:
        i=S-(i+r)
        file_a.write(f"{S}\t{i:.6f}\t{r:.6f}\n")
        break
      
if days<99: # אולי אפשר להעביר את זה אל הלולאה
    r=i
    i=0
    file_a.write(f"{S}\t{i:.6f}\t{r:.6f}\n")
   