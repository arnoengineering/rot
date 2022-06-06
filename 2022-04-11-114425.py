def disp_merc()

def rot_z(th):
    return [[cos(th),-sin(th), 0],
           [sin(th),cos(th), 0],
           [0, 0, 1]]

def rot_y(th):
    [[cos(th), 0, sin(th)],
     [0, 1, 0],
     [-sin(th), 0, cos(th)]

def rot_x(th):
     return[[1, 0, 0],
           [0, cos(th), -sin(th)],
           [0, sin(th), cos(th)]]


def solve(point):
    """ a = 2
     b = 3
     k = 6
    k**2 = (point[0]**2 +point[1]**2)/a + point[2]**2/b
    x**2+y**2=r**2
    k**2=r**2/a+point[2]**2/b"""
      a = 2
     b = 3
     k = 6
    z = sqrt(k**2*b - (point[0]**2 +point[1]**2)*b/a)
    "gess z"
     return z
def calc_point_3d(x,y,surf):
    alpha = surf.ang
    beta = surf.ang2
    gamma = surf.ang3
    v = np.array([x,y,0])
    
    point_eq = rot_z(alpha) @ rot_y(beta) @ rot_x(gamma) @ v.T
    sol = surf.solve(point_eq[:2])
    return sol

def calc_r_thea()
     return r, th, phi
     
def draw(r, th):
     ra = np.linspace(0,2*pi)
     for i in range(2):
       replace theta,phi with linpace hold other still

     p = r*[cos(th[]),sintheta*sin(phia),cos(phia)]theta]
    draw line from all opints


def on_click()
setpoint
drawpoint
if close to point:
    dont set, select
    can del
if one already set:
    set second
    then draw
    
can draw puting in coords
if coords slill sraw lines

for point:
    pout same points lines on other projection or vise versea
    rightclick sets new eq center
    on project if country select show size if scaled from new eq

def drag()
rotate






















