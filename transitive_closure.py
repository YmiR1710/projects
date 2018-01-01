while True:
    matrixstr = []
    matrixint = []
    print("Введіть булеву (n x n) матрицю(не розділяючи значення пробілами і розділяючи рядки за допомогою Enter). для завершення натисінть Enter двічі\n")
    while True:
        try:
            bool1 = input()
        except:
            None
        if bool1 == "":
            break
        else:
            matrixstr.append(bool1)
            continue

    for i in matrixstr:
        rows = []
        for num in i:
            try:
                num = int(num)
            except:
                None
            rows.append(num)
        matrixint.append(rows)

    try:
        for v in range(len(matrixint[0])):
            for i in range(len(matrixint[0])):
                if v != i and matrixint[i][v]:
                    for u in range(len(matrixint[0])):
                        matrixint[i][u] = matrixint[i][u] or matrixint[v][u]
    except:
        print("Неправильне подання матриці")
    invalid_input_identifier = 0
    for row in matrixint:
        for i in row:
            if i != 0 and i != 1:
                invalid_input_identifier += 1
    if invalid_input_identifier == 0:
        for y in matrixint:
            print(str(y))
    else:
        print("Неправильне подання матриці")

    print("введіть 'stop' щоб завершити програму або натисніть Enter щоб продовжити")
    key = input()
    try:
        if key == "stop":
            break
        else:
            continue
    except:
        None
