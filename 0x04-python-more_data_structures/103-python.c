#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * process_python_object - Process a Python object
 *
 * @p: Python Object
 * Return: no return
 */
void process_python_object(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		print_python_bytes(p);
	}
	else if (PyList_Check(p))
	{
		print_python_list(p);
	}
	else
	{
		printf("  [ERROR] Invalid Python Object\n");
	}
}

int main()
{
	Py_Initialize();

	/* Example usage of process_python_object */
	PyObject *sample_bytes = PyBytes_FromStringAndSize("Hello, World!", 13);
	process_python_object(sample_bytes);

	PyObject *sample_list = PyList_New(3);
	PyList_SetItem(sample_list, 0, PyBytes_FromStringAndSize("Python", 6));
	PyList_SetItem(sample_list, 1, PyBytes_FromStringAndSize("C", 1));
	PyList_SetItem(sample_list, 2, PyBytes_FromStringAndSize("C++", 3));
	process_python_object(sample_list);

	Py_DECREF(sample_bytes);
	Py_DECREF(sample_list);

	Py_Finalize();

	return 0;
}

