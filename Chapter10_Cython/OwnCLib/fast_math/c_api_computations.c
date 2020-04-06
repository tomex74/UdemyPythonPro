#include "Python.h"

static PyObject* fast_math_c_api_clip(PyObject *self, PyObject *args) 
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
static PyMethodDef fast_math_c_api_FunctionsTable[] = {
  {"c_api_clip",  fast_math_c_api_clip, METH_VARARGS, "Clipping the list values."},
  { NULL, NULL, 0, NULL}
};

/* Module structure */
static struct PyModuleDef fast_math_c_api_Module = {
  PyModuleDef_HEAD_INIT,
  "fast_math_c_api",
  "Python wrapper for custom C extension of the fast_math library.", 
  -1,
  fast_math_c_api_FunctionsTable
};

/* Module initialization function */
PyMODINIT_FUNC * PyInit_fast_math_c_api(void) 
{
  return PyModule_Create(&fast_math_c_api_Module);
}
