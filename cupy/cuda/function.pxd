from libc.stdint cimport intptr_t


cdef class CPointer:
    cdef void* ptr
    cdef Py_ssize_t size


cdef class Function:

    cdef:
        public Module module
        public intptr_t ptr

    cpdef linear_launch(self, size_t size, args, size_t shared_mem=*,
                        size_t block_max_size=*, stream=*)


cdef class Module:

    cdef:
        public intptr_t ptr

    cpdef load_file(self, filename)
    cpdef load(self, bytes cubin)
    cpdef get_global_var(self, name)
    cpdef get_function(self, name)


cdef class LinkState:

    cdef:
        public intptr_t ptr

    cpdef add_ptr_data(self, unicode data, unicode name)
    cpdef bytes complete(self)
