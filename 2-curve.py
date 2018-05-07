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
        sum += tuples[i][0]**xt * tuples[i][1]**yt  * tuples[i][2]**zt
    sum = sum * 1.0 / n
    print sum
    return sum




def createMatrix(tuples):
    m1 = np.array([[2,0,0],[1,1,0],[0,2,0],[1,0,0],[0,1,0],[0,0,0]])
    m = []
    for i in range(0, 6):
        m_s1 = m1 + m1[i]
        print m_s1
        for j in range(0, 6):
            m.append(mean(tuples, m_s1[j][0],m_s1[j][1], m_s1[j][2]))
    m_n = np.asmatrix(np.array(m).reshape(6,6))
    print m_n
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
    print mat1, arr1
    return np.linalg.solve(mat1, arr1)

def check(x, y, z, ans):
    z1 = ans[0] * x * x + ans[1] * x * y + ans[2] * y * y +  \
         ans[3] * x + ans[4] * y + ans[5]
    print (z, z1)
    



def testEqu(x, y):
    return (x, y, x * x + 2 * y * y - 3 * x * y + 4)

# z = x^2 + 2y^2 - 3xy + x + 1
tuples = [testEqu(1,2), testEqu(3,5), testEqu(9,3), testEqu(14,5), testEqu(27,6), testEqu(68,13), testEqu(13,21), testEqu(66, 63), testEqu(32,51)]
ans = solve(tuples)
print ans
t1 = testEqu(54,43)
check(t1[0], t1[1], t1[2],  ans)
