def solve (exp):
    ### Determine power of expression ###
    ind=[0]
    if '**' in exp:
        while '**' in exp[ind[-1]:len(exp)+1] and ind[-1]+2<len(exp)-1:
            ind.append(exp.find('**',ind[-1],len(exp))+2)
            print(ind)
        order=0
        for i in ind:
            if i>order:
                order=int(exp[i])
    elif 'x' in exp:
        order=1
    else:
        order=0
        return False
    print('order='+str(order))
        
    ######################################
    xtol=1/order
    ytol=0.1*order
    min_abs_y=10**5
    i=0
    while min_abs_y>ytol:
        x1=0
        x2=x1+xtol
        x3=x1
        x4=x3-xtol
        xlist=[x1,x2,x3,x4]
        roots=[]
        j=0
        while j<10**4/(xtol):
            ylist=[eval(exp) for x in xlist]
            for y_ind in range(0,len(ylist)):
                if ylist[y_ind]==0:
                    roots.append(xlist[y_ind])
            if ylist[0]*ylist[1]<0:
                roots.append((xlist[0]+xlist[1])/2)
            if ylist[2]*ylist[3]<0:
                roots.append((xlist[2]+xlist[3])/2)
            xlist[0]=xlist[1]
            xlist[1]=xlist[0]+xtol
            xlist[2]=xlist[3]
            xlist[3]=xlist[2]-xtol
            j=j+1
        i=i+1
        y=[eval(exp) for x in roots]
        abs_y=[-1*x if x<0 else x for x in y]
        min_abs_y=abs_y[0]
        for k in range(1,len(abs_y)):
            if abs_y[k]<min_abs_y:
                min_abs_y=abs_y[k]
        xtol=xtol/order
        print(roots)
    roots_temp=roots
    roots=[]
    for r in roots_temp:
        if r in roots:
            continue
        else:
            roots.append(r)
    roots_temp=roots
    return roots
