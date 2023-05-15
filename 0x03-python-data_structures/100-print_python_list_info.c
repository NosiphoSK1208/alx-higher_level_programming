/*
 * File: 100-print_python_list_info.c
 */

#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @pyobject: A PyObject list.
 */
void print_python_list_info(PyObject *pyobject)
{
	int asize, allo, v;
	PyObject *obj;

	asize = Py_SIZE(pyobject);
	allo = ((PyListObject *)pyobject)->allocated;

	printf("[*] Size of the Python List = %d\n", asize);
	printf("[*] Allocated = %d\n", allo);

	for (v = 0; v < asize; v++)
	{
		printf("Element %d: ", v);

		obj = PyList_GetItem(pyobject, v);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
