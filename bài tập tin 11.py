n=input()
s=0

                if i!=o:
                    if n[i]==n[o]:
                        n=n[:o]+n[o+1:]
                        s=s+1
print(n)

