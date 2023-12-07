#include <Python.h>

void print_python_list(PyObject *p)
{
    long int len = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", len);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (long int i = 0; i < len; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    long int size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
    for (long int i = 0; i < size + 1 && i < 10; i++)
    {
        printf("%02hhx", ((PyBytesObject *)p)->ob_sval[i]);
        if (i < 9 && i < size)
            printf(" ");
    }
    printf("\n");
}

