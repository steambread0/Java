def wordPattern(pattern, str):
    s=[]
    left=0
    for i in range(len(str)):
        right=i
        if str[i]==' ':
            s.append(str[left:right])
            left=i+1
        elif i==len(str)-1:
            s.append(str[left:(right+1)])
    if len(s)!=len(pattern):
        return(False)
    else:
    	dc={}
    	k=True
    	for i in range(len(pattern)):
        	if pattern[i] in dc:
        		if dc[pattern[i]]!=s[i]:
        			k=False
        			break
        	else:
        		dc[pattern[i]]=s[i]
		values=list(dc.values())
		for i in range(len(values)):
			if values.count(values[i])>1:
				k=False
				break
    return(k)

pattern='abba'
str='ab ac ac ab'
print(wordPattern(pattern,str))