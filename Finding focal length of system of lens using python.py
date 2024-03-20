import numpy as np


def symmetric_system_function():
    u1 = float(input("Enter refractive index of first medium:"))
    u2 = float(input("Enter refractive index of second medium:"))
    R = float(input("Enter the radius of curvature:"))
    p = (u2 - u1) / R
    D = float(input("Enter the distance:"))
    m1 = np.array([[1.0, -p], [0.0, 1.0]])
    m2 = np.array([[1.0, 0.0], [D / u1, 1.0]])
    m3 = np.array([[1.0, -p], [0.0, 1.0]])
    print("Matrices\n")
    system = (m1).dot(m2).dot(m3)
    print(f"Refraction1:\n{m1}")
    print(f"Translation1:\n{m2}")
    print(f"Refraction2:\n{m3}")
    print(f"System matrix\n{system}")
    a = system[0][1]
    f = -1 / a
    print("Focal length=", f)
    b = system[0][0]
    c = system[1][1]
    d = system[1][0]
    w = (1 - b) / a
    e = (c - 1) / a
    print("Unit plane from first surface=", w)
    print("Unit plane from second surface=", e)


def refraction():
    u1 = float(input("Enter refractive index of first medium:"))
    u2 = float(input("Enter refractive index of second medium:"))
    R = float(input("Enter the radius of curvature:"))
    p = (u2 - u1) / R
    m1 = np.array([[1.0, -p], [0.0, 1.0]])
    print("Matrices\n")
    print(f"Refraction1:\n{m1}")


def translation():
    u1 = float(input("Enter refractive index of first medium:"))
    D = float(input("Enter the distance:"))
    m2 = np.array([[1.0, 0.0], [D / u1, 1.0]])
    print(f"Translation1:\n{m2}")


def assymmetric_system_function():
    u1 = float(input("Enter refractive index of first medium:"))
    u2 = float(input("Enter refractive index of second medium:"))
    R1 = float(input("Enter the radius of curvature of first surface:"))
    R2 = float(input("Enter the radius of curvature second surface:"))
    p1 = (u2 - u1) / R1
    p2 = (u2 - u1) / R2
    D = float(input("Enter the distance:"))
    m1 = np.array([[1.0, -p1], [0.0, 1.0]])
    m2 = np.array([[1.0, 0.0], [D / u1, 1.0]])
    m3 = np.array([[1.0, -p2], [0.0, 1.0]])
    print("Matrices\n")
    system = (m3).dot(m2).dot(m1)
    print(f"Refraction1:\n{m1}")
    print(f"Translation1:\n{m2}")
    print(f"Refraction2:\n{m3}")
    print(f"System matrix\n{system}")
    a = system[0][1]
    f = -1 / a
    print("Focal length=", f)
    b = system[0][0]
    c = system[1][1]
    w = (1 - b) / a
    e = (c - 1) / a
    print("Unit plane from first surface=", w)
    print("Unit plane from second surface=", e)


def two_lens():
    system1=assymmetric_system_function()
    m2=translation()
    system2 = assymmetric_system_function()
    lens = (system2).dot(m2)
    two_lens = (lens).dot(system1)
    print(f"System matrix for combination\n{two_lens}")
    a = two_lens[0][1]
    f = -1 / a
    print("Focal length=", f)
    b = two_lens[0][0]
    c = two_lens[1][1]
    d = two_lens[1][0]
    w = (1 - b) / a
    e = (c - 1) / a
    print("Unit plane from first surface=", w)
    print("Unit plane from second surface=", e)
def ramsden():
    o=float(input("Focal length of the lenses="))
    m4 = np.array([[1.0, -1/o], [0.0, 1.0]])
    m5 = np.array([[1.0, 0.0], [(2*o)/3, 1.0]])
    s=(m4).dot(m5).dot(m4)
    print(f"System matrix of Ist lens:\n{m4}")
    print(f"Translation:\n{m5}")
    print(f"System matrix of IInd lens:\n{m4}")
    print(f"System matrix of Ramsden's eyepiece\n{s}")
    a= s[0][1]
    f=-1/a
    print("Focal length of combination=", f)
    b = s[0][0]
    c = s[1][1]
    w = (1 - b) / a
    e = (c - 1) / a
    print("Unit plane from first surface=", w)
    print("Unit plane from second surface=", e)
print("What would you like to do today?\n1. Define a system matrix for a symmetric lens.\n2. Define a system matrix for a assymmetric lens.\n3. Define a system matrix for a two lens combination.\n4.Ramsden's eyepiece.")
q=int(input("Enter your choice:"))
if q == 1:
    symmetric_system_function()
elif q == 2:
    assymmetric_system_function()
elif q == 3:
    two_lens()
elif q==4:
    ramsden()
