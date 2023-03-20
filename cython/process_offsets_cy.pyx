import numpy as np
cimport numpy as np

cpdef int process_offsets(np.ndarray[np.int64_t, ndim=1] offsets):
    cdef Py_ssize_t length, pos, prev, steps
    length = offsets.shape[0]
    pos, prev, steps = 0, 0, 0

    while 0 <= pos < length:
        prev = pos
        pos += offsets[pos]
        steps += 1
        offsets[prev] = offsets[prev] + 1 if offsets[prev] < 3 else offsets[prev] - 1

    return steps
