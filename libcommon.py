def dprint(msg):
    # type: (object) -> object
    print("DEBUG:", msg)

def eprint(msg):
    print("ERROR:", msg)

def fn():
    import sys
    return(sys._getframe(1).f_code.co_name)

# Supposed to be a uniq sorting function for lists
def list_sort_uniq(mylist):
    import itertools, operator
    import sys
    if sys.hexversion < 0x030000000:
        mapper = itertools.imap # 2.4 <=  Python <3
    else:
        mapper = map # Python > 3
    return mapper(operator.itemgetter(0),itertools.groupby(sorted(mylist)))

def dir_walk(dpath):
        import os
        if os.path.exists(dpath):
                list_of_file_paths = []
                for root,sub_directories,files in os.walk(dpath):
                        for individual_file in files:
                                list_of_file_paths.append(os.path.join(root,individual_file))
                        for individual_directory in sub_directories:
                                list_of_file_paths.append(os.path.join(root,individual_directory))
                return(list_of_file_paths)
        else:
                return(-2)

def dir_find_containing_folder(dpath):
    import os
    Z = os.path.dirname(Y)
    return (Z)

def add_prefix(prefix_string, list_of_files):
    returnlist = []
    for basename in list_of_files:
        returnlist.append(prefix_string + basename)
    return(returnlist)

def add_suffix(suffix_string, list_of_files):
    returnlist=[]
    for filename in list_of_files:
        returnlist.append(filename + suffix_string)
    return(returnlist)

