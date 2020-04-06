#include "Python.h"

static PyObject* FastMathComputations_clip(PyObject *self, PyObject *args) 
{
  PyObject *input_list;
  PyObject *output_list;
  long *min_value;
  long *max_value;

  if (!PyArg_ParseTuple(args, "OiiO", &input_list, &min_value, &max_value, &output_list)) 
  {
    printf("Invalid args.\n");
    return NULL;
  }

  Py_ssize_t n = PyList_Size(input_list);
  if (n < 0) 
  {
    printf("Invalid list length.\n");
    return NULL;
  }

  PyLongObject *input_value;
  for (int i = 0; i < n; i++) 
  {
      input_value = PyList_GetItem(input_list, i);
      if (!PyLong_Check(input_value))
      {
        continue;
      }

      long input_value_c = PyLong_AsLong(input_value);

      if(input_value_c > max_value)
      {
        input_value_c = max_value;
      }
      else if(input_value_c < min_value)
      {
        input_value_c = min_value;
      }
      
      PyLongObject *clipped_input_value = PyLong_FromLong(input_value_c);
      PyList_SetItem(output_list, i, clipped_input_value);
  }

  return Py_BuildValue("i", PyLong_FromLong(0));
}

/* Module method table */
static PyMethodDef FastMathComputations_FunctionsTable[] = {
  {"c_api_clip",  FastMathComputations_clip, METH_VARARGS, "Clipping the list values."},
  { NULL, NULL, 0, NULL}
};

/* Module structure */
static struct PyModuleDef FastMathComputations_Module = {
  PyModuleDef_HEAD_INIT,
  "fast_math.c_api_clip",
  "Python wrapper for custom C extension of the fast_math library.", 
  -1,
  FastMathComputations_FunctionsTable
};

/* Module initialization function */
PyMODINIT_FUNC * PyInit_FastMathComputations(void) 
{
  return PyModule_Create(&FastMathComputations_Module);
}
