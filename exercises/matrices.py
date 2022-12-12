def well_formed_matrix(m):
    prev_len = None

    if len(m) == 0:
        return False

    for i in range(len(m)):
        m_i = m[i]
        if len(m_i) == 0 or (i > 0 and len(m_i) != prev_len):
            return False

        prev_len = len(m_i)

    return True


def transpose(m):
    if not well_formed_matrix(m):
        raise ValueError("m is not a well-formed matrix")

    t = []
    for i in range(len(m[0])):
        r = []
        for row in m:
            r.append(row[i])

        t.append(r)

    return t
