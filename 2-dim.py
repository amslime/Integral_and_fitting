import numpy as np
# z = a * x * x + b * x * y + c * y * y + d * x + e * y + f
# SSz = S ( S (a * x * x + b * x * y + c * y * y + d * x + e * y + f) dx) dy
# S (a * x * x + b * x * y + c * y * y + d * x + e * y + f) dx =
#     a/3 * x^3 +  by/2 * x^2 + cy^2 * x + d/2 * x^2 + eyx + fx  | r_x,l_x =
#     a/3 * (r_x^3 - l_x^3) + d/2 * (r_x^2 - l_x^2) + f * (r_x - l_x) +
#     by/2 (r_x^2 - l_x^2) + cy^2(r_x - l_x) + ey(r_x - l_x)

# let x_c = a/3 * (r_x^3 - l_x^3) + d/2 * (r_x^2 - l_x^2) + f * (r_x - l_x)
#     x_p2 = r_x^2 - l_x^2, x_p = r_x - l_x

# SSz = S (x_p * c * y^2 + b/2 * x_p2 * y + e*x_p*y + x_c) dy =
#   c * x_p / 3 * y^3 + (b/2 * x_p2 + e * x_p)/2 * y^2 + x_c * y | r_y, l_y


# z = a * x * x + b * x * y + c * y * y + d * x + e * y + f
# SSz = S ( S (a * x * x + b * x * y + c * y * y + d * x + e * y + f) dx) dy
def cal2DcurveIntegals(a, b, c, d, e, f, l_x, r_x, l_y, r_y):
    x_p3 = r_x**3 - l_x**3
    x_p2 = r_x**2 - l_x**2
    x_p = r_x - l_x
    x_c = a / 3.0 * x_p3 + d / 2.0 * x_p2 + f * x_p

    r_sum = c * x_p / 3.0 * (r_y ** 3) +  \
            (b / 2.0 * x_p2 + e * x_p) / 2.0 * (r_y ** 2) + \
            x_c * r_y

    l_sum = c * x_p / 3.0 * (l_y ** 3) +  \
            (b / 2.0 * x_p2 + e * x_p) / 2.0 * (l_y ** 2) + \
            x_c * l_y

    return r_sum - l_sum


def cal2DcurveIntegalsCheck(a, b, c, d, e, f, l_x, r_x, l_y, r_y, cut_x, cut_y):
    dx = (r_x - l_x) * 1.0 / cut_x
    dy = (r_y - l_y) * 1.0 / cut_y
    sum = 0;
    s_x = l_x + dx / 2.0
    for i in range(0, cut_x):
        s_y = l_y + dy / 2.0
        for j in range(0, cut_y):
            s_z = a * s_x * s_x + b * s_x * s_y + c * s_y * s_y \
                  + d * s_x + e * s_y + f
            sum += s_z * dx * dy
            s_y += dy
        s_x += dx

    return sum

print cal2DcurveIntegals(1, 1, -2, 15 ,2 ,1, 0, 1, 0, 1)
print cal2DcurveIntegalsCheck  (1, 1, -2, 15 ,2 ,1, 0, 1, 0, 1, 100, 100)
