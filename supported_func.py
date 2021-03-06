supported_functions = {
	'__eq__$bool_$bool_',
	'__ne__$bool_$bool_',
	'__lt__$bool_$bool_',
	'__le__$bool_$bool_',
	'__gt__$bool_$bool_',
	'__ge__$bool_$bool_',
	'__bool__$bool_',
	'__int__$bool_',
	'__float__$bool_',
	'__and__$bool_$bool_',
	'__or__$bool_$bool_',
	'__xor__$bool_$bool_',
	'__getitem__$dict$',
	'__setitem__$dict$$',
	'__contains__$dict$',
	'__delitem__$dict$',
	'__bool__$dict',
	'__len__$dict',
	'__eq__$dict$dict',
	'__ne__$dict$dict',
	'__iter__$dict',
	'make$dict_iterator',
	'__next__$dict_iterator',
	'__add__$float_$float_',
	'__sub__$float_$float_',
	'__mul__$float_$float_',
	'__truediv__$float_$floa',
	'__mod__$float_$float_',
	'__eq__$float_$float_',
	'__ne__$float_$float_',
	'__lt__$float_$float_',
	'__le__$float_$float_',
	'__ge__$float_$float_',
	'__gt__$float_$float_',
	'__bool__$float_',
	'__add__',
	'__sub__',
	'__mul__',
	'__truediv__',
	'__mod__',
	'__len__',
	'__getitem__',
	'__contains_',
	'__setitem__',
	'__delitem__',
	'__bool__',
	'__eq__',
	'__ne__',
	'__ge__',
	'__gt__',
	'__lt__',
	'__le__',
	'__and__',
	'__or__',
	'__xor__',
	'__invert__',
	'__lshift__',
	'__rshift__',
	'__iter__',
	'__next__',
	'append',
	'add',
	'remove',
	'pop',
	'__add__$int_$int_',
	'__sub__$int_$int_',
	'__mul__$int_$int_',
	'__mod__$int_$int_',
	'__float__$int_',
	'__eq__$int_$int_',
	'__ne__$int_$int_',
	'__lt__$int_$int_',
	'__le__$int_$int_',
	'__ge__$int_$int_',
	'__gt__$int_$int_',
	'__bool__$int_',
	'__and__$int_$int_',
	'__or__$int_$int_',
	'__xor__$int_$int_',
	'__invert__$int_',
	'__lshift__$int_$int_',
	'__rshift__$int_$int_',
	'make$list',
	'append$list$',
	'pop$list',
	'__getitem__$list$',
	'__getitem__$list$int_',
	'__getitem__$list$slice',
	'__setitem__$list$$',
	'__setitem__$list$int_$',
	'__setitem__$list$slice',
	'__add__$list$list',
	'__mul__$list$int_',
	'__len__$list',
	'__eq__$list$list',
	'__ne__$list$list',
	'__lt__$list$list',
	'__le__$list$list',
	'__ge__$list$list',
	'__gt__$list$list',
	'__contains__$list$',
	'__delitem__$list$int_',
	'__delitem__$list$slice',
	'__bool__$list',
	'__iter__$list',
	'make$list_iterator',
	'__next__$list_iterator',
	'make$none',
	'__bool__$none',
	'__eq__$none$none',
	'__ne__$none$none',
	'range$int_',
	'range$int_$int_',
	'range$int_$int_$int_',
	'__iter__$range',
	'__next__$range_iterator',
	'make$set',
	'add$set$',
	'remove$set$',
	'__contains__$set$',
	'__bool__$set',
	'__len__$set',
	'__eq__$set$set',
	'__ne__$set$set',
	'__lt__$set$set',
	'__le__$set$set',
	'__ge__$set$set',
	'__gt__$set$set',
	'__iter__$set',
	'make$set_iterator',
	'__next__$set_iterator',
	'slice$int_',
	'slice$int_$int_',
	'slice$int_$int_$int_',
	'make$str',
	'__getitem__$str$',
	'__getitem__$str$int_',
	'__getitem__$str$slice',
	'__len__$str',
	'__add__$str$str',
	'__mul__$str$int_',
	'__eq__$str$str',
	'__ne__$str$str',
	'__lt__$str$str',
	'__le__$str$str',
	'__ge__$str$str',
	'__gt__$str$str',
	'__contains__$str$str',
	'__bool__$str',
	'print'
}

builtin_func_mapper = {
	'len': '__len__',
	'bool': '__bool__',
	'iter': '__iter__',
	'next': '__next__',
}

binary_func_mapper = {
	'+' : "__add__",
	'-' : "__sub__",
	'*' : "__mul__",
	'/' : "__truediv__",
	'%' : "__mod__",
	'>' : "__gt__",
	'<' : "__lt__",
	'>=': "__ge__",
	'<=': "__le__",
	'&' : "__and__",
	'|' : "__or__",
	'^' : "__xor__",
	'<<': "__lshift__",
	'>>': "__rshift__",
	'==': "__eq__",
    '!=': "__ne__",
}