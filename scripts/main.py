n=200
start_sick=25
beta=0.1 #יחידות ליום
gama=0.05 #ימים
num_sick0=n*(start_sick/100)
print(num_sick0)
S=n+num_sick0
i=num_sick0
r=0
r=i*gama
S_cunt=0
file_a=open('results/CF_freq.fasta', 'w')
file_a.write("S\ti\tr\n")
file_a.write(f"{S}\t{i:.6f}\t{r:.6f}\n")
for inf in range(100):
    S_cunt=S-(i+r)
    if (S-(i+r))>(i+r): #לא ידוע איך להתעסק אם הסכומים זה לא נכון לצורה זאת
        i=i+i*beta
        r=i*gama
        file_a.write(f"{S_cunt}\t{i:.6f}\t{r:.6f}\n")
    else:
        i=S-(i+r)
        file_a.write(f"{S_cunt}\t{i:.6f}\t{r:.6f}\n")
        
if inf<99:
    r=i
    i=0
    file_a.write(f"{S_cunt}\t{i:.6f}\t{r:.6f}\n")