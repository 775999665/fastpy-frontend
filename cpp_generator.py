from supported_func import supported_functions, binary_func_mapper, builtin_func_mapper
import optimizer

string_constant_table = {
    
}

constant_no = 0

def sym_cpp(id):
    global constant_no
    if id[0] == 'symbol':
        return id[1]
    elif id[0] == 'constant':
        if type(id[1]) == type(None):
            return 'make$none()'
        elif type(id[1]) == list:
            return 'make$list()'
        elif type(id[1]) == dict:
            return 'make$dict()'
        elif type(id[1]) == set:
            return 'make$set()'
        elif type(id[1]) == str:
            raw = repr(id[1])[1:-1]
            if not raw in string_constant_table:
                string_constant_table[raw] = '_c' + str(constant_no) + '$'
                constant_no = constant_no + 1
            return string_constant_table[raw]
        elif type(id[1]) == int:
            return 'make$int_(%s)' % id[1]
        elif type(id[1]) == float:
            return 'make$float_(%s)' % id[1]
        elif type(id[1]) == bool:
            return 'make$bool_(%s)' % ('true' if id[1] else 'false')
    raise Exception('Unknow occur in sym_cpp')
def func_cpp(name, args):
    try:
        if name in builtin_func_mapper:
            name = builtin_func_mapper[name]
        if name in supported_functions:
            return name
        types = ['' if len(arg[2]) > 1 else list(arg[2])[0] + '_' if list(arg[2])[0] in ['int', 'float', 'bool']  else list(arg[2])[0] for arg in args]
        for i in range(len(types),-1,-1):
            candinate_name = '$'.join([name] + types[:i] + [''] * (len(types) - i))
            if candinate_name in supported_functions:
                return candinate_name
        return name;
    except Exception  as e:
        print(name)
        print(args)

def cpp_generator(source, tofile):
    header = """
#include "type.h"
#include "list.h"
#include "int.h"
#include "float.h"
#include "str.h"
#include "dict.h"
#include "bool.h"
#include "set.h"
#include "func.h"
#include "none.h"
#include "range.h"
#include "range_iterator.h"
#include "dict_iterator.h"
#include "list_iterator.h"
#include "generated.h"
#include "set_iterator.h"
#include "slice.h"
"""
    supported_functions.update(source.keys())
    f = open(tofile, 'w')
    print(header, file = f)
    main = source['_main$']
    if main['vars']:
        print('value %s;' % ', '.join(main['vars']), file = f)

    for func_name in source:
        print('value %s(%s);\n' % (func_name, ', '.join(['value %s' % arg for arg in source[func_name]['paras']])), file = f)
    for func_name in source:
        code_lines = code_generator(source[func_name]['code'])
        source[func_name]['code_lines'] = code_lines

    for con in string_constant_table:
        print('value %s = make$str("%s");\n' % (string_constant_table[con], con), file = f)

    for func_name in source:
        code_lines = source[func_name]['code_lines']
        if '_$$ret$%s' % func_name in source[func_name]['vars']:
            code_lines.append('return _$$ret$%s;' % func_name)
        print('value %s(%s) {\n\t%s\n}' % (func_name, ', '.join(['value %s' % arg for arg in source[func_name]['paras']]), ('' if func_name == '_main$' else 'value ' + ', '.join(source[func_name]['vars']) + ';\n\t') + '\n\t'.join(code_lines)), file = f)

    print('int main(){_main$();}', file = f)
    f.close()


def code_generator(lines):
    cpp_code = []
    jmp_targets = set()
    for code_tuple in lines:
        if code_tuple[0] == '=':
            cpp_code.append(sym_cpp(code_tuple[1]) + ' = ' + sym_cpp(code_tuple[2]))
        elif code_tuple[0] == '~':
            cpp_code.append(sym_cpp(code_tuple[1]) + ' = ' + sym_cpp(code_tuple[2]))
        elif code_tuple[0] == 'call':
            func_name = func_cpp(code_tuple[2], code_tuple[3])
            if code_tuple[1]:
                cpp_code.append(sym_cpp(code_tuple[1]) + ' = ' + func_name + '(' + ', '.join([sym_cpp(arg) for arg in code_tuple[3]]) + ')')
            else:
                cpp_code.append(func_name + '(' +  ', '.join([sym_cpp(arg) for arg in code_tuple[3]]) +')')
        elif code_tuple[0] in optimizer.BINARY_OPERATORS:
            func_name = func_cpp(binary_func_mapper[code_tuple[0]], [code_tuple[2], code_tuple[3]])
            if code_tuple[1]:
                cpp_code.append(sym_cpp(code_tuple[1]) + ' = ' + func_name + '(' + ', '.join([sym_cpp(code_tuple[2]), sym_cpp(code_tuple[3])]) + ')')
            else:
                cpp_code.append(func_name + '(' +  ', '.join([sym_cpp(code_tuple[2]), sym_cpp(code_tuple[3])]) +')')
        elif code_tuple[0] == 'jmp':
            cpp_code.append('goto L'+str(code_tuple[1]))
            jmp_targets.add(code_tuple[1])
        elif code_tuple[0] == 'if':
            cpp_code.append('if(%s.boolval) goto L%s' % (sym_cpp(code_tuple[1]), code_tuple[2]))
            jmp_targets.add(code_tuple[2])
        elif code_tuple[0] == 'ifnot':
            cpp_code.append('if(!%s.boolval) goto L%s' % (sym_cpp(code_tuple[1]), code_tuple[2]))
            jmp_targets.add(code_tuple[2])

    for i in range(len(cpp_code)):
        if i in jmp_targets:
            cpp_code[i] = 'L%s: ' % i + cpp_code[i]
        cpp_code[i] = cpp_code[i] + ';'
    if len(cpp_code) in jmp_targets:
        cpp_code.append('L%s:;' % len(cpp_code))
    return cpp_code

