#include "util.h"
#pragma warning (push)
#pragma warning(disable: 4100)
#pragma warning(disable: 4127)
#pragma warning(disable: 4244)
#define BOOST_PYTHON_STATIC_LIB
#include <boost/python.hpp>
#pragma warning(pop)

BOOST_PYTHON_MODULE(util)
{
    using boost::python::def;
    def("add", add);
};
