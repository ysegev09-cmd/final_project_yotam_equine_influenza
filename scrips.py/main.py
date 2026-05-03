n=200
start_sick=25
beta=10 #יחידות ליום
gama=5 #ימים
num_sick0=n*(start_sick/100)
print(num_sick0)
S=n
i=num_sick0
r=o
R0=beta/gama
r=i*gama
file_a=open('results/CF_freq.fasta', 'w')
file_a.write("Generation\tFreq_c\tFreq_CC\tFreq_Cc\tFreq_cc\n")!
file_a.write(f"{i}\t{q:.6f}\t{freq_CC:.6f}\t{freq_Cc:.6f}\t{freq_cc:.6f}\n")