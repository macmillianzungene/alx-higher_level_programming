#include <Python.h>

void print_python_string(PyObject *p)
{
    long int length;

    /* Check if p is a string */
    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    /* Get the length of the string */
    length = PyUnicode_GET_LENGTH(p);

    /* Print the string */
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}

