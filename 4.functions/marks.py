def marks(
    phy,
    chem,
    eng,
    sci,
    hi,
):
    total = phy + chem + eng + sci + hi
    per = total / 500 * 100
    print(f"Your total marks {total}")
    print(f"Your percentage scored {per:.2f}")


marks(phy=78, 80, 75, 86, 65)
