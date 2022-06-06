max_pop = 10
rate_grow = 2
x = np.linspace(0,1)
# todo find pop of pred-prey
y = r*x*(1-x)
    plot yf
x0 = 5
final_pop = []
year_cnt = linspace(0,30): # todo can change to stable
    
    # exersize
    book
    
for r in linspace(0.1,30):
    x_ls = [x0]
    for t in range(len_near):
        xi= x_ls[-1]
        x_ls.append(r*xi*(1-xi))  # stable pop, todo lim stablizes
    final_pop.append(x_ls[-1])
    plot(year_cnt, x_ls)
plot(r,final_pop)
    plot yf
    
dy/dt=(x/y)
dx/dt = y/x
plot x,y