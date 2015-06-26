'''pylint_werkzeug module'''

from astroid import MANAGER
from astroid.builder import AstroidBuilder
from astroid import nodes
import importlib
import os.path
from ipdb import launch_ipdb_on_exception

def register(_):
    # `register` is expected by pylint for plugins, but we are creating a
    # transform, not registering a checker.
    pass

MODULE_TRANSFORMS = {}

def transform(module):
    '''Run the transformation associated with module.name in MODULE_TRANSFORMS.'''
    try:
        transformer = MODULE_TRANSFORMS[module.name]
        print('ran for module {}'.format(module.name))
    except KeyError:
        pass
    else:
        transformer(module)

MANAGER.register_transform(nodes.Module, transform)

def werkzeug_transform(module):
    '''Werkzeug uses all_by_module to lazily expose modules.'''
    werk_spec = importlib.machinery.PathFinder.find_spec('werkzeug')
    werk_origin = werk_spec.origin
    werk_dir = os.path.dirname(werk_origin)
    werk_module_ast = None
    with open(werk_origin, 'r') as werk_init_file:
        werk_module_ast = AstroidBuilder(MANAGER).string_build(werk_init_file.read())
    lazy_mods = werk_module_ast['all_by_module']
    werk_mods_init_str = [stmt.as_string() for stmt in lazy_mods.assigned_stmts()][0]
    werk_exported_mods_dict = eval(werk_mods_init_str)

    for mod_str, exports in werk_exported_mods_dict.items():
        print("{}".format(mod_str))
        spec = importlib.machinery.PathFinder.find_spec(mod_str)
        origin = werk_spec.origin
        print("    origin: {}".format(origin))
        mod_name = mod_str.split('.')[-1]
        mod_filepath = os.path.join(werk_dir, mod_name + '.py')
        if mod_str == 'werkzeug.debug':
            continue
        print("    mod_filepath: {}".format(mod_filepath))
        mod_ast = None
        with open(mod_filepath, 'r') as init_file:
            mod_ast = AstroidBuilder(MANAGER).string_build(init_file.read())
        for export in exports:
            print('    {}'.format(export))
            node = mod_ast[export]
            module.locals[export] = node

MODULE_TRANSFORMS['werkzeug'] = werkzeug_transform
