// Transcrypt'ed from Python, 2022-09-22 15:10:26
var random = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
var __name__ = '__main__';
export var gen_random_int = function (number, seed) {
	var result = null;
	var mylist = [];
	random.seed (seed);
	for (var x = 0; x < number - 1; x++) {
		mylist.append (x);
	}
	random.shuffle (mylist);
	var result = mylist;
	return result;
};
export var listtostring = function (s) {
	var string = '';
	var count = 0;
	for (var number of s) {
		string += str (number);
		count++;
		if (count < len (s)) {
			string += ',';
		}
		else {
			string += '.';
		}
	}
	return string;
};
export var generate = function () {
	var number = 10;
	var seed = 200;
	var array = gen_random_int (number, seed);
	var array_str = listtostring (array);
	document.getElementById ('generate').innerHTML = array_str;
};
export var stringtolist = function (s) {
	var string = s;
	var new_array = string.py_split (',');
	for (var i = 0; i < len (new_array); i++) {
		new_array [i] = int (new_array [i]);
	}
	return new_array;
};
export var bubble_sort = function (list) {
	var array = list;
	var n = len (array);
	for (var outer_index = 1; outer_index < n - 1; outer_index++) {
		for (var inner_index = 1; inner_index < n; inner_index++) {
			var first_number = array [inner_index - 1];
			var second_number = array [inner_index];
			if (first_number > second_number) {
				array [inner_index] = first_number;
				array [inner_index - 1] = second_number;
			}
		}
	}
	return array;
};
export var sortnumber1 = function () {
	var array = stringtolist (document.getElementById ('generate').innerHTML);
	var new_array = bubble_sort (array);
	var array_str = listtostring (new_array);
	document.getElementById ('sorted').innerHTML = array_str;
};
export var sortnumber2 = function () {
	var value = document.getElementsByName ('numbers') [0].value;
	if (value == '') {
		window.alert ('Your textbox is empty');
		return ;
	}
	var array = stringtolist (value);
	var new_array = bubble_sort (array);
	var array_str = listtostring (new_array);
	document.getElementById ('sorted').innerHTML = array_str;
};

//# sourceMappingURL=library.map