# Dhava Gautama
# https://github.com/dhava-stmkg/interpolation

import numpy as np # Import modul numpy sebagai np
import sympy as sy # Import modul sympy sebagai sy
from tabulate import tabulate as tbl # Import sub-modul tabulate dari modul tabulate sebagai tbl

# Define t as symbol using sympy lib
t = sy.Symbol('t')

# Data
x = np.array([0, 10, 15, 20, 22.5, 30])
y = np.array([0, 227.04, 362.78, 517.35, 602.97, 901.67])
tabel = []
for i in range(len(x)):
    tabel.append([x[i],y[i]])
table = tbl(tabel, headers=['t(s)', 'v(t) (mm/s)'], tablefmt='orgtbl')
print(table)

# Function
def direct_method(x, y):
    vander_matrix = np.vander(x, increasing=False)  # Membuat matrix Vandermonde dengan menggunakan modul numpy
    coef = np.linalg.solve(vander_matrix, y)  # Menyelesaikan persamaan dengan modul numpy
    return coef  # Mengembalikan nilai koefisien


def newt_method(x, y):
    m = len(x)  # Mengambil jumlah data
    newt_table = np.zeros([m, m])  # Membuat matrix kosong dengan ukuran mxm
    newt_table[::, 0] = y  # Mengisi kolom pertama dengan nilai y
    for i in range(1, m):  # Loop kolom
        for j in range(m - i):  # Loop baris
            newt_table[j][i] = (newt_table[j + 1][i - 1] - newt_table[j][i - 1]) / (x[j + i] - x[j])  # Mengisi nilai tabel
    coef = newt_table[0]  # Koefisien berada pada baris pertama
    return coef  # Menembalikan nilai koefisien


# 4th order (quartic)
# Membutuhkan 5 titik, sedangkan pada data terdapat 6 titik, maka satu titik dihapus. Dihapus titik (0,0) karena jaraknya lebih jauh dari nilai yang akan dicari.
x = x[1:]  # x = [10,15,20,22.5,30]
y = y[1:]  # y = [227.04,362.78,517.35,602.97,901.67]
# Direct method
direct_coeficient_4 = direct_method(x, y)  # Menjalankan fungsi direct method dengan menggunakan data yang telah diubah.
direct_val_t_16_4 = np.polyval(direct_coeficient_4, 16)  # Mengevaluasi nilai v pada saat t = 16 menggunakan modul numpy
# Newton method
newton_ceficient_4 = newt_method(x, y)  # Menjalankan fungsi newton method dengan menggunakan data yang telah diubah.
newton_eq_4 = sy.simplify(newton_ceficient_4[0] + newton_ceficient_4[1] * (t - x[0]) + newton_ceficient_4[2] * (t - x[0]) * (t - x[1]) + newton_ceficient_4[3] * (t - x[0]) * (t - x[1]) * (t - x[2]) + newton_ceficient_4[4] * (t - x[0]) * (t - x[1]) * (t - x[2]) * (t - x[3]))  # Memasukan nilai koefisien kedalam persamaan polinomial newton untuk mendapat persamaan v, kemudian di simplifikasi dengan menggunakan modul sympy.
newton_val_t_16_4 = newton_eq_4.subs(t,16)  # Mengevaluasi nilai v pada t = 16 dengan mensubtitusi nilai t = 16 ke persamaan yang ditemukan.

# 3th order (cubic)
# Membutuhkan 4 titik, sedangkan pada data terdapat 6 titik, maka satu titik dihapus. Dihapus titik (30,901.67) karena jaraknya lebih jauh dari nilai yang akan dicari.
x = x[:-1] # x = [10,15,20,22.5]
y = y[:-1] # y = [227.04,362.78,517.35,602.97]
# Direct method
direct_coeficient_3 = direct_method(x, y) # Menjalankan fungsi direct method dengan menggunakan data yang telah diubah.
direct_val_t_16_3 = np.polyval(direct_coeficient_3, 16) # Mengevaluasi nilai v pada saat t = 16 menggunakan modul numpy
# Newton method
newton_ceficient_3 = newt_method(x, y)  # Menjalankan fungsi newton method dengan menggunakan data yang telah diubah.
newton_eq_3 = sy.simplify(newton_ceficient_3[0] + newton_ceficient_3[1] * (t - x[0]) + newton_ceficient_3[2] * (t - x[0]) * (t - x[1]) + newton_ceficient_3[3] * (t - x[0]) * (t - x[1]) * (t - x[2])) # Memasukan nilai koefisien kedalam persamaan polinomial newton untuk mendapat persamaan v, kemudian di simplifikasi dengan menggunakan modul sympy.
newton_val_t_16_3 = newton_eq_3.subs(t,16) # Mengevaluasi nilai v pada t = 16 dengan mensubtitusi nilai t = 16 ke persamaan yang ditemukan.

# 2nd order (quadratic)
# Membutuhkan 3 titik, sedangkan pada data terdapat 6 titik, maka satu titik dihapus. Dihapus titik (22.5,602.97) karena jaraknya lebih jauh dari nilai yang akan dicari.
x = x[:-1] # x = [10,15,20]
y = y[:-1] # y = [227.04,362.78,517.35]
# Direct method
direct_coeficient_2 = direct_method(x, y) # Menjalankan fungsi direct method dengan menggunakan data yang telah diubah.
direct_val_t_16_2 = np.polyval(direct_coeficient_2, 16) # Mengevaluasi nilai v pada saat t = 16 menggunakan modul numpy
# Newton method
newton_ceficient_2 = newt_method(x, y)  # Menjalankan fungsi newton method dengan menggunakan data yang telah diubah.
newton_eq_2 = sy.simplify(newton_ceficient_2[0] + newton_ceficient_2[1] * (t - x[0]) + newton_ceficient_2[2] * (t - x[0]) * (t - x[1])) # Memasukan nilai koefisien kedalam persamaan polinomial newton untuk mendapat persamaan v, kemudian di simplifikasi dengan menggunakan modul sympy.
newton_val_t_16_2 = newton_eq_2.subs(t,16)  # Mengevaluasi nilai v pada t = 16 dengan mensubtitusi nilai t = 16 ke persamaan yang ditemukan.

# 1st order (linear)
# Membutuhkan 2 titik, sedangkan pada data terdapat 6 titik, maka satu titik dihapus. Dihapus titik (10,227.04) karena jaraknya lebih jauh dari nilai yang akan dicari.
x = x[1:] # x = [15,20]
y = y[1:] # y = [362.78,517.35]
# Direct method
direct_coeficient_1 = direct_method(x, y) # Menjalankan fungsi direct method dengan menggunakan data yang telah diubah.
direct_val_t_16_1 = np.polyval(direct_coeficient_1, 16) # Mengevaluasi nilai v pada saat t = 16 menggunakan modul numpy
# Newton method
newton_ceficient_1 = newt_method(x, y)  # Menjalankan fungsi newton method dengan menggunakan data yang telah diubah.
newton_eq_1 = sy.simplify(newton_ceficient_1[0] + newton_ceficient_1[1] * (t - x[0])) # Memasukan nilai koefisien kedalam persamaan polinomial newton untuk mendapat persamaan v, kemudian di simplifikasi dengan menggunakan modul sympy.
newton_val_t_16_1 = newton_eq_1.subs(t,16) # Mengevaluasi nilai v pada t = 16 dengan mensubtitusi nilai t = 16 ke persamaan yang ditemukan.

# Absolute relative error
rel_err_4 = abs((direct_val_t_16_4 - direct_val_t_16_1) / direct_val_t_16_4)  # Menghitung nilai absolute relative error untuk persamaan direct method orde 4
rel_err_3 = abs((direct_val_t_16_3 - direct_val_t_16_1) / direct_val_t_16_3)  # Menghitung nilai absolute relative error untuk persamaan direct method orde 3
rel_err_2 = abs((direct_val_t_16_2 - direct_val_t_16_1) / direct_val_t_16_3)  # Menghitung nilai absolute relative error untuk persamaan direct method orde 2

# Finding the distace of droplet observet by rocket at t = 11s and t = 16s using integration of third order newton method
dist_11_16 = sy.integrate(newton_eq_3, (t, 11, 16))  # Integrasi persamaan newton orde 3 terhadap t, dari t = 11, sampai t = 16

# Finding the droplet droplet acceleration at t = 16s using differentation
accel_newt_4 = newton_eq_4.diff(t, 1).subs(t,16)  # Turunkan sekali persamaan newton orde 4 terhadap t, kemudian substitusi nilai t = 16
accel_newt_3 = newton_eq_3.diff(t, 1).subs(t,16)  # Turunkan sekali persamaan newton orde 3 terhadap t, kemudian substitusi nilai t = 16
accel_newt_2 = newton_eq_2.diff(t, 1).subs(t,16)  # Turunkan sekali persamaan newton orde 2 terhadap t, kemudian substitusi nilai t = 16
accel_newt_1 = newton_eq_1.diff(t, 1).subs(t,16)  # Turunkan sekali persamaan newton orde 1 terhadap t, kemudian substitusi nilai t = 16

print("1. Find the value for downward velocity at t = 16 seconds using Direct method:")
print("\ta. For first order/linear, second, third, and fourth order polynomial (%.2f)")
print("\t\tFirst order/linear, v(16) = %.2f" % direct_val_t_16_1, "mm/s")
print("\t\tSecond order, v(16) = %.2f" % direct_val_t_16_2, "mm/s")
print("\t\tThird order, v(16) = %.2f" % direct_val_t_16_3, "mm/s")
print("\t\tFourth order, v(16) = %.2f" % direct_val_t_16_4, "mm/s")
print("\tb. What are their absolute relative approximate errors? (%.5f)")
print("\t\tSecond order, Ea = %.5f" % rel_err_4, "%")
print("\t\tThird order, Ea = %.5f" % rel_err_3, "%")
print("\t\tFourth order, Ea = %.5f" % rel_err_2, "%")
print("2. Find the value for downward velocity at t = 16 seconds using Newton method:")
print("\ta. For first order/linear, second, third, and fourth order polynomial (%.2f)")
print("\t\tFirst order/linear, v(16) = %.2f" % newton_val_t_16_1, "mm/s")
print("\t\tSecond order, v(16) = %.2f" % newton_val_t_16_2, "mm/s")
print("\t\tThird order, v(16) = %.2f" % newton_val_t_16_3, "mm/s")
print("\t\tFourth order, v(16) = %.2f" % newton_val_t_16_4, "mm/s")
print("\tb. Use the third order of Newton method to find the distance of droplet observed by rocket at t= 11s and t=16 s")
print("\t\tDistance of droplet observed by rocket at t= 11s and t=16 s is %.2f"%dist_11_16, "mm")
print("\tc. What is droplet acceleration at t = 16s?")
print("\t\tFirst order/linear, a(16) = %.2f" % accel_newt_1, "mm/s^2")
print("\t\tSecond order, a(16) = %.2f" % accel_newt_2, "mm/s^2")
print("\t\tThird order, a(16) = %.2f" % accel_newt_3, "mm/s^2")
print("\t\tFourth order, a(16) = %.2f" % accel_newt_4, "mm/s^2")