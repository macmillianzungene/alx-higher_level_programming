#include <Python.h>

/**
 * print_python_string - Prints Python strings.
 * @p: PyObject pointer.
 *
 * Return: Nothing.
 */
void print_python_string(PyObject *p)
{
    long int length;

    /* Check if p is a string */
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    /* Get string length */
    length = PyUnicode_GET_LENGTH(p);

    /* Print string type and length */
    printf("  Type: %s\n  Length: %ld\n",
           PyUnicode_KIND(p) == PyUnicode_1BYTE_KIND ? "compact ascii" : "compact unicode object",
           length);

    /* Print string as unicode object */
    printf("  Value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}

