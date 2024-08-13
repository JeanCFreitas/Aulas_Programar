nterms=15
n1, n2=0, 1
count=0
while (count<=nterms):
    nth=n1+n2
    n1=n2
    n2=nth
    print(f"{count}º termo:{nth}")
    count=count+1