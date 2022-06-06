h=200
v_s = 340
v = 360
v2 = 200
dt = 0.1

pers_l = 100
pix_met = 5

def draw_t():
    painter.eraseRect(self.rect())
    dt_tot = 10  # todo fix, len
    for n, ii in enumerate(x_p):
        dt_p = dt_tot - n*dt
        r=v_s*dt_p
        painnter.drawPoint(ii,h)  # todo diff color
        painnter.DrawElipse(ii,h,r,r)
        if v>vs:  # todo find tan, angle
            ang = np.arcsin(v/vs)
        # drawline fromlast point to full at angle
    

x_p = []

for i in np.arange(0,10,dt):
    dx = i*v
    x_p.append(dx)
    draw_t()