n=eval(input())
s=input()
st=[]
for i in n:
    if i.startswith(s)==True:
        st.append(i)
print(st)        
