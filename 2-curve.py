import numpy as np

# least squares method
# e = axx + bxy + cyy + dx + ey + f - z

# min sum(e^2)

# aX^4 + bX^3Y + cX^2Y^2 + dX^3 + eX^2Y + fX^2 = ZX^2

# x^2, xy, y^2, x, y, 1, -1 

def mean(tuples, xt, yt, zt):
    n = len(tuples)
    sum = 0;
    for i in range(0, n):
        sum += tuples[i][0]**xt + tuples[i][1]**yt + tuples[i][2]**zt
    sum = sum * 1.0 / n
    return sum




def createMatrix(tuples):
    m1 = np.array([[2,0,0],[1,1,0],[0,2,0],[1,0,0],[0,1,0],[0,0,0]])
    m = []
    for i in range(0, 6):
        m_s1 = m1 + m1[i]
        for j in range(0, 6):
            m.append(mean(tuples, m_s1[j][0],m_s1[j][1], m_s1[j][2]))
    m_n = np.asmatrix(np.array(m).reshape(6,6))
    #print m_n
    return m_n

def createArray(tuples):
    m1 = np.array([[2,0,1],[1,1,1],[0,2,1],[1,0,1],[0,1,1],[0,0,1]])
    m = []
    for j in range(0, 6):
        m.append(mean(tuples, m1[j][0],m1[j][1], m1[j][2]))
    return np.array(m)


def solve(tuples):
    mat1 = createMatrix(tuples)
    arr1 = createArray(tuples)
    return np.linalg.solve(mat1, arr1)

def check(x, y, z, ans):
    z1 = ans[0] * x * x + ans[1] * x * y + ans[2] * y * y +  \
         ans[3] * x + ans[4] * y + ans[5]
    print (z, z1)
    


tuples = [(6, 5, 8), (4, 1, 7), (3,9,2)]

print mean(tuples, 2, 0, 1)

a = np.array([1,2,3])
b = np.array([4,5,6])
#print np.append(a,b).reshape(3,2)

m1 = np.array([[2,1,1],[2,0,1]])
#print m1 + np.array([1,1,1])

ans = solve(tuples)
