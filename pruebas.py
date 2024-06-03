from llvmlite import ir

module = ir.Module("main")
func_name: str = "main"
param_types = []
type_map = {
            'int': ir.IntType(32),
            'float': ir.FloatType()
        }
return_type : ir.Type = type_map["int"]
fnty = ir.FunctionType(return_type, param_types)
func = ir.Function(module, fnty, name=func_name)

block = func.append_basic_block(f"{func_name}_entry")
builder = ir.IRBuilder(block)

# Define integer types
int32_type = ir.IntType(32)

# Create integer values
a = ir.Constant(int32_type, 10)
b = ir.Constant(int32_type, 20)

# Perform addition
sum_value :ir.Instruction = builder.add(a, b, name="my_addition")
print(type(sum_value))

print(sum_value)