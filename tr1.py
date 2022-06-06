#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt


# In[2]:


# sigularities
def sing(x,a,n):
    ni = np.zeros(x.size)
    for i in range(x.size):
        if x[i] >=a and n>=0:
            ni[i] = (x[i]-a)**n
    return ni

def lx(a,b,pc, l2,l3):

    a_p = np.math.factorial(a)
    b_p = np.math.factorial(b)
    return (1-pc)*m*sing(xx,0,a)/a_p-m/l2*sing(xx,l3,b)/b_p+m/l2*sing(xx,l3+l2,b)/b_p+pc*m*sing(xx,l1,a)/a_p


# In[3]:


#constants
l1 = 200
m = 18400
S = 5.61


# In[4]:


# predefined arrays
xx = np.linspace(0,200)
lii = np.linspace(10, 120, 15)


# In[ ]:





# In[17]:


o_m_l = []
max_loc = []
m_full = []
# loop through locations
for lis in lii:

    # initialize constants for each
    max_p = [[0,0]]
    l_f = []
    min_x_x = lis/40
    min_x = np.ceil((min_x_x, 10-min_x_x))/10
    # print('-minx: ', min_x)
    for p in np.arange(min_x[0],min_x[1],0.1):
        l4 = 200*p-lis/2  # calculates resulting length

        #singularity
        load = lx(0,1,p,lis,l4)
        mom = lx(1,2,p,lis,l4)

        sig = mom/(2*S)  # stress

        l_f.append([load, mom, sig])
        max_sig = np.max(np.abs(sig))

        max_p.append([p*1, max_sig*1])  # max stress for this loading condition and this location

    # tabulation of this location, and max of location
    max_p = np.array(max_p)
    m_full.append(l_f)
    m_n = np.argmax(max_p,0)
    m_a = max_p[m_n[1],:]

    # adding to list of all locs
    max_loc.append(max_p)
    o_m_l.append(m_a)

# max of all
o_m_l = np.array(o_m_l)
m_aa = np.argmax(o_m_l,0)

m_aaa = o_m_l[m_aa[1],:]

# max for each percent, len
for i in range(len(max_loc)):
    print(f'\n------------loading for Dis load len: {round(lii[i],1)}(in)')
    for ii in max_loc[i]:
        print(f'at rear load: {int(ii[0]*100)}% = Max \u03C3: {round(ii[1],2)}(psi)')
print(f'\n--------------------\n')

ni = 0
# max for each len
for i in o_m_l:
    print(f'max at len: {round(lii[ni],1)}(in), rear load: {int(i[0]*100)}%, \u03C3 = {round(i[1], 2)}(psi)')
    ni +=1
print(f'\n--------------------\noverall max at len(in): {round(lii[m_aa[1]], 2)}, rear load: {int(m_aaa[0]*100)}%,  \u03C3 = {round(m_aaa[1], 2)}(psi)')


# In[13]:


# SFD BMD, \u03C3 vs distance for each condition of len,percent

for ii in range(len(m_full)):
    fig, ax = plt.subplots(1,1)
    m_half_2 = m_full[ii]
    m_half = m_half_2[len(m_half_2)//2]

    ax.plot(xx,m_half[0])
    ax.plot(xx,m_half[1]*1e-2)
    ax.plot(xx,m_half[2]*1e-1)

    ax.legend(['Shear (lb)', 'Moment(100*lb*in)', 'Sigma (10*psi)'])
    fig.suptitle(f'Plots for len of load: {round(lii[ii],2)}(in)')
    ax.set_title('SFD BMD, \u03C3 allong trailer(in) for current loading')
    fig.show()

# init plots
title = ['\u03C3(psi) vs percentage rear load at max condition: for meadian length load', '\u03C3(psi) vs length load(in): for  median percent rear load']

fig, ax = plt.subplots(1,2)
#for same loc
ax[0].plot(max_loc[7][:,0], max_loc[7][:,1])

# for same per
ax[1].plot(lii,[i[i.shape[0]//2,1] for i in max_loc])

# for readbility
fig.suptitle('overall plots')
for iii in range(2):
    ax[iii].grid(True)
    ax[iii].set_title(title[iii])
fig.show()


# In[ ]:


for i in lii:
    print(i/400)


# In[ ]:




