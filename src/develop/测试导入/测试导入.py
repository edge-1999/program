from importlib import import_module

module_name = "math"
function_name = "sqrt"
module = import_module(module_name)
function = getattr(module, function_name)
print(function(4))
